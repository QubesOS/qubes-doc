---
layout: wiki
title: Qrexec
permalink: /wiki/Qrexec/
---

Command execution in VM (and Qubes RPC)
=======================================

In order to manage VMs easily, there is a need for a mechanism to allow dom0 to force command execution in a VM. For instance, when user selects from KDE menu an application, it should be started in the selected VM. Also it is often useful to be able to pass stdin/stdout/stderr from an application running in VM to dom0.

Qrexec basics
-------------

During domain creation a process named *qrexec-daemon* is started in dom0, and a process named *qrexec-agent* is started in the VM. They are connected over *vchan* channel. *qrexec-daemon* listens on the the unix socket */var/run/qubes/qrexec.XID* for connections from dom0 utility named *qrexec-client*. Typically, the first thing that a *qrexec-client* instance does is to send a request to *qrexec-agent* to start a process (let's name it VMprocess) with a given command line. Since then, stdin/stdout/stderr from the VMprocess is passed via *qrexec-daemon* and *qrexec-agent* to the *qrexec-client* process.

So, for example, executing in dom0

*qrexec-client -d someVM user:bash//*

allows to work with the remote shell. The string before first semicolon specifies what user to run the command as. Adding *-e* on the *qrexec-client* command line results in mere command execution (no data passing), and *qrexec-client* exits immediately after sending the execution request. There is also the *-l local\_program* flag - with it, *qrexec-client* passes stdin/stdout of the remote program not to its stdin/stdout, but to the (spawned for this purpose) *local\_program*.

The *qvm-run* command is heavily based on *qrexec-client*. It also takes care for additional activities, e.g. starting the domain if it is not up yet, and starting the GUI daemon. Thus, it is usually more convenient to use *qvm-run*.

There can be almost arbitrary number of *qrexec-client* processes for a domain (so, connected to the same *qrexec-daemon*, same domain) - their data is multiplexed independently.

Qubes RPC basics
----------------

Some tasks (like intervm file copy) share the same rpc-like structure: a process in one VM (say, file sender) needs to invoke and pass/receive data to some process in other VM (say, file receiver). Thus, the Qubes RPC framework was written, facilitating such actions.

Obviously, such interVM communication must be tightly controlled, to prevent one VM from taking control over other, possibly more privileged, VM. Therefore the design decision was made to pass all communication via dom0, that can enforce proper authorization. Then, it is natural to reuse the already-existing qrexec framework. As basically it provides only dom0\<-\>VM channel, then we need to glue two qrexec connections in order to provide VM\<-\>VM channel.

Also, note that bare qrexec provides VM\<-\>dom0 connectivity, but the command execution is always initiated by dom0. There are cases when VM needs to invoke and send data to a command in dom0 (e.g. to pass information on newly installed .desktop files). Thus, the framework allows dom0 to be the rpc target as well.

Thanks to the framework, RPC programs are very simple - both rpc client and server just use their stdin/stdout to pass data. The framework does all the inner work to connect these file descriptors to each other via *qrexec-daemon* and *qrexec-agent*. Additionally, disposable VMs are tightly integrated - rpc to a disposableVM is identical to rpc to a normal domain, all one needs is to pass "\$dispvm" as the remote domain name.

Qubes RPC administration
------------------------

In dom0, there is a bunch of files in */etc/qubes-rpc/policy* directory, whose names describe the available rpc actions; their content is the rpc access policy database. Currently defined actions are:

-   qubes.Filecopy
-   qubes.OpenInVM
-   qubes.[ReceiveUpdates?](/wiki/ReceiveUpdates)
-   qubes.[SyncAppMenus?](/wiki/SyncAppMenus)
-   qubes.VMShell
-   qubes.[ClipboardPaste?](/wiki/ClipboardPaste)
-   qubes.Gpg
-   qubes.[NotifyUpdates?](/wiki/NotifyUpdates)
-   qubes.[PdfConvert?](/wiki/PdfConvert)

These files contain lines with the following format:

srcvm destvm (allow|deny|ask)[,user=user\_to\_run\_as][,target=VM\_to\_redirect\_to]

You can specify srcvm and destvm by name, or by one of "\$anyvm", "\$dispvm", "dom0" reserved keywords (note string "dom0" does not match the \$anyvm pattern; all other names do). Only "\$anyvm" keyword makes sense in srcvm field (service calls from dom0 are currently always allowed, "\$dispvm" means "new VM created for this particular request" - so it is never a source of request). Currently there is no way to specify source VM by type. Whenever a rpc request for action X is received, the first line in /etc/qubes-rpc/policy/X that match srcvm/destvm is consulted to determine whether to allow rpc, what user account the program should run in target VM under, and what VM to redirect the execution to. If the policy file does not exits, user is prompted to create one; if still there is no policy file after prompting, the action is denied.

On target VM, the */etc/qubes-rpc/RPC\_ACTION\_NAME* must exist, containing the file name of the program that will be invoked.

On src VM, one should invoke the client via

*/usr/lib/qubes/qrexec-client-vm target\_vm\_name RPC\_ACTION\_NAME rpc\_client\_path client arguments*

Note that only stdin/stdout is passed between rpc server and client - notably, the no cmdline argument are passed. Source VM name is given by QREXEC\_REMOTE\_DOMAIN environment variable. By default, stderr of client and server is logged to respective /var/log/qubes/qrexec.XID files.

Be very careful when coding and adding a new rpc service. Unless the offered functionality equals full control over the target (it is the case with e.g. qubes.VMShell action), any vulnerability in a rpc server can be fatal to qubes security. On the other hand, this mechanism allows to delegate processing of untrusted input to less privileged (or throwaway) AppVMs, thus wise usage of it increases security.

### Qubes RPC example

We will show the necessary files to create rpc call that adds two integers on the target and returns back the result to the invoker.

-   rpc client code (*/usr/bin/our\_test\_add\_client*)

    ``` {.wiki}
    #!/bin/sh
    echo $1 $2    # pass data to rpc server
    exec cat >&$SAVED_FD_1 # print result to the original stdout, not to the other rpc endpoint
    ```

-   rpc server code (*/usr/bin/our\_test\_add\_server*)

    ``` {.wiki}
    #!/bin/sh
    read arg1 arg2 # read from stdin, which is received from the rpc client
    echo $(($arg1+$arg2)) # print to stdout - so, pass to the rpc client
    ```

-   policy file in dom0 (*/etc/qubes-rpc/policy/test.Add* )

    ``` {.wiki}
    $anyvm $anyvm ask
    ```

-   server path definition ( */etc/qubes-rpc/test.Add*)

    ``` {.wiki}
    /usr/bin/our_test_add_server
    ```

-   invoke rpc via

    ``` {.wiki}
    /usr/lib/qubes/qrexec-client-vm target_vm test.Add /usr/bin/our_test_add_client 1 2
    ```

and we should get "3" as answer, after dom0 allows it.

Qubes RPC internals
-------------------

When an user in VM executes the */usr/lib/qubes/qrexec-client-vm* utility, the following steps are taken:

-   *qrexec-client-vm* connects to *qrexec-agent's* */var/run/qubes/qrexec-agent-fdpass* unix socket 3 times. Reads 4 bytes from each of them, which is the fd number of the accepted socket in agent. These 3 integers, in text, concatenated, form "connection identifier" (CID)
-   *qrexec-client-vm* writes to */var/run/qubes/qrexec-agent* fifo a blob, consisting of target vmname, rpc action, and CID
-   *qrexec-client-vm* executes the rpc client, passing the above mentioned unix sockets as process stdin/stdout, and optionally stderr (if the PASS\_LOCAL\_STDERR env variable is set)
-   *qrexec-agent* passes the blob to *qrexec-daemon*, via MSG\_AGENT\_TO\_SERVER\_TRIGGER\_CONNECT\_EXISTING message over vchan
-   *qrexec-daemon* executes *qrexec-policy*, passing source vmname, target vmname, rpc action, and CID as cmdline arguments
-   *qrexec-policy* evaluates the policy file. If successful, creates a pair of *qrexec-client* processes, whose stdin/stdout are cross-connencted.
    -   The first *qrexec-client* connects to the src VM, using the *-c CID* parameter, which results in not creating a new process, but connecting to the existing process file descriptors (these are the fds of unix socket created in step 1).
    -   The second *qrexec-client* connects to the target VM, and executes *qubes-rpc-multiplexer* command there with the rpc action as the cmdline argument. Finally, *qubes-rpc-multiplexer* executes the correct rpc server on the target.
-   In the above step, if the target VM is *\$dispvm*, the dispvm is created via the *qfile-daemon-dvm* program. The latter waits for the *qrexec-client* process to exit, and then destroys the dispvm.

[![No image "qubes\_rpc.png" attached to Qrexec](/chrome/common/attachment.png "No image "qubes_rpc.png" attached to Qrexec")](/attachment/wiki/Qrexec/qubes_rpc.png)
