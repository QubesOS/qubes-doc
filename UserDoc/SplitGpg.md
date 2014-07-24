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

### Setting up the *vault* AppVM (Split GPG backend)

### Setting up the client AppVM to use split GPG backend from *vault* AppVM

### Importing public keys
