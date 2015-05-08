---
layout: doc
title: Qrexec
permalink: /doc/Qrexec/
redirect_from: /wiki/Qrexec/
---

Command execution in VM (and Qubes RPC)
=======================================

Qubes **qrexec** is a framework for implementing inter-VM (incl. Dom0-VM) services. It offers a mechanism to start programs in VMs, redirect their stdin/stdout, and a policy framework to control this all.

Basic Dom0-VM command execution
-------------------------------

During domain creation a process named `qrexec-daemon` is started in dom0, and a process named `qrexec-agent` is started in the VM. They are connected over `vchan` channel.

Typically, the first thing that a `qrexec-client` instance does is to send a request to `qrexec-agent` to start a process in the VM. Since then, the stdin/stdout/stderr from this remote process is passed to the `qrexec-client` process.

E.g. to start a primitive shell in a VM type the following in Dom0 console:

{% highlight trac-wiki %}
[user@dom0 ~]$ /usr/lib/qubes/qrexec-client -d <vm name> user:bash
{% endhighlight %}

The string before first semicolon specifies what user to run the command as.

Adding `-e` on the `qrexec-client` command line results in mere command execution (no data passing), and `qrexec-client` exits immediately after sending the execution request.

There is also the `-l <local program>` flag, which directs `qrexec-client` to pass stdin/stdout of the remote program not to its stdin/stdout, but to the (spawned for this purpose) `<local program>`.

The `qvm-run` command is heavily based on `qrexec-client`. It also takes care for additional activities, e.g. starting the domain if it is not up yet, and starting the GUI daemon. Thus, it is usually more convenient to use `qvm-run`.

There can be almost arbitrary number of `qrexec-client` processes for a domain (so, connected to the same `qrexec-daemon`, same domain) - their data is multiplexed independently.

There is a similar command line utility avilable inside Linux AppVMs (note the `-vm` suffix): `qrexec-client-vm` that will be described in subsequent sections.

Qubes Inter-VM Services (Qubes RPC)
-----------------------------------

Apart from simple Dom0-\>VM command executions, as discussed above, it is also useful to have more advanced infrastructure for controlled inter-VM RPC/services. This might be used for simple things like inter-VM file copy operations, as well as more complex tasks like starting a Disposable VM, and requesting it to do certain operations on a handed file(s).

Instead of implementing complex RPC-like mechanisms for inter-VM communication, Qubes takes a much simpler and pragmatic approach and aims to only provide simple *pipes* between the VMs, plus ability to request *pre-defined* programs (servers) to be started on the other end of such pipes, and a centralized policy (enforced in Dom0) which says which VMs can request what services from what VMs.

Thanks to the framework and automatic stdin/stdout redirection, RPC programs are very simple - both the client and server just use their stdin/stdout to pass data. The framework does all the inner work to connect these file descriptors to each other via `qrexec-daemon` and `qrexec-agent`. Additionally, disposable VMs are tightly integrated - RPC to a DisposableVM is a simple matter of using a magic `$dispvm` keyword as the target VM name.

All services in Qubes are identified by a single string, which by convention takes a form of `qubes.ServiceName`. Each VM can provide handlers for each of the known services by providing a file in `/etc/qubes-rpc/` directory with the same name as the service it is supposed to handle. This file will be then executed by the qrexec service, if the Dom0 policy allowed service to be requested (see below). Typically the files in `/etc/qubes-rpc/` contain just one line, which is a path to the specific binary that acts as a server for the incoming request, however they might also be the actual executable themselves. Qrexec framework takes care about connecting the stdin/stdout of the server provess with the corresponding stdin/stdout of the requesting process in the requesting VM (see example Hello World service described below).

Qubes Services (RPC) policy
---------------------------

Besides each VM needing to provide explicit programs to serve each supported service, the inter-VM service RPC is also governed by a central policy in Dom0.

In dom0, there is a bunch of files in `/etc/qubes-rpc/policy/` directory, whose names describe the available RPC actions; their content is the RPC access policy database. Some example of the default services in Qubes are:

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

{% highlight trac-wiki %}
srcvm destvm (allow|deny|ask)[,user=user_to_run_as][,target=VM_to_redirect_to]
{% endhighlight %}

You can specify `srcvm` and `destvm` by name, or by one of `$anyvm`, `$dispvm`, `dom0` reserved keywords (note string `dom0` does not match the `$anyvm` pattern; all other names do). Only `$anyvm` keyword makes sense in the `srcvm` field (service calls from dom0 are currently always allowed, `$dispvm` means "new VM created for this particular request" - so it is never a source of request). Currently there is no way to specify source VM by type, but this is planned for Qubes R3.

