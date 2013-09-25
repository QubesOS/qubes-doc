---
layout: wiki
title: VerifyingSignatures
permalink: /wiki/VerifyingSignatures/
---

On Digital Signatures and Key Verification
==========================================

What Digital Signatures Can and Cannot Prove
--------------------------------------------

Most people--even programmers--”are confused about the basic concepts underlying digital signatures. Therefore, most people should read this section, even if it looks trivial at first sight.

Digital signatures can prove both **authenticity** and **integrity** to a reasonable degree of certainty. **Authenticity** ensures that a given file was indeed created by the person who signed it (i.e., that it was not forged by a third party). **Integrity** ensures that the contents of the file have not been tampered with (i.e., that a third party has not undetectably altered its contents *en route*).

Digital signatures **cannot** prove any other property, e.g., that the signed file is not malicious. In fact, there is nothing that could stop someone from signing a malicious program (and it happens from time to time in reality).

The point is, of course, that people must choose who they will trust (e.g., Linus Torvalds, Microsoft, the Qubes Project, etc.) and assume that if a given file was signed by a trusted party, then it should not be malicious or buggy in some horrible way. But the decision of whether to trust any given party is beyond the scope of digital signatures. It's more of a sociological and political decision.

Once we make the decision to trust certain parties, digital signatures are useful, because they make it possible for us to limit our trust only to those few parties we choose and not to worry about all the "Bad Things That Can Happen In The Middle" between us and the them, e.g., server compromises (qubes-os.org will surely be compromised one day), dishonest IT stuff at the hosting company, dishonest stuff at the ISPs, Wi-Fi attacks, etc.

By verifying all the files we download which purport to be authored by a party we've chosen to trust, we eliminate concerns about the bad things discussed above, since we can easily detect whether any files have been tampered with (and subsequently choose to refrain from executing, installing, or opening them).

However, for digital signatures to make any sense, we must ensure that the public keys we use for signature verification are indeed the original ones. Anybody can generate a GPG key pair that purports to belong to "The Qubes Project," but of course only the key pair that we (i.e., the Qubes developers) generated is the legitimate one. The next section explains how to verify the validity of the Qubes signing keys.

Importing Qubes Signing Keys
----------------------------

Every file published by the Qubes Project (rpm, tgz, git repositories) is digitally signed by one of the developer or release keys. Each such key is signed by the Qubes Master Signing Key (`0x36879494`).

The public portion of the Master Key can be downloaded from a keyserver, e.g.:

``` {.wiki}
gpg --recv-keys 0x36879494
```

(You can use other key server than `pgp.mit.edu`, which is just an example)

For additional security we also publish the the Master Key's fingerprint here in this document:

``` {.wiki}
pub   4096R/36879494 2010-04-01
      Key fingerprint = 427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494
uid   Qubes Master Signing Key
```

There should also be a copy of this key at the project's main website, as well as in the [​archives of the project's mailing list](https://groups.google.com/forum/#!msg/qubes-devel/RqR9WPxICwg/kaQwknZPDHkJ).

Once you have downloaded and verified the fingerprint of the Master Signing Key, you should import this key and set its trust level to "ultimate" (oh, well), so that it can be used to automatically verify all the developers' keys:

``` {.wiki}
gpg --edit-key 0x36879494
and then: trust, 5, y, q
```

Now you can easily download any of the developer or release keys that happen to be used to sign particular rpm, tgz, or git tags. E.g.:

``` {.wiki}
$ gpg --recv-keys AC1BF9B3
gpg: requesting key AC1BF9B3 from hkp server keys.gnupg.net
gpg: key AC1BF9B3: public key "Qubes OS Release 1 Signing Key" imported
gpg: no ultimately trusted keys found
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)
```

You can also download all the currently used developers' keys (and also a copy of the Master Key) in the keys directory on our server:

[​http://keys.qubes-os.org/keys/](http://keys.qubes-os.org/keys/)

The developer keys are set to be valid for 1 year only, while the Qubes Master Signing Key has no expiration date. This latter key was generated and is kept only within a dedicated, air-gapped "vault" machine, and the private portion will (hopefully) never leave this isolated machine.

Having problems verifying the ISO? See this thread:

[​https://groups.google.com/group/qubes-devel/browse\_thread/thread/4bdec1cd19509b38/9f8e219c41e1b232](https://groups.google.com/group/qubes-devel/browse_thread/thread/4bdec1cd19509b38/9f8e219c41e1b232)

Verifying Qubes Code
--------------------

Developers who fetch code from our Git server should always verify tags on the latest commit. Any commits that are not followed by a signed tag should not be trusted!

To verify a signature on a git tag, you can use:

``` {.wiki}
$ git tag -v <tag name>
```
