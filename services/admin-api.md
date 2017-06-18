---
layout: doc-full
title: Admin API
permalink: /doc/admin-api/
redirect_from:
- /doc/mgmt/
- /doc/mgmt1/
---

# Admin API

*(This page is the current draft of the proposal. It is not implemented yet.)*

The API should be implemented as a set of qrexec calls. This is to make it easy
to set the policy using current mechanism.

## The calls

| call                                  | dest      | argument  | inside                                    | return                                                    | note |
| ------------------------------------- | --------- | --------- | ----------------------------------------- | --------------------------------------------------------- | ---- |
| `admin.vmclass.List`                   | `dom0`    | -         | -                                         | `<class>\n`                                               |
| `admin.vm.List`                        | `dom0|<vm>` | -         | -                                         | `<name> class=<class> state=<state>\n`                    |
| `admin.vm.Create.<class>`              | `dom0`    | template  | `name=<name> label=<label>`               | -                                                         |
| `admin.vm.CreateInPool.<class>`        | `dom0`    | template  | `name=<name> label=<label> `<br/>`pool=<pool> pool:<volume>=<pool>`   | -                                                         | either use `pool=` to put all volumes there, <br/>or `pool:<volume>=` for individual volumes - both forms are not allowed at the same time
| `admin.vm.CreateTemplate`              | `dom0`    | name      | `root.img`                                | -                                                         |
| `admin.vm.Remove`                      | vm        | -         | -                                         | -                                                         |
| `admin.label.List`                     | `dom0`    | -         | -                                         | `<property>\n`                                            |
| `admin.label.Create`                   | `dom0`    | label     | `0xRRGGBB`                                | -                                                         |
| `admin.label.Get`                      | `dom0`    | label     | -                                         | `0xRRGGBB`                                                |
| `admin.label.Index`                    | `dom0`    | label     | -                                         | `<label-index>`                                           |
| `admin.label.Remove`                   | `dom0`    | label     | -                                         | -                                                         |
| `admin.property.List`                  | `dom0`    | -         | -                                         | `<property>\n`                                            |
| `admin.property.Get`                   | `dom0`    | property  | -                                         | `default={yes|no} `<br/>`type={str|int|bool|vm|label} <value>`   |
| `admin.property.Help`                  | `dom0`    | property  | -                                         | `help`                                                    |
| `admin.property.HelpRst`               | `dom0`    | property  | -                                         | `help.rst`                                                |
| `admin.property.Reset`                 | `dom0`    | property  | -                                         | -                                                         |
| `admin.property.Set`                   | `dom0`    | property  | value                                     | -                                                         |
| `admin.vm.property.List`               | vm        | -         | -                                         | `<property>\n`                                            |
| `admin.vm.property.Get`                | vm        | property  | -                                         | `default={yes|no} <value>`                                |
| `admin.vm.property.Help`               | vm        | property  | -                                         | `help`                                                    |
| `admin.vm.property.HelpRst`            | vm        | property  | -                                         | `help.rst`                                                |
| `admin.vm.property.Reset`              | vm        | property  | -                                         | -                                                         |
| `admin.vm.property.Set`                | vm        | property  | value                                     | -                                                         |
| `admin.vm.feature.List`                | vm        | -         | -                                         | `<feature>\n`                                             |
| `admin.vm.feature.Get`                 | vm        | feature   | -                                         | value                                                     |
| `admin.vm.feature.CheckWithTemplate`   | vm        | feature   | -                                         | value                                                     |
| `admin.vm.feature.Remove`              | vm        | feature   | -                                         | -                                                         |
| `admin.vm.feature.Set`                 | vm        | feature   | value                                     | -                                                         |
| `admin.vm.tag.List`                    | vm        | -         | -                                         | `<tag>\n`                                                 |
| `admin.vm.tag.Get`                     | vm        | tag       | -                                         | `0` or `1`                                                | retcode? |
| `admin.vm.tag.Remove`                  | vm        | tag       | -                                         | -                                                         |
| `admin.vm.tag.Set`                     | vm        | tag       | -                                         | -                                                         |
| `admin.vm.firewall.Get`                | vm        | -         | -                                         | `<rule>\n`                                                | rules syntax as in [firewall interface](/doc/vm-interface/#firewall-rules-in-4x) with addition of `expire=` and `comment=` options; `comment=` (if present) must be the last option
| `admin.vm.firewall.Set`                | vm        | -         | `<rule>\n`                                | -                                                         | set firewall rules, see `admin.vm.firewall.Get` for syntax
| `admin.vm.firewall.Flush`              | vm        | -         | -                                         | -                                                         |
| `admin.vm.firewall.SetPolicy`          | vm        | -         | `accept|drop`                             | -                                                         |
| `admin.vm.firewall.GetPolicy`          | vm        | -         | -                                         | `accept|drop`                                             |
| `admin.vm.firewall.Reload`             | vm        | -         | -                                         | -                                                         | force reload firewall without changing any rule
| `admin.vm.device.<class>.Attach`       | vm        | device    | options                                   | -                                                         | `device` is in form `<backend-name>+<device-ident>` <br/>optional options given in `key=value` format, separated with spaces; <br/>options can include `persistent=yes` to "persistently" attach the device (default is temporary)
| `admin.vm.device.<class>.Detach`       | vm        | device    | -                                         | -                                                         | `device` is in form `<backend-name>+<device-ident>`
| `admin.vm.device.<class>.List`         | vm        | -         | -                                         | `<device> <options>\n`                                    | options can include `persistent=yes` for "persistently" attached devices (default is temporary)
| `admin.vm.device.<class>.Available`    | vm        | device-ident | -                                         | `<device-ident> <properties> description=<desc>\n`        | optional service argument may be used to get info about a single device, <br/>optional (device class specific) properties are in `key=value` form, <br/>`description` must be the last one and is the only one allowed to contain spaces
| `admin.pool.List`                      | `dom0`    | -         | -                                         | `<pool>\n`                                                |
| `admin.pool.ListDrivers`               | `dom0`    | -         | -                                         | `<pool-driver> <property> ...\n`                          | Properties allowed in `admin.pool.Add`
| `admin.pool.Info`                      | `dom0`    | pool      | -                                         | `<property>=<value>\n`                                    |
| `admin.pool.Add`                       | `dom0`    | driver    | `<property>=<value>\n`                    | -                                                         |
| `admin.pool.Remove`                    | `dom0`    | pool      | -                                         | -                                                         |
| `admin.pool.volume.List`               | `dom0`    | pool      | -                                         | volume id                                                 |
| `admin.pool.volume.Info`               | `dom0`    | pool      | vid                                       | `<property>=<value>\n`                                    |
| `admin.pool.volume.ListSnapshots`      | `dom0`    | pool      | vid                                       | `<snapshot>\n`                                            |
| `admin.pool.volume.Snapshot`           | `dom0`    | pool      | vid                                       | snapshot                                                  |
| `admin.pool.volume.Revert`             | `dom0`    | pool      | `<vid> <snapshot>`                        | -                                                         |
| `admin.pool.volume.Resize`             | `dom0`    | pool      | `<vid> <size_in_bytes>`                   | -                                                         |
| `admin.pool.volume.Import`             | `dom0`    | pool      | `<vid>\n<raw volume data>`                | -                                                         |
| `admin.vm.volume.List`                 | vm        | -         | -                                         | `<volume>\n`                                              | `<volume>` is per-VM volume name (`root`, `private`, etc), `<vid>` is pool-unique volume id
| `admin.vm.volume.Info`                 | vm        | volume    | -                                         | `<property>=<value>\n`                                    |
| `admin.vm.volume.ListSnapshots`        | vm        | volume    | -                                         | snapshot                                                  | duplicate of `admin.pool.volume.`, but with other call params |
| `admin.vm.volume.Snapshot`             | vm        | volume    | -                                         | snapshot                                                  | id. |
| `admin.vm.volume.Revert`               | vm        | volume    | snapshot                                  | -                                                         | id. |
| `admin.vm.volume.Resize`               | vm        | volume    | size_in_bytes                             | -                                                         | id. |
| `admin.vm.volume.Import`               | vm        | volume    | raw volume data                           | -                                                         | id. |
| `admin.vm.volume.Clone`                | vm        | volume    | dest VM name                              | -                                                         | copy volume data from `volume` of `vm` to same volume of `dest VM name` |
| `admin.vm.Start`                       | vm        | -         | -                                         | -                                                         |
| `admin.vm.Shutdown`                    | vm        | -         | -                                         | -                                                         |
| `admin.vm.Pause`                       | vm        | -         | -                                         | -                                                         |
| `admin.vm.Unpause`                     | vm        | -         | -                                         | -                                                         |
| `admin.vm.Kill`                        | vm        | -         | -                                         | -                                                         |
| `admin.backup.Execute`                 | `dom0`    | config id | -                                         | -                                                         | config in `/etc/qubes/backup/<id>.conf`, only one backup operation of given `config id` can be running at once |
| `admin.backup.Info`                    | `dom0`    | config id | -                                         | backup info                                               | info what would be included in the backup
| `admin.Events`                         | `dom0|vm` | -         | -                                         | events                                                    |

Volume properties:

 - `pool`
 - `vid`
 - `size`
 - `usage`
 - `rw`
 - `internal`
 - `source`
 - `save_on_stop`
 - `snap_on_start`


## Returned messages

First byte of a message is a message type. This is 8 bit non-zero integer.
Values start at 0x30 (48, `'0'`, zero digit in ASCII) for readability in hexdump.
Next byte must be 0x00 (a separator).

This alternatively can be thought of as zero-terminated string containing
single ASCII digit.

### OK (0)

```
30 00 <content>
```

Server will close the connection after delivering single message.

### EVENT (1)

```
31 00 <subject> 00 <event> 00 ( <key> 00 <value> 00 )* 00
```

Events are returned as stream of messages in selected API calls. Normally server
will not close the connection.

A method yielding events will not ever return a `OK` or `EXCEPTION` message.

When calling such method, it will produce an artificial event
`connection-established` just after connection, to help avoiding race
conditions during event handler registration.

### EXCEPTION (2)

```
32 00 <type> 00 ( <traceback> )? 00 <format string> 00 ( <field> 00 )*
```

Server will close the connection.

Traceback may be empty, can be enabled server-side as part of debug mode.
Delimiting zero-byte is always present.

Fields are should substituted into `%`-style format string, possibly after
client-side translation, to form final message to be displayed unto user. Server
does not by itself support translation.

## Tags

*not implemented yet*

The tags provided can be used to write custom policies. They are not used in
a&nbsp;default Qubes OS installation. However, they are created anyway.

- `created-by-<vm>` &mdash;&nbsp;Created in an extension to qubesd at the
  moment of creation of the VM. Cannot be changed via API, which is also
  enforced by this extension.
- `managed-by-<vm>` &mdash;&nbsp;Can be used for the same purpose, but it is
  not created automatically, nor is it forbidden to set or reset this tag.

## General notes

- there is no provision for `qvm-run`, but there already exists `qubes.VMShell` call
- generally actions `*.List` return a list of objects and have "object
  identifier" as first word in a row. Such action can be also called with "object
  identifier" in argument to get only a single entry (in the same format).
- closing qrexec connection normally does _not_ interrupt running operation; this is important to avoid leaving the system in inconsistent state
- actual operation starts only after caller send all the parameters (including a payload), signaled by sending EOF mark; there is no support for interactive protocols, to keep the protocol reasonable simple

## TODO

- something to configure/update policy
- notifications
  - how to constrain the events?
  - how to pass the parameters? maybe XML, since this is trusted anyway and
    parser may be complicated
- how to constrain the possible values for `admin.vm.property.Set` etc, like
  "you can change `netvm`, but you have to pick from this set"; this currently
  can be done by writing an extension
- a call for executing `*.desktop` file from `/usr/share/applications`, for use
  with appmenus without giving access to `qubes.VMShell`; currently this can be
  done by writing custom qrexec calls
- maybe some generator for `.desktop` for appmenus, which would wrap calls in
  `qrexec-client-vm`

<!-- vim: set ts=4 sts=4 sw=4 et : -->
