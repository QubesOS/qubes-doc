---
layout: doc
title: Reducing the fingerprint of the text-based web browser w3m
permalink: /doc/w3m/
redirect_from:
- /en/doc/mutt/
- /doc/W3m/
- /wiki/W3m/
---

Reducing the fingerprint of the text-based web browser w3m
====

[w3m](http://w3m.sourceforge.net/) 'is a text-based web browser as well as a pager like `more` or `less`. With w3m you can browse web pages through a terminal emulator window (xterm, rxvt or something like that). Moreover, w3m can be used as a text formatting tool which typesets HTML into plain text.'

You can reduce the [fingerprint](https://panopticlick.eff.org/about#browser-fingerprinting) of w3m by adjusting some settings to those of the Tor Browser Bunde (TBB) with JavaScript disabled.

**BEWARE: As very few people use w3m for browsing chances are high that you will still be the only person with this fingerprint on your adversary's radar. Also, I am nothing but a wannabe security expert, so do not rely on my advise for anything critical.**

Apply the following changes to `~/.w3m/config` in any AppVM you want to use w3m in. If you have not run w3m yet, you might need to copy the config file from elsewhere. You can also apply the same changes to `/etc/w3m/config` in the relevant TempVM(s) to have them apply to multiple AppVMs; but make sure they are not reversed by the contents of `~/.w3m/config` in any of the AppVMs. (w3m reads `~/.w3m/config` after `/etc/w3m/config`).

* Set `user_agent` to `user_agent Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0`.
* Make w3m use the same HTTP_ACCEPT headers the TBB by adding the following lines at the end of the file:

		accept_language en-US,en;q=0.5
		accept_encoding gzip, deflate
		accept_media text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Testing the settings on <https://browserprint.info> (<https://panopticlick.eff.org> does not work) returns a fingerprint that is destinguishable from that of the TBB (with JavaScript disabled) only by 'Screen Size (CSS)' and 'Browser supports HSTS?'.* Thus by using these settings (and browsing through a torified connection) you will be distinguishable from TBB users, but, if my assumptions are correct, not from me. That is, whoever uses these settings will have the same fingerprint as anyone else using w3m with the same configuration, but for the time being I am probably the only one. (According to Browserprint.info only I have this fingerprint.)

PS: You still need to delete cookies manually (`~/.w3m/cookie`) if you are not running w3m in a DispVM anyway. If you set w3m to not accept cookies, its fingerprint will change. (You can configure w3m to not use store cookies or accept new ones (or both), but the setting `use_cookie` seems to really mean `accept_cookie` and vice-versa, so maybe it is best to delete them manually for now.)

* * *

\* Does someone know how to fix this?
