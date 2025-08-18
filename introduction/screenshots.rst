===========
Screenshots
===========


|r4.0-xfce-desktop.png|

The default desktop environment is Xfce4.


----


|r4.0-xfce-start-menu.png|

Starting applications from different domains (AppVMs) is very easy.


----


|r4.0-xfce-three-domains-at-work.png|

In this example, the word processor runs in the “work” domain, which has been assigned the “blue” label. It is fully isolated from other domains, such as the “untrusted” domain (assigned the “red” label – “Watch out!”, “Danger!”) used for random Web browsing, news reading, as well as from the “work-web” domain (assigned the “yellow” label), which is used for work-related Web browsing that is not security critical. Apps from different domains run in different AppVMs and have different X servers, filesystems, etc. Notice the different color frames (labels) and VM names in the titlebars. These are drawn by the trusted Window Manager running in Dom0, and apps running in domains cannot fake them:


----


|r2b3-windows-seamless-1.png|

Qubes Release 2 can also run Windows AppVMs in seamless mode, integrated onto the common Qubes trusted desktop, just like Linux AppVMs! The seamless GUI integration has been introduced in Qubes R2 Beta 3. This requires :github:`Qubes Windows Tools <Qubes-Community/Contents/blob/master/docs/os/windows/windows-tools.md>` to be installed in the Windows VMs first.


----


|r2b3-windows-seamless-filecopy.png|

Windows AppVMs are fully integrated with the rest of the Qubes OS system, which includes things such as secure, policy governed, inter-VM file copy, clipboard, and generally our whole elastic qrexec infrastructure for secure inter-VM RPC! Starting with Qubes R2 Beta 3 we also support HVM-based templates allowing to instantly create many Windows AppVMs with shared “root filesystem” from the Template VM (but one should ensure their license allows for such instantiation of the OS in the template). Just like with Linux AppVMs!


----


|r4.0-xfce-programmers-desktop.png|

Here we see Xfce4.14 Window Manager running in Dom0 (instead of KDE as on previous versions). Qubes supports customized Xfce4 in dom0 beginning with R2 Beta 2!


----


|r4.0-password-prompt.png|

It is always clearly visible to which domain a given window belongs. Here it’s immediately clear that the passphrase-prompting window belongs to some domain with the “blue” label. When we look at the titlebar, we see “[qubes]”, which is the name of the actual domain. Theoretically, the untrusted application (here, the red Tor Browser running in a DisposableVM) beneath the prompt window could draw a similar looking window within its contents. In practice, this would be very hard, because it doesn’t know, e.g., the exact decoration style that is in use. However, if this is a concern, the user can simply try to move the more trusted window onto some empty space on the desktop such that no other window is present beneath it. Or, better yet, use the Expose-like effect (available via a hot-key). A malicious application from an untrusted domain cannot spoof the whole desktop because the trusted Window Manager will never let any domain “own” the whole screen. Its titlebar will always be visible.


----


|r4.0-xfce-tray-icons.png|

Qubes is all about seamless integration from the user’s point of view. Here you can see how it virtualizes tray icons from other domains. Notice the network icon is in red. This icon is in fact managed by the Network Manager running in a separate NetVM.


----


|r4.0-manager-and-sysnet-network-prompt.png|

All the networking runs in a special, unprivileged NetVM. (Notice the red frame around the Network Manager dialog box on the screen above.) This means that in the event that your network card driver, Wi-Fi stack, or DHCP client is compromised, the integrity of the rest of the system will not be affected! This feature requires Intel VT-d or AMD IOMMU hardware (e.g., Core i5/i7 systems)


----


|r4.0-software-update.png|

Qubes lets you update all the software in all the domains all at once, in a centralized way. This is possible thanks to Qubes’ unique TemplateVM technology. Note that the user is not required to shut down any AppVMs (domains) for the update process. This can be done later, at a convenient moment, and separately for each AppVM.


----


|r4.0-copy-paste.png|

