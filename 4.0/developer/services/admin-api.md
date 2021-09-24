---
lang: en
layout: doc
permalink: /doc/4.0/admin-api/
redirect_from:
- /doc/qubes-admin-api/
- /doc/mgmt/
- /doc/mgmt1/
- /doc/mgmt-architecture/
- /doc/admin-api-architecture/
ref: 36
title: Admin API
---

_You may also be interested in the article
[Introducing the Qubes Admin API](/news/2017/06/27/qubes-admin-api/)._

## Goals

The goals of the Admin API system is to provide a way for the user to manage
the domains without direct access to dom0.

Foreseen benefits include:

- Ability to remotely manage the Qubes OS.
- Possibility to create multi-user system, where different users are able to use
  different sets of domains, possibly overlapping. This would also require to
  have separate GUI domain.

The API would be used by:

- Qubes OS Manager (or any tools that would replace it)
- CLI tools, when run from another VM (and possibly also from dom0)
- remote management tools
- any custom tools

## Threat model

TBD

## Components

![Admin API Architecture](/attachment/doc/admin-api-architecture.svg)

A central entity in the Qubes Admin API system is a `qubesd` daemon, which
holds information about all domains in the system and mediates all actions (like
starting and stopping a qube) with `libvirtd`. The `qubesd` daemon also manages
the `qubes.xml` file, which stores all persistent state information and
dispatches events to extensions. Last but not least, `qubesd` is responsible for
querying the RPC policy for qrexec daemon.

The `qubesd` daemon may be accessed from other domains through a set of qrexec
API calls called the "Admin API". This API is the intended
management interface supported by the Qubes OS. The API is stable. When called,
the RPC handler performs basic validation and forwards the request to the
`qubesd` via UNIX domain socket. The socket API is private, unstable, and not
yet documented.

## The calls

The API should be implemented as a set of qrexec calls. This is to make it easy
to set the policy using current mechanism.

[View this table on a fullscreen page.](/doc/admin-api/table/)

{% include admin-api-table.md %}

[View this table on a fullscreen page.](/doc/admin-api/table/)

Volume properties:

- `pool`
- `vid`
- `size`
- `usage`
- `rw`
- `source`
- `save_on_stop`
- `snap_on_start`
- `revisions_to_keep`
- `is_outdated`

Method `admin.vm.Stats` returns `vm-stats` events every `stats_interval` seconds, for every running VM. Parameters of `vm-stats` events:

- `memory_kb` - memory usage in kB
- `cpu_time` - absolute CPU time (in milliseconds) spent by the VM since its startup, normalized for one CPU
- `cpu_usage` - CPU usage in percents

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

The tags provided can be used to write custom policies. They are not used in
a&nbsp;default Qubes OS installation. However, they are created anyway.

- `created-by-<vm>` &mdash;&nbsp;Created in an extension to qubesd at the
  moment of creation of the VM. Cannot be changed via API, which is also
  enforced by this extension.
- `managed-by-<vm>` &mdash;&nbsp;Can be used for the same purpose, but it is
  not created automatically, nor is it forbidden to set or reset this tag.

## Backup profile

Backup-related calls do not allow (yet) to specify what should be included in
the backup. This needs to be configured separately in dom0, with a backup
profile, stored in `/etc/qubes/backup/<profile>.conf`. The file use yaml syntax
and have following settings:

- `include` - list of VMs to include, can also contains tags using
  `$tag:some-tag` syntax or all VMs of given type using `$type:AppVM`, known
  from qrexec policy
- `exclude` - list of VMs to exclude, after evaluating `include` setting
- `destination_vm` - VM to which the backup should be send
- `destination_path` - path to which backup should be written in
  `destination_vm`. This setting is given to `qubes.Backup` service and
  technically it's up to it how to interpret it. In current implementation it is
  interpreted as a directory where a new file should be written (with a name
  based on the current timestamp), or a command where the backup should
  be piped to
- `compression` - should the backup be compressed (default: True)? The value can be either
  `False` or `True` for default compression, or a compression command (needs to
  accept `-d` argument for decompression)
- `passphrase_text` - passphrase used to encrypt and integrity protect the backup
- `passphrase_vm` - VM which should be asked what backup passphrase should be
  used. The asking is performed using `qubes.BackupPassphrase+profile_name`
  service, which is expected to output chosen passphrase to its stdout. Empty
  output cancel the backup operation. This service can be used either to ask
  the user interactively, or to have some automated passphrase handling (for
  example: generate randomly, then encrypt with a public key and send
  somewhere)

Not all settings needs to be set.

Example backup profile:

```yaml
# Backup only selected VMs
include:
  - work
  - personal
  - vault
  - banking

# Store the backup on external disk
destination_vm: sys-usb
destination_path: /media/my-backup-disk

# Use static passphrase
passphrase_text: "My$Very!@Strong23Passphrase"
```

And slightly more advanced one:

```yaml
# Include all VMs with a few exceptions
include:
  - $type:AppVM
  - $type:TemplateVM
  - $type:StandaloneVM
exclude:
  - untrusted
  - $tag:do-not-backup

# parallel gzip for faster backup
compression: pigz

# ask 'vault' VM for the backup passphrase
passphrase_vm: vault

# send the (encrypted) backup directly to remote server
destination_vm: sys-net
destination_path: ncftpput -u my-ftp-username -p my-ftp-pass -c my-ftp-server /directory/for/backups
```

## General notes

- there is no provision for `qvm-run`, but there already exists `qubes.VMShell` call
- generally actions `*.List` return a list of objects and have "object
  identifier" as first word in a row. Such action can be also called with "object
  identifier" in argument to get only a single entry (in the same format).
- closing qrexec connection normally does _not_ interrupt running operation; this is important to avoid leaving the system in inconsistent state
- actual operation starts only after caller send all the parameters (including a payload), signaled by sending EOF mark; there is no support for interactive protocols, to keep the protocol reasonable simple

## Policy admin API

There is also an API to view and update [Qubes RPC policy files](/doc/qrexec) in dom0. All of the following calls have dom0 as destination:

| call                                       | argument | inside               | return                  |
| ---------------------------------------------- | ---- | -------------------- | ----------------------- |
| `policy.List` <br> `policy.include.List`       | -    | -                    | `<name1>\n<name2>\n...` |
| `policy.Get` <br> `policy.include.Get`         | name | -                    | `<token>\n<content>`    |
| `policy.Replace` <br> `policy.include.Replace` | name | `<token>\n<content>` | -                       |
| `policy.Remove` <br> `policy.include.Remove`   | name | `<token>`            | -                       |

The `policy.*` calls refer to main policy files (`/etc/qubes/policy.d/`), and
the `policy.include.*` calls refer to the include directory
(`/etc/qubes/policy.d/include/`). The `.policy` extension for files in the main
directory is always omitted.

The responses do not follow admin API protocol, but signal error using an exit
code and a message on stdout.

The changes are validated before saving, so that the policy cannot end up in an
invalid state (e.g. syntax error, missing include file).

In addition, there is a mechanism to prevent concurrent modifications of the policy files:

- A `*.Get` call returns a file along with a *token* (currently implemented as
  a hash of the file).
- When calling `Replace` or `Remove`, you need to include the current token as
  first line. If the token does not match, the modification will fail.
- When adding a new file using `Replace`, pass `new` as token. This will ensure
  that the file does not exist before adding.
- To skip the check, pass `any` as token.

## TODO

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
