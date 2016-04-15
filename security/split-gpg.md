---
layout: doc
title: Split GPG
permalink: /doc/split-gpg/
redirect_from:
- /en/doc/split-gpg/
- /doc/SplitGpg/
- /doc/UserDoc/SplitGpg/
- /wiki/UserDoc/SplitGpg/
- /doc/open-pgp/
- /en/doc/open-pgp/
- /doc/OpenPGP/
- /doc/UserDoc/OpenPGP/
- /wiki/UserDoc/OpenPGP/
---

Qubes Split GPG
===============

What is Split GPG and why should I use it instead of the standard GPG?
----------------------------------------------------------------------
Split GPG implements a concept similar to having a smart card with your
private GPG keys, except that the role of the "smart card" plays another Qubes
AppVM. This way one, not-so-trusted domain, e.g. the one where Thunderbird is
running, can delegate all crypto operations, such as encryption/decryption
and signing to another, more trusted, network-isolated, domain. This way
the compromise of your domain where Thunderbird or another client app is
running -- arguably a not-so-unthinkable scenario -- does not allow the
attacker to automatically also steal all your keys. (We should make a rather
obvious comment here that the so-often-used passphrases on private keys are
pretty meaningless because the attacker can easily set up a simple backdoor
which would wait until the user enters the passphrase and steal the key then.)

The diagram below presents the big picture of Split GPG architecture.

![split-gpg-diagram.png](/attachment/wiki/SplitGpg/split-gpg-diagram.png)

### Advantages of Split GPG vs. traditional GPG with a smart card ###

It is often thought that the use of smart cards for private key storage
guarantees ultimate safety. While this might be true (unless the attacker
can find a usually-very-expensive-and-requiring-physical-presence way to
extract the key from the smart card) but only with regards to the safety of
the private key itself. However, there is usually nothing that could stop
the attacker from requesting the smart card to perform decryption of all the
user documents the attacker has found or need to decrypt. In other words,
while protecting the user's private key is an important task, we should not
forget that ultimately it is the user data that are to be protected and that
the smart card chip has no way of knowing the requests to decrypt documents
are now coming from the attacker's script and not from the user sitting in
front of the monitor. (Similarly the smart card doesn't make the process
of digitally signing a document or a transaction in any way more secure --
the user cannot know what the chip is really signing. Unfortunately this
problem of signing reliability is not solvable by Split GPG)

With Qubes Split GPG this problem is drastically minimized, because each time
the key is to be used the user is asked for consent (with a definable time
out, 5 minutes by default), plus is always notified each time the key is used
via a tray notification from the domain where GPG backend is running. This
way it would be easy to spot unexpected requests to decrypt documents.

![r2-split-gpg-1.png](/attachment/wiki/SplitGpg/r2-split-gpg-1.png)
![r2-split-gpg-3.png](/attachment/wiki/SplitGpg/r2-split-gpg-3.png)

### Current limitations ###

