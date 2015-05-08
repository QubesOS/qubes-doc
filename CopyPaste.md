---
layout: doc
title: CopyPaste
permalink: /doc/CopyPaste/
redirect_from: /wiki/CopyPaste/
---

Copy and Paste between domains
==============================

Qubes fully supports secure copy and paste operation between domains. In order to copy a clipboard from domain A to domain B, follow those steps:

1.  Click on the application window in the domain A where you have selected text for copying. Then use the *app-specific* hot-key (or menu option) to copy this into domain's local clipboard (in other words: do the copy operation as usual, in most cases by pressing Ctrl-C).
2.  Then (when the app in domain A is still in focus) press Ctrl-Shift-C magic hot-key. This will tell Qubes that we want to select this domain's clipboard for *global copy* between domains.
3.  Now select the destination app, running in domain B, and press Ctrl-Shift-V, another magic hot-key that will tell Qubes to make the clipboard marked in the previous step available to apps running in domain B. This step is necessary because it ensures that only domain B will get access to the clipboard copied from domain A, and not any other domain that might be running in the system.
4.  Now, in the destination app use the app-specific key combination (usually Ctrl-V) for pasting the clipboard.

Note that the global clipboard will be cleared after step \#3, to prevent accidental leakage to another domain, if the user accidentally pressed Ctrl-Shift-V later.

This 4-step process might look complex, but after some little practice it really is very easy and fast. At the same time it provides the user with full control over who has access to the clipboard.

Note that only simple plain text copy/paste is supported between AppVMs. This is discussed in a bit more detail in [this message](https://groups.google.com/group/qubes-devel/msg/57fe6695eb8ec8cd).

On Copy/Paste Security
----------------------

The scheme is *secure* because it doesn't allow other VMs to steal the content of the clipboard. However, one should keep in mind that performing a copy and paste operation from *less trusted* to *more trusted* domain can always be potentially insecure, because the data that we insert might potentially try to exploit some hypothetical bug in the destination VM (e.g. the seemingly innocent link that we copy from untrusted domain, might turn out to be, in fact, a large buffer of junk that, when pasted into the destination VM's word processor could exploit a hypothetical bug in the undo buffer). This is a general problem and applies to any data transfer between *less trusted to more trusted* domain. It even applies to copying files between physically separate machines (air-gapped) systems. So, you should always copy clipboard and data only from *more trusted* to *less trusted* domains.

See also [this article](http://theinvisiblethings.blogspot.com/2011/03/partitioning-my-digital-life-into.html) for more information on this topic, and some ideas of how we might solve this problem in some future version of Qubes.

And [this message](https://groups.google.com/group/qubes-devel/msg/48b4b532cee06e01) from qubes-devel.

Copy/Paste between dom0 and other domains
-----------------------------------------

Copy/Paste between dom0 and other domains is intentionally prohibited by default. There should normally be no reason for any data exchange between dom0 and other VMs (except for the reporting of error logs). In order to easily copy/paste the contents of logs from dom0 to the inter-VM clipboard:

1.  Right-click on the desired VM in the Qubes VM Manager.
2.  Click "Logs."
3.  Click on the desired log.
4.  Click "Copy to Qubes clipboard."

You may now paste the log contents to any VM as you normally would (i.e., Ctrl-Shift-V, then Ctrl-V).

For data other than logs, there are two options:

1.  [Copy it as a file.](/wiki/CopyToDomZero)
2.  Paste the data to `/var/run/qubes/qubes-clipboard.bin`, then write "dom0" to `/var/run/qubes/qubes-clipboard.bin.source`. Then use Ctrl-Shift-V to paste the data to the desired VM.

Clipboard automatic policy enforcement
--------------------------------------

The Qubes clipboard policy is configurable in:

{% highlight trac-wiki %}
/etc/qubes-rpc/policy/qubes.ClipboardPaste
{% endhighlight %}

You may wish to configure this policy in order to prevent user error. For example, if you are certain that you never wish to paste *into* your "vault" AppVM (and it is highly recommended that you do not), then you should edit the policy as follows:

{% highlight trac-wiki %}
$anyvm  vault   deny
$anyvm  $anyvm  ask
{% endhighlight %}

Shortcut Configuration
----------------------

The copy/paste shortcuts are configurable in:

{% highlight trac-wiki %}
/etc/qubes/guid.conf
{% endhighlight %}
