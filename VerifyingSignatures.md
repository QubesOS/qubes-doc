---
layout: doc
title: VerifyingSignatures
permalink: /doc/VerifyingSignatures/
redirect_from: /wiki/VerifyingSignatures/
---

On Digital Signatures and Key Verification
==========================================

What Digital Signatures Can and Cannot Prove
--------------------------------------------

Most people – even programmers – are confused about the basic concepts underlying digital signatures. Therefore, most people should read this section, even if it looks trivial at first sight.

Digital signatures can prove both **authenticity** and **integrity** to a reasonable degree of certainty. **Authenticity** ensures that a given file was indeed created by the person who signed it (i.e., that it was not forged by a third party). **Integrity** ensures that the contents of the file have not been tampered with (i.e., that a third party has not undetectably altered its contents *en route*).

Digital signatures **cannot** prove any other property, e.g., that the signed file is not malicious. In fact, there is nothing that could stop someone from signing a malicious program (and it happens from time to time in reality).

The point is, of course, that people must choose who they will trust (e.g., Linus Torvalds, Microsoft, the Qubes Project, etc.) and assume that if a given file was signed by a trusted party, then it should not be malicious or buggy in some horrible way. But the decision of whether to trust any given party is beyond the scope of digital signatures. It's more of a sociological and political decision.

Once we make the decision to trust certain parties, digital signatures are useful, because they make it possible for us to limit our trust only to those few parties we choose and not to worry about all the "Bad Things That Can Happen In The Middle" between us and them, e.g., server compromises (qubes-os.org will surely be compromised one day), dishonest IT staff at the hosting company, dishonest staff at the ISPs, Wi-Fi attacks, etc.

By verifying all the files we download which purport to be authored by a party we've chosen to trust, we eliminate concerns about the bad things discussed above, since we can easily detect whether any files have been tampered with (and subsequently choose to refrain from executing, installing, or opening them).

However, for digital signatures to make any sense, we must ensure that the public keys we use for signature verification are indeed the original ones. Anybody can generate a GPG key pair that purports to belong to "The Qubes Project," but of course only the key pair that we (i.e., the Qubes developers) generated is the legitimate one. The next section explains how to verify the validity of the Qubes signing keys.

Importing Qubes Signing Keys
----------------------------

