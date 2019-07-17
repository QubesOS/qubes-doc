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

TL;DR: You can reduce the amount of information w3m gives about itself and the environment it is running in (and, by extension, you). **It will not make you anonymous; your fingerprint will still be unique.** But it may improve your privacy.

[w3m](http://w3m.sourceforge.net/) 'is a text-based web browser as well as a pager like `more` or `less`. With w3m you can browse web pages through a terminal emulator window (xterm, rxvt or something like that). Moreover, w3m can be used as a text formatting tool which typesets HTML into plain text.'

You can reduce the [browser fingerprint](https://panopticlick.eff.org/about#browser-fingerprinting) by applying the following changes to `~/.w3m/config` in any AppVM you want to use w3m in. (If you have not run w3m yet, you might need to copy the config file from elsewhere.) You can also apply the same changes to `/etc/w3m/config` in the relevant TemplateVM(s) to have them apply to multiple AppVMs; but make sure they are not reversed by the contents of `~/.w3m/config` in any of the AppVMs. (w3m reads `~/.w3m/config` after `/etc/w3m/config`).

* Set `user_agent` to `user_agent Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0`.

	By default w3m identifies itself as `w3m/` + version number. The user agent `Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0` is the most common and the one used by the Tor Browser Bundle (TBB). One in fourteen browsers fingerprinted by Panopticlick has this value.

* Make w3m use the same HTTP_ACCEPT headers the TBB by adding the following lines at the end of the file:

		accept_language en-US,en;q=0.5
		accept_encoding gzip, deflate
		accept_media text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
		
	These changes will hide your computer's locale and some other information that may or may not be unique to the VM in which it is running. With the modifications above w3m will have the same headers as about one in fifteen browsers fingerprinted by Panopticlick.
	
Testing these settings on <https://browserprint.info> returns a fingerprint that is distinguishable from that of the TBB (with JavaScript disabled) only by 'Screen Size (CSS)' and 'Browser supports HSTS?'.\* (<https://panopticlick.eff.org> does not work with w3m.) Due to the low number of w3m users it is highly likely that you will have an unique browser fingerprint among the visitors of a website using somewhat sophisticated browser fingerprinting technology. But at least your browser fingerprint will not reveal your computer's locale settings or other specifics about it in the HTTP_ACCEPT headers. And while it may be inferred from your fingerprint that you use w3m, it is not be explicitly stated in the User-Agent header.

**Reminder: Do not rely on these settings for anonymity. Using w3m is all but guaranteed to make you stand out in the crowd.**

PS: You still need to delete cookies manually (`~/.w3m/cookie`) if you are not running w3m in a DispVM anyway. If you set w3m to not accept cookies, its fingerprint will change. (You can configure w3m to not use store cookies or accept new ones (or both), but the setting `use_cookie` seems to really mean `accept_cookie` and vice-versa, so maybe it is best to delete them manually for now.)

* * *

\* Does someone know how to fix this?
