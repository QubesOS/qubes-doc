---
layout: doc
title: Tweaking Tor Browser
permalink: /doc/tweaking-tor-browser/
redirect_from:
- /en/doc/tweaking-tor-browser/
- /doc/tweaking-tor-browser/
- /wiki/TweakingTorBrowser/
---

# Tweaking Tor Browser

## Download Tor Browser Bundle

Download [Tor Browser Bundle](https://www.torproject.org/projects/torbrowser.html.en) or [Tor Browser Launcher](https://github.com/micahflee/torbrowser-launcher) (which downloads, verifies and install Tor Browser Bundle for you).


## Setting Tor Browser as the default web browser

See the [instructions for setting default applications](https://qubes-os.org/docs/doc/default-applications/). To create a `*.desktop` file execute `~/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/start-tor-browser --register-app` (This copies `~/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/start-tor-browser.desktop` to `~/.local/share/applications/`.)

If Tor Browser does not launch as expected try to edit the `.desktop` file by replacing the *two* lines

	Exec=sh -c '"/home/user/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/start-tor-browser" --detach || ([ !  -x "/home/user/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/start-tor-browser" ] && "$(dirname "$*")"/Browser/start-tor-browser --detach)' dummy %k
	X-TorBrowser-ExecShell=./Browser/start-tor-browser --detach

with the *single* line

	Exec=/home/user/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/start-tor-browser --detach %U


## Add a Start Menu entry to launch Tor Browser in a new DispVM

Instructions at <https://groups.google.com/d/msg/qubes-users/MObJDMu7kck/v3RmRaTWAwAJ>. Additional information for i3/dmenu users: <https://groups.google.com/d/msg/qubes-users/MObJDMu7kck/18g0XCcJCQAJ>.


## Running multiple instances of Tor Browser with different IP-addresses (in the same VM)

Follow [these instructions](https://tor.stackexchange.com/questions/2006/how-to-run-multiple-tor-browsers-with-different-ips). Though with Qubes it is usually better to use several DispVMs (with one Tor Browser per VM) instead.

## Using Tor Browser without Tor.

Why?

> The TOR browser is a nice browser even without TOR. Using full on TOR seems a bit extreme to me and is beyond my patience, on the other hand, using a normal Firefox feels like yelling my canvas fingerprints all over the internet. Can I configure the TOR browser to **not** go through the TOR network?

Also, if you use Whonix as NetVM the traffic will be routed through Tor anyway.

The (simple) instructions are here: <https://superuser.com/questions/1117383/can-i-use-tor-browser-without-using-tor-network>

Side effect: Tor Browser is not able to open `.onion` links anymore.

You can check whether the traffic is in fact relayed through Tor by going to <https://check.torproject.org>.

## Open new links in an existing instance of Tor Browser.

By default Tor Browser is launched with the flag `--no-remote`. As a consequence it does not accept remote commands. It is only possible to open new links from within Tor Browser; it will refuse any requests from other applications. There is a good reason for this. Visiting the wrong sites during a browsing session may compromise your anonymity, so it makes sense to minimize the risk of this happening inadvertedly. **By modifying this behavior you open a new attack vector against your anonymity and privacy. Do not proceed unless you understand the implications.**

Add the flag `--allow-remote` to any command that will be used to starting Tor Browser and/or opening a new URL in an existing instance of Tor Browser (e.g. relevant `.desktop` files).
