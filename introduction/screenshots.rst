===========
Screenshots
===========

.. image:: /attachment/doc/r4.0-xfce-desktop.png
   :alt: Qubes Desktop running Xfce 
   :width: 100%

The default desktop environment is Xfce4.


----

.. image:: /attachment/doc/r4.0-xfce-three-domains-at-work.png
   :alt: Qubes Desktop showing windows from different qubes.
   :width: 100%


In this example, the word processor runs in the “work” :term:`qube`, which has been assigned the “blue” label. It is fully isolated from other qubes, such as the “untrusted” qube (assigned the “red” label – “Watch out!”, “Danger!”) used for random Web browsing, news reading, as well as from the “work-web” qube (assigned the “yellow” label), which is used for work-related Web browsing that is not security critical. These applications run in different qubes each of which has its own X server, filesystems, etc. Notice the different color frames (labels) and qube names in the titlebars. These are drawn by the trusted Window Manager running in Dom0, and apps running in qubes cannot fake them.


----


.. image:: /attachment/doc/r2b3-windows-seamless-1.png
   :alt: Qubes Desktop showing use of qubes running Windows
   :width: 100%


Qubes can also run Windows qubes in seamless mode, integrated into the common Qubes trusted desktop, just like Linux qubes! (Seamless GUI integration was introduced in Qubes R2 Beta 3.) This requires :doc:`Qubes Windows Tools </user/templates/windows/qubes-windows-tools>` to be installed in the Windows qube first.


----


.. image:: /attachment/doc/r2b3-windows-seamless-filecopy.png
   :alt: Qubes Desktop showing inter qube file copy in Windows qubes
   :width: 100%


Windows qubes are fully integrated with the rest of the Qubes OS system: this includes things such as secure, policy governed, inter-qube file copy, clipboard, and generally our whole elastic qrexec infrastructure for secure inter-qube RPC! Starting with Qubes R2 Beta 3 Qubes also supports HVM-based templates, allowing you to instantly create many Windows qubes with a shared “root filesystem” from the Template (you should ensure your license allows for such instantiation of the OS in the template). Just like with Linux qubes!


----

.. image:: /attachment/doc/r4.0-password-prompt.png
   :alt: Each window shows the name and color of the qube.
   :width: 100%


You can always see clearly to which qube a given window belongs. Here it’s immediately clear that the passphrase-prompting window belongs to some qube with the “blue” label. When we look at the titlebar, we see “[qubes]”, which is the name of the actual qube. Theoretically, the untrusted application (here, the red Tor Browser running in a :term:`disposable`) beneath the prompt window could draw a similar looking window within its contents. In practice, this would be very hard, because it doesn’t know, e.g., the exact decoration style that is in use. However, if this is a concern, the user can simply try to move the more trusted window onto some empty space on the desktop such that no other window is present beneath it. Or, better yet, use the Expose-like effect (available via a hot-key). A malicious application from an untrusted qube cannot spoof the whole desktop because the trusted Window Manager will never let any qube “own” the whole screen. Its titlebar will always be visible.


----


.. image:: /attachment/doc/r4.3/tray.png
   :alt: Tray icons include icons from qubes
   :scale: 100%
   :align: center

Qubes is all about seamless integration from the user’s point of view. Here you can see how it virtualizes tray icons from other qubes. Notice the network icon is in red. This icon is in fact managed by the Network Manager running in a separate :term:`net qube`.


----



.. image:: /attachment/doc/r4.0-manager-and-sysnet-network-prompt.png
   :alt: Qubes desktop showing networking prompt from the net qube, identifiable by color and name.
   :width: 100%


All the networking runs in a special, unprivileged net qube. (Notice the red frame around the Network Manager dialog box on the screen above, which reflects the color assigned to the net qube.) This means that in the event that your network card driver, Wi-Fi stack, or DHCP client is compromised, the integrity of the rest of the system will not be affected! This feature requires Intel VT-d or AMD IOMMU hardware (e.g., Core i5/i7 systems)


----


.. image:: /attachment/doc/r4.3/qubes-os-update.png
   :alt: Qubes Update Tool shows templates that may need updating, and allows you to select which will be updated.
   :width: 100%

Qubes lets you update all the software in all the qubes all at once, in a centralized way. This is possible thanks to Qubes’ unique template technology. Note that the user is not required to shut down any AppVMs (qubes) for the update process to run. This can be done later, at a convenient moment, and separately for each qube.


----


.. image:: /attachment/doc/r4.0-copy-paste.png
   :alt: Qubes desktop showing information window about data securely copied to the global clipboard
   :width: 100%


Qubes supports secure text copy-and-paste operations between qubes. Only the user can initiate a copy or paste operation using a special key combination (Ctrl-Shift-C/V). Other qubes have no access to the clipboard buffer, so they cannot steal data from the clipboard. Only the user decides which qubes should be given access to the clipboard. (This is done by selecting the destination qubes’ window and pressing the Ctrl-Shift-V combination.)


----


.. image:: /attachment/doc/r4.0-copy-to-other-appvm-1.png
   :alt: Qubes desktop showing use of menu to copy file to global clipboard
   :width: 100%


.. image:: /attachment/doc/r4.0-copy-to-other-appvm-2.png
   :alt: Qubes desktop showing security prompt when pasting file from global clipboard
   :width: 100%

Qubes also supports secure file copying between qubes.


----


.. image:: /attachment/doc/r4.3-domU-filemanager-disp-pdfviewer.png 
   :alt: Menu showing option to edit file in disposable
   :width: 100%


.. image:: /attachment/doc/r4.3-domU-filemanager-disp-pdfviewer-open.png
   :alt: Qubes desktop showing source qube and disposable with file open for editing
   :width: 100%


Qubes' unique :term:`disposable` qubes allow the user to open any file in a disposable in a matter of seconds! A file can be edited in a disposable, and any changes are sent back to the original file.

----


.. image:: /attachment/doc/r4.0-convert-to-trusted-pdf-1.png
   :alt: File manager menu with option to convert a file to a trusted PDF
   :width: 100%


.. image:: /attachment/doc/r4.1-converting-pdf.png
   :alt: Qubes desktop showing progress bar for PDF conversion process
   :width: 100%

Qubes provides an advanced infrastructure for programming inter-qube services, such as a PDF converter for untrusted files (which is described in `this article <https://blog.invisiblethings.org/2013/02/21/converting-untrusted-pdfs-into-trusted.html>`__).


----


.. image:: /attachment/doc/r4.3/settings-firewall.png
   :alt: GUI showing how firewall rules can be edited for a qube
   :width: 100%

Qubes provides a dedicated firewall that itself runs in an isolated FirewallVM.


----


And some more screenshots:

.. image:: /attachment/doc/r4.0-xfce-red-and-green-terminals.png
   :alt: Qubes desktop with terminal windows open from different qubes, each with own color assigned.
   :width: 100%


.. image:: /attachment/doc/r2b3-windows-seamless-2.png
   :alt: Qubes desktop with windows open from different qubes running Windows, each with own color assigned.
   :width: 100%

