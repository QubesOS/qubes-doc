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

Creating a Shortcut in KDE
--------------------------

Let's make Signal a bit more usable by creating a shortcut in our desktop
panel that launches Signal directly. This assumes that you're using KDE in Dom0
and that your AppVM is named `Signal`.

1. Create a Chromium shortcut (Q -> Domain: Signal -> Signal: Add more
   shortcuts... -> Select "Chromium web browser")
2. Follow [these instructions][shortcut] to create a desktop shortcut.
3. Right-click on Chromium icon in panel and select "Icon Settings".
4. Change the "Command" field of the "Application" tab to:

        qvm-run -a --tray Signal '/usr/lib64/chromium-browser/chromium-browser.sh --profile-directory=Default --app-id=<long string which you'll get from the properties of the desktop shortcut you created above>'

   **Note:** Another method (more "correct" but less straightforward) is to [use
   the way Qubes handles shortcuts internally to create a `.desktop`
   file][shortcut-desktop].
5. (Optional) Copy the Signal app icon file from the Signal AppVM to dom0.
   (**Warning**: copying untrusted files to dom0 is dangerous! Do this only if
   you understand and accept the risks!)

        [user@dom0]$ qvm-run --pass-io Signal 'cat /home/user/.local/share/icons/hicolor/48x48/apps/chrome-<long-appID>-Default.png' > /home/users/signal-icon.png
6. (Optional) Change your new shortcut's icon from Chrome to Signal by pointing
   it to `/home/users/signal-icon.png`.

-----

These instructions were contributed by Qubes community member Alex (IX4 Svs) in
a [message] to the `qubes-users` [mailing list]. Thanks, Alex!


[Signal]: https://whispersystems.org/
[signal-wikipedia]: https://en.wikipedia.org/wiki/Signal_(software)
[shortcut]: http://support.whispersystems.org/hc/en-us/articles/216839277-Where-is-Signal-Desktop-on-my-computer-
[shortcut-desktop]: /doc/managing-appvm-shortcuts/#tocAnchor-1-1-1
[message]: https://groups.google.com/d/msg/qubes-users/rMMgeR-KLbU/XXOFri26BAAJ
[mailing list]: /mailing-lists/

