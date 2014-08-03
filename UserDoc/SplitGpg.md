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

-   Current implementation requires importing of public keys to the vault domain. This opens up an avenue to attack the gpg running in the backend domain via a hypothetical bug in public key importing code. See ticket \#474 for more details and plans how to get around this problem, as well as the section on using split GPG with subkeys below.

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

### Configuring [Thunderbird/Enigmail?](/wiki/UserDoc/Thunderbird/Enigmail) for use with Split GPG

However, when using Thunderbird with Enigmail extension it is not enough, because Thunderbird doesn't preserve the environment variables. Instead it is recommended to use a simple script provided by `/usr/bin/qubes-gpg-client-wrapper` file by pointing Enigmail to use this script instead of the standard GnuPG binary:

[![No image "tb-enigmail-split-gpg-settings-2.png" attached to UserDoc/SplitGpg](/chrome/common/attachment.png "No image "tb-enigmail-split-gpg-settings-2.png" attached to UserDoc/SplitGpg")](/attachment/wiki/UserDoc/SplitGpg/tb-enigmail-split-gpg-settings-2.png)

The script also sets the QUBES\_GPG\_DOMAIN variable automatically based on the content of the file `/rw/config/gpg-split-domain`, which should be set to the name of the GPG backend VM. This file survives the AppVM reboot, of course.

``` {.wiki}
[user@work ~]$ sudo bash
[user@work ~]$ echo "work-gpg" > /rw/config/gpg-split-domain
```

*NOTE*: A recent engimail update, version `thunderbird-enigmail-1.7-1`, introduced changes in how Enigmail expects to execute GPG binary and so requires an updated split-gpg package with version \>= `qubes-gpg-split-2.0.7-1`. Please make sure you have all the latest qubes packages installed in your template.

### Importing public keys

Use `qubes-gpg-import-key` in the client AppVM to import the key into the GPG backend VM. Of course a (safe, unspoofable) user consent dialog box is displayed to accept this.

``` {.wiki}
[user@work ~]$ export QUBES_GPG_DOMAIN=work-gpg
[user@work ~]$ qubes-gpg-import-key ~/Downloads/marmarek.asc
```

[![No image "r2-split-gpg-5.png" attached to UserDoc/SplitGpg](/chrome/common/attachment.png "No image "r2-split-gpg-5.png" attached to UserDoc/SplitGpg")](/attachment/wiki/UserDoc/SplitGpg/r2-split-gpg-5.png)

Advanced: Using Split GPG with Subkeys
--------------------------------------

Users with particularly high security requirements may wish to use split GPG with [​subkeys](https://wiki.debian.org/Subkeys). However, this setup comes at a significant cost: It will be impossible to sign other people's keys without breaking this security model. Nonetheless, if signing others' keys is not required, then split GPG with subkeys offers unparalleled security for one's master secret key.

### Setup Description

In this example, the following keys are stored in the following locations:

||
|**PGP Key(s)**|**VM Name**|
|master secret key|vault|
|secret subkeys|work-gpg|
|public key|work-email|

master secret key (sec)  
It is recommended that this key be created as a **certify-only (C)** key, i.e., a key which is capable only of signing other keys. This key may be created *without* an expiration date. This is for two reasons. First, the master secret key is never to leave the vault VM, so it is extremely unlikely ever to be obtained by an adversary (see below). Second, an adversary who *does* manage to obtain the master secret key either possesses the passphrase to unlock the key, or he does not. If he does, then he can simply use the passphrase in order to legally extend the expiration date of the key (or remove it entirely). If he does not, then he cannot use the key. In either case, an expiration date provides no additional benefit. It is, however, recommended that a **revocation certificate** be created so that the master keypair may be revoked in the (exceedingly unlikely) event that an adversary obtains both the master secret key *and* the passphrase. It is recommended that the master secret key passphrase only ever be input in the vault VM. (Subkeys should use a different passphrase; see below).

secret subkeys (ssb)  
It is recommended that two subkeys be created: one for **signing (S)**, and one for **encryption (E)**. It is further recommended that a *different* passphrase be used for these subkeys than for the master secret key. Finally, it is recommended that each of these subkeys be created with a reasonable expiration date (e.g., one year), and that a *new* set of subkeys be created whenever the existing set expires, rather than the expiration date of the existing keys being extended. This is because an adversary who obtains any existing encryption subkey (for example) will be able to use it in order to decrypt all emails (for example) which were encrypted with that subkey. If the same subkey were to continue to be used--and its expiration date continually extended--only that one key would need to be stolen (e.g., as a result of the work-gpg VM being compromised; see below) in order to decrypt *all* of the user's emails. If, on the other hand, each encryption subkey is used for at most approximately one year, then an adversary who obtains the secret subkey will be capable of decrypting at most approximately one year's worth of emails.

public key (pub)  
This is the complement of the master secret key. It should be uploaded to keyservers and may be signed by others.

vault  
This is a network-isolated VM. The initial master keypair and subkeys are generated in this VM. The master secret key *never* leaves this VM under *any* circumstances. No files or text is *ever* copied or transferred into this VM under *any* circumstances.

work-gpg  
This is a network-isolated VM. This VM is used *only* as the GPG backend for work-email. The secret subkeys (but *not* the master secret key) are copied from the vault VM to this VM. Files from less trusted VMs are *never* copied or transferred into this VM under *any* circumstances.

work-email  
This VM has access to the mail server. It accesses the work-gpg VM via the split GPG protocol. The public key may be stored in this VM so that it can be attached to emails and for other such purposes.

### Security Benefits

In the standard split GPG setup, there are at least two ways in which the work-gpg VM might be compromised:

First, an attacker who is capable of exploiting a hypothetical bug in work-email's [​MUA](https://en.wikipedia.org/wiki/Mail_user_agent) could send a malformed request which exploits a hypothetical bug in the GPG backend (running in the work-gpg VM), giving the attacker control of the work-gpg VM. Second, a malicious public key file which is imported to the work-gpg VM might exploit a hypothetical bug in the GPG backend which is running there, giving the attacker control of work-gpg. In either case, such an attacker might then be able to leak the master secret key back to work-email or to another VM (e.g., the netvm) via the split GPG protocol or other covert channels.

In the alternative setup described in this section (i.e., the subkey setup), even an attacker who manages to gain control of the work-gpg VM will not be able to obtain the user's master secret key without a general Xen VM escape exploit, since the master secret key is not present in the work-gpg VM. Rather, the master secret key remains in the vault VM (which, in the absence of a general Xen VM escape exploit, is assumed not to be compromised, since nothing is ever copied or transferred into it).

### Subkey Tutorials and Discussions

(Note: Although the tutorials below were not written with Qubes Split GPG in mind, they can be adapted with a few commonsense adjustments. As always, exercise caution and use your good judgment.)

-   [​"OpenPGP in Qubes OS" on the qubes-users mailing list](https://groups.google.com/d/topic/qubes-users/Kwfuern-R2U/discussion)
-   [​"Creating the Perfect GPG Keypair" by Alex Cabal](https://alexcabal.com/creating-the-perfect-gpg-keypair/)
-   [​"GPG Offline Master Key w/ smartcard" maintained by Abel Luck](https://gist.github.com/abeluck/3383449)
-   [​"Using GnuPG with QubesOS" by Alex](https://apapadop.wordpress.com/2013/08/21/using-gnupg-with-qubesos/)

