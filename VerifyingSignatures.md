---
layout: wiki
title: VerifyingSignatures
permalink: /wiki/VerifyingSignatures/
---

On Digital Signatures and Key Verification
==========================================

What do the Digital Signatures Prove and What They DO NOT Prove
---------------------------------------------------------------

Most people, even programmers, often confuse the basic ideas behind digital signatures. Most people should read this section, even if it looks trivial at first sight.

Digital Signatures can prove that a given file is authentic, i.e. that is has been indeed created by a person that signed it, and that its contents has not been tampered (so, integrity is preserved).

Digital Signatures do \*not\* prove any other property, e.g. that the file is not malicious. In fact there is nothing that could stop people from signing a malicious program (and it happens from time to time in realty).

The point is, of course, that people need to choose to trust some people, e.g. Linus Torvalds, Microsoft, etc. and assume that if a file(s) was indeed signed by those individuals, then indeed it should not be malicious and buggy in some horrible way. But the decision of whether to trust certain people (e.g. those behind the Qubes Project) is beyond the scope of digital signatures. It's more of a sociological and political decision.

However, once we make a decision to trust somebody (e.g. The Qubes Project and the files released by them), then the digital signatures are useful, because they make it possible to limit our trust only to those few people we chose, and not to worry about all the Bad Things That Can Happen In The Middle between us and the them (i.e. the vendor), like e.g.: server compromises (qubes-os.org will surely get compromised one day), dishonest IT stuff at the hosting company, dishonest stuff at the ISPs, WiFi attacks, etc.

If we verify all the files we download from the vendor, we don't need to worry about all the above bad things, because we would easily be able to detect when the file(s) has been tampered (and not execute/install/open them).

However, for the digital signatures to make any sense, one should ensure that the public keys we use for signature verification are indeed the original ones. Anybody can generate a GPG key pair that would pretend to be for "Qubes Project", but only the key pair that we generated is the legitimate one. The next paragraph describes how to verify the validity of the Qubes signing keys.

Importing Qubes Signing Keys
----------------------------

Every file published by the Qubes Project (rpm, tgz, git repositories) is digitally signed by one of the developer or release keys. Each such key is signed by the Qubes Master Signing Key (`0x36879494`).

The public portion of the Master Key can be download from a keyserver, e.g.:

``` {.wiki}
gpg --recv 0x36879494
```

(You can use other key server than `pgp.mit.edu`, which is just an example)

For additional security we also publish the The Master Key's fingerprint here in this document:

``` {.wiki}
pub   4096R/36879494 2010-04-01
      Key fingerprint = 427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494
uid   Qubes Master Signing Key
```

There should also be a copy of this key at the project's main website, as well as in the archives of the projects mailing list.

Once you download and verified the fingerprint of the Master Signing Key, you should import this key and set its trust level to 'ultimate' (oh, well), so that it could be used to automatically verify all the developer's keys:

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

You can also download all the currently used developer's keys (and also a copy of the Master Key) in the keys directory on our server:

[​http://keys.qubes-os.org/keys/](http://keys.qubes-os.org/keys/)

The developer keys are set to be valid for 1 year only, while the Qubes Master Singing Key has no expiration date. This key has been generated and is kept only within a special 'vault' machine that has no networking, and the private portion (hopefully) is never to leave this isolated machine.

Verifying Qubes code
--------------------

Developers who fetch code from our Git server should always verify tags on the latest commit. Any commits that are not followed by a signed tag should not be trusted!

To verify a signature on a git tag, you can use:

``` {.wiki}
$ git tag -v <tag name>
```
