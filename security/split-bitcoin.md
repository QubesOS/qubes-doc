---
layout: doc
title: Split Bitcoin
permalink: /doc/split-bitcoin/
---

How to Set Up a Split Bitcoin Wallet in Qubes
=============================================


What is a "Split" Bitcoin Wallet?
---------------------------------

A "split" bitcoin wallet is a strategy of protecting your bitcoin by having your wallet split into an offline "[cold storage](https://en.bitcoin.it/wiki/Cold_storage)" wallet and an online "watching only" wallet.


A "Watching" Wallet and a "Cold" Wallet
---------------------------------------

1. Create a Debian 8 backports template using the Qubes VM Manager or running
   `qvm-clone debian-8 debian-8-backports` in dom0.

2. Add backports to the sources for the new template by opening a terminal in
   the new template, run `sudo vi /etc/apt/sources.list` and add
   `deb http://http.debian.net/debian jessie-backports main`.

   (If you are new to `vi` text editing, type `i` to be able to edit, and when
   done editing press `ESC` then type `:x` and press `ENTER`.)

3. Update source list: `sudo apt-get update`.

4. Install `electrum` from backports:
   `sudo apt-get -t jessie-backports install electrum`.

5. shut down your `debian-8-backports` template

6. create an `offline-bitcoin` qube based on `debian-8-backports` using the Qubes VM Manager or running `qvm-create -t debian-8-backports -l black offline-bitcoin` and `qvm-prefs -s offline-bitcoin netvm none` in dom0.

7. follow the [electrum documentation in creating an offline wallet](http://docs.electrum.org/en/latest/coldstorage.html#create-an-offline-wallet)

8. create a `watching-bitcoin` qubes based on `debian-8-backports` connecting to the internet how ever you prefer using the Qubes VM Manager or running for example `qvm-create -t debian-8-backports -l green watching-bitcoin` and `qvm-prefs -s watching-bitcoin netvm sys-whonix` in dom0.

9. follow the [electrum documentation in creating an online watching-only wallet](http://docs.electrum.org/en/latest/coldstorage.html#create-a-watching-only-version-of-your-wallet)

Important Notes
---------------

* The private keys (xpriv) should never be moved outside of `offline-bitcoin`.
* For copying out the public keys (xpub), Qubes provides two secure, convenient
  methods: the [inter-VM clipboard] and [inter-VM file copy] tools. Compared to
  traditional physically air-gapped machines, these tools make it very easy to
  copy out public keys.

[inter-VM clipboard]: /doc/copy-paste/
[inter-VM file copy]: /doc/copying-files/

