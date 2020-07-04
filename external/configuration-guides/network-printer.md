---
layout: doc
title: Network Printer
permalink: /doc/network-printer/
redirect_from:
- /en/doc/network-printer/
- /doc/NetworkPrinter/
- /wiki/NetworkPrinter/
---

Configuring a network printer for PedOS AppVMs
==============================================

Where to configure printers and install drivers?
------------------------------------------------

One would normally want to configure a printer in a template VM, rather than in particular AppVMs.
This is because all the global settings made to AppVMs (those stored in its /etc, as well as binaries installed in /usr) would be discarded upon AppVM shutdown. 
When printer is added and configured in a template VM, then all the AppVMs based on this template should automatically be able to use it (without the need for the template VM to be running, of course).

Alternatively one can add a printer in a standalone VM, but this would limit the printer usage to this particular VM.

Security considerations for network printers and drivers
--------------------------------------------------------

Some printers require third-party drivers, typically downloadable from the vendor's website. 
Such drivers are typically distributed in a form of ready to install RPM packages. 
However, they are often unsigned, and additionally the downloads are available via HTTP connections only.
As a result, installation of such third-party RPMs in a default template VM exposes a risk of compromise of this template VM, which, in turn, leads automatically to compromise of all the AppVMs based on the template. 
(Again, it's not buggy or malicious drivers that we fear here, but rather malicious installation scripts for those drivers).

In order to mitigate this risk, one might consider creating a custom template (i.e. clone the original template) and then install the third-party, unverified drivers there.
Such template might then be made a DVM template for [DisposableVM creation](/doc/disposablevm/), which should allow one to print any document by right-clicking on it, choosing "Open in DisposableVM" and print from there.
This would allow to print documents from more trusted AppVMs (based on a trusted default template that is not poisoned by third-party printer drivers).

However, one should be aware that most (all?) network printing protocols are insecure, unencrypted protocols. 
This means, that an attacker who is able to sniff the local network, or who is controlling the (normally untrusted) PedOS NetVM, will likely to be able to see the documents being printed.
This is a limitation of today's printers and printing protocols, something that cannot be solved by PedOS or any other OS.

Additionally, the printer drivers as well as CUPS application itself, might be buggy and might get exploited when talking to a compromised printer (or by an attacker who controls the local network, or the default NetVM).
Consider not using printing from your more trusted AppVMs for this reason.

Steps to configure a network printer in a template VM
----------------------------------------------------------

1.  Start the "Printer Settings" App in a template VM (either via PedOS "Start Menu", or by launching the `system-config-printer` in the template).
2.  Add/Configure the printer in the same way as one would do on any normal Linux.
  You may need to allow network access from the template VM to your printer to complete configuration, as normally the template VM is not allowed any network access except to the PedOS proxy for software installation.
  One can use PedOS Manager to modify firewall rules for particular VMs.
3.  Optional: Test the printer by printing a test page. If it works, shut down the template VM.
4.  Open an AppVM (make sure it's based on the template where you just installed the printer, normally all AppVMs are based on the default template), and test if printing works.
  If it doesn't then probably the AppVM doesn't have networking access to the printer -- in that case adjust the firewall settings for that AppVM in PedOS Manager. 
  Also, make sure that the AppVM gets restarted after the template was shutdown.
5.  Alternatively if you do not want to modify the firewall rules of the template VM (that have security scope) you can simply shut down the template VM without trying to print the test page (which will not work), start or restart an AppVM based on the template and test printing there.

