---
lang: en
layout: doc
permalink: /doc/rpc-policy/
ref: 178
---

RPC Policies
============

This document explains the basics of RPC policies in Qubes.
For more information, see [Qrexec: command execution in VMs](/doc/qrexec3/).

Here's an example of an RPC policy file in dom0:

```
[user@dom0 user ~]$ cat /etc/qubes-rpc/policy/qubes.FileCopy
(...)
@tag:work   @default    ask
@tag:work   @tag:work   allow
@tag:work   @anyvm      deny
@anyvm      @tag:work   deny
@anyvm      @anyvm      ask
```

It has three columns (from left to right): source, destination, and permission.
Each row is a rule.
For example, the second row says that we're **allowed** (third column) to copy a file (since this is the policy file for `qubes.FileCopy`) **from** (first column) any VM tagged with "work" **to** (second column) any VM tagged with "work".
In other words, all the VMs tagged with "work" are allowed to copy files to each other without any prompts.
(If the third column were "ask" instead of "allow", there would be prompts.
I.e., we would be **asked** to approve the action, instead of it always being **allowed**.)

Now, the whole policy file is parsed from top to bottom.
As soon as a rule is found that matches the action being evaluated, parsing stops.
We can see what this means by looking at the third row.
It says that we're **denied** from attempting to copy a file **from** any VM tagged with "work" **to** any VM whatsoever.
(That's what the `@anyvm` keyword means -- literally any VM in the system, except for dom0).
But, wait a minute, didn't we just say (in the second row) that all the VMs tagged with work are **allowed** to copy files to each other?
That's exactly right.
The second and third rows contradict each other, but that's intentional.
Since we know that parsing goes from top to bottom (and stops at the first match), we intentionally put the second row above the third row so that it would take precedence.
This is how we create a policy that says: "VMs tagged with 'work' are allowed to copy files to each other but not to any *other* VMs (i.e., not to VMs that *aren't* tagged with 'work')."

When an operation is initiated with a specific target, e.g. `qvm-copy-to-vm other_work_vm some_file` the policy mechanism looks for a row
matching `source_work_vm other_work_vm PERMISSION`. In this case, assuming both VMs have the `work` tag, the second row would match, and
the operation would be `allow`ed without any prompts. When an operation is initiated without a specific target, e.g. `qvm-copy some_file`,
the policy mechanism looks for a row matching `source_work_vm @default PERMISSION`. In this case, the first row indicates that the user
should be prompted for the destination. The list of destination VMs in the prompt is filtered to only include VMs that are valid as per
the policy (so in this example, only other work VMs would be listed). If the first row was commented out, the second row would not match
(the `@default` placeholder is not included in `@tag:work`) but the third row would match (the `@default` placeholder is included in
`@anyvm`). The `qvm-copy` operation would therefore terminate immediately with the message `Request refused`, without prompting the user
with a list of valid destination VMs, and only `qvm-copy-to-vm` operations with valid destinations would be allowed.

The fourth row says that we're **denied** from copying files **from** any VM in the system **to** any VM tagged with "work".
Again, since parsing goes from top to bottom, this doesn't mean that no files can ever be copied from *any* VM to a VM tagged with "work".
Rather, it means that only VMs that match an earlier rule can do so (in this case, only VMs tagged with "work").

The fifth and final row says that we're **asked** (i.e., prompted) to copy files **from** any VM in the system **to** any VM in the system.
(This rule was already in the policy file by default.
We added the first four.)
Note that it wouldn't make sense to add any rules after this one, since every possible pair of VMs will match the `@anyvm  @anyvm` pattern.
Therefore, parsing will always stop at this rule, and no rules below it will ever be evaluated.

All together, the four rules we added say that all VMs tagged with "work" are allowed to copy files to each other; however, they're denied from copying files to other VMs (without the "work" tag), and other VMs (without the "work" tag) are denied from copying files to them.
The fifth rule means that the user gets prompted for any situation not already covered.

Further details about how this system works can be found in [Qrexec: command execution in VMs](/doc/qrexec3/).

(***Note**: the `$` character is deprecated in qrexec keywords -- please use `@` instead (e.g. `@anyvm`).
For more information, see the bulletin [here](https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-038-2018.txt).*)

