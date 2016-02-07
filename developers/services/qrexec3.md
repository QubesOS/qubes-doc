---
layout: doc
title: Qrexec3
permalink: /doc/qrexec3/
redirect_from:
- /en/doc/qrexec3/
- /doc/Qrexec3/
- /wiki/Qrexec3/
- /doc/qrexec/
- /en/doc/qrexec/
- /doc/Qrexec/
- /wiki/Qrexec/
- /doc/qrexec3-implementation/
- /en/doc/qrexec3-implementation/
- /doc/Qrexec3Implementation/
- /wiki/Qrexec3Implementation/
---

# Command execution in VMs #

(*This page is about qrexec v3. For qrexec v2, see
[here](/doc/qrexec2/).*)

The **qrexec** framework is used by core Qubes components to implement
communication between domains. Qubes domains are isolated by design, but
there is a need for a mechanism to allow the administrative domain (dom0) to
force command execution in another domain (VM). For instance, when user
selects an application from the KDE menu, it should be started in the selected
VM. Also, it is often useful to be able to pass stdin/stdout/stderr from an
application running in a VM to dom0 (and the other way around). In specific
circumstances, Qubes allows VMs to be initiators of such communications (so,
for example, a VM can notify dom0 that there are updates available for it).


## Qrexec basics ##