Every file published by the Qubes Project (ISO, RPM, TGZ files and git repositories) is digitally signed by one of the developer or release signing keys. Each such key is signed by the Qubes Master Signing Key ([\`0x36879494\`](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc)).

The public portion of the Qubes Master Signing Key can be imported directly from a [ keyserver](https://en.wikipedia.org/wiki/Key_server_%28cryptographic%29#Keyserver_examples) (specified on first use with --keyserver URI, keyserver saved in \~/.gnupg/gpg.conf), e.g.,

{% highlight trac-wiki %}
gpg --keyserver pool.sks-keyservers.net --recv-keys 0x427F11FD0FAA4B080123F01CDDFA1A3E36879494
{% endhighlight %}

or downloaded [here](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc) and imported with gpg,

{% highlight trac-wiki %}
$ gpg --import ./qubes-master-signing-key.asc 
{% endhighlight %}

or fetched directly with gpg.

{% highlight trac-wiki %}
$ gpg --fetch-keys https://keys.qubes-os.org/keys/qubes-master-signing-key.asc
{% endhighlight %}

For additional security we also publish the fingerprint of the Qubes Master Signing Key ([\`0x36879494\`](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc)) here in this document:

{% highlight trac-wiki %}
pub   4096R/36879494 2010-04-01
      Key fingerprint = 427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494
uid   Qubes Master Signing Key
{% endhighlight %}

There should also be a copy of this key at the project's main website, in the [Qubes Security Pack](/wiki/SecurityPack), and in the archives of the project's [developer](https://groups.google.com/forum/#!msg/qubes-devel/RqR9WPxICwg/kaQwknZPDHkJ) and [user](https://groups.google.com/d/msg/qubes-users/CLnB5uFu_YQ/ZjObBpz0S9UJ) mailing lists.

Once you have obtained the Qubes Master Signing Key ([\`0x36879494\`](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc)), you should verify the fingerprint of this key very carefully by obtaining copies of the fingerprint from trustworthy independent sources and comparing them to the downloaded key's fingerprint to ensure they match. Then set its trust level to "ultimate" (oh, well), so that it can be used to automatically verify all the keys signed by the Qubes Master Signing Key:

{% highlight trac-wiki %}
$ gpg --edit-key 0x36879494
gpg (GnuPG) 1.4.18; Copyright (C) 2014 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.


pub  4096R/36879494  created: 2010-04-01  expires: never       usage: SC  
                     trust: unknown       validity: unknown
[ unknown] (1). Qubes Master Signing Key

gpg> fpr
pub   4096R/36879494 2010-04-01 Qubes Master Signing Key
 Primary key fingerprint: 427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494

gpg> trust
pub  4096R/36879494  created: 2010-04-01  expires: never       usage: SC  
                     trust: unknown       validity: unknown
[ unknown] (1). Qubes Master Signing Key

Please decide how far you trust this user to correctly verify other users' keys
(by looking at passports, checking fingerprints from different sources, etc.)

  1 = I don't know or won't say
  2 = I do NOT trust
  3 = I trust marginally
  4 = I trust fully
  5 = I trust ultimately
  m = back to the main menu

Your decision? 5
Do you really want to set this key to ultimate trust? (y/N) y

pub  4096R/36879494  created: 2010-04-01  expires: never       usage: SC  
                     trust: ultimate      validity: unknown
[ unknown] (1). Qubes Master Signing Key
Please note that the shown key validity is not necessarily correct
unless you restart the program.

gpg> q
{% endhighlight %}

Now you can easily download any of the developer or release signing keys that happen to be used to sign particular ISO, RPM, TGZ files or git tags.

For example: Qubes OS Release 2 Signing Key ([\`0x0A40E458\`](https://keys.qubes-os.org/keys/qubes-release-2-signing-key.asc)) is used for all Release 2 ISO images.

{% highlight trac-wiki %}
$ gpg --recv-keys 0x3F01DEF49719158EF86266F80C73B9D40A40E458
gpg: requesting key 0A40E458 from hkp server keys.gnupg.net
gpg: key 0A40E458: public key "Qubes OS Release 2 Signing Key" imported
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   1  signed:   1  trust: 0-, 0q, 0n, 0m, 0f, 1u
gpg: depth: 1  valid:   1  signed:   0  trust: 1-, 0q, 0n, 0m, 0f, 0u
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)
{% endhighlight %}

You can also download all the currently used developers' signing keys and current and older release signing keys (and also a copy of the Qubes Master Signing Key) from the [keys directory on our server](https://keys.qubes-os.org/keys/) and from the [Qubes Security Pack](/wiki/SecurityPack).

The developer signing keys are set to be valid for 1 year only, while the Qubes Master Signing Key ([\`0x36879494\`](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc)) has no expiration date. This latter key was generated and is kept only within a dedicated, air-gapped "vault" machine, and the private portion will (hopefully) never leave this isolated machine.

You can now verify the ISO image (Qubes-R2-x86\_64-DVD.iso) matches its signature (Qubes-R2-x86\_64-DVD.iso.asc):

{% highlight trac-wiki %}
$ gpg -v --verify Qubes-R2-x86_64-DVD.iso.asc
gpg: armor header: Version: GnuPG v1
gpg: assuming signed data in `Qubes-R2-x86_64-DVD.iso'
gpg: Signature made Tue Sep 23 08:38:40 2014 UTC using RSA key ID 0A40E458
gpg: using PGP trust model
gpg: Good signature from "Qubes OS Release 2 Signing Key"
gpg: binary signature, digest algorithm SHA1
{% endhighlight %}

The Release 2 Signing Key ([\`0x0A40E458\`](https://keys.qubes-os.org/keys/qubes-release-2-signing-key.asc)) used to sign this ISO image should be signed by the Qubes Master Signing Key ([\`0x36879494\`](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc)):

{% highlight trac-wiki %}
$ gpg --list-sig 0A40E458
pub   4096R/0A40E458 2012-11-15
uid                  Qubes OS Release 2 Signing Key
sig          36879494 2012-11-15  Qubes Master Signing Key
sig 3        0A40E458 2012-11-15  Qubes OS Release 2 Signing Key
{% endhighlight %}

Having problems verifying the ISO images? Make sure you have the corresponding release signing key and see this thread:

[https://groups.google.com/group/qubes-devel/browse\_thread/thread/4bdec1cd19509b38/9f8e219c41e1b232](https://groups.google.com/group/qubes-devel/browse_thread/thread/4bdec1cd19509b38/9f8e219c41e1b232)

Verifying Qubes Code
--------------------

Developers who fetch code from our Git server should always verify tags on the latest commit. Any commits that are not followed by a signed tag should not be trusted!

To verify a signature on a git tag, you can use:

{% highlight trac-wiki %}
$ git tag -v <tag name>
{% endhighlight %}
