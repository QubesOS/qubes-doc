---
layout: doc
title: Tips and Tricks
redirect_from:
- /doc/tips-and-tricks/
---

Tips and Tricks
===============
This section provides user suggested tips that aim to increase Qubes OS usability, security or that allow users to discover new ways to use your computer that are unique to Qubes OS.

Opening links in your preferred AppVM
-------------------------------------
To increase both security and usability you can set an AppVM so that it automatically opens any link in an different AppVM of your choice. You can do this for example in the email AppVM, in this way you avoid to make mistakes like opening links in it. To learn more you can check [security guidelines](/doc/security-guidelines/) and [security goals](/security/goals/).

The command `qvm-open-in-vm` lets you open a document or a URL in another VM. It takes two parameters: vmname and filename.

For example, if you launch this command from your email AppVM:

`qvm-open-in-vm untrusted https://duckduckgo.com`

it will open duckduckgo.com in the `untrusted` AppVM (after you confirmed the request).

If you want this to happen automatically you can create a .desktop file that advertises itself as a handler for http/https links, and then set this as your default browser.

Open a text editor and copy and paste this into it:

    [Desktop Entry]
    Encoding=UTF-8
    Name=BrowserVM
    Exec=qvm-open-in-vm APPVMNAME %u
    Terminal=false
    X-MultipleArgs=false
    Type=Application
    Categories=Network;WebBrowser;
    MimeType=x-scheme-handler/unknown;x-scheme-handler/about;text/html;text/xml;application/xhtml+xml;application/xml;application/vnd.mozilla.xul+xml;application/rss+xml;application/rdf+xml;image/gif;image/jpeg;image/png;x-scheme-handler/http;x-scheme-handler/https;

Replace `APPVMNAME` with the AppVM name you want to open links in. Now save, in the AppVM that you want to modify, this file to `~/.local/share/applications/browser_vm.desktop`

Finally, set it as your default browser:

`xdg-settings set default-web-browser browser_vm.desktop`

Credit: [Micah Lee](https://micahflee.com/2016/06/qubes-tip-opening-links-in-your-preferred-appvm/)

Preventing data leaks
---------------------
First make sure to read [Understanding and Preventing Data Leaks](/doc/data-leaks/) section to understand the limits of this tip.

Suppose that you have within a not so trusted environment - for example, a Windows VM - an application that tracks and reports its usage, or you simply want to protect your data.

Start the Windows TemplateVM (which has no user data), install/upgrade apps; then start Windows AppVM (with data) in offline mode. So, if you worry (hypothetically) that your Windows or app updater might want to send your data away, this Qubes OS trick will prevent this.
This applies also to any TemplateBasedVM relative to its parent TemplateVM, but the privacy risk is especially high in the case of Windows.

Credit: [Joanna Rutkovska](https://twitter.com/rootkovska/status/832571372085850112)

