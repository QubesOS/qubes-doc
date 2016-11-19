---
layout: doc
title: Management API
permalink: /doc/mgmt1/
---

# Management API

*(This page is the current draft of the proposal. It is not implemented yet.)*

The API should be implemented as a set of qrexec calls. This is to make it easy
to set the policy using current mechanism.

## The calls

| call                                    | dest                   | argument      | inside                                    | return                                                   | note |
| --------------------------------------- | ---------------------- | ------------- | ----------------------------------------- | -------------------------------------------------------- | ---- |
| mgmt1.vm.List                           | "dom0"                 | -             | -                                         | "&lt;name&gt; class=&lt;class&gt; state=&lt;state&gt;\n" | |
| mgmt1.vm.Create                         | template or "dom0"     | class         | "name=&lt;name&gt; label=&lt;label&gt;"   | -                                       | |
| mgmt1.vm.CreateInPool                   | template or "dom0"     | class         | "name=&lt;name&gt; label=&lt;label&gt; pool=&lt;pool&gt;" | -                       | |
| mgmt1.vm.CreateTemplate                 | "dom0"                 | name          | root.img                                  | -                                       | |
| mgmt1.vm.property.List                  | vm                     | -             | -                                         | "&lt;property&gt;\n"                    | |
| mgmt1.vm.property.Get                   | vm                     | property      | -                                         | "default={yes|no} &lt;value&gt;"        | |
| mgmt1.vm.property.Help                  | vm                     | property      | -                                         | help.rst                                | |
| mgmt1.vm.property.Reset                 | vm                     | property      | -                                         | -                                       | |
| mgmt1.vm.property.Set                   | vm                     | property      | value                                     | -                                       | |
| mgmt1.vm.feature.List                   | vm                     | -             | -                                         | "&lt;feature&gt;\n"                     | |
| mgmt1.vm.feature.Get                    | vm                     | feature       | -                                         | value                                   | |
| mgmt1.vm.feature.CheckWithTemplate      | vm                     | feature       | -                                         | value                                   | |
| mgmt1.vm.feature.Remove                 | vm                     | feature       | -                                         | -                                       | |
| mgmt1.vm.feature.Set                    | vm                     | feature       | value                                     | -                                       | |
| mgmt1.vm.tag.List                       | vm                     | tag           | -                                         | "&lt;tag&gt;\n"                         | |
| mgmt1.vm.tag.Get                        | vm                     | tag           | -                                         | "0" or "1"                              |retcode? |
| mgmt1.vm.tag.Remove                     | vm                     | tag           | -                                         | -                                       | |
| mgmt1.vm.tag.Set                        | vm                     | tag           | -                                         | -                                       | |
| mgmt1.vm.firewall.Get                   | vm                     | position      | -                                         | "&lt;rule id&gt; &lt;rule&gt;\n"        | |
| mgmt1.vm.firewall.InsertRule            | vm                     | position      | rule                                      | rule id                                 | |
| mgmt1.vm.firewall.RemoveRule            | vm                     | rule id       | -                                         | -                                       | |
| mgmt1.vm.firewall.Flush                 | vm                     | -             | -                                         | -                                       | |
| mgmt1.vm.device.&lt;class&gt;.Attach    | vm                     | device        | -                                         | -                                       | |
| mgmt1.vm.device.&lt;class&gt;.Detach    | vm                     | device        | -                                         | -                                       | |
| mgmt1.vm.device.&lt;class&gt;.List      | vm                     | -             | -                                         | "&lt;device&gt;\n"                      | |
| mgmt1.vm.device.&lt;class&gt;.Available | vm                     | -             | -                                         | "&lt;device&gt;\n"                      | |
| mgmt1.vm.microphone.Attach              | vm                     | -             | -                                         | -                                       | |
| mgmt1.vm.microphone.Detach              | vm                     | -             | -                                         | -                                       | |
| mgmt1.pool.List                         | "dom0"                 | -             | -                                         | "&lt;pool&gt;\n"                        | |
| mgmt1.pool.Info                         | "dom0"                 | pool          | -                                         | "&lt;property&gt;=&lt;value&gt;\n"      | |
| mgmt1.pool.Add                          | "dom0"                 | pool          | "&lt;property&gt;=&lt;value&gt;\n"        | -                                       | |
| mgmt1.pool.Remove                       | "dom0"                 | pool          | -                                         | -                                       | |
| mgmt1.pool.volume.List                  | "dom0"                 | pool          | -                                         | volume id                               | |
| mgmt1.pool.volume.Info                  | "dom0"                 | pool:vid      | -                                         | "&lt;property&gt;=&lt;value&gt;\n"      | |
| mgmt1.pool.volume.ListSnapshots         | "dom0"                 | pool:vid      | -                                         | "&lt;snapshot&gt;\n"                    | |
| mgmt1.pool.volume.Snapshot              | "dom0"                 | pool:vid      | -                                         | snapshot                                | |
| mgmt1.pool.volume.Revert                | "dom0"                 | pool:vid      | snapshot                                  | -                                       | |
| mgmt1.pool.volume.Extend                | "dom0"                 | pool:vid      | -                                         | "&lt;size_in_bytes&gt;"                 | |
| mgmt1.vm.volume.List                    | vm                     | -/pool?       | -                                         | ?                                       | |
| mgmt1.vm.volume.Info                    | vm                     | volume        | -                                         | ?                                       | |
| mgmt1.vm.volume.ListSnapshots           | vm                     | volume        | -                                         | snapshot                                |duplicate of mgmt1.pool.volume., but with other call params |
| mgmt1.vm.volume.Snapshot                | vm                     | volume        | -                                         | snapshot                                |id. |
| mgmt1.vm.volume.Revert                  | vm                     | volume        | snapshot                                  | -                                       |id. |
| mgmt1.vm.volume.Extend                  | vm                     | volume        | -                                         | "&lt;size_in_bytes&gt;"                 |id. |
| mgmt1.vm.volume.Attach                  | vm                     | volume        | -                                         | -                                       | |
| mgmt1.vm.volume.Detach                  | vm                     | volume        | -                                         | -                                       | |
| mgmt1.vm.Start                          | vm                     | -             | -                                         | -                                       | |
| mgmt1.vm.Shutdown                       | vm                     | -             | -                                         | -                                       | |
| mgmt1.vm.Pause                          | vm                     | -             | -                                         | -                                       | |
| mgmt1.vm.Unpause                        | vm                     | -             | -                                         | -                                       | |
| mgmt1.vm.Kill                           | vm                     | -             | -                                         | -                                       | |
| mgmt1.backup.Execute                    | "dom0"                 | config id     | -                                         | -                                       |config in /etc/qubes/backup/&lt;id&gt;.conf |
| mgmt1.backup.Info                       | "dom0"                 | ?             | content?                                  | ?                                       | |
| mgmt1.backup.Restore                    | "dom0"                 | ?             | content                                   | ?                                       | |


## Tags

- created-by-&lt;vm&gt;
- managed-by-&lt;vm&gt;
- backup-&lt;id&gt;

## TODO

- something to configure/update policy