Qrexec is built on top of vchan (a library providing data links between
VMs). During domain creation a process named `qrexec-daemon` is started
in dom0, and a process named `qrexec-agent` is started in the VM. They are
connected over **vchan** channel. `qrexec-daemon` listens for connections
from dom0 utility named `qrexec-client`. Typically, the first thing that a
`qrexec-client` instance does is to send a request to `qrexec-daemon` to
start a process (let's name it `VMprocess`) with a given command line in
a specified VM (`someVM`). `qrexec-daemon` assigns unique vchan connection
details and sends them both to `qrexec-client` (in dom0) and `qrexec-agent`
(in `someVM`). `qrexec-client` starts a vchan server which `qrexec-agent`
connects to. Since then, stdin/stdout/stderr from the VMprocess is passed
via vchan between `qrexec-agent` and the `qrexec-client` process.

So, for example, executing in dom0:

    qrexec-client -d someVM user:bash

allows to work with the remote shell. The string before the first
semicolon specifies what user to run the command as. Adding `-e` on the
`qrexec-client` command line results in mere command execution (no data
passing), and `qrexec-client` exits immediately after sending the execution
request and receiving status code from `qrexec-agent` (whether the process
creation succeeded). There is also the `-l local_program` flag -- with it,
`qrexec-client` passes stdin/stdout of the remote process to the (spawned
for this purpose) `local_program`, not to its own stdin/stdout.

The `qvm-run` command is heavily based on `qrexec-client`. It also takes care
of additional activities, e.g. starting the domain if it is not up yet and
starting the GUI daemon. Thus, it is usually more convenient to use `qvm-run`.

There can be almost arbitrary number of `qrexec-client` processes for a
domain (so, connected to the same `qrexec-daemon`, same domain) -- their
data is multiplexed independently. Number of available vchan channels is
the limiting factor here, it depends on the underlying hypervisor.


## Qubes RPC services ##

Some tasks (like inter-vm file copy) share the same rpc-like structure:
a process in one VM (say, file sender) needs to invoke and send/receive
data to some process in other VM (say, file receiver). Thus, the Qubes RPC
framework was created, facilitating such actions.

Obviously, inter-VM communication must be tightly controlled to prevent one
VM from taking control over other, possibly more privileged, VM. Therefore
the design decision was made to pass all control communication via dom0,
that can enforce proper authorization. Then, it is natural to reuse the
already-existing qrexec framework.

Also, note that bare qrexec provides `VM <-> dom0` connectivity, but the
command execution is always initiated by dom0. There are cases when VM needs
to invoke and send data to a command in dom0 (e.g. to pass information on
newly installed `.desktop` files). Thus, the framework allows dom0 to be
the rpc target as well.

Thanks to the framework, RPC programs are very simple -- both rpc client
and server just use their stdin/stdout to pass data. The framework does all
the inner work to connect these processes to each other via `qrexec-daemon`
and `qrexec-agent`. Additionally, disposable VMs are tightly integrated --
rpc to a DisposableVM is identical to rpc to a normal domain, all one needs
is to pass `$dispvm` as the remote domain name.


## Qubes RPC administration ##

(*TODO: fix for non-linux dom0*)

In dom0, there is a bunch of files in `/etc/qubes-rpc/policy` directory,
whose names describe the available rpc actions. Their content is the rpc
access policy database. Currently defined actions are:

    qubes.Filecopy
    qubes.OpenInVM
    qubes.ReceiveUpdates
    qubes.SyncAppMenus
    qubes.VMShell
    qubes.ClipboardPaste
    qubes.Gpg
    qubes.NotifyUpdates
    qubes.PdfConvert

These files contain lines with the following format:

    srcvm destvm (allow|deny|ask)[,user=user_to_run_as][,target=VM_to_redirect_to]

You can specify srcvm and destvm by name, or by one of `$anyvm`, `$dispvm`,
`dom0` reserved keywords (note string `dom0` does not match the `$anyvm`
pattern; all other names do). Only `$anyvm` keyword makes sense in srcvm
field (service calls from dom0 are currently always allowed, `$dispvm`
means "new VM created for this particular request," so it is never a
source of request). Currently there is no way to specify source VM by
type. Whenever a rpc request for action X is received, the first line in
`/etc/qubes-rpc/policy/X` that match srcvm/destvm is consulted to determine
whether to allow rpc, what user account the program should run in target
VM under, and what VM to redirect the execution to. If the policy file does
not exits, user is prompted to create one; if still there is no policy file
after prompting, the action is denied.

In the target VM, the `/etc/qubes-rpc/RPC_ACTION_NAME` must exist, containing
the file name of the program that will be invoked.

In the src VM, one should invoke the client via:

    /usr/lib/qubes/qrexec-client-vm target_vm_name RPC_ACTION_NAME rpc_client_path client arguments

Note that only stdin/stdout is passed between rpc server and client --
notably, no command line argument are passed. Source VM name is specified by
`QREXEC_REMOTE_DOMAIN` environment variable. By default, stderr of client
and server is logged to respective `/var/log/qubes/qrexec.XID` files.

Be very careful when coding and adding a new rpc service. Unless the
offered functionality equals full control over the target (it is the case
with e.g. `qubes.VMShell` action), any vulnerability in a rpc server can
be fatal to Qubes security. On the other hand, this mechanism allows to
delegate processing of untrusted input to less privileged (or throwaway)
AppVMs, thus wise usage of it increases security.


### Revoking "Yes to All" authorization ###

Qubes RPC policy supports "ask" action. This will prompt the user whether given
RPC call should be allowed. That prompt window has also "Yes to All" option,
which will allow the action and add new entry to the policy file, which will
unconditionally allow further calls for given service-srcVM-dstVM tuple.

In order to remove such authorization, issue this command from a dom0 terminal
(for `qubes.Filecopy` service):

    sudo nano /etc/qubes-rpc/policy/qubes.Filecopy

and then remove the first line(s) (before the first `##` comment) which are
the "Yes to All" results.


### Qubes RPC example ###

We will show the necessary files to create rpc call that adds two integers
on the target and returns back the result to the invoker.

 * rpc client code (`/usr/bin/our_test_add_client`):

       #!/bin/sh
       echo $1 $2    # pass data to rpc server
       exec cat >&$SAVED_FD_1 # print result to the original stdout, not to the other rpc endpoint

 * rpc server code (*/usr/bin/our\_test\_add\_server*)

       #!/bin/sh
       read arg1 arg2 # read from stdin, which is received from the rpc client
       echo $(($arg1+$arg2)) # print to stdout - so, pass to the rpc client

 * policy file in dom0 (*/etc/qubes-rpc/policy/test.Add* )

       $anyvm $anyvm ask

 * server path definition ( */etc/qubes-rpc/test.Add*)

       /usr/bin/our_test_add_server

 * invoke rpc via

       /usr/lib/qubes/qrexec-client-vm target_vm test.Add /usr/bin/our_test_add_client 1 2

and we should get "3" as answer, after dom0 allows it.

**Note:** For a real world example of writing a qrexec service, see this
[blog post](http://theinvisiblethings.blogspot.com/2013/02/converting-untrusted-pdfs-into-trusted.html).


# Qubes RPC internals #

(*This is about the implementation of qrexec v3. For the implementation of
qrexec v2, see [here](/doc/qrexec2/#qubes-rpc-internals).*)

Qrexec framework consists of a number of processes communicating with each
other using common IPC protocol (described in detail below). Components
residing in the same domain use pipes as the underlying transport medium,
while components in separate domains use vchan link.


## Dom0 tools implementation ##

 * `/usr/lib/qubes/qrexec-daemon`: One instance is required for every active
   domain. Responsible for:
   * Handling execution and service requests from **dom0** (source:
     `qrexec-client`).
   * Handling service requests from the associated domain (source:
     `qrexec-client-vm`, then `qrexec-agent`).
 * Command line: `qrexec-daemon domain-id domain-name [default user]`
 * `domain-id`: Numeric Qubes ID assigned to the associated domain.
 * `domain-name`: Associated domain name.
 * `default user`: Optional. If passed, `qrexec-daemon` uses this user as
   default for all execution requests that don't specify one.
 * `/usr/lib/qubes/qrexec-policy`: Internal program used to evaluate the
   RPC policy and deciding whether a RPC call should be allowed.
 * `/usr/lib/qubes/qrexec-client`: Used to pass execution and service requests
   to `qrexec-daemon`. Command line parameters:
   * `-d target-domain-name`: Specifies the target for the execution/service
     request.
   * `-l local-program`: Optional. If present, `local-program` is executed
     and its stdout/stdin are used when sending/receiving data to/from the
     remote peer.
   * `-e`: Optional. If present, stdout/stdin are not connected to the remote
     peer. Only process creation status code is received.
   * `-c <request-id,src-domain-name,src-domain-id>`: used for connecting
     a VM-VM service request by `qrexec-policy`. Details described below in
     the service example.
   * `cmdline`: Command line to pass to `qrexec-daemon` as the
     execution/service request. Service request format is described below in
     the service example.

**Note:** None of the above tools are designed to be used by users directly.


## VM tools implementation ##

 * `qrexec-agent`: One instance runs in each active domain. Responsible for:
   * Handling service requests from `qrexec-client-vm` and passing them to
     connected `qrexec-daemon` in dom0.
   * Executing associated `qrexec-daemon` execution/service requests.
 * Command line parameters: none.
 * `qrexec-client-vm`: Runs in an active domain. Used to pass service requests
   to `qrexec-agent`.
 * Command line: `qrexec-client-vm target-domain-name service-name local-program [local program arguments]`
 * `target-domain-name`: Target domain for the service request. Source is
   the current domain.
 * `service-name`: Requested service name.
 * `local-program`: `local-program` is executed locally and its stdin/stdout
   are connected to the remote service endpoint.


## Qrexec protocol details ##

Qrexec protocol is message-based. All messages share a common header followed
by an optional data packet.

    /* uniform for all peers, data type depends on message type */
    struct msg_header {
       uint32_t type;           /* message type */
       uint32_t len;            /* data length */
    };

When two peers establish connection, the server sends `MSG_HELLO` followed by
`peer_info` struct:

    struct peer_info {
       uint32_t version; /* qrexec protocol version */
    };

The client then should reply with its own `MSG_HELLO` and `peer_info`. If
protocol versions don't match, the connection is closed.

(*TODO: fallback for backwards compatibility, don't do handshake in the
same domain?*)

Details of all possible use cases and the messages involved are described below.


### dom0: request execution of `some_command` in domX and pass stdin/stdout ###

-   **dom0**: `qrexec-client` is invoked in **dom0** as follows:

    `qrexec-client -d domX [-l local_program] user:some_command`

    - `user` may be substituted with the literal `DEFAULT`. In that case,
    default Qubes user will be used to execute `some_command`.

- **dom0**: `qrexec-client` sets `QREXEC_REMOTE_DOMAIN` environment variable
to **domX**.
- **dom0**: If `local_program` is set, `qrexec-client` executes it and uses
that child's stdin/stdout in place of its own when exchanging data with
`qrexec-agent` later.
- **dom0**: `qrexec-client` connects to **domX**'s `qrexec-daemon`.
- **dom0**: `qrexec-daemon` sends `MSG_HELLO` header followed by `peer_info`
to `qrexec-client`.
- **dom0**: `qrexec-client` replies with `MSG_HELLO` header followed by
`peer_info` to `qrexec-daemon`.
- **dom0**: `qrexec-client` sends `MSG_EXEC_CMDLINE` header followed by
`exec_params` to `qrexec-daemon`.

        /* variable size */
        struct exec_params {
           uint32_t connect_domain; /* target domain id */
           uint32_t connect_port;   /* target vchan port for i/o exchange */
           char cmdline[0];         /* command line to execute, size = msg_header.len - sizeof(struct exec_params) */
        };

    In this case, `connect_domain` and `connect_port` are set to 0.

- **dom0**: `qrexec-daemon` replies to `qrexec-client` with
`MSG_EXEC_CMDLINE` header followed by `exec_params`, but with empty `cmdline`
field. `connect_domain` is set to Qubes ID of **domX** and `connect_port`
is set to a vchan port allocated by `qrexec-daemon`.
- **dom0**: `qrexec-daemon` sends `MSG_EXEC_CMDLINE` header followed
by `exec_params` to the associated **domX** `qrexec-agent` over
vchan. `connect_domain` is set to 0 (**dom0**), `connect_port` is the same
as sent to `qrexec-client`. `cmdline` is unchanged except that the literal
`DEFAULT` is replaced with actual user name, if present.
- **dom0**: `qrexec-client` disconnects from `qrexec-daemon`.
- **dom0**: `qrexec-client` starts a vchan server using the details received
from `qrexec-daemon` and waits for connection from **domX**'s `qrexec-agent`.
- **domX**: `qrexec-agent` receives `MSG_EXEC_CMDLINE` header followed by
`exec_params` from `qrexec-daemon` over vchan.
- **domX**: `qrexec-agent` connects to `qrexec-client` over vchan using the
details from `exec_params`.
- **domX**: `qrexec-agent` executes `some_command` in **domX** and connects
the child's stdin/stdout to the data vchan. If the process creation fails,
`qrexec-agent` sends `MSG_DATA_EXIT_CODE` to `qrexec-client` followed by
the status code (**int**) and disconnects from the data vchan.
- Data read from `some_command`'s stdout is sent to the data vchan using
`MSG_DATA_STDOUT` by `qrexec-agent`. `qrexec-client` passes data received as
`MSG_DATA_STDOUT` to its own stdout (or to `local_program`'s stdin if used).
- `qrexec-client` sends data read from local stdin (or `local_program`'s
stdout if used) to `qrexec-agent` over the data vchan using
`MSG_DATA_STDIN`. `qrexec-agent` passes data received as `MSG_DATA_STDIN`
to `some_command`'s stdin.
- `MSG_DATA_STDOUT` or `MSG_DATA_STDIN` with data `len` field set to 0 in
`msg_header` is an EOF marker. Peer receiving such message should close the
associated input/output pipe.
- When `some_command` terminates, **domX**'s `qrexec-agent` sends
`MSG_DATA_EXIT_CODE` header to `qrexec-client` followed by the exit code
(**int**). `qrexec-agent` then disconnects from the data vchan.


### domY: invoke execution of qubes service `qubes.SomeRpc` in domX and pass stdin/stdout ###

-   **domY**: `qrexec-client-vm` is invoked as follows:

        `qrexec-client-vm domX qubes.SomeRpc local_program [params]`

- **domY**: `qrexec-client-vm` connects to `qrexec-agent` (via local
socket/named pipe).
- **domY**: `qrexec-client-vm` sends `trigger_service_params` data to
`qrexec-agent` (without filling the `request_id` field):

         struct trigger_service_params {
            char service_name[64];
            char target_domain[32];
            struct service_params request_id; /* service request id */
         };
        
         struct service_params {
            char ident[32];
        };

- **domY**: `qrexec-agent` allocates a locally-unique (for this domain)
`request_id` (let's say `13`) and fills it in the `trigger_service_params`
struct received from `qrexec-client-vm`.
- **domY**: `qrexec-agent` sends `MSG_TRIGGER_SERVICE` header followed by
`trigger_service_params` to `qrexec-daemon` in **dom0** via vchan.
- **dom0**: **domY**'s `qrexec-daemon` executes `qrexec-policy`: `qrexec-policy
domY_id domY domX qubes.SomeRpc 13`.
- **dom0**: `qrexec-policy` evaluates if the RPC should be allowed or
denied. If the action is allowed it returns `0`, if the action is denied it
returns `1`.
- **dom0**: **domY**'s `qrexec-daemon` checks the exit code of `qrexec-policy`.
    - If `qrexec-policy` returned **not** `0`: **domY**'s `qrexec-daemon`
    sends `MSG_SERVICE_REFUSED` header followed by `service_params` to
    **domY**'s `qrexec-agent`. `service_params.ident` is identical to the one
    received. **domY**'s `qrexec-agent` disconnects its `qrexec-client-vm`
    and RPC processing is finished.
    - If `qrexec-policy` returned `0`, RPC processing continues.
- **dom0**: if `qrexec-policy` allowed the RPC, it executed `qrexec-client
-d domX -c 13,domY,domY_id user:QUBESRPC qubes.SomeRpc domY`.
- **dom0**: `qrexec-client` sets `QREXEC_REMOTE_DOMAIN` environment variable
to **domX**.
- **dom0**: `qrexec-client` connects to **domX**'s `qrexec-daemon`.
- **dom0**: **domX**'s `qrexec-daemon` sends `MSG_HELLO` header followed by
`peer_info` to `qrexec-client`.
- **dom0**: `qrexec-client` replies with `MSG_HELLO` header followed by
`peer_info` to **domX**'s`qrexec-daemon`.
- **dom0**: `qrexec-client` sends `MSG_EXEC_CMDLINE` header followed by
`exec_params` to **domX**'s`qrexec-daemon`

        /* variable size */
        struct exec_params {
           uint32_t connect_domain; /* target domain id */
           uint32_t connect_port;   /* target vchan port for i/o exchange */
           char cmdline[0];         /* command line to execute, size = msg_header.len - sizeof(struct exec_params) */
        };

    In this case, `connect_domain` is set to id of **domY** (from the `-c`
    parameter) and `connect_port` is set to 0. `cmdline` field contains the
    RPC to execute, in this case `user:QUBESRPC qubes.SomeRpc domY`.

- **dom0**: **domX**'s `qrexec-daemon` replies to `qrexec-client` with
`MSG_EXEC_CMDLINE` header followed by `exec_params`, but with empty `cmdline`
field. `connect_domain` is set to Qubes ID of **domX** and `connect_port`
is set to a vchan port allocated by **domX**'s `qrexec-daemon`.
- **dom0**: **domX**'s `qrexec-daemon` sends `MSG_EXEC_CMDLINE` header
followed by `exec_params` to **domX**'s `qrexec-agent`. `connect_domain`
and `connect_port` fields are the same as in the step above. `cmdline` is
set to the one received from `qrexec-client`, in this case `user:QUBESRPC
qubes.SomeRpc domY`.
- **dom0**: `qrexec-client` disconnects from **domX**'s `qrexec-daemon`
after receiving connection details.
- **dom0**: `qrexec-client` connects to **domY**'s `qrexec-daemon` and
exchanges `MSG_HELLO` as usual.
- **dom0**: `qrexec-client` sends `MSG_SERVICE_CONNECT` header followed by
`exec_params` to **domY**'s `qrexec-daemon`. `connect_domain` is set to ID
of **domX** (received from **domX**'s `qrexec-daemon`) and `connect_port` is
the one received as well. `cmdline` is set to request ID (`13` in this case).
- **dom0**: **domY**'s `qrexec-daemon` sends `MSG_SERVICE_CONNECT` header
followed by `exec_params` to **domY**'s `qrexec-agent`. Data fields are
unchanged from the step above.
- **domY**: `qrexec-agent` starts a vchan server on the port received in
the step above. It acts as a `qrexec-client` in this case because this is
a VM-VM connection.
- **domX**: `qrexec-agent` connects to the vchan server of **domY**'s
`qrexec-agent` (connection details were received before from **domX**'s
`qrexec-daemon`).
- After that, connection follows the flow of the previous example (dom0-VM).