- Current implementation requires importing of public keys to the vault
domain. This opens up an avenue to attack the gpg running in the backend domain
via a hypothetical bug in public key importing code. See ticket [#474] for more
details and plans how to get around this problem, as well as the section on
[using split GPG with subkeys] below.

- It doesn't solve the problem of allowing the user to know what is to be
signed before the operation gets approved. Perhaps the GPG backend domain
could start a Disposable VM and have the to-be-signed document displayed
there? To Be Determined.


Configuring and using Split GPG
-------------------------------

In dom0, make sure the `qubes-gpg-split-dom0` package is installed.

    sudo qubes-dom0-update qubes-gpg-split-dom0
    
If using templates based on Debian, make sure you have the `qubes-gpg-split`
package installed.

    sudo apt-get install qubes-gpg-split
    
For Fedora.

    sudo yum install qubes-gpg-split

Start with creating a dedicated AppVM for storing your keys (the GPG backend
domain). It is recommended that this domain be network disconnected (set its
netvm to `none`) and only used for this one purpose. In later examples this
AppVM is named `work-gpg`, but of course it might have any other name.

### Setting up the GPG backend domain ###

Make sure the gpg is installed there and there are some private keys in the
keyring, e.g.:

    [user@work-gpg ~]$ gpg -K
    /home/user/.gnupg/secring.gpg
    -----------------------------
    sec   4096R/3F48CB21 2012-11-15
    uid                  Qubes OS Security Team <security@qubes-os.org>
    ssb   4096R/30498E2A 2012-11-15
    (...)

This is pretty much all that is required. However one might also want to modify
the default timeout which tells the backend for how long the user's approval
for key access should be valid (default 5 minutes). This is adjustable via
`QUBES_GPG_AUTOACCEPT` variable. One can override it e.g. in `~/.bash_profile`:

    [user@work-gpg ~]$ echo "export QUBES_GPG_AUTOACCEPT=86400" >> ~/.bash_profile

### Configuring the client apps to use Split GPG backend ###

Normally it should be enough to set the `QUBES_GPG_DOMAIN` to the GPG backend
domain name and use `qubes-gpg-client` in place of `gpg`, e.g.:

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

Note that running normal `gpg -K` in the demo above shows no private keys
stored in this AppVM.

A note on `gpg` and `gpg2`:

Throughout this guide, we refer to `gpg`, but note that Split-GPG uses `gpg2`
under the hood for compatibility with programs like Enigmail (which now supports
only `gpg2`). If you encounter trouble while trying to set up Split-GPG, make
sure you're using `gpg2` for your configuration and testing, since keyring data
may differ between the two installations.

### Configuring Thunderbird/Enigmail for use with Split GPG ###

However, when using Thunderbird with Enigmail extension it is
not enough, because Thunderbird doesn't preserve the environment
variables. Instead it is recommended to use a simple script provided by
`/usr/bin/qubes-gpg-client-wrapper` file by pointing Enigmail to use this
script instead of the standard GnuPG binary:

![tb-enigmail-split-gpg-settings-2.png](/attachment/wiki/SplitGpg/tb-enigmail-split-gpg-settings-2.png)

The script also sets the `QUBES_GPG_DOMAIN` variable automatically based on
the content of the file `/rw/config/gpg-split-domain`, which should be set to
the name of the GPG backend VM. This file survives the AppVM reboot, of course.

    [user@work ~]$ sudo bash
    [user@work ~]$ echo "work-gpg" > /rw/config/gpg-split-domain

A note on passphrases:

You may experience trouble when attempting to use a PGP key *with a passphrase*
along with Split-GPG and Enigmail. If you do, you may need to remove the
passphrase from your (sub)key(s) in order to get Split-GPG working correctly.
As mentioned above, we do not believe PGP key passphrases to be significant
from a security perspective.

### Importing public keys ###

Use `qubes-gpg-import-key` in the client AppVM to import the key into the
GPG backend VM. Of course a (safe, unspoofable) user consent dialog box is
displayed to accept this.

    [user@work ~]$ export QUBES_GPG_DOMAIN=work-gpg
    [user@work ~]$ qubes-gpg-import-key ~/Downloads/marmarek.asc

![r2-split-gpg-5.png](/attachment/wiki/SplitGpg/r2-split-gpg-5.png)

<br />

Advanced: Using Split GPG with Subkeys
--------------------------------------
Users with particularly high security requirements may wish to use Split
GPG with [​subkeys]. However, this setup
comes at a significant cost: It will be impossible to sign other people's keys
with the master secret key without breaking this security model. Nonetheless,
if signing others' keys is not required, then Split GPG with subkeys offers
unparalleled security for one's master secret key.

### Setup Description ###

In this example, the following keys are stored in the following locations
(see below for defintions of these terms):

| PGP Key(s) | VM Name      |
| ---------- | ------------ |
| `sec`      | `vault`      |
| `ssb`      | `work-gpg`   |
| `pub`      | `work-email` |

<br />

 * `sec` (master secret key)

   Depending on your needs, you may wish to create this as a **certify-only
   (C)** key, i.e., a key which is capable only of signing (a.k.a.,
   "certifying") other keys. This key may be created *without* an expiration
   date. This is for two reasons. First, the master secret key is never to
   leave the `vault` VM, so it is extremely unlikely ever to be obtained by
   an adversary (see below). Second, an adversary who *does* manage to obtain
   the master secret key either possesses the passphrase to unlock the key
   (if one is used), or he does not. If he does, then he can simply use
   the passphrase in order to legally extend the expiration date of the key
   (or remove it entirely). If he does not, then he cannot use the key at
   all. In either case, an expiration date provides no additional benefit.

   By the same token, however, having a passphrase on the key is of little
   value. An adversary who is capable of stealing the key from your `vault`
   would almost certainly also be capable of stealing the passphrase as
   you enter it. An adversary who obtains the passphrase can then use it
   in order to change or remove the passphrase from the key. Therefore,
   using a passphrase at all should be considered optional. It is, however,
   recommended that a **revocation certificate** be created and safely stored
   in multiple locations so that the master keypair can be revoked in the
   (exceedingly unlikely) event that it is ever compromised.

 * `ssb` (secret subkey)

   Depending on your needs, you may wish to create two different subkeys: one
   for **signing (S)** and one for **encryption (E)**. You may also wish to
   give these subkeys reasonable expiration dates (e.g., one year). Once these
   keys expire, it is up to you whether to *renew* these keys by extending the
   expiration dates or to create *new* subkeys when the existing set expires.

   On the one hand, an adversary who obtains any existing encryption subkey
   (for example) will be able to use it in order to decrypt all emails (for
   example) which were encrypted to that subkey. If the same subkey were to
   continue to be used--and its expiration date continually extended--only
   that one key would need to be stolen (e.g., as a result of the `work-gpg`
   VM being compromised; see below) in order to decrypt *all* of the user's
   emails. If, on the other hand, each encryption subkey is used for at most
   approximately one year, then an adversary who obtains the secret subkey will
   be capable of decrypting at most approximately one year's worth of emails.

   On the other hand, creating a new signing subkey each year without
   renewing (i.e., extending the expiration dates of) existing signing
   subkeys would mean that all of your old signatures would eventually
   read as "EXPIRED" whenever someone attempts to verify them. This can be
   problematic, since there is no consensus on how expired signatures should
   be handled. Generally, digital signatures are intended to last forever,
   so this is a strong reason against regularly retiring one's signing subkeys.

 * `pub` (public key)

   This is the complement of the master secret key. It can be uploaded to
   keyservers (or otherwise publicly distributed) and may be signed by others.

 * `vault`

   This is a network-isolated VM. The initial master keypair and
   subkeys are generated in this VM. The master secret key *never*
   leaves this VM under *any* circumstances. No files or text is *ever*
   [copied] or
   [pasted] into this VM under *any*
   circumstances.

 * `work-gpg`

   This is a network-isolated VM. This VM is used *only* as the
   GPG backend for `work-email`. The secret subkeys (but *not*
   the master secret key) are [copied] from the
   `vault` VM to this VM. Files from less trusted VMs are *never*
   [copied] into this
   VM under *any* circumstances.

 * `work-email`

   This VM has access to the mail server. It accesses the `work-gpg` VM via
   the Split GPG protocol. The public key may be stored in this VM so that
   it can be attached to emails and for other such purposes.

### Security Benefits ###

In the standard Split GPG setup, there are at least two ways in
which the `work-gpg` VM might be compromised. First, an attacker
who is capable of exploiting a hypothetical bug in `work-email`'s
[​MUA] could gain control of
the `work-email` VM and send a malformed request which exploits a hypothetical
bug in the GPG backend (running in the `work-gpg` VM), giving the attacker
control of the `work-gpg` VM. Second, a malicious public key file which is
imported into the `work-gpg` VM might exploit a hypothetical bug in the GPG
backend which is running there, again giving the attacker control of the
`work-gpg` VM. In either case, such an attacker might then be able to leak
both the master secret key and its passphrase (if any is used, it would
regularly be input in the work-gpg VM and therefore easily obtained by an
attacker who controls this VM) back to the `work-email` VM or to another VM
(e.g., the `netvm`, which is always untrusted by default) via the Split GPG
protocol or other [covert channels]. Once the master secret
key is in the `work-email` VM, the attacker could simply email it to himself
(or to the world).

In the alternative setup described in this section (i.e., the subkey
setup), even an attacker who manages to gain access to the `work-gpg` VM
will not be able to obtain the user's master secret key since it is simply
not there. Rather, the master secret key remains in the `vault` VM, which
is extremely unlikely to be compromised, since nothing is ever copied or
transferred into it.<sup>\*</sup> The attacker might nonetheless be able to
leak the secret subkeys from the `work-gpg` VM in the manner described above,
but even if this is successful, the secure master secret key can simply be
used to revoke the compromised subkeys and to issue new subkeys in their
place. (This is significantly less devastating than having to create a new
*master* keypair.)

<sup>\*</sup>In order to gain access to the `vault` VM, the attacker
would require the use of, e.g., a general Xen VM escape exploit
or a [signed, compromised package which is already installed in the
TemplateVM][trusting-templates]
upon which the `vault` VM is based.

### Subkey Tutorials and Discussions ###

(Note: Although the tutorials below were not written with Qubes Split GPG
in mind, they can be adapted with a few commonsense adjustments. As always,
exercise caution and use your good judgment.)

-   [​"OpenPGP in Qubes OS" on the qubes-users mailing list][openpgp-in-qubes-os]
-   [​"Creating the Perfect GPG Keypair" by Alex Cabal][cabal]
-   [​"GPG Offline Master Key w/ smartcard" maintained by Abel Luck][luck]
-   [​"Using GnuPG with QubesOS" by Alex][apapadop]


[#474]: https://github.com/QubesOS/qubes-issues/issues/474
[using split GPG with subkeys]: #advanced-using-split-gpg-with-subkeys
[​subkeys]: https://wiki.debian.org/Subkeys
[copied]: /doc/copying-files#on-inter-domain-file-copy-security
[pasted]: /doc/copy-paste#on-copypaste-security
[​MUA]: https://en.wikipedia.org/wiki/Mail_user_agent
[covert channels]: /doc/data-leaks
[trusting-templates]: /doc/SoftwareUpdateVM#notes-on-trusting-your-template-vms
[openpgp-in-qubes-os]: https://groups.google.com/d/topic/qubes-users/Kwfuern-R2U/discussion
[cabal]: https://alexcabal.com/creating-the-perfect-gpg-keypair/
[luck]: https://gist.github.com/abeluck/3383449
[apapadop]: https://apapadop.wordpress.com/2013/08/21/using-gnupg-with-qubesos/