Whenever a RPC request for service named "XYZ" is received, the first line in `/etc/qubes-rpc/policy/XYZ` that matches the actual `srcvm`/`destvm` is consulted to determine whether to allow RPC, what user account the program should run in target VM under, and what VM to redirect the execution to. If the policy file does not exits, user is prompted to create one *manually*; if still there is no policy file after prompting, the action is denied.

On the target VM, the `/etc/qubes-rpc/XYZ` must exist, containing the file name of the program that will be invoked.

Requesting VM-VM (and VM-Dom0) services execution
-------------------------------------------------

On src VM, one should invoke the qrexec client via the follwing command:

{% highlight trac-wiki %}
/usr/lib/qubes/qrexec-client-vm <target vm name> <service name> <local program path> [local program arguments]`
{% endhighlight %}

Note that only stdin/stdout is passed between RPC server and client - notably, no cmdline argument are passed.

The source VM name can be accessed in the server process via QREXEC\_REMOTE\_DOMAIN environment variable. (Note the source VM has *no* control over the name provided in this variable -- the name of the VM is provided by Dom0, and so is trusted).

By default, stderr of client and server is logged to respective `/var/log/qubes/qrexec.XID` files, in each of the VM.

Be very careful when coding and adding a new RPC service! Any vulnerability in a RPC server can be fatal to security of the target VM!

Requesting VM-VM (and VM-Dom0) services execution (without cmdline helper)
--------------------------------------------------------------------------

Connect directly to `/var/run/qubes/qrexec-agent-fdpass` socket as described [here](https://wiki.qubes-os.org/wiki/Qrexec2Implementation#Allthepiecestogetheratwork).

### Revoking "Yes to All" authorization

Qubes RPC policy supports the "ask" action. This will prompt the user whether a given RPC call should be allowed. That prompt window has an option to click "Yes to All", which allows the action and adds a new entry to the policy file, which will unconditionally allow further calls for given service-srcVM-dstVM tuple.

In order to remove such authorization, issue this command from a Dom0 terminal (example below for qubes.Filecopy service):

{% highlight trac-wiki %}
sudo nano /etc/qubes-rpc/policy/qubes.Filecopy
{% endhighlight %}

and then remove the first line/s (before the first \#\# comment) which are the "Yes to All" results.

### Qubes RPC "Hello World" service

We will show the necessary files to create a simple RPC call that adds two integers on the target VM and returns back the result to the invoking VM.

-   Client code on source VM (`/usr/bin/our_test_add_client`)

{% highlight trac-wiki %}
#!/bin/sh
echo $1 $2    # pass data to rpc server
exec cat >&$SAVED_FD_1 # print result to the original stdout, not to the other rpc endpoint
{% endhighlight %}

-   Server code on target VM (`/usr/bin/our_test_add_server`)

{% highlight trac-wiki %}
#!/bin/sh
read arg1 arg2 # read from stdin, which is received from the rpc client
echo $(($arg1+$arg2)) # print to stdout - so, pass to the rpc client
{% endhighlight %}

-   Policy file in dom0 (`/etc/qubes-rpc/policy/test.Add`)

{% highlight trac-wiki %}
$anyvm $anyvm ask
{% endhighlight %}

-   Server path definition on target VM (`/etc/qubes-rpc/test.Add`)

{% highlight trac-wiki %}
/usr/bin/our_test_add_server
{% endhighlight %}

-   To test this service, run the following in the source VM:

{% highlight trac-wiki %}
/usr/lib/qubes/qrexec-client-vm <target VM> test.Add /usr/bin/our_test_add_client 1 2
{% endhighlight %}

and we should get "3" as answer, provided dom0 policy allows the call to pass through, which would happen after we click "Yes" in the popup that should appear after the invocation of this command. If we changed the policy from "ask" to "allow", then no popup should be presented, and the call will always be allowed.

More high-level RPCs?
---------------------

As previously noted, Qubes aims to provide mechanisms that are very simple and thus with very small attack surface. This is the reason why the inter-VM RPC framework is very primitive and doesn't include any serialization or other function arguments passing, etc. We should remember, however, that users/app developers are always free to run more high-level RPC protocols on top of qrexec. Care should be taken, however, to consider potential attack surfaces that are exposed to untrusted or less trusted VMs in that case.

Qubes RPC internals
-------------------

The internal implementation of qrexec in Qubes R2 is described [here](/wiki/Qrexec2Implementation), and in Qubes R3 [here](/wiki/Qrexec3Implementation).
