---
layout: doc
title: Signal
permalink: /doc/signal/
---

Signal
======

What is [Signal]?

[According to Wikipedia:][signal-wikipedia]

> Signal is an encrypted instant messaging and voice calling application
> for Android and iOS. It uses end-to-end encryption to secure all
> communications to other Signal users. Signal can be used to send and receive
> encrypted instant messages, group messages, attachments and media messages.
> Users can independently verify the identity of their messaging correspondents
> by comparing key fingerprints out-of-band. During calls, users can check the
> integrity of the data channel by checking if two words match on both ends of
> the call.
> 
> Signal is developed by Open Whisper Systems. The clients are published as free
> and open-source software under the GPLv3 license.

How to install Signal in Qubes
------------------------------

If you're a Signal user on Android, you can now have Signal inside Qubes.

1. Install the Chromium browser in a TemplateVM.
2. Shut down the TemplateVM.
3. Create a new AppVM based on this TemplateVM.
4. Launch Chromium browser in the new AppVM, type `chrome://extensions/` in the
   address bar, and follow the link to the Chrome app store.
4. In the app store, search for "Signal Private Messenger" and install the app.
5. The app launches automatically on first install. Follow the prompts to "link"
   this app with your phone.
6. Signal should now work in your AppVM.


Creating a Shortcut in the applications menu
--------------------------------------------

Let's make Signal a bit more usable by creating a shortcut in our desktop
panel that launches Signal directly. This assumes that you're using KDE or Xfce in Dom0,
you use Signal in an AppVM named `Signal`, and this AppVM uses `fedora-23` as its TemplateVM.

1. Follow [these instructions][shortcut] to create a desktop shortcut on the Desktop of your Signal AppVM.
   Let's assume the shortcut file you get is `/home/user/Desktop/chrome-bikioccmkafdpakkkcpdbhpfkkhcmohk-Default.desktop`
2. Copy this shortcut file to the AppVM's TemplateVM - in this case, to `fedora-23`.

       [user@Signal ~]$ qvm-copy-to-vm fedora-23 /home/user/Desktop/chrome-bikioccmkafdpakkkcpdbhpfkkhcmohk-Default.desktop

3. You'll also want to copy across an icon for your new shortcut - you can find this at
   `/home/user/.local/share/icons/hicolor/48x48/apps/chrome-bikioccmkafdpakkkcpdbhpfkkhcmohk-Default.png`
   Copy this icon to the `fedora-23` TemplateVM in the same way as step 2.
4. Open a terminal in your `fedora-23` TemplateVM and `cd` to `/home/user/QubesIncoming/Signal/`.
   You should find your shortcut and icon files just transferred across from the Signal AppVM.
   Move these files to the following locations:
   
        [user@fedora-23 Signal]$ sudo mv chrome-bikioccmkafdpakkkcpdbhpfkkhcmohk-Default.desktop /usr/share/applications/
        [user@fedora-23 Signal]$ sudo mv chrome-bikioccmkafdpakkkcpdbhpfkkhcmohk-Default.png /usr/share/icons/hicolor/48x48/apps/

5. From a Dom0 terminal, instruct Qubes to synchronize the application menus of this TemplateVM:

        [user@dom0 ~]$ qvm-sync-appmenus fedora-23
        
6. Stop both the AppVM (`Signal`) and its TemplateVM (`fedora-23`).
   The `Signal` VM will now see the desktop file in `/usr/share/applications` when it is next started.

7. With your mouse select the `Q` menu -> `Domain: Signal` -> `Signal: Add more shortcuts`
   Select `Signal Private Messenger` from the left `Available` column, move it to the right `Selected` column by clicking the `>` button and then `OK` to apply the changes and close the window.
8. (optional, only on KDE:) Follow the `Q` menu once more, right-click on the new `Signal: Signal Private Messenger` menu item and select `Add to Panel`.

You can now launch the Signal messenger inside its own dedicated AppVM directly from the desktop.

The same steps should work for any Chrome app.