Qubes supports secure copy-and-paste operations between AppVMs. Only the user can initiate a copy or paste operation using a special key combination (Ctrl-Shift-C/V). Other AppVMs have no access to the clipboard buffer, so they cannot steal data from the clipboard. Only the user decides which AppVM should be given access to the clipboard. (This is done by selecting the destination AppVM’s window and pressing the Ctrl-Shift-V combination.)


----


|“r4.0-copy-to-other-appvm-1.png| |r4.0-copy-to-other-appvm-3.png|

Qubes also supports secure file copying between AppVMs.


----


|r4.0-open-in-dispvm-1.png| |r4.0-open-in-dispvm-2.png|

Qubes’ unique DisposableVMs (DispVMs) allow the user to open any file in a disposable VM in a matter of seconds! A file can be edited in a disposable VM, and any changes are projected back onto the original file. Currently, there is no way to mark files to be automatically opened in a disposable VM (one needs to right-click on the file and choose the “View in DisposableVM” or “Edit in DisposableVM” option), but this is planned for the R2 Beta 3 release.


----


|r4.0-convert-to-trusted-pdf-1.png| |r4.1-converting-pdf.png|

Qubes provides an advanced infrastructure for programming inter-VM services, such as a PDF converter for untrusted files (which is described in `this article <https://blog.invisiblethings.org/2013/02/21/converting-untrusted-pdfs-into-trusted.html>`__).


----


|r4.0-manager-firewall.png|

Qubes provides a dedicated firewall that itself runs in an isolated FirewallVM.


----


And some more screenshots:

|r4.0-xfce-red-and-green-terminals.png|

|r2b3-windows-seamless-2.png|

.. |r4.0-xfce-desktop.png| image:: /attachment/doc/r4.0-xfce-desktop.png
   

.. |r4.0-xfce-start-menu.png| image:: /attachment/doc/r4.0-xfce-start-menu.png
   

.. |r4.0-xfce-three-domains-at-work.png| image:: /attachment/doc/r4.0-xfce-three-domains-at-work.png
   

.. |r2b3-windows-seamless-1.png| image:: /attachment/doc/r2b3-windows-seamless-1.png
   

.. |r2b3-windows-seamless-filecopy.png| image:: /attachment/doc/r2b3-windows-seamless-filecopy.png
   

.. |r4.0-xfce-programmers-desktop.png| image:: /attachment/doc/r4.0-xfce-programmers-desktop.png
   

.. |r4.0-password-prompt.png| image:: /attachment/doc/r4.0-password-prompt.png
   

.. |r4.0-xfce-tray-icons.png| image:: /attachment/doc/r4.0-xfce-tray-icons.png
   

.. |r4.0-manager-and-sysnet-network-prompt.png| image:: /attachment/doc/r4.0-manager-and-sysnet-network-prompt.png
   

.. |r4.0-software-update.png| image:: /attachment/doc/r4.0-software-update.png
   

.. |r4.0-copy-paste.png| image:: /attachment/doc/r4.0-copy-paste.png
   

.. |“r4.0-copy-to-other-appvm-1.png| image:: /attachment/doc/r4.0-copy-to-other-appvm-1.png
   

.. |r4.0-copy-to-other-appvm-3.png| image:: /attachment/doc/r4.0-copy-to-other-appvm-2.png
   

.. |r4.0-open-in-dispvm-1.png| image:: /attachment/doc/r4.0-open-in-dispvm-1.png
   

.. |r4.0-open-in-dispvm-2.png| image:: /attachment/doc/r4.0-open-in-dispvm-2.png
   

.. |r4.0-convert-to-trusted-pdf-1.png| image:: /attachment/doc/r4.0-convert-to-trusted-pdf-1.png
   

.. |r4.1-converting-pdf.png| image:: /attachment/doc/r4.1-converting-pdf.png
   

.. |r4.0-manager-firewall.png| image:: /attachment/doc/r4.0-manager-firewall.png
   

.. |r4.0-xfce-red-and-green-terminals.png| image:: /attachment/doc/r4.0-xfce-red-and-green-terminals.png
   

.. |r2b3-windows-seamless-2.png| image:: /attachment/doc/r2b3-windows-seamless-2.png
   
