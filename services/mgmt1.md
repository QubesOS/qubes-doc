---
layout: doc-full
title: Management API
permalink: /doc/mgmt1/
---

# Management API

*(This page is the current draft of the proposal. It is not implemented yet.)*

The API should be implemented as a set of qrexec calls. This is to make it easy
to set the policy using current mechanism.

## The calls

| call                                    | dest                   | argument      | inside                                    | return                                   | note |
| --------------------------------------- | ---------------------- | ------------- | ----------------------------------------- | ---------------------------------------- | ---- |
| `mgmt.vm.List`                          | `dom0`                 | -             | -                                         | `<name> class=<class> state=<state>\n`   |
| `mgmt.vm.Create.<class>`                | `dom0`                 | template      | `name=<name> label=<label>`               | -                                        |
| `mgmt.vm.CreateInPool.<class>`          | `dom0`                 | template      | `name=<name> label=<label> pool=<pool>`   | -                                        |
| `mgmt.vm.CreateTemplate`                | `dom0`                 | name          | `root.img`                                | -                                        |
| `mgmt.vm.property.List`                 | vm                     | -             | -                                         | `<property>\n`                           |
| `mgmt.vm.property.Get`                  | vm                     | property      | -                                         | `default={yes|no} <value>`               |
| `mgmt.vm.property.Help`                 | vm                     | property      | -                                         | `help.rst`                               |
| `mgmt.vm.property.Reset`                | vm                     | property      | -                                         | -                                        |
| `mgmt.vm.property.Set`                  | vm                     | property      | value                                     | -                                        |
| `mgmt.vm.feature.List`                  | vm                     | -             | -                                         | `<feature>\n`                            |
| `mgmt.vm.feature.Get`                   | vm                     | feature       | -                                         | value                                    |
| `mgmt.vm.feature.CheckWithTemplate`     | vm                     | feature       | -                                         | value                                    |
| `mgmt.vm.feature.Remove`                | vm                     | feature       | -                                         | -                                        |
| `mgmt.vm.feature.Set`                   | vm                     | feature       | value                                     | -                                        |
| `mgmt.vm.tag.List`                      | vm                     | tag           | -                                         | `<tag>\n`                                |
| `mgmt.vm.tag.Get`                       | vm                     | tag           | -                                         | `0` or `1`                               | retcode? |
| `mgmt.vm.tag.Remove`                    | vm                     | tag           | -                                         | -                                        |
| `mgmt.vm.tag.Set`                       | vm                     | tag           | -                                         | -                                        |
| `mgmt.vm.firewall.Get`                  | vm                     | position      | -                                         | `<rule id> <rule>\n`                     |
| `mgmt.vm.firewall.InsertRule`           | vm                     | position      | rule                                      | rule id                                  |
| `mgmt.vm.firewall.RemoveRule`           | vm                     | rule id       | -                                         | -                                        |
| `mgmt.vm.firewall.Flush`                | vm                     | -             | -                                         | -                                        |
| `mgmt.vm.device.<class>.Attach`         | vm                     | device        | -                                         | -                                        |
| `mgmt.vm.device.<class>.Detach`         | vm                     | device        | -                                         | -                                        |
| `mgmt.vm.device.<class>.List`           | vm                     | -             | -                                         | `<device>\n`                             |
| `mgmt.vm.device.<class>.Available`      | vm                     | -             | -                                         | `<device>\n`                             |
| `mgmt.vm.microphone.Attach`             | vm                     | -             | -                                         | -                                        |
| `mgmt.vm.microphone.Detach`             | vm                     | -             | -                                         | -                                        |
| `mgmt.pool.List`                        | `dom0`                 | -             | -                                         | `<pool>\n`                               |
| `mgmt.pool.Info`                        | `dom0`                 | pool          | -                                         | `<property>=<value>\n`                   |
| `mgmt.pool.Add`                         | `dom0`                 | pool          | `<property>=<value>\n`                    | -                                        |
| `mgmt.pool.Remove`                      | `dom0`                 | pool          | -                                         | -                                        |
| `mgmt.pool.volume.List`                 | `dom0`                 | pool          | -                                         | volume id                                |
| `mgmt.pool.volume.Info`                 | `dom0`                 | pool:vid      | -                                         | `<property>=<value>\n`                   |
| `mgmt.pool.volume.ListSnapshots`        | `dom0`                 | pool:vid      | -                                         | `<snapshot>\n`                           |
| `mgmt.pool.volume.Snapshot`             | `dom0`                 | pool:vid      | -                                         | snapshot                                 |
| `mgmt.pool.volume.Revert`               | `dom0`                 | pool:vid      | snapshot                                  | -                                        |
| `mgmt.pool.volume.Extend`               | `dom0`                 | pool:vid      | -                                         | `<size_in_bytes>`                        |
| `mgmt.vm.volume.List`                   | vm                     | -/pool?       | -                                         | ?                                        |
| `mgmt.vm.volume.Info`                   | vm                     | volume        | -                                         | ?                                        |
| `mgmt.vm.volume.ListSnapshots`          | vm                     | volume        | -                                         | snapshot                                 | duplicate of `mgmt.pool.volume.`, but with other call params |
| `mgmt.vm.volume.Snapshot`               | vm                     | volume        | -                                         | snapshot                                 | id. |
| `mgmt.vm.volume.Revert`                 | vm                     | volume        | snapshot                                  | -                                        | id. |
| `mgmt.vm.volume.Extend`                 | vm                     | volume        | -                                         | `<size_in_bytes>`                        | id. |
| `mgmt.vm.volume.Attach`                 | vm                     | volume        | -                                         | -                                        |
| `mgmt.vm.volume.Detach`                 | vm                     | volume        | -                                         | -                                        |
| `mgmt.vm.Start`                         | vm                     | -             | -                                         | -                                        |
| `mgmt.vm.Shutdown`                      | vm                     | -             | -                                         | -                                        |
| `mgmt.vm.Pause`                         | vm                     | -             | -                                         | -                                        |
| `mgmt.vm.Unpause`                       | vm                     | -             | -                                         | -                                        |
| `mgmt.vm.Kill`                          | vm                     | -             | -                                         | -                                        |
| `mgmt.backup.Execute`                   | `dom0`                 | config id     | -                                         | -                                        | config in `/etc/qubes/backup/<id>.conf` |
| `mgmt.backup.Info`                      | `dom0`                 | ?             | content?                                  | ?                                        |
| `mgmt.backup.Restore`                   | `dom0`                 | ?             | content                                   | ?                                        |

## Returned messages

First two bytes of a message is a message type. This is 16 bit little endian
integer. Values start at 0x30 (48, `'0'`, zero digit in ASCII) for readability
in hexdump.

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

- `created-by-<vm>`
- `managed-by-<vm>`
- `backup-<id>`

## General notes

- there is no provision for `qvm-run`, but there already exists `qubes.VMShell` call

## TODO

- something to configure/update policy
- notifications
  - how to constrain the events?
  - how to pass the parameters? maybe XML, since this is trusted anyway and
    parser may be complicated
- how to constrain the possible values for `mgmt.vm.property.Set` etc, like
  "you can change `netvm`, but you have to pick from this set"; this currently
  can be done by writing an extension
- a call for executing `*.desktop` file from `/usr/share/applications`, for use
  with appmenus without giving access to `qubes.VMShell`; currently this can be
  done by writing custom qrexec calls
- maybe some generator for `.desktop` for appmenus, which would wrap calls in
  `qrexec-client-vm`
