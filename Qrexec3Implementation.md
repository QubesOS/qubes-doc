---
layout: wiki
title: Qrexec3Implementation
permalink: /wiki/Qrexec3Implementation/
---

Implementation of qrexec in Qubes R2
====================================

This page describes implementation of the [qrexec framework](/wiki/Qrexec) in Qubes OS R2.

Qrexec framework consists of a number of processes communicating with each other using common IPC protocol (described in detail below). Components residing in the same domain use pipes as the underlying transport medium, while components in separate domains use vchan link.

Dom0 tools implementation
-------------------------

-   `/usr/lib/qubes/qrexec-daemon` \<- one instance is required for every active domain. Responsible for:
    -   Handling execution and service requests from **dom0** (source: `qrexec-client`).
    -   Handling service requests from the associated domain (source: `qrexec-client-vm`, then `qrexec-agent`).

> Command line: `qrexec-daemon domain-id domain-name [default user]`

> *domain-id*: numeric Qubes ID assigned to the associated domain.

> *domain-name*: associated domain name.

> *default user*: optional. If passed, `qrexec-daemon` uses this user as default for all execution requests that don't specify one.

-   `/usr/lib/qubes/qrexec-policy` \<- internal program used to evaluate the RPC policy and deciding whether a RPC call should be allowed.
-   `/usr/lib/qubes/qrexec-client` \<- used to pass execution and service requests to `qrexec-daemon`. Command line parameters:

> `-d target-domain-name` Specifies the target for the execution/service request.

> `-l local-program` Optional. If present, `local-program` is executed and its stdout/stdin are used when sending/receiving data to/from the remote peer.

> `-e` Optional. If present, stdout/stdin are not connected to the remote peer. Only process creation status code is received.

> `-c <request-id,src-domain-name,src-domain-id>` Used for connecting a VM-VM service request by `qrexec-policy`. Details described below in the service example.

> `cmdline` Command line to pass to `qrexec-daemon` as the execution/service request. Service request format is described below in the service example.

Note: none of the above tools are designed to be used by users directly.

VM tools implementation
-----------------------

-   `qrexec-agent` \<- one instance runs in each active domain. Responsible for:
    -   Handling service requests from `qrexec-client-vm` and passing them to connected `qrexec-daemon` in **dom0**.
    -   Executing associated `qrexec-daemon` execution/service requests.

> Command line parameters: none.

-   `qrexec-client-vm` \<- runs in an active domain. Used to pass service requests to `qrexec-agent`.

> Command line: `qrexec-client-vm target-domain-name service-name local-program [local program arguments]`

> `target-domain-name` Target domain for the service request. Source is the current domain.

> `service-name` Requested service name.

> `local-program` **local-program** is executed locally and its stdin/stdout are connected to the remote service endpoint.

Qrexec protocol details
-----------------------

Qrexec protocol is message-based. All messages share a common header followed by an optional data packet.

``` {.wiki}
/* uniform for all peers, data type depends on message type */
struct msg_header {
   uint32_t type;           /* message type */
   uint32_t len;            /* data length */
};
```

When two peers establish connection, the server sends `MSG_HELLO` followed by `peer_info` struct:

``` {.wiki}
struct peer_info {
   uint32_t version; /* qrexec protocol version */
};
```

The client then should reply with its own `MSG_HELLO` and `peer_info`. If protocol versions don't match, the connection is closed. TODO: fallback for backwards compatibility.

Details of all possible use cases and the messages involved are described below.

### dom0: request execution of some\_command in domX and pass stdin/stdout

-   `qrexec-client` is invoked in **dom0** as follows:

> `qrexec-client -d domX [-l local_program] user:some_command`

> `user` may be substituted with the literal `DEFAULT`. In that case, default Qubes user will be used to execute `some_command`.

-   `qrexec-client` sets `QREXEC_REMOTE_DOMAIN` environment variable to **domX**.
-   If `local_program` is set, `qrexec-client` executes it and uses that child's stdin/stdout in place of its own when exchanging data with `qrexec-agent` later.
-   `qrexec-client` connects to **domX**'s `qrexec-daemon`.
-   `qrexec-daemon` sends `MSG_HELLO` followed by `peer_info` to `qrexec-client`.
-   `qrexec-client` replies with `MSG_HELLO` followed by `peer_info` to `qrexec-daemon`.
-   `qrexec-client` sends `MSG_EXEC_CMDLINE` followed by `exec_params` to `qrexec-daemon`

    ``` {.wiki}
     /* variable size */
     struct exec_params {
        uint32_t connect_domain; /* target domain id */
        uint32_t connect_port;   /* target vchan port for i/o exchange */
        char cmdline[0];         /* command line to execute, size = msg_header.len - sizeof(struct exec_params) */
     };
    ```

    In this case, `connect_domain` and `connect_port` are set to 0.

-   `qrexec-daemon` replies to `qrexec-client` with `MSG_EXEC_CMDLINE` followed by `exec_params`, but with empty `cmdline` field. `connect_domain` is set to Qubes ID of **domX** and `connect_port` is set to a vchan port allocated by `qrexec-daemon`.
-   `qrexec-daemon` sends `MSG_EXEC_CMDLINE` followed by `exec_params` to the associated **domX** `qrexec-agent` over vchan. `connect_domain` is set to 0 (**dom0**), `connect_port` is the same as sent to `qrexec-client`. `cmdline` is unchanged except that the literal `DEFAULT` is replaced with actual user name, if present.
-   `qrexec-client` disconnects from `qrexec-daemon`.
-   `qrexec-client` starts a vchan server using the details received from `qrexec-daemon` and waits for connection from **domX**'s `qrexec-agent`.
-   **domX**'s `qrexec-agent` receives `MSG_EXEC_CMDLINE` followed by `exec_params` from `qrexec-daemon` over vchan.
-   **domX**'s `qrexec-agent` connects to `qrexec-client` over vchan using the details from `exec_params`.
-   **domX**'s `qrexec-agent` executes `some_command` in **domX** and connects the child's stdin/stdout to the data vchan. If the process creation fails, `qrexec-agent` sends `MSG_DATA_EXIT_CODE` to `qrexec-client` followed by the status code (**int**) and disconnects from the data vchan.
-   Data read from `some_command`'s stdout is sent to the data vchan using `MSG_DATA_STDOUT` by `qrexec-agent`. `qrexec-client` passes data received as `MSG_DATA_STDOUT` to its own stdout (or to `local_program`'s stdin if used).
-   `qrexec-client` sends data read from local stdin (or `local_program`'s stdout if used) to `qrexec-agent` over the data vchan using `MSG_DATA_STDIN`. `qrexec-agent` passes data received as `MSG_DATA_STDIN` to `some_command`'s stdin.
-   `MSG_DATA_STDOUT` or `MSG_DATA_STDIN` with data `len` field set to 0 in `msg_header` is an EOF marker. Peer receiving such message should close the associated input/output pipe.
-   When `some_command` terminates, **domX**'s `qrexec-agent` sends `MSG_DATA_EXIT_CODE` to `qrexec-client` followed by the exit code (**int**). `qrexec-agent` then disconnects from the data vchan.

