---
layout: doc
title: OpenPGP
permalink: /en/doc/open-p-g-p/
redirect_from:
- /doc/OpenPGP/
- "/doc/UserDoc/OpenPGP/"
- "/wiki/UserDoc/OpenPGP/"
---

**Note 2014-08-03: This page is deprecated by [SplitGpg](/wiki/UserDoc/SplitGpg). The content of this page has been integrated into that page.**

Using OpenPGP in Qubes
======================

One of the main advantages of Qubes is that it allows the user to isolate sensitive data in network-disconnected VMs. This is particularly useful in the case of securing secret keys. Work on split GPG is currently ongoing (\#474), but it's still possible to set up a very secure system right now.

Basic Instructions
------------------

The basic procedure is to create a master keypair and any number of signing/encryption subkeys in your ultimately trusted "vault" domain. The secret portion of the master keypair should never leave your vault. The public portion of the master key, along with the subkeys, can then be [copied](/wiki/VmTools/QvmCopyToVm) to any number of less trusted domains, e.g. "work," where they will be used normally. If your work domain is ever compromised (and your subkeys along with it), your master key will still be safe, and you can issue new subkeys. For detailed instructions, see the [tutorials and discussions](/wiki/UserDoc/OpenPGP#TutorialsandDiscussions) below.

Security Recommendations
------------------------

(Note: Here "vault" refers to whichever domain you have chosen to house the secret portion of your master keypair.)

1.  Key Isolation

> > All keys should be created in the vault, and the secret portion of the master keypair should never leave it.

1.  No Vault Networking

> > The vault should not be connected to a network (NetVM: none).

1.  No Vault Importing

> > Untrusted files should never be imported into the vault. In addition to the networking restriction in point 2, this means not [copying](/wiki/VmTools/QvmCopyToVm) untrusted files to the vault. Whether any given file is "untrusted" is an individual user decision, but we recommend that users never copy from a less trusted domain to a more trusted domain. At present, this means that there is no secure way to sign other people's keys with the master key.

Tutorials and Discussions
-------------------------

(Note: Although some of the tutorials below were not written with Qubes in mind, they can be adapted to Qubes with a few adjustments. As always, exercise caution and use your good judgment.)

-   [​"OpenPGP in Qubes OS" on the qubes-users mailing list](https://groups.google.com/d/topic/qubes-users/Kwfuern-R2U/discussion)
-   [​"Creating the Perfect GPG Keypair" by Alex Cabal](https://alexcabal.com/creating-the-perfect-gpg-keypair/)
-   [​"GPG Offline Master Key w/ smartcard" maintained by Abel Luck](https://gist.github.com/abeluck/3383449)
    -   Author's note: "It is not Qubes OS specific, and in fact assumes you want to use a smartcard, which might not be the case, so skip those bits. Also, use your vault vm instead of booting into an offline livecd as described."
-   [​"Using GnuPG with QubesOS" by Alex](https://apapadop.wordpress.com/2013/08/21/using-gnupg-with-qubesos/)

