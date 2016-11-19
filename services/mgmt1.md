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
| `mgmt1.vm.List`                         | `dom0`                 | -             | -                                         | `<name> class=<class> state=<state>\n`   |
| `mgmt1.vm.Create`                       | template or `dom0`     | class         | `name=<name> label=<label>`               | -                                        |
| `mgmt1.vm.CreateInPool`                 | template or `dom0`     | class         | `name=<name> label=<label> pool=<pool>`   | -                                        |
| `mgmt1.vm.CreateTemplate`               | `dom0`                 | name          | `root.img`                                | -                                        |
| `mgmt1.vm.property.List`                | vm                     | -             | -                                         | `<property>\n`                           |
| `mgmt1.vm.property.Get`                 | vm                     | property      | -                                         | `default={yes|no} <value>`               |
| `mgmt1.vm.property.Help`                | vm                     | property      | -                                         | `help.rst`                               |
| `mgmt1.vm.property.Reset`               | vm                     | property      | -                                         | -                                        |
| `mgmt1.vm.property.Set`                 | vm                     | property      | value                                     | -                                        |
| `mgmt1.vm.feature.List`                 | vm                     | -             | -                                         | `<feature>\n`                            |
| `mgmt1.vm.feature.Get`                  | vm                     | feature       | -                                         | value                                    |
| `mgmt1.vm.feature.CheckWithTemplate`    | vm                     | feature       | -                                         | value                                    |
| `mgmt1.vm.feature.Remove`               | vm                     | feature       | -                                         | -                                        |
| `mgmt1.vm.feature.Set`                  | vm                     | feature       | value                                     | -                                        |
| `mgmt1.vm.tag.List`                     | vm                     | tag           | -                                         | `<tag>\n`                                |
| `mgmt1.vm.tag.Get`                      | vm                     | tag           | -                                         | `0` or `1`                               |retcode? |
| `mgmt1.vm.tag.Remove`                   | vm                     | tag           | -                                         | -                                        |
| `mgmt1.vm.tag.Set`                      | vm                     | tag           | -                                         | -                                        |
| `mgmt1.vm.firewall.Get`                 | vm                     | position      | -                                         | `<rule id> <rule>\n`                     |
| `mgmt1.vm.firewall.InsertRule`          | vm                     | position      | rule                                      | rule id                                  |
| `mgmt1.vm.firewall.RemoveRule`          | vm                     | rule id       | -                                         | -                                        |
| `mgmt1.vm.firewall.Flush`               | vm                     | -             | -                                         | -                                        |
| `mgmt1.vm.device.<class>.Attach`        | vm                     | device        | -                                         | -                                        |
| `mgmt1.vm.device.<class>.Detach`        | vm                     | device        | -                                         | -                                        |
| `mgmt1.vm.device.<class>.List`          | vm                     | -             | -                                         | `<device>\n`                             |
| `mgmt1.vm.device.<class>.Available`     | vm                     | -             | -                                         | `<device>\n`                             |
| `mgmt1.vm.microphone.Attach`            | vm                     | -             | -                                         | -                                        |
| `mgmt1.vm.microphone.Detach`            | vm                     | -             | -                                         | -                                        |
| `mgmt1.pool.List`                       | `dom0`                 | -             | -                                         | `<pool>\n`                               |
| `mgmt1.pool.Info`                       | `dom0`                 | pool          | -                                         | `<property>=<value>\n`                   |
| `mgmt1.pool.Add`                        | `dom0`                 | pool          | `<property>=<value>\n`                    | -                                        |
| `mgmt1.pool.Remove`                     | `dom0`                 | pool          | -                                         | -                                        |
| `mgmt1.pool.volume.List`                | `dom0`                 | pool          | -                                         | volume id                                |
| `mgmt1.pool.volume.Info`                | `dom0`                 | pool:vid      | -                                         | `<property>=<value>\n`                   |
| `mgmt1.pool.volume.ListSnapshots`       | `dom0`                 | pool:vid      | -                                         | `<snapshot>\n`                           |
| `mgmt1.pool.volume.Snapshot`            | `dom0`                 | pool:vid      | -                                         | snapshot                                 |
| `mgmt1.pool.volume.Revert`              | `dom0`                 | pool:vid      | snapshot                                  | -                                        |
| `mgmt1.pool.volume.Extend`              | `dom0`                 | pool:vid      | -                                         | `<size_in_bytes>`                        |
| `mgmt1.vm.volume.List`                  | vm                     | -/pool?       | -                                         | ?                                        |
| `mgmt1.vm.volume.Info`                  | vm                     | volume        | -                                         | ?                                        |
| `mgmt1.vm.volume.ListSnapshots`         | vm                     | volume        | -                                         | snapshot                                 |duplicate of `mgmt1.pool.volume.`, but with other call params |
| `mgmt1.vm.volume.Snapshot`              | vm                     | volume        | -                                         | snapshot                                 |id. |
| `mgmt1.vm.volume.Revert`                | vm                     | volume        | snapshot                                  | -                                        |id. |
| `mgmt1.vm.volume.Extend`                | vm                     | volume        | -                                         | `<size_in_bytes>`                        |id. |
| `mgmt1.vm.volume.Attach`                | vm                     | volume        | -                                         | -                                        |
| `mgmt1.vm.volume.Detach`                | vm                     | volume        | -                                         | -                                        |
| `mgmt1.vm.Start`                        | vm                     | -             | -                                         | -                                        |
| `mgmt1.vm.Shutdown`                     | vm                     | -             | -                                         | -                                        |
| `mgmt1.vm.Pause`                        | vm                     | -             | -                                         | -                                        |
| `mgmt1.vm.Unpause`                      | vm                     | -             | -                                         | -                                        |
| `mgmt1.vm.Kill`                         | vm                     | -             | -                                         | -                                        |
| `mgmt1.backup.Execute`                  | `dom0`                 | config id     | -                                         | -                                        |config in `/etc/qubes/backup/<id>.conf` |
| `mgmt1.backup.Info`                     | `dom0`                 | ?             | content?                                  | ?                                        |
| `mgmt1.backup.Restore`                  | `dom0`                 | ?             | content                                   | ?                                        |


## Tags

- `created-by-<vm>`
- `managed-by-<vm>`
- `backup-<id>`

## TODO

- something to configure/update policy
