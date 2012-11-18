---
layout: wiki
title: QubesScreenshots
permalink: /wiki/QubesScreenshots/
---

Select Qubes OS Screenshots
===========================

Starting applications from different domains (AppVMs) is very easy:

[![](http://files.qubes-os.org/Screenshots_files/snapshot15.png "http://files.qubes-os.org/Screenshots_files/snapshot15.png")](http://files.qubes-os.org/Screenshots_files/snapshot15.png)

In this example, the word processor runs in the “work” domain, which has been assigned “green” label, and is fully isolated from other domains, such as the “red” domain (assigned the “red” label -- “Watch out!”, “Danger!”) used for random Web browsing, news reading, etc. Apps from different domains run in different AppVMs and have different X servers, filesystems, etc. Notice the different color frames (labels), and VM names in the titlebar -- these are drawn by the trusted Window Manager running in Dom0 and apps running in domains cannot fake them:

[![](http://files.qubes-os.org/Screenshots_files/snapshot13.png "http://files.qubes-os.org/Screenshots_files/snapshot13.png")](http://files.qubes-os.org/Screenshots_files/snapshot13.png)

And here's just another example (click to zoom):

[![](http://2.bp.blogspot.com/-zJFn81JdryI/UAqu7H9KSHI/AAAAAAAAAJ0/q_vVqkoEDTY/s1600/snapshot9.png "http://2.bp.blogspot.com/-zJFn81JdryI/UAqu7H9KSHI/AAAAAAAAAJ0/q_vVqkoEDTY/s1600/snapshot9.png")](http://2.bp.blogspot.com/-zJFn81JdryI/UAqu7H9KSHI/AAAAAAAAAJ0/q_vVqkoEDTY/s1600/snapshot9.png)

It is always clearly visible to which domain a given window belongs. Here it’s immediately clear that the passphrase-prompting window belongs to some domain with “green” label. Then, when we look at the titlebar, we see “[work]”, which is the name of the actual domain. Theoretically, the untrusted application (here, the “red” Firefox) beneath the prompt window could draw a similarly looking window within its contents. In practice this would be very hard, because it doesn’t know e.g. the exact decoration style that is in use. However, if that is a concern, the user can simply try to move the more trusted window onto some empty space on the desktop, i.e. so that no other window was present beneath it. Or, better yet use the Expose-like effect (available via a hot-key). A malicious application from untrusted domain cannot spoof the whole desktop, because the trusted Window Manager will never let any domain to “own” the whole screen -- its titlebar will always be visible:

[![](http://files.qubes-os.org/Screenshots_files/password-prompt.png "http://files.qubes-os.org/Screenshots_files/password-prompt.png")](http://files.qubes-os.org/Screenshots_files/password-prompt.png)

Qubes is all about seamless integration from the user’s point of view -- here you can see how it virtualizes tray icons from other domains. Notice the network icon in a red frame. This icon is in fact managed by the Network Manager running in a separate NetVM. The notes icon (with green frame around) has been drawn by the note-taking app running in the work domain (that gas green label):

[![](http://files.qubes-os.org/Screenshots_files/snapshot6.png "http://files.qubes-os.org/Screenshots_files/snapshot6.png")](http://files.qubes-os.org/Screenshots_files/snapshot6.png)

All the networking runs in a special, unprivileged NetVM (notice the red frame around the [NetworkManager?](/wiki/NetworkManager) dialog box on the screen above). Thanks to this, a potential compromise of your network card driver, or [WiFi?](/wiki/WiFi) stack, or DHCP client, would not affect the integrity of the rest of the system! This feature requires Intel VT-d or AMD IOMMU hardware (e.g. Core i5/i7 systems):

[![](http://files.qubes-os.org/Screenshots_files/snapshot9.png "http://files.qubes-os.org/Screenshots_files/snapshot9.png")](http://files.qubes-os.org/Screenshots_files/snapshot9.png)

Qubes lets you update all the software in all the domains all at once, in a centralized way. This is possible thanks to Qubes unique Template VM technology. Note that one doesn’t need to shutdown other VMs (domains) for the update process. This can be done later, in a convenient moment, and separately per each VM:

[![](http://files.qubes-os.org/Screenshots_files/snapshot1.png "http://files.qubes-os.org/Screenshots_files/snapshot1.png")](http://files.qubes-os.org/Screenshots_files/snapshot1.png)

Qubes supports secure copy-and-paste operations between AppVMs. Only the user can initiate a copy and paste operation using a special key combination (Ctrl-Shift-C/V). Other AppVMs have no access to the clipboard buffer, so they cannot steal data from the clipboard. Only the user decides which AppVM should be given access to the clipboard (this is done by selecting the destination AppVM’s window and pressing Ctrl-Shift-V combination):

[![](http://files.qubes-os.org/Screenshots_files/copy-paste-1.png "http://files.qubes-os.org/Screenshots_files/copy-paste-1.png")](http://files.qubes-os.org/Screenshots_files/copy-paste-1.png) [![](http://files.qubes-os.org/Screenshots_files/copy-paste-2.png "http://files.qubes-os.org/Screenshots_files/copy-paste-2.png")](http://files.qubes-os.org/Screenshots_files/copy-paste-2.png)

Qubes also supports secure file copying between AppVMs:

[![](http://files.qubes-os.org/Screenshots_files/snapshot21.png "http://files.qubes-os.org/Screenshots_files/snapshot21.png")](http://files.qubes-os.org/Screenshots_files/snapshot21.png)

Qubes provides a dedicated firewall that itself runs in an isolated FirewallVM:

[![](http://files.qubes-os.org/Screenshots_files/snapshot25.png "http://files.qubes-os.org/Screenshots_files/snapshot25.png")](http://files.qubes-os.org/Screenshots_files/snapshot25.png)
