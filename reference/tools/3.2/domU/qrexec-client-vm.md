---
layout: doc
title: qrexec-client-vm
permalink: /doc/tools/3.2/domU/qrexec-client-vm/
redirect_from:
- /doc/domU-tools/qrexec-client-vm/
- /en/doc/domU-tools/qrexec-client-vm/
---

```
================
qrexec-client-vm
================

NAME
====
qrexec-client-vm - call Qubes RPC service

SYNOPSIS
========
| qrexec-client-vm *target_vmname* *service* [*local_program* [*local program arguments*]]

DESCRIPTION
===========

Call Qubes RPC (aka qrexec) service to a different VM. The service call request
is sent to dom0, where Qubes RPC policy is evaluated and when it allows the
call, it is forwarded to appropriate target VM (which may be different than
requested, if policy says so). Local program (if given) is started only
when service call is allowed by the policy.

Remote service can communicate with the caller (``qrexec-client-vm``) using
stdin/stdout.  When *local_program* is given, its stdin/stdout is connected to
service stdin/stdout (stderr is not redirected), otherwise - service
stdin/stdout is connected to those of ``qrexec-client-vm``.

OPTIONS
=======

*target_vmname*

    Name of target VM to which service is requested. Qubes RPC policy may
    ignore this value and redirect call somewhere else.

    This argument, can contain VM name, or one of special values:

    * ``$dispvm`` - new Disposable VM

    This field is limited to 31 characters (alphanumeric, plus ``-_.$``).

*service*

    Requested service. Besides service name, it can contain a service argument
    after ``+`` character. For example ``some.service+argument``.

    This field is limited to 63 characters (alphanumeric, plus ``-_.$+``).

*local_program*

    Full path to local program to be connected with remote service. Optional.

*local program arguments*

    Arguments to *local_program*. Optional.

EXIT STATUS
===========

If service call is allowed by dom0 and ``qrexec-client-vm`` is started without
*local_program* argument, it reports remote service exit code.

If service call is allowed by dom0 and ``qrexec-client-vm`` is started with
*local_program* argument, it reports the local program exit code. There is no
way to learn exit code of remote service in this case.

In both cases, if process (local or remote) was terminated by a signal, exit
status is 128+signal number.

If service call is denied by dom0, ``qrexec-client-vm`` exit with status 126.

AUTHORS
=======
| Joanna Rutkowska <joanna at invisiblethingslab dot com>
| Rafal Wojtczuk <rafal at invisiblethingslab dot com>
| Marek Marczykowski-Górecki <marmarek at invisiblethingslab dot com>
```
