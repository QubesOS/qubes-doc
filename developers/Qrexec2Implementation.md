---
layout: doc
title: Qrexec2Implementation
permalink: /en/doc/qrexec2-implementation/
redirect_from:
- /doc/Qrexec2Implementation/
- /wiki/Qrexec2Implementation/
---

Implementation of qrexec in Qubes R2
====================================

This page describes implementation of the [qrexec framework](/doc/Qrexec/) in Qubes OS R2. Note that the implementation has changed significantly in Qubes R3 (see [Qrexec3Implementation](/doc/Qrexec3Implementation/)), although the user API reminded backwards compatible (i.e. qrexec apps written for Qubes R2 should run without modifications on Qubes R3).

Dom0 tools implementation
-------------------------

Players:

-   `/usr/lib/qubes/qrexec-daemon` \<- started by mgmt stack (qubes.py) when a VM is started.
-   `/usr/lib/qubes/qrexec-policy` \<- internal program used to evaluate the policy file and making the 2nd half of the connection.
-   `/usr/lib/qubes/qrexec-client` \<- raw command line tool that talks to the daemon via unix socket (`/var/run/qubes/qrexec.XID`)

Note: none of the above tools are designed to be used by users.

Linux VMs implementation
------------------------

Players:

-   `/usr/lib/qubes/qrexec-agent` \<- started by VM bootup scripts, a daemon.
-   `/usr/lib/qubes/qubes-rpc-multiplexer` \<- executes the actual service program, as specified in VM's `/etc/qubes-rpc/qubes.XYZ`.
-   `/usr/lib/qubes/qrexec-client-vm` \<- raw command line tool that talks to the agent.

Note: none of the above tools are designed to be used by users. `qrexec-client-vm` is designed to be wrapped up by Qubes apps.

Windows VMs implemention
------------------------

%QUBES\_DIR% is the installation path (`c:\Program Files\Invisible Things Lab\Qubes OS Windows Tools` by default).

-   `%QUBES_DIR%\bin\qrexec-agent.exe` \<- runs as a system service. Responsible both for raw command execution and interpreting RPC service requests.
-   `%QUBES_DIR%\qubes-rpc` \<- directory with `qubes.XYZ` files that contain commands for executing RPC services. Binaries for the services are contained in `%QUBES_DIR%\qubes-rpc-services`.
-   `%QUBES_DIR%\bin\qrexec-client-vm` \<- raw command line tool that talks to the agent.

Note: neither of the above tools are designed to be used by users. `qrexec-client-vm` is designed to be wrapped up by Qubes apps.

All the pieces together at work
-------------------------------

Note: this section is not needed to use qrexec for writing Qubes apps. Also note the qrexec framework implemention in Qubes R3 significantly differs from what is described in this section.

The VM-VM channels in Qubes R2 are made via "gluing" two VM-Dom0 and Dom0-VM vchan connections:

![qrexec2-internals.png](/attachment/wiki/Qrexec2Implementation/qrexec2-internals.png)

Note: Dom0 never examines the actual data flowing in neither of the two vchan connections.

When a user in a source VM executes `qrexec-client-vm` utility, the following steps are taken:

-   `qrexec-client-vm` connects to `qrexec-agent`'s `/var/run/qubes/qrexec-agent-fdpass` unix socket 3 times. Reads 4 bytes from each of them, which is the fd number of the accepted socket in agent. These 3 integers, in text, concatenated, form "connection identifier" (CID)
-   `qrexec-client-vm` writes to `/var/run/qubes/qrexec-agent` fifo a blob, consisting of target vmname, rpc action, and CID
-   `qrexec-client-vm` executes the rpc client, passing the above mentioned unix sockets as process stdin/stdout, and optionally stderr (if the PASS\_LOCAL\_STDERR env variable is set)
-   `qrexec-agent` passes the blob to `qrexec-daemon`, via MSG\_AGENT\_TO\_SERVER\_TRIGGER\_CONNECT\_EXISTING message over vchan
-   `qrexec-daemon` executes `qrexec-policy`, passing source vmname, target vmname, rpc action, and CID as cmdline arguments
-   `qrexec-policy` evaluates the policy file. If successful, creates a pair of `qrexec-client` processes, whose stdin/stdout are cross-connencted.
    -   The first `qrexec-client` connects to the src VM, using the `-c ClientID` parameter, which results in not creating a new process, but connecting to the existing process file descriptors (these are the fds of unix socket created in step 1).
    -   The second `qrexec-client` connects to the target VM, and executes `qubes-rpc-multiplexer` command there with the rpc action as the cmdline argument. Finally, `qubes-rpc-multiplexer` executes the correct rpc server on the target.
-   In the above step, if the target VM is `$dispvm`, the DispVM is created via the `qfile-daemon-dvm` program. The latter waits for the `qrexec-client` process to exit, and then destroys the DispVM.

Protocol description ("wire-level" spec)
----------------------------------------

TODO
