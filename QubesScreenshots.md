---
layout: wiki
title: QubesScreenshots
permalink: /wiki/QubesScreenshots/
---

Select Qubes OS Screenshots
===========================

[![No image "r2b2-kde-start-menu.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-kde-start-menu.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-kde-start-menu.png)

Starting applications from different domains (AppVMs) is very easy.

* * * * *

[![No image "r2b2-kde-three-domains-at-work.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-kde-three-domains-at-work.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-kde-three-domains-at-work.png)

In this example, the word processor runs in the “work” domain, which has been assigned the “green” label. It is fully isolated from other domains, such as the “untrusted” domain (assigned the “red” label -- “Watch out!”, “Danger!”) used for random Web browsing, news reading, as well as from the "work-web" domain (assigned the "yellow" label), which is used for work-related Web browsing that is not security critical. Apps from different domains run in different AppVMs and have different X servers, filesystems, etc. Notice the different color frames (labels) and VM names in the titlebars. These are drawn by the trusted Window Manager running in Dom0, and apps running in domains cannot fake them:

* * * * *

[![No image "r2b1-two-win-vms-3.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b1-two-win-vms-3.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b1-two-win-vms-3.png)

Qubes Release 2 can also run Windows domains, though, at the moment, there is no seamless GUI virtualization for Windows domains. (I.e., all the Windows VM's applications are displayed within one window.) Other Qubes features, such as the secure inter-VM clipboard, secure file copy, and qrexec in general, all work fine with Windows domains via our (proprietary) Qubes Windows Tools, which must be installed within Windows VMs). In R2 Beta 3, we plan to also introduce seamless GUI mode for Windows VMs. (Linux domains have had seamless GUI integration since day one.)

* * * * *

[![No image "r2b2-xfce4-programmers-desktop-2.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-xfce4-programmers-desktop-2.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-xfce4-programmers-desktop-2.png)

Here we see Xfce4.10 Window Manager running in Dom0 (instead of KDE as on previous screens). Qubes supports customized Xfce4 in dom0 beginning with R2 Beta 2!

* * * * *

[![](http://files.qubes-os.org/Screenshots_files/password-prompt.png "http://files.qubes-os.org/Screenshots_files/password-prompt.png")](http://files.qubes-os.org/Screenshots_files/password-prompt.png)

It is always clearly visible to which domain a given window belongs. Here it’s immediately clear that the passphrase-prompting window belongs to some domain with the “green” label. When we look at the titlebar, we see “[work]”, which is the name of the actual domain. Theoretically, the untrusted application (here, the “red” Firefox) beneath the prompt window could draw a similar looking window within its contents. In practice, this would be very hard, because it doesn’t know, e.g., the exact decoration style that is in use. However, if this is a concern, the user can simply try to move the more trusted window onto some empty space on the desktop such that no other window is present beneath it. Or, better yet, use the Expose-like effect (available via a hot-key). A malicious application from an untrusted domain cannot spoof the whole desktop because the trusted Window Manager will never let any domain “own” the whole screen. Its titlebar will always be visible.

* * * * *

[![No image "r2b2-kde-tray-icons.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-kde-tray-icons.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-kde-tray-icons.png)

Qubes is all about seamless integration from the user’s point of view. Here you can see how it virtualizes tray icons from other domains. Notice the network icon in a red frame. This icon is in fact managed by the Network Manager running in a separate NetVM. The notes icon (with the green frame around it) has been drawn by the note-taking app running in the work domain (which has the "green" label).

* * * * *

[![No image "r2b2-manager-and-netvm-network-prompt.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-manager-and-netvm-network-prompt.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-manager-and-netvm-network-prompt.png)

All the networking runs in a special, unprivileged NetVM. (Notice the red frame around the Network Manager dialog box on the screen above.) This means that in the event that your network card driver, Wi-Fi stack, or DHCP client is compromised, the integrity of the rest of the system will not be affected! This feature requires Intel VT-d or AMD IOMMU hardware (e.g., Core i5/i7 systems).

* * * * *

[![No image "r2b2-software-update.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-software-update.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-software-update.png)

Qubes lets you update all the software in all the domains all at once, in a centralized way. This is possible thanks to Qubes' unique TemplateVM technology. Note that the user is not required to shut down any AppVMs (domains) for the update process. This can be done later, at a convenient moment, and separately for each AppVM.

* * * * *

[![](http://files.qubes-os.org/Screenshots_files/copy-paste-1.png "http://files.qubes-os.org/Screenshots_files/copy-paste-1.png")](http://files.qubes-os.org/Screenshots_files/copy-paste-1.png) [![](http://files.qubes-os.org/Screenshots_files/copy-paste-2.png "http://files.qubes-os.org/Screenshots_files/copy-paste-2.png")](http://files.qubes-os.org/Screenshots_files/copy-paste-2.png)

Qubes supports secure copy-and-paste operations between AppVMs. Only the user can initiate a copy or paste operation using a special key combination (Ctrl-Shift-C/V). Other AppVMs have no access to the clipboard buffer, so they cannot steal data from the clipboard. Only the user decides which AppVM should be given access to the clipboard. (This is done by selecting the destination AppVM’s window and pressing the Ctrl-Shift-V combination.)

* * * * *

[![No image "r2b2-copy-to-other-appvm-1.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-copy-to-other-appvm-1.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-copy-to-other-appvm-1.png) [![No image "r2b2-copy-to-other-appvm-3.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-copy-to-other-appvm-3.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-copy-to-other-appvm-3.png)

Qubes also supports secure file copying between AppVMs.

* * * * *

[![No image "r2b2-open-in-dispvm-1.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-open-in-dispvm-1.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-open-in-dispvm-1.png) [![No image "r2b2-open-in-dispvm-3.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-open-in-dispvm-3.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-open-in-dispvm-3.png)

Qubes' unique Disposable VMs (DispVMs) allow the user to open any file in a disposable VM in a matter of seconds! A file can be edited in a disposable VM, and any changes are projected back onto the original file. Currently, there is no way to mark files to be automatically opened in a disposable VM (one needs to right-click on the file and choose the "Open in Disposable VM" option), but this is planned for the R2 Beta 3 release.

* * * * *

[![No image "r2b2-convert-to-trusted-pdf-3.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-convert-to-trusted-pdf-3.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-convert-to-trusted-pdf-3.png) [![No image "r2b2-converting-pdf-2.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-converting-pdf-2.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-converting-pdf-2.png)

Qubes provides an advanced infrastructure for programming inter-VM services, such as a PDF converter for untrusted files (which is described in [​this article](http://theinvisiblethings.blogspot.com/2013/02/converting-untrusted-pdfs-into-trusted.html)).

* * * * *

[![No image "r2b1-manager-firewall.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b1-manager-firewall.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b1-manager-firewall.png)

Qubes provides a dedicated firewall that itself runs in an isolated FirewallVM.

* * * * *

And some more screenshots:

[![No image "r2b2-xfce4-start-menu-3.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-xfce4-start-menu-3.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-xfce4-start-menu-3.png)

[![No image "r2b2-kde-red-and-green-terminals.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-kde-red-and-green-terminals.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-kde-red-and-green-terminals.png)

[![No image "r2b2-windows-hvm-power-point.png" attached to QubesScreenshots](/chrome/common/attachment.png "No image "r2b2-windows-hvm-power-point.png" attached to QubesScreenshots")](/attachment/wiki/QubesScreenshots/r2b2-windows-hvm-power-point.png)
