---
layout: doc
title: Qubes RPC internals
permalink: /doc/qrexec-internals/
redirect_from:
- /doc/qrexec3-implementation/
- /en/doc/qrexec3-implementation/
- /doc/Qrexec3Implementation/
- /wiki/Qrexec3Implementation/
---

# Qubes RPC internals

(*This page details the current implementation of qrexec (qrexec3).
A [general introduction](/doc/qrexec/) to qrexec is also available.
For the implementation of qrexec2, see [here](/doc/qrexec2/#qubes-rpc-internals).*)

The qrexec framework consists of a number of processes communicating with each other using common IPC protocol (described in detail below).
Components residing in the same domain (`qrexec-client-vm` to `qrexec-agent`, `qrexec-client` to `qrexec-daemon`) use local sockets as the underlying transport medium.
Components in separate domains (`qrexec-daemon` to `qrexec-agent`, data channel between `qrexec-agent`s) use vchan links.
Because of [vchan limitation](https://github.com/qubesos/qubes-issues/issues/951), it is not possible to establish qrexec connection back to the source domain.

## Dom0 tools implementation

### qrexec-daemon
* `/usr/sbin/qrexec-daemon`: One instance is required for every active domain. Responsible for:
  * Handling execution and service requests from **dom0** (source: `qrexec-client`).
  * Handling service requests from the associated domain (source: `qrexec-client-vm`, then `qrexec-agent`).
* Command line: `qrexec-daemon domain-id domain-name [default user]`
* `domain-id`: Numeric Qubes ID assigned to the associated domain.
* `domain-name`: Associated domain name.
* `default user`: Optional. If passed, `qrexec-daemon` uses this user as default for all execution requests that don't specify one.

### qrexec-policy
* `/usr/bin/qrexec-policy`: Internal program used to evaluate the RPC policy and deciding whether a RPC call should be allowed.

### qrexec-client
* `/usr/bin/qrexec-client`: Used to pass execution and service requests to `qrexec-daemon`. Command line parameters:
  * `-d target-domain-name`: Specifies the target for the execution/service request.
  * `-l local-program`: Optional. If present, `local-program` is executed and its stdout/stdin are used when sending/receiving data to/from the remote peer.
  * `-e`: Optional. If present, stdout/stdin are not connected to the remote   peer. Only process creation status code is received.
  * `-c <request-id,src-domain-name,src-domain-id>`: used for connecting a VM-VM service request by `qrexec-policy`. Details described below in the service example.
  * `cmdline`: Command line to pass to `qrexec-daemon` as the execution/service request. Service request format is described below in the service example.

**Note:** None of the above tools are designed to be used by users directly.

## VM tools implementation

### `qrexec-agent`: One instance runs in each active domain. Responsible for:
  * Handling service requests from `qrexec-client-vm` and passing them to connected `qrexec-daemon` in dom0.
  * Executing associated `qrexec-daemon` execution/service requests.
* Command line parameters: none.

### `qrexec-client-vm`: Runs in an active domain. Used to pass service requests to `qrexec-agent`.
* Command line: `qrexec-client-vm target-domain-name service-name local-program [local program arguments]`
* `target-domain-name`: Target domain for the service request. Source is the current domain.
* `service-name`: Requested service name.
* `local-program`: `local-program` is executed locally and its stdin/stdout are connected to the remote service endpoint.

## Qrexec protocol details

The qrexec protocol is message-based.
All messages share a common header followed by an optional data packet.

    /* uniform for all peers, data type depends on message type */
    struct msg_header {
       uint32_t type;           /* message type */
       uint32_t len;            /* data length */
    };

When two peers establish connection, the server sends `MSG_HELLO` followed by `peer_info` struct:

    struct peer_info {
       uint32_t version; /* qrexec protocol version */
    };

The client then should reply with its own `MSG_HELLO` and `peer_info`.
The lower of two versions define protocol used for this connection.
If either side does not support this version, the connection is closed.

Details of all possible use cases and the messages involved are described below.

### dom0: request execution of `some_command` in domX and pass stdin/stdout

![qrexec basics diagram](/attachment/wiki/qrexec3/qrexec-internals-dom0.png)

- **dom0**: `qrexec-client` is invoked in **dom0** as follows:

      qrexec-client -d domX [-l local_program] user:some_command`

  `user` may be substituted with the literal `DEFAULT`. In that case, default Qubes user will be used to execute `some_command`.
- **dom0**: `qrexec-client` sets `QREXEC_REMOTE_DOMAIN` environment variable to **domX**.
- **dom0**: If `local_program` is set, `qrexec-client` executes it and uses that child's stdin/stdout in place of its own when exchanging data with `qrexec-agent` later.
- **dom0**: `qrexec-client` connects to **domX**'s `qrexec-daemon`.
- **dom0**: `qrexec-daemon` sends `MSG_HELLO` header followed by `peer_info` to `qrexec-client`.
- **dom0**: `qrexec-client` replies with `MSG_HELLO` header followed by `peer_info` to `qrexec-daemon`.
- **dom0**: `qrexec-client` sends `MSG_EXEC_CMDLINE` header followed by `exec_params` to `qrexec-daemon`.

        /* variable size */
        struct exec_params {
           uint32_t connect_domain; /* target domain id */
           uint32_t connect_port;   /* target vchan port for i/o exchange */
           char cmdline[0];         /* command line to execute, size = msg_header.len - sizeof(struct exec_params) */
        };

    In this case, `connect_domain` and `connect_port` are set to 0.

- **dom0**: `qrexec-daemon` replies to `qrexec-client` with `MSG_EXEC_CMDLINE` header followed by `exec_params`, but with empty `cmdline` field. `connect_domain` is set to Qubes ID of **domX** and `connect_port` is set to a vchan port allocated by `qrexec-daemon`.
- **dom0**: `qrexec-daemon` sends `MSG_EXEC_CMDLINE` header followed by `exec_params` to the associated **domX** `qrexec-agent` over vchan. `connect_domain` is set to 0 (**dom0**), `connect_port` is the same as sent to `qrexec-client`. `cmdline` is unchanged except that the literal `DEFAULT` is replaced with actual user name, if present.
- **dom0**: `qrexec-client` disconnects from `qrexec-daemon`.
- **dom0**: `qrexec-client` starts a vchan server using the details received from `qrexec-daemon` and waits for connection from **domX**'s `qrexec-agent`.
- **domX**: `qrexec-agent` receives `MSG_EXEC_CMDLINE` header followed by `exec_params` from `qrexec-daemon` over vchan.
- **domX**: `qrexec-agent` connects to `qrexec-client` over vchan using the details from `exec_params`.
- **domX**: `qrexec-agent` executes `some_command` in **domX** and connects the child's stdin/stdout to the data vchan. If the process creation fails, `qrexec-agent` sends `MSG_DATA_EXIT_CODE` to `qrexec-client` followed by the status code (**int**) and disconnects from the data vchan.
- Data read from `some_command`'s stdout is sent to the data vchan using `MSG_DATA_STDOUT` by `qrexec-agent`. `qrexec-client` passes data received as `MSG_DATA_STDOUT` to its own stdout (or to `local_program`'s stdin if used).
- `qrexec-client` sends data read from local stdin (or `local_program`'s stdout if used) to `qrexec-agent` over the data vchan using `MSG_DATA_STDIN`. `qrexec-agent` passes data received as `MSG_DATA_STDIN` to `some_command`'s stdin.
- `MSG_DATA_STDOUT` or `MSG_DATA_STDIN` with data `len` field set to 0 in `msg_header` is an EOF marker. Peer receiving such message should close the associated input/output pipe.
- When `some_command` terminates, **domX**'s `qrexec-agent` sends `MSG_DATA_EXIT_CODE` header to `qrexec-client` followed by the exit code (**int**). `qrexec-agent` then disconnects from the data vchan.

### domY: invoke execution of qubes service `qubes.SomeRpc` in domX and pass stdin/stdout

![qrexec basics diagram](/attachment/wiki/qrexec3/qrexec-internals-domY.png)

- **domY**: `qrexec-client-vm` is invoked as follows:

      qrexec-client-vm domX qubes.SomeRpc local_program [params]

- **domY**: `qrexec-client-vm` connects to `qrexec-agent` (via local socket/named pipe).
- **domY**: `qrexec-client-vm` sends `trigger_service_params` data to `qrexec-agent` (without filling the `request_id` field):

         struct trigger_service_params {
            char service_name[64];
            char target_domain[32];
            struct service_params request_id; /* service request id */
         };

         struct service_params {
            char ident[32];
        };

- **domY**: `qrexec-agent` allocates a locally-unique (for this domain) `request_id` (let's say `13`) and fills it in the `trigger_service_params` struct received from `qrexec-client-vm`.
- **domY**: `qrexec-agent` sends `MSG_TRIGGER_SERVICE` header followed by `trigger_service_params` to `qrexec-daemon` in **dom0** via vchan.
- **dom0**: **domY**'s `qrexec-daemon` executes `qrexec-policy`: `qrexec-policy domY_id domY domX qubes.SomeRpc 13`.
- **dom0**: `qrexec-policy` evaluates if the RPC should be allowed or denied. If the action is allowed it returns `0`, if the action is denied it returns `1`.
- **dom0**: **domY**'s `qrexec-daemon` checks the exit code of `qrexec-policy`.
    - If `qrexec-policy` returned **not** `0`: **domY**'s `qrexec-daemon` sends `MSG_SERVICE_REFUSED` header followed by `service_params` to **domY**'s `qrexec-agent`. `service_params.ident` is identical to the one received. **domY**'s `qrexec-agent` disconnects its `qrexec-client-vm` and RPC processing is finished.
    - If `qrexec-policy` returned `0`, RPC processing continues.
- **dom0**: if `qrexec-policy` allowed the RPC, it executed `qrexec-client -d domX -c 13,domY,domY_id user:QUBESRPC qubes.SomeRpc domY`.
- **dom0**: `qrexec-client` sets `QREXEC_REMOTE_DOMAIN` environment variable to **domX**.
- **dom0**: `qrexec-client` connects to **domX**'s `qrexec-daemon`.
- **dom0**: **domX**'s `qrexec-daemon` sends `MSG_HELLO` header followed by `peer_info` to `qrexec-client`.
- **dom0**: `qrexec-client` replies with `MSG_HELLO` header followed by `peer_info` to **domX**'s`qrexec-daemon`.
- **dom0**: `qrexec-client` sends `MSG_EXEC_CMDLINE` header followed by `exec_params` to **domX**'s`qrexec-daemon`

        /* variable size */
        struct exec_params {
           uint32_t connect_domain; /* target domain id */
           uint32_t connect_port;   /* target vchan port for i/o exchange */
           char cmdline[0];         /* command line to execute, size = msg_header.len - sizeof(struct exec_params) */
        };

    In this case, `connect_domain` is set to id of **domY** (from the `-c` parameter) and `connect_port` is set to 0. `cmdline` field contains the RPC to execute, in this case `user:QUBESRPC qubes.SomeRpc domY`.

- **dom0**: **domX**'s `qrexec-daemon` replies to `qrexec-client` with `MSG_EXEC_CMDLINE` header followed by `exec_params`, but with empty `cmdline` field. `connect_domain` is set to Qubes ID of **domX** and `connect_port` is set to a vchan port allocated by **domX**'s `qrexec-daemon`.
- **dom0**: **domX**'s `qrexec-daemon` sends `MSG_EXEC_CMDLINE` header followed by `exec_params` to **domX**'s `qrexec-agent`. `connect_domain` and `connect_port` fields are the same as in the step above. `cmdline` is set to the one received from `qrexec-client`, in this case `user:QUBESRPC qubes.SomeRpc domY`.
- **dom0**: `qrexec-client` disconnects from **domX**'s `qrexec-daemon` after receiving connection details.
- **dom0**: `qrexec-client` connects to **domY**'s `qrexec-daemon` and exchanges `MSG_HELLO` as usual.
- **dom0**: `qrexec-client` sends `MSG_SERVICE_CONNECT` header followed by `exec_params` to **domY**'s `qrexec-daemon`. `connect_domain` is set to ID of **domX** (received from **domX**'s `qrexec-daemon`) and `connect_port` is the one received as well. `cmdline` is set to request ID (`13` in this case).
- **dom0**: **domY**'s `qrexec-daemon` sends `MSG_SERVICE_CONNECT` header followed by `exec_params` to **domY**'s `qrexec-agent`. Data fields are unchanged from the step above.
- **domY**: `qrexec-agent` starts a vchan server on the port received in the step above. It acts as a `qrexec-client` in this case because this is a VM-VM connection.
- **domX**: `qrexec-agent` connects to the vchan server of **domY**'s `qrexec-agent` (connection details were received before from **domX**'s `qrexec-daemon`).
- After that, connection follows the flow of the previous example (dom0-VM).

