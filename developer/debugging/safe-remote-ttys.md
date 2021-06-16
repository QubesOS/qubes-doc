---
lang: en
layout: doc
permalink: /doc/safe-remote-ttys/
redirect_from:
- /en/doc/safe-remote-ttys/
ref: 49
---

Safe Remote Dom0 Terminals
==========================

If you do not have working graphics in Dom0, then using a terminal can be quite annoying!
This was the case for the author while trying to debug PCI-passthrough of a machine's primary (only) GPU.

Your first thought might be to just allow network access to Dom0, enable ssh, and connect in remotely.
But, this gravely violates the Qubes security model.

Instead, a better solution is to split the input and output paths of using a terminal.
Use your normal keyboard for input, but have the output go to a remote machine in a unidirectional manner.

To do this, we make use of script(1), qvm-run, and optionally your network transport of choice.

To a different VM
-----------------

As an example of forwarding terminal output to another VM on the same machine:

~~~
$ mkfifo /tmp/foo
$ qvm-run -p some-vm 'xterm -e "cat 0<&5" 5<&0' </tmp/foo >/dev/null 2>&1 &
$ script -f /tmp/foo
~~~

To a different machine
----------------------

In this case over SSH (from a network-connected VM):

~~~
$ mkfifo /tmp/foo
$ qvm-run -p some-vm \
    'ssh user@host sh -c "DISPLAY=:0 xterm -e \"cat 0<&5\" 5<&0"' \
    </tmp/foo >/dev/null 2>&1 &
$ script -f /tmp/foo
~~~

Note that no data received over SSH is ever treated as terminal input in Dom0.
The input path remains only from your trusted local keyboard.

Multiple terminals
------------------

For multiple terminals, you may find it easier to just use tmux than to try to blindly switch to the correct window.

Terminal size
-------------

It is up to you to ensure the sizes of the local and remote terminal are the same, otherwise things may display incorrectly (especially in interactive programs).
Depending on your shell, the size of your local (blind) terminal is likely stored in the `$LINES` and `$COLUMNS` variables.

~~~
$ echo $COLUMNS $LINES
80 24
~~~

A note on serial consoles
-------------------------

If your machine has a serial console, you may with to use that, but note that a similar split-I/O model should be used to ensure Dom0 integrity.
If you use the serial console as normal (via e.g. getty on ttyX, and logging in as normal), then the machine at the end of the serial cable could compromise your machine!
Ideally, you would take input from your trusted keyboard, and only send the output over the serial cable via e.g. disabling getty and using:

~~~
script -f /dev/ttyS0
~~~

You don't even need to connect the TX pin.
