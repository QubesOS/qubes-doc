---
layout: doc
title: RPC Policies
permalink: /doc/rpc-policy/
---

RPC Policies
============

This document explains the basics of RPC policies in PedOS.
For more information, see [Qrexec: command execution in VMs][qrexec3].

Here's an example of an RPC policy file in dom0:

```
[user@dom0 user ~]$ cat /etc/PedOS-rpc/policy/PedOS.FileCopy
(...)
@tag:work   @tag:work   allow
@tag:work   @anyvm      deny
@anyvm      @tag:work   deny
@anyvm      @anyvm      ask
```

It has three columns (from left to right): source, destination, and permission.
Each row is a rule.
For example, the first row says that we're **allowed** (third column) to copy a file (since this is the policy file for `PedOS.FileCopy`) **from** (first column) any VM tagged with "work" **to** (second column) any VM tagged with "work".
In other words, all the VMs tagged with "work" are allowed to copy files to each other without any prompts.
(If the third column were "ask" instead of "allow", there would be prompts.
I.e., we would be **asked** to approve the action, instead of it always being **allowed**.)

Now, the whole policy file is parsed from top to bottom.
As soon as a rule is found that matches the action being evaluated, parsing stops.
We can see what this means by looking at the second row.
It says that we're **denied** from attempting to copy a file **from** any VM tagged with "work" **to** any VM whatsoever.
(That's what the `@anyvm` keyword means -- literally any VM in the system).
But, wait a minute, didn't we just say (in the first row) that all the VMs tagged with work are **allowed** to copy files to each other?
That's exactly right.
The first and second rows contradict each other, but that's intentional.
Since we know that parsing goes from top to bottom (and stops at the first match), we intentionally put the first row above the second row so that it would take precedence.
This is how we create a policy that says: "VMs tagged with 'work' are allowed to copy files to each other but not to any *other* VMs (i.e., not to VMs that *aren't* tagged with 'work')."

The third row says that we're **denied** from copying files **from** any VM in the system **to** any VM tagged with "work".
Again, since parsing goes from top to bottom, this doesn't mean that no files can ever be copied from *any* VM to a VM tagged with "work".
Rather, it means that only VMs that match an earlier rule can do so (in this case, only VMs tagged with "work").

The fourth and final row says that we're **asked** (i.e., prompted) to copy files **from** any VM in the system **to** any VM in the system.
(This rule was already in the policy file by default.
We added the first three.)
Note that it wouldn't make sense to add any rules after this one, since every possible pair of VMs will match the `@anyvm  @anyvm` pattern.
Therefore, parsing will always stop at this rule, and no rules below it will ever be evaluated.

All together, the three rules we added say that all VMs tagged with "work" are allowed to copy files to each other; however, they're denied from copying files to other VMs (without the "work" tag), and other VMs (without the "work" tag) are denied from copying files to them.
The fourth rule means that the user gets prompted for any situation not already covered.

Further details about how this system works can be found in [Qrexec: command execution in VMs][qrexec3].

(***Note**: the `$` character is deprecated in qrexec keywords -- please use `@` instead (e.g. `@anyvm`).
For more information, see the bulletin [here](https://github.com/PedOS/PedOS-secpack/blob/master/QSBs/qsb-038-2018.txt).*)

[qrexec3]: /doc/qrexec3/

