---
layout: doc
title: Qrexec3
permalink: /doc/qrexec3/
redirect_from:
- /en/doc/qrexec3/
- /doc/Qrexec3/
- /wiki/Qrexec3/
---

Command execution in VM (and Qubes RPC)
=======================================

*[Note: this documents describes Qrexec v3 (Odyssey)]*

Qrexec framework is used by core Qubes components to implement communication between domains. Qubes domains are isolated by design but there is a need for a mechanism to allow administrative domain (dom0) to force command execution in another domain (VM). For instance, when user selects an application from KDE menu, it should be started in the selected VM. Also it is often useful to be able to pass stdin/stdout/stderr from an application running in VM to dom0 (and the other way around). In specific circumstances Qubes allows VMs to be initiators of such communication (so for example a VM can notify dom0 that there are updates available for it).

Qrexec basics
-------------

Qrexec is built on top of vchan (a library providing data links between VMs). During domain creation a process named *qrexec-daemon* is started in dom0, and a process named *qrexec-agent* is started in the VM. They are connected over *vchan* channel. *qrexec-daemon* listens for connections from dom0 utility named *qrexec-client*. Typically, the first thing that a *qrexec-client* instance does is to send a request to *qrexec-daemon* to start a process (let's name it VMprocess) with a given command line in a specified VM (someVM). *qrexec-daemon* assigns unique vchan connection details and sends them both to *qrexec-client* (in dom0) and *qrexec-agent* (in someVM). *qrexec-client* starts a vchan server which *qrexec-agent* connects to. Since then, stdin/stdout/stderr from the VMprocess is passed via vchan between *qrexec-agent* and the *qrexec-client* process.

So, for example, executing in dom0

`qrexec-client -d someVM user:bash`

allows to work with the remote shell. The string before the first semicolon specifies what user to run the command as. Adding `-e` on the *qrexec-client* command line results in mere command execution (no data passing), and *qrexec-client* exits immediately after sending the execution request and receiving status code from *qrexec-agent* (whether the process creation succeeded). There is also the `-l local_program` flag -- with it, *qrexec-client* passes stdin/stdout of the remote process to the (spawned for this purpose) *local\_program*, not to its own stdin/stdout.

The `qvm-run` command is heavily based on *qrexec-client*. It also takes care of additional activities, e.g. starting the domain if it is not up yet and starting the GUI daemon. Thus, it is usually more convenient to use `qvm-run`.

There can be almost arbitrary number of *qrexec-client* processes for a domain (so, connected to the same *qrexec-daemon*, same domain) -- their data is multiplexed independently. Number of available vchan channels is the limiting factor here, it depends on the underlying hypervisor.

Qubes RPC services
------------------

Some tasks (like intervm file copy) share the same rpc-like structure: a process in one VM (say, file sender) needs to invoke and send/receive data to some process in other VM (say, file receiver). Thus, the Qubes RPC framework was created, facilitating such actions.

Obviously, inter-VM communication must be tightly controlled to prevent one VM from taking control over other, possibly more privileged, VM. Therefore the design decision was made to pass all control communication via dom0, that can enforce proper authorization. Then, it is natural to reuse the already-existing qrexec framework.

Also, note that bare qrexec provides VM\<-\>dom0 connectivity, but the command execution is always initiated by dom0. There are cases when VM needs to invoke and send data to a command in dom0 (e.g. to pass information on newly installed .desktop files). Thus, the framework allows dom0 to be the rpc target as well.

Thanks to the framework, RPC programs are very simple -- both rpc client and server just use their stdin/stdout to pass data. The framework does all the inner work to connect these processes to each other via *qrexec-daemon* and *qrexec-agent*. Additionally, disposable VMs are tightly integrated -- rpc to a disposableVM is identical to rpc to a normal domain, all one needs is to pass "\$dispvm" as the remote domain name.

Qubes RPC administration
------------------------

[TODO: fix for non-linux dom0]

In dom0, there is a bunch of files in */etc/qubes-rpc/policy* directory, whose names describe the available rpc actions; their content is the rpc access policy database. Currently defined actions are:

-   qubes.Filecopy
-   qubes.OpenInVM
-   qubes.ReceiveUpdates
-   qubes.SyncAppMenus
-   qubes.VMShell
-   qubes.ClipboardPaste
-   qubes.Gpg
-   qubes.NotifyUpdates
-   qubes.PdfConvert

These files contain lines with the following format:

srcvm destvm (allow|deny|ask)[,user=user\_to\_run\_as][,target=VM\_to\_redirect\_to]

You can specify srcvm and destvm by name, or by one of "\$anyvm", "\$dispvm", "dom0" reserved keywords (note string "dom0" does not match the \$anyvm pattern; all other names do). Only "\$anyvm" keyword makes sense in srcvm field (service calls from dom0 are currently always allowed, "\$dispvm" means "new VM created for this particular request" - so it is never a source of request). Currently there is no way to specify source VM by type. Whenever a rpc request for action X is received, the first line in /etc/qubes-rpc/policy/X that match srcvm/destvm is consulted to determine whether to allow rpc, what user account the program should run in target VM under, and what VM to redirect the execution to. If the policy file does not exits, user is prompted to create one; if still there is no policy file after prompting, the action is denied.

In the target VM, the */etc/qubes-rpc/RPC\_ACTION\_NAME* must exist, containing the file name of the program that will be invoked.

In the src VM, one should invoke the client via

`/usr/lib/qubes/qrexec-client-vm target_vm_name RPC_ACTION_NAME rpc_client_path client arguments`

Note that only stdin/stdout is passed between rpc server and client -- notably, no command line argument are passed. Source VM name is specified by QREXEC\_REMOTE\_DOMAIN environment variable. By default, stderr of client and server is logged to respective /var/log/qubes/qrexec.XID files.

Be very careful when coding and adding a new rpc service. Unless the offered functionality equals full control over the target (it is the case with e.g. qubes.VMShell action), any vulnerability in a rpc server can be fatal to qubes security. On the other hand, this mechanism allows to delegate processing of untrusted input to less privileged (or throwaway) AppVMs, thus wise usage of it increases security.

### Revoking "Yes to All" authorization

Qubes RPC policy supports "ask" action. This will prompt the user whether given RPC call should be allowed. That prompt window has also "Yes to All" option, which will allow the action and add new entry to the policy file, which will unconditionally allow further calls for given service-srcVM-dstVM tuple.

In order to remove such authorization, issue this command from a Dom0 terminal (for qubes.Filecopy service):

`sudo nano /etc/qubes-rpc/policy/qubes.Filecopy`

and then remove the first line/s (before the first \#\# comment) which are the "Yes to All" results.

### Qubes RPC example

We will show the necessary files to create rpc call that adds two integers on the target and returns back the result to the invoker.

-   rpc client code (*/usr/bin/our\_test\_add\_client*)

    ~~~
    #!/bin/sh
    echo $1 $2    # pass data to rpc server
    exec cat >&$SAVED_FD_1 # print result to the original stdout, not to the other rpc endpoint
    ~~~

-   rpc server code (*/usr/bin/our\_test\_add\_server*)

    ~~~
    #!/bin/sh
    read arg1 arg2 # read from stdin, which is received from the rpc client
    echo $(($arg1+$arg2)) # print to stdout - so, pass to the rpc client
    ~~~

-   policy file in dom0 (*/etc/qubes-rpc/policy/test.Add* )

    ~~~
    $anyvm $anyvm ask
    ~~~

-   server path definition ( */etc/qubes-rpc/test.Add*)

    ~~~
    /usr/bin/our_test_add_server
    ~~~

-   invoke rpc via

    ~~~
    /usr/lib/qubes/qrexec-client-vm target_vm test.Add /usr/bin/our_test_add_client 1 2
    ~~~

and we should get "3" as answer, after dom0 allows it.

Qubes RPC internals
-------------------

See [QrexecProtocol?](/doc/QrexecProtocol/).
