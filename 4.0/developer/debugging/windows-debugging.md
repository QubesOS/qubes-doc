---
lang: en
layout: doc
permalink: /doc/4.0/4.0/windows-debugging/
redirect_from:
- /en/doc/windows-debugging/
- /doc/WindowsDebugging/
- /wiki/WindowsDebugging/
ref: 50
title: Windows debugging
---

Debugging Windows code can be tricky in a virtualized environment. The guide below assumes Xen hypervisor and Windows 7 VMs.

User-mode debugging is usually straightforward if it can be done on one machine. Just duplicate your normal debugging environment in the VM.

Things get complicated if you need to perform kernel debugging or troubleshoot problems that only manifest on system boot, user logoff or similar. For that you need two Windows VMs: the *host* and the *target*. The *host* will contain [WinDbg](https://msdn.microsoft.com/en-us/library/windows/hardware/ff551063(v=vs.85).aspx) installation, your source code and private symbols. The *target* will run the code being debugged. Both will be linked by virtual serial ports.

- First, you need to prepare separate copies of both *target* and *host* VM configuration files with some changes. Copy the files from **/var/lib/qubes/appvms/vmname/vmname.conf** to some convenient location, let's call them **host.conf** and **target.conf**.
- In both copied files add the following line at the end: `serial = 'pty'`. This will make Xen connect VM's serial ports to dom0's ptys.
- From now on you need to start both VMs like this: `qvm-start --custom-config=/your/edited/host.conf host`
- To connect both VM serial ports together you will either need [socat](http://www.dest-unreach.org/socat/) or a custom utility described later.
- To determine which dom0 pty corresponds to VM's serial port you need to read xenstore, example script below:

```bash
#!/bin/sh

id1=$(xl domid "$1-dm")
tty1=$(xenstore-read /local/domain/${id1}/device/console/3/tty)
echo $tty1
```

Pass it a running VM name and it will output the corresponding pty name.

- To connect both ptys you can use [socat](http://www.dest-unreach.org/socat/) like that:

```bash
#!/bin/sh

id1=$(xl domid "$1-dm")
id2=$(xl domid "$2-dm")
tty1=$(xenstore-read /local/domain/${id1}/device/console/3/tty)
tty2=$(xenstore-read /local/domain/${id2}/device/console/3/tty)
socat $tty1,raw $tty2,raw
```

...but there is a catch. Xen seems to process the traffic that goes through serial ports and changes all **0x0a** bytes into **0x0d, 0x0a** pairs (newline conversion). I didn't find a way to turn that off (setting ptys to raw mode didn't change anything) and it's not mentioned anywhere on the Internet, so maybe it's something on my system. If the above script works for you then you don't need anything more in dom0.

- On the *target* system, run `bcdedit /set debug on` on the console to turn on kernel debugging. It defaults to the first serial port.
- On the *host* system, install [WinDbg](http://msdn.microsoft.com/en-us/library/windows/hardware/ff551063(v=vs.85).aspx) and start the kernel debug (Ctrl-K), choose **com1** as the debug port.
- Reboot the *target* VM.
- Run the above shell script in dom0.
- If everything is fine you should see the proper kernel debugging output in WinDbg. However, if you see something like that:

    ~~~
    Opened \\.\com1
    Waiting to reconnect...
    Connected to Windows 7 7601 x64 target at (Wed Mar 19 20:35:43.262 2014 (UTC + 1:00)), ptr64 TRUE
    Kernel Debugger connection established.
    Symbol search path is: srv*c:\symbols*http://msdl.microsoft.com/download/symbols
    Executable search path is:
    ... Retry sending the same data packet for 64 times.
    The transport connection between host kernel debugger and target Windows seems lost.
    please try resync with target, recycle the host debugger, or reboot the target Windows.
    Unable to read KTHREAD address fffff8000281ccc0
    **************************************************************************
    Unable to read debugger data block header
    **************************************************************************
    Unable to read KTHREAD address fffff8000281ccc0
    Unable to read PsLoadedModuleList
    Unable to read KTHREAD address fffff8000281ccc0
    **************************************************************************
    Unable to read debugger data block header
    **************************************************************************
    ~~~

    ...then you're most likely a victim of the CRLF issue mentioned above. To get around it I wrote a small utility that basically does what socat would do and additionally corrects those replaced bytes in the stream. It's not pretty but it works:

```c
#include <errno.h>
#include <stdio.h>
#include <fcntl.h>
#include <termios.h>

int fd1, fd2;
char mark = ' ';

void out(unsigned char c)
{
    static int count = 0;
    static unsigned char buf[17] = {0};

    // relay to ouptput port
    write(fd2, &c, 1);
    fprintf(stderr, "%c", mark);

    /* dump all data going over the line
    if (count == 0)
        fprintf(stderr, "%c", mark);
    fprintf(stderr, "%02x ", c);
    if (c >= 0x20 && c < 0x80)
        buf[count] = c;
    else
        buf[count] = '.';
    count++;
    if (count == 0x10)
    {
        count = 0;
        fprintf(stderr, " %s\n", buf);
    }
    */
}

int main(int argc, char* argv[])
{
    unsigned char c = 0;
    struct termios tio;
    ssize_t size;

    if (argc < 3)
    {
        fprintf(stderr, "Usage: %s pty1 pty2 [mark character]\n", argv[0]);
        return EINVAL;
    }

    fd1 = open(argv[1], O_RDONLY | O_NOCTTY);
    if (fd1 <= 0)
    {
        perror("open fd1");
        return errno;
    }
    fd2 = open(argv[2], O_WRONLY | O_NOCTTY);
    if (fd2 <= 0)
    {
        perror("open fd2");
        return errno;
    }
/*
    // This doesn't make any difference which supports the theory
    // that it's Xen who corrupts the byte stream.
    cfmakeraw(&tio);
    if (tcsetattr(fd1, TCSANOW, &tio) < 0)
    {
        perror("tcsetattr 1");
        return errno;
    }
    if (tcsetattr(fd2, TCSANOW, &tio) < 0)
    {
        perror("tcsetattr 2");
        return errno;
    }
*/
    if (argc == 4)
        mark = argv[3][0];

    while (1)
    {
        size = read(fd1, &c, 1);
        if (size <= 0)
            break;

parse:
        if (c == 0x0d)
        {
            size = read(fd1, &c, 1);
            if (size <= 0)
            {
                out(0x0d);
                break;
            }
            if (c == 0x0a)
            {
                out(0x0a);
            }
            else
            {
                out(0x0d);
                goto parse;
            }
        }
        else
            out(c);
    }

    close(fd1);
    close(fd2);
    return 0;
}
```

> This utility is a unidirectional relay so you need to run two instances to get duplex communication, like:
>
>     #!/bin/sh
>
>     id1=$(xl domid "$1-dm")
>     id2=$(xl domid "$2-dm")
>     tty1=$(xenstore-read /local/domain/${id1}/device/console/3/tty)
>     tty2=$(xenstore-read /local/domain/${id2}/device/console/3/tty)
>     ./ptycrlf ${tty1} ${tty2} - &
>     ./ptycrlf ${tty2} ${tty1} + &

> With this everything should be good:
>
> ~~~
> Opened \\.\com1
> Waiting to reconnect...
> Connected to Windows 7 7601 x64 target at (Wed Mar 19 20:56:31.371 2014 (UTC + 1:00)), ptr64 TRUE
> Kernel Debugger connection established.
> Symbol search path is: srv*c:\symbols*http://msdl.microsoft.com/download/symbols
> Executable search path is:
> Windows 7 Kernel Version 7601 MP (1 procs) Free x64
> Built by: 7601.18247.amd64fre.win7sp1_gdr.130828-1532
> Machine Name:
> Kernel base = 0xfffff800`0261a000 PsLoadedModuleList = 0xfffff800`0285d6d0
> System Uptime: not available
> ~~~

# Debugging HVMs in the Qubes R4.0

There are two main issues to be adopted to get all things to work in the R4.0.

## Add a virtual serial port

Qemu in the stub domain with virtual serial port added in a recommended way (```<serial type="pty"/>```) fails to start (Could not open '/dev/hvc1': No such device). It seems like a lack of multiple xen consoles support/configuration. The only way that I have found is to attach serial port explicitly to the available console.

1. Unpack stub domain in dom0:

```shell_session
$ mkdir stubroot
$ cp /usr/lib/xen/boot/stubdom-linux-rootfs stubroot/stubdom-linux-rootfs.gz
$ cd stubroot
$ gunzip stubdom-linux-rootfs.gz
$ cpio -i -d -H newc --no-absolute-filenames < stubdom-linux-rootfs
$ rm stubdom-linux-rootfs
```

2. Edit Init script to remove last loop and to add "-serial /dev/hvc0" to the qemu command line.

3. Apply changes:

```shell_session
$ find . -print0 | cpio --null -ov --format=newc | gzip -9 > ../stubdom-linux-rootfs
$ sudo mv ../stubdom-linux-rootfs /usr/lib/xen/boot
```

## Connect two consoles

Run the following script:

```shell
debugname1=win7new
debugname2=win7dbg
id1=$(xl domid "$debugname1-dm")
id2=$(xl domid "$debugname2-dm")

tty1=$(xenstore-read /local/domain/${id1}/console/tty)
tty2=$(xenstore-read /local/domain/${id1}/console/tty)

socat $tty1,raw $tty2,raw
```

Happy debugging!
