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

Oepn Whisper Systems develops a desktop version of Signal with the same text messaging functionality as the iPhone and Android apps. Signal for desktops is a Chrome app, which means it requires Google Chrome or its open source alternative Chromium to function. In order to install it on Qubes, you'll need to complete these steps:

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
panel that launches Signal directly. 
This assumes that you're using KDE or Xfce in Dom0,
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

Installing Signal without Chrome
---------------------------------------------------------
Despite the existence of a freedom-respecting open source version of Chrome available for install, some users might want to use it without the browser. Unfortunately, Signal Desktop currently only exists in the form of a Chrome app. In August 2016, Google announced that it is going to [discontinue Chrome apps][discontinuing Chrome apps] starting from the second half of 2017. OWS developers have mentioned on Github that they are planning to [switch to a different platform][Signal moving away from chrome] by then:

> Chrome apps are officially being deprecated and this might be the first signs of it. I don't know what their release schedule looks like but I just upgraded to 57, and hopefully we'll be migrated to a different platform by the time 59 is out.

According to the Chromium developer schedule, 59 is targeted to be out by June 6, 2017.

Based on OWS's [2017 job listings][job listings], the "different platform" will probably be Node or Electron, and a standalone app that's built from the legacy's javascript code.


[Signal]: https://whispersystems.org/
[signal-wikipedia]: https://en.wikipedia.org/wiki/Signal_(software)
[shortcut]: http://support.whispersystems.org/hc/en-us/articles/216839277-Where-is-Signal-Desktop-on-my-computer-
[shortcut-desktop]: /doc/managing-appvm-shortcuts/#tocAnchor-1-1-1
[message]: https://groups.google.com/d/msg/qubes-users/rMMgeR-KLbU/XXOFri26BAAJ
[mailing list]: /mailing-lists/
[job listings]: https://web-beta.archive.org/web/20170126221917/https://whispersystems.org/workworkwork
[discontinuing Chrome apps]: https://blog.chromium.org/2016/08/from-chrome-apps-to-web.html
[Signal moving away from chrome]: https://github.com/WhisperSystems/Signal-Desktop/issues/1100#issuecomment-289234685
