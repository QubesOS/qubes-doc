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

**CAUTION:** Before proceeding, please carefully read [On Digital Signatures and Key Verification][qubes-verifying-signatures].
This website cannot guarantee that any PGP key you download from the Internet is authentic.
Always obtain a trusted key fingerprint via other channels, and always check any key you download against your trusted copy of the fingerprint.

1. (Optional)Create a TemplateVM (Debian 8)

       [user@dom0 ~]$ sudo qubes-dom0-update qubes-template-debian-8

2. Open a terminal in Debian 8

       [user@dom0 ~]$ qvm-run -a debian-8 gnome-terminal
       
3. Use these commands in your terminal

       (Optional)[user@debian-8 ~]$ sudo apt-get install curl
       [user@debian-8 ~]$ curl -s https://updates.signal.org/desktop/apt/keys.asc | sudo apt-key add -
       [user@debian-8 ~]$ echo "deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main" | sudo tee -a /etc/apt/sources.list.d/signal-xenial.list
       [user@debian-8 ~]$ sudo apt update && sudo apt install signal-desktop

5. Shutdown the TemplateVM :

        [user@dom0 ~]$ qvm-shutdown debian-8
        
6. Create an AppVM based on this TemplateVM
7. With your mouse select the `Q` menu -> `Domain: "AppVM Name"` -> `"AppVM Name": Add more shortcuts`
(or `"AppVM Name": VM Settings` -> `Applications`). 
   Select `Signal` from the left `Available` column, move it to the right `Selected` column by clicking the `>` button and then `OK` to apply the changes and close the window.

-----

[qubes-verifying-signatures]: /security/verifying-signatures/
[Signal]: https://whispersystems.org/
[signal-wikipedia]: https://en.wikipedia.org/wiki/Signal_(software)
[shortcut]: https://support.whispersystems.org/hc/en-us/articles/216839277-Where-is-Signal-Desktop-on-my-computer-
[shortcut-desktop]: /doc/managing-appvm-shortcuts/#tocAnchor-1-1-1
[message]: https://groups.google.com/d/msg/qubes-users/rMMgeR-KLbU/XXOFri26BAAJ
[mailing list]: /support/