Creating a shortcut in the applications menu for a StandaloneVM
---------------------------------------------------------------

If you want to add to the standalone VM rather than a template, then follow below.
The following part will also assume that the .desktop file has been correctly made.
This can also be used to add a application portable application/script from a tar archive, also this part of the guide is assuming that the StandaloneVM is called `Signal`.

1. First you will need to copy/move the .desktop file: `/home/user/Desktop/chrome-bikioccmkafdpakkkcpdbhpfkkhcmohk-Default.desktop`to the applications folder on the StandaloneVM: `/usr/share/applications/`

        [user@Signal ~]$ sudo mv /home/user/Desktop/chrome-bikioccmkafdpakkkcpdbhpfkkhcmohk-Default.desktop /usr/share/applications/

2. Now copy/move over the icon file to make it look all nice and pretty.  

        [user@Signal ~]$ sudo mv /home/user/Desktop/chrome-bikioccmkafdpakkkcpdbhpfkkhcmohk-Default.desktop /usr/share/icons/hicolor/48x48/apps/

3. Now fire up the `dom0` Terminal Emulator from `Q` Menu -> `Terminal Emulator`. All you need to do now is run the command to sync the app menus `qvm-sync-appmenus` along with the Standalone VM name `Signal`.

        [user@dom0 ~]$ qvm-sync-appmenus Signal

4. Now stop the StandaloneVM: `Signal`.

5. With your mouse select the `Q` menu -> `Domain: Signal` -> `Signal: Add more shortcuts`. Select `Signal Private Messenger` from the left `Available` column, move it to the right `Selected` column by clicking the `>` button and then `OK` to apply the changes and close the window.
   
6. (optional, only on KDE:) Follow the `Q` menu once more, right-click on the new `Signal: Signal Private Messenger` menu item and select `Add to Panel`.

Use AppVM based on debian
---------------------------------------------------------------

**CAUTION:** Before proceeding, please carefully read [On Digital Signatures and Key Verification][qubes-verifying-signatures].
This website cannot guarantee that any PGP key you download from the Internet is authentic.
Always obtain a trusted key fingerprint via other channels, and always check any key you download against your trusted copy of the fingerprint.

If you don't use chromium, you can install signal with debian :

1. (Optional)Create a TemplateVM (debian 8)

       [user@dom0 ~]$ sudo qubes-dom0-update qubes-template-debian-8
2. Open a terminal in debian 8

       [user@dom0 ~]$ qvm-run -a debian-8 gnome-terminal
       
3. Use these commands in your terminal

       (Optional)[user@debian-8 ~]$ sudo apt-get install curl
       [user@debian-8 ~]$ curl -s https://updates.signal.org/desktop/apt/keys.asc | sudo apt-key add -
       [user@debian-8 ~]$ echo "deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main" | sudo tee -a /etc/apt/sources.list.d/signal-xenial.list
       [user@debian-8 ~]$ sudo apt uptdate && sudo apt install signal-desktop

5. Shutdown the TemplateVM :

        [user@dom0 ~]$ qvm-shutdown debian-8
        
6. Create a AppVM based on this TemplateVM
7. With your mouse select the `Q` menu -> `Domain: "AppVM Name"` -> `"AppVM Name": Add more shortcuts`
   Select `Signal` from the left `Available` column, move it to the right `Selected` column by clicking the `>` button and then `OK` to apply the changes and close the window.

-----

[qubes-verifying-signatures]: /security/verifying-signatures/
[Signal]: https://whispersystems.org/
[signal-wikipedia]: https://en.wikipedia.org/wiki/Signal_(software)
[shortcut]: https://support.whispersystems.org/hc/en-us/articles/216839277-Where-is-Signal-Desktop-on-my-computer-
[shortcut-desktop]: /doc/managing-appvm-shortcuts/#tocAnchor-1-1-1
[message]: https://groups.google.com/d/msg/qubes-users/rMMgeR-KLbU/XXOFri26BAAJ
[mailing list]: /mailing-lists/
