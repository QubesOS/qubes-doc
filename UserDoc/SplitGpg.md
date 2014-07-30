---
layout: wiki
title: SplitGpg
permalink: /wiki/UserDoc/SplitGpg/
---

Qubes Split GPG
===============

What is Split GPG and why should I use it instead of the standard GPG?
----------------------------------------------------------------------

Split GPG implements a concept similar to having a smart card with your private GPG keys, except that the role of the "smart card" plays another Qubes AppVM. This way one, not-so-trusted domain, e.g. the one where Thunderbird is running, can delegate all crypto operations, such as encryption/decryption and signing to another, more trusted, network-isolated, domain. This way a compromise of your domain where the Thunderbird or other client app is running -- arguably a not-so-unthinkable scenario -- does not allow the attacker to automatically also steal all your keys (we should make a rather obvious comment here that the so-often-used passphrases on private keys are pretty meaningless because the attacker can easily set up a simple backdoor which would wait until the user enters the passphrase and steal the key then).

The diagram below presents the big picture of Split GPG architecture.

[![No image "split-gpg-diagram.png" attached to UserDoc/SplitGpg](/chrome/common/attachment.png "No image "split-gpg-diagram.png" attached to UserDoc/SplitGpg")](/attachment/wiki/UserDoc/SplitGpg/split-gpg-diagram.png)

### Advantages of Split GPG vs. traditional GPG with a smart card

It is often thought that the use of smart cards for private key storage guarantees ultimate safety. While this might be true (unless the attacker can find a usually-very-expensive-and-requiring-physical-presence way to extract the key from the smart card) but only with regards to the safety of the private key itself. However, there is usually nothing that could stop the attacker from requesting the smart card to perform decryption of all the user documents the attacker has found or need to decrypt. In other words, while protecting the user's private key is an important task, we should not forget that ultimately it is the user data that are to be protected and that the smart card chip has no way of knowing the requests to decrypt documents are now coming from the attacker's script and not from the user sitting in front of the monitor. (Similarly the smart card doesn't make the process of digitally signing a document or a transaction in any way more secure -- the user cannot know what the chip is really signing. Unfortunately this problem of signing reliability is not solvable by Split GPG)

With Qubes Split GPG this problem is drastically minimized, because each time the key is to be used the user is asked for consent (with a definable time out, 5 minutes by default), plus is always notified each time the key is used via a tray notification from the domain where GPG backend is running. This way it would be easy to spot unexpected requests to decrypt documents.

[![No image "r2-split-gpg-1.png" attached to UserDoc/SplitGpg](/chrome/common/attachment.png "No image "r2-split-gpg-1.png" attached to UserDoc/SplitGpg")](/attachment/wiki/UserDoc/SplitGpg/r2-split-gpg-1.png) [![No image "r2-split-gpg-3.png" attached to UserDoc/SplitGpg](/chrome/common/attachment.png "No image "r2-split-gpg-3.png" attached to UserDoc/SplitGpg")](/attachment/wiki/UserDoc/SplitGpg/r2-split-gpg-3.png)

### Current limitations

-   Current implementation requires importing of public keys to the vault domain. This opens up an avenue to attack the gpg running in the backend domain via a hypothetical bug in public key importing code. See this ticker \#474 for more details and plans how to get around this problem.

-   It doesn't solve the problem of allowing the user to know what is to be signed before the operation gets approved. Perhaps the GPG backend domain could start a Disposable VM and have the to-be-signed document displayed there? To Be Determined.

Configuring and using Split GPG
-------------------------------

Start with creating a dedicated AppVM for storing your keys (the GPG backend domain). It is recommended that this domain be network disconnected (set its netvm to `none`) and only used for this one purpose. In later examples this AppVM is named `work-gpg`, but of course it might have any other name.

### Setting up the GPG backend domain

Make sure the gpg is installed there and there are some private keys in the keyring, e.g.:

``` {.wiki}
[user@work-gpg ~]$ gpg -K
/home/user/.gnupg/secring.gpg
-----------------------------
sec   4096R/3F48CB21 2012-11-15
uid                  Qubes OS Security Team <security@qubes-os.org>
ssb   4096R/30498E2A 2012-11-15
(...)
```

This is pretty much all that is required. However one might also want to modify the default timeout which tells the backend for how long the user's approval for key access should be valid (default 5 minutes). This is adjustable via `QUBES_GPG_AUTOACCEPT` variable. One can override it e.g. in `~/.bash_profile`:

``` {.wiki}
[user@work-gpg ~]$ echo "export QUBES_GPG_AUTOACCEPT=86400" >> ~/.bash_profile
```

### Configuring the client apps to use split GPG backend

Normally it should be enough to set the `QUBES_GPG_DOMAIN` to the GPG backend domain name and use `qubes-gpg-client` in place of `gpg`, e.g.:

``` {.wiki}
[user@work ~]$ export QUBES_GPG_DOMAIN=work-gpg
[user@work ~]$ gpg -K
[user@work ~]$ qubes-gpg-client -K
/home/user/.gnupg/secring.gpg
-----------------------------
sec   4096R/3F48CB21 2012-11-15
uid                  Qubes OS Security Team <security@qubes-os.org>
ssb   4096R/30498E2A 2012-11-15
(...)

[user@work ~]$ qubes-gpg-client secret_message.txt.asc 
(...)
```

Note that running normal `gpg -K` in the demo above shows no private keys stored in this AppVM.

However, when using Thunderbird with Enigmail extension it is not enough, because Thunderbird doesn't preserve the environment variables. Instead it is recommended to use a simple script provided by `/usr/bin/qubes-gpg-client-wrapper` file by pointing Enigmail to use this script instead of the standard GnuPG binary:

[![No image "tb-enigmail-split-gpg-settings-2.png" attached to UserDoc/SplitGpg](/chrome/common/attachment.png "No image "tb-enigmail-split-gpg-settings-2.png" attached to UserDoc/SplitGpg")](/attachment/wiki/UserDoc/SplitGpg/tb-enigmail-split-gpg-settings-2.png)

The script also sets the QUBES\_GPG\_DOMAIN variable automatically based on the content of the file `/rw/config/gpg-split-domain`, which should be set to the name of the GPG backend VM. This file survives the AppVM reboot, of course.

``` {.wiki}
[user@work ~]$ sudo bash
[user@work ~]$ echo "work-gpg" > /rw/config/gpg-split-domain
```

### Importing public keys

Use `qubes-gpg-import-key` in the client AppVM to import the key into the GPG backend VM. Of course a (safe, unspoofable) user consent dialog box is displayed to accept this.

``` {.wiki}
[user@work ~]$ export QUBES_GPG_DOMAIN=work-gpg
[user@work ~]$ qubes-gpg-import-key ~/Downloads/marmarek.asc
```

[![No image "r2-split-gpg-5.png" attached to UserDoc/SplitGpg](/chrome/common/attachment.png "No image "r2-split-gpg-5.png" attached to UserDoc/SplitGpg")](/attachment/wiki/UserDoc/SplitGpg/r2-split-gpg-5.png)
