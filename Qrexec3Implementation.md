---
layout: wiki
title: Qrexec3Implementation
permalink: /wiki/Qrexec3Implementation/
---

*[Note: This document describes Qrexec protocol v3 (Odyssey)]*

Qrexec framework consists of a number of processes communicating with each other using common IPC protocol (described in detail below). Components residing in the same domain use pipes as the underlying transport medium, while components in separate domains use vchan link.

qrexec-daemon
=============

Runs in **dom0**. One instance is required for every active domain.

Responsible for
---------------

-   Handling execution and service requests from **dom0** (source: *qrexec-client*).
-   Handling service requests from the associated domain (source: *qrexec-client-vm*, then *qrexec-agent*).

Command line parameters
-----------------------

domain-id domain-name [default user]

*domain-id*  
Numeric Qubes ID assigned to the associated domain.

*domain-name*  
Associated domain name.

*default user*  
Optional. If passed, *qrexec-daemon* uses this user as default for all execution requests that don't specify one.

qrexec-client
=============

Runs in **dom0**. Used to pass execution and service requests to *qrexec-daemon*.

Command line parameters
-----------------------

-d target-domain-name

 

Specifies the target for the execution/service request.

-l local-program

 

Optional. If present, *local-program* is executed and its stdout/stdin are used when sending/receiving data to/from the remote peer.

-e

Optional. If present, stdout/stdin are not connected to the remote peer. Only process creation status code is received.

-c \<request-id,src-domain-name,src-domain-id\>

 

Used for connecting a VM-VM service request by *qrexec-policy*. Details described below in the service example.

*cmdline*  
Command line to pass to *qrexec-daemon* as the execution/service request. Service request format is described below in the service example.

qrexec-agent
============

One instance runs in each active domain.

Responsible for
---------------

-   Handling service requests from *qrexec-client-vm* and passing them to connected *qrexec-daemon* in **dom0**.
-   Executing associated *qrexec-daemon* execution/service requests.

Command line parameters
-----------------------

None.

qrexec-client-vm
================

Runs in an active domain. Used to pass service requests to *qrexec-agent*.

Command line parameters
-----------------------

target-domain-name service-name local-program [local program arguments]

*target-domain-name*  
Target domain for the service request. Source is the current domain.

*service-name*  
Requested service name.

*local-program*  
*local-program* is executed locally and its stdin/stdout are connected to the remote service endpoint.

Qrexec protocol details
=======================

Qrexec protocol is message-based. All messages share a common header followed by an optional data packet.

``` {.literal-block}
/* uniform for all peers, data type depends on message type */
struct msg_header {
    uint32_t type;           /* message type */
    uint32_t len;            /* data length */
};
```

When two peers establish connection, the server sends *MSG\_HELLO* followed by *peer\_info* struct:

``` {.literal-block}
struct peer_info {
    uint32_t version; /* qrexec protocol version */
};
```

The client then should reply with its own *MSG\_HELLO* and *peer\_info*. If protocol versions don't match, the connection is closed.

Details of all possible use cases and the messages involved are described below.

dom0: request execution of some\_command in domX and pass stdin/stdout
----------------------------------------------------------------------

1.  *qrexec-client* is invoked in **dom0** as follows:

    `qrexec-client -d domX [-l local_program] user:some_command`

    *user* may be substituted with the literal `DEFAULT`. In that case, default Qubes user will be used to execute *some\_command*.

2.  *qrexec-client* sets *QREXEC\_REMOTE\_DOMAIN* environment variable to **domX**.

3.  If *local\_program* is set, *qrexec-client* executes it and uses that child's stdin/stdout in place of its own when exchanging data with *qrexec-agent* later.

4.  *qrexec-client* connects to **domX** *qrexec-daemon*.

5.  *qrexec-daemon* sends *MSG\_HELLO* followed by *peer\_info* to *qrexec-client*.

6.  *qrexec-client* replies with *MSG\_HELLO* followed by *peer\_info* to *qrexec-daemon*.

7.  *qrexec-client* sends *MSG\_EXEC\_CMDLINE* followed by *exec\_params* to *qrexec-daemon*:

    ``` {.literal-block}
    /* variable size */
    struct exec_params {
        uint32_t connect_domain; /* target domain id */
        uint32_t connect_port;   /* target vchan port for i/o exchange */
        char cmdline[0];         /* command line to execute, size = msg_header.len - sizeof(struct exec_params) */
    };
    ```

    In this case, *connect\_domain* and *connect\_port* are set to 0.

8.  *qrexec-daemon* replies to *qrexec-client* with *MSG\_EXEC\_CMDLINE* followed by *exec\_params*, but with empty *cmdline* field. *connect\_domain* is set to Qubes ID of **domX** and *connect\_port* is set to a vchan port allocated by *qrexec-daemon*.

9.  *qrexec-daemon* sends *MSG\_EXEC\_CMDLINE* followed by *exec\_params* to associated **domX** *qrexec-agent* over vchan. *connect\_domain* is set to 0 (**dom0**), *connect\_port* is the same as sent to *qrexec-client*. *cmdline* is unchanged except that the literal `DEFAULT` is replaced with actual user name, if present.

10. *qrexec-client* disconnects from *qrexec-daemon*.

11. *qrexec-client* starts a vchan server using the details received from *qrexec-daemon* and waits for connection from **domX** *qrexec-agent*.

12. **domX** *qrexec-agent* receives *MSG\_EXEC\_CMDLINE* followed by *exec\_params* from *qrexec-daemon* over vchan.

13. **domX** *qrexec-agent* connects to *qrexec-client* over vchan using the details from *exec\_params*.

14. **domX** *qrexec-agent* executes *some\_command* in **domX** and connects the child's stdin/stdout to the data vchan. If the process creation fails, *qrexec-agent* sends *MSG\_DATA\_EXIT\_CODE* to *qrexec-client* followed by the status code (*int*) and disconnects from the data vchan.

15. Data read from *some\_command*'s stdout is sent to the data vchan using *MSG\_DATA\_STDOUT* by *qrexec-agent*. *qrexec-client* passes data received as *MSG\_DATA\_STDOUT* to its own stdout (or to *local\_program*'s stdin if used).

16. *qrexec-client* sends data read from local stdin (or *local\_program*'s stdout if used) to *qrexec-agent* over the data vchan using *MSG\_DATA\_STDIN*. *qrexec-agent* passes data received as *MSG\_DATA\_STDIN* to *some\_command*'s stdin.

17. *MSG\_DATA\_STDOUT* or *MSG\_DATA\_STDIN* with data *len* field set to 0 in *msg\_header* is an EOF marker. Peer receiving such message should close the associated input/output pipe.

18. When *some\_command* terminates, **domX** *qrexec-agent* sends *MSG\_DATA\_EXIT\_CODE* to *qrexec-client* followed by the exit code (*int*). *qrexec-agent* then disconnects from the data vchan.


