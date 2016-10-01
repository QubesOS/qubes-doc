---
layout: doc
title: Verifying Signatures
permalink: /doc/verifying-signatures/
redirect_from:
- /en/doc/verifying-signatures/
- /doc/VerifyingSignatures/
- /wiki/VerifyingSignatures/
---

On Digital Signatures and Key Verification
==========================================

What Digital Signatures Can and Cannot Prove
--------------------------------------------

Most people – even programmers – are confused about the basic concepts
underlying digital signatures. Therefore, most people should read this section,
even if it looks trivial at first sight.

Digital signatures can prove both **authenticity** and **integrity** to a
reasonable degree of certainty. **Authenticity** ensures that a given file was
indeed created by the person who signed it (i.e., that it was not forged by a
third party). **Integrity** ensures that the contents of the file have not been
tampered with (i.e., that a third party has not undetectably altered its
contents *en route*).

Digital signatures **cannot** prove any other property, e.g., that the signed
file is not malicious. In fact, there is nothing that could stop someone from
signing a malicious program (and it happens from time to time in reality).

The point is, of course, that people must choose who they will trust (e.g.,
Linus Torvalds, Microsoft, the Qubes Project, etc.) and assume that if a given
file was signed by a trusted party, then it should not be malicious or buggy in
some horrible way. But the decision of whether to trust any given party is
beyond the scope of digital signatures. It's more of a sociological and
political decision.

Once we make the decision to trust certain parties, digital signatures are
useful, because they make it possible for us to limit our trust only to those
few parties we choose and not to worry about all the "Bad Things That Can
Happen In The Middle" between us and them, e.g., server compromises
(qubes-os.org will surely be compromised one day), dishonest IT staff at the
hosting company, dishonest staff at the ISPs, Wi-Fi attacks, etc.

By verifying all the files we download which purport to be authored by a party
we've chosen to trust, we eliminate concerns about the bad things discussed
above, since we can easily detect whether any files have been tampered with
(and subsequently choose to refrain from executing, installing, or opening
them).

However, for digital signatures to make any sense, we must ensure that the
public keys we use for signature verification are indeed the original ones.
Anybody can generate a GPG key pair that purports to belong to "The Qubes
Project," but of course only the key pair that we (i.e., the Qubes developers)
generated is the legitimate one. The next section explains how to verify the
validity of the Qubes signing keys.

Importing Qubes Signing Keys
----------------------------

Every file published by the Qubes Project (ISO, RPM, TGZ files and git
repositories) is digitally signed by one of the developer or release signing
keys. Each such key is signed by the [Qubes Master Signing Key]
(`0xDDFA1A3E36879494`).

The public portion of the Qubes Master Signing Key can be imported directly
from a [keyserver] (specified on first use with `--keyserver <URI>`, keyserver
saved in `~/.gnupg/gpg.conf`), e.g.,

    gpg --keyserver pool.sks-keyservers.net --recv-keys 0x427F11FD0FAA4B080123F01CDDFA1A3E36879494

or downloaded [here][Qubes Master Signing Key] and imported with gpg,

    $ gpg --import ./qubes-master-signing-key.asc 

or fetched directly with gpg.

    $ gpg --fetch-keys https://keys.qubes-os.org/keys/qubes-master-signing-key.asc

For additional security we also publish the fingerprint of the Qubes Master
Signing Key here in this document:

    pub   4096R/36879494 2010-04-01
          Key fingerprint = 427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494
    uid   Qubes Master Signing Key

There should also be a copy of this key at the project's main website, in the
[Qubes Security Pack], and in the archives of the project's
[developer][devel-master-key-msg] and [user][user-master-key-msg] [mailing lists].

Once you have obtained the Qubes Master Signing Key,
you should verify the fingerprint of this key very carefully by obtaining
copies of the fingerprint from trustworthy independent sources and comparing
them to the downloaded key's fingerprint to ensure they match. Then set its
trust level to "ultimate" (oh, well), so that it can be used to automatically
verify all the keys signed by the Qubes Master Signing Key:


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

Now you can easily download any of the developer or release signing keys that
happen to be used to sign particular ISO, RPM, TGZ files or git tags.

For example, the Qubes OS [Release 3 Signing Key] (`0xCB11CA1D03FA5082`) is
used for all Release 3 ISO images:

    $ gpg --recv-keys 0xC52261BE0A823221D94CA1D1CB11CA1D03FA5082
    gpg: requesting key 03FA5082 from hkp server keys.gnupg.net
    gpg: key 03FA5082: public key "Qubes OS Release 3 Signing Key" imported
    gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
    gpg: depth: 0  valid:   1  signed:   1  trust: 0-, 0q, 0n, 0m, 0f, 1u
    gpg: depth: 1  valid:   1  signed:   0  trust: 1-, 0q, 0n, 0m, 0f, 0u
    gpg: Total number processed: 1
    gpg:               imported: 1  (RSA: 1)

You can also download all the currently used developers' signing keys and
current and older release signing keys (and also a copy of the Qubes Master
Signing Key) from the [Qubes OS Keyserver] and from the [Qubes Security Pack].

The developer signing keys are set to be valid for 1 year only, while the Qubes
Master Signing Key has no expiration date. This latter key was generated and is
kept only within a dedicated, air-gapped "vault" machine, and the private
portion will (hopefully) never leave this isolated machine.

You can now verify the ISO image (`Qubes-R3.1-x86_64.iso`) matches its
signature (`Qubes-R3.1-x86_64.iso.asc`):

    $ gpg -v --verify Qubes-R3.1-x86_64.iso.asc Qubes-R3.1-x86_64.iso
    gpg: armor header: Version: GnuPG v1
    gpg: Signature made Tue 08 Mar 2016 07:40:56 PM PST using RSA key ID 03FA5082
    gpg: using PGP trust model
    gpg: Good signature from "Qubes OS Release 3 Signing Key"
    gpg: binary signature, digest algorithm SHA256

The Release 3 Signing Key used to sign this ISO image should be signed by the
Qubes Master Signing Key:

    $ gpg --list-sig 03FA5082
    pub   4096R/03FA5082 2014-11-19
    uid                  Qubes OS Release 3 Signing Key
    sig 3        03FA5082 2014-11-19  Qubes OS Release 3 Signing Key
    sig          36879494 2014-11-19  Qubes Master Signing Key

Having problems verifying the ISO images? Make sure you have the corresponding
release signing key and see this thread:

[https://groups.google.com/group/qubes-devel/browse\_thread/thread/4bdec1cd19509b38/9f8e219c41e1b232](https://groups.google.com/group/qubes-devel/browse_thread/thread/4bdec1cd19509b38/9f8e219c41e1b232)

Verifying Digests
-----------------

Each ISO is also accompanied by a plain text file ending in `.DIGESTS`. This
file contains the output of running several different crytographic hash
functions on the ISO in order to obtain alphanumeric outputs known as "digests."
These digests are provided as an alternative verification method to PGP
signatures (though the digests themselves are also PGP-signed -- see below). If
you've already verified the signatures on the ISO directly, then verifying
digests is not necessary.

For example, `Qubes-R3.1-x86_64.iso` is accompanied by
`Qubes-R3.1-x86_64.iso.DIGESTS` which has the following content:

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA256

    f99634b05d15f6bb2ac02ee03e4338a0 *Qubes-R3.1-x86_64.iso
    990b7765ee209b42b3cad78673463daae769c729 *Qubes-R3.1-x86_64.iso
    2d82a684d507ad5789ed83272af4311fd04375e782364d5dd9df4b3d7118cc28 *Qubes-R3.1-x86_64.iso
    083d6cfc3fb5dc97fd91d8f9f70301c154e3674114ff1727b0415c2c663b233c22e0830d0bfc1f7a532549d7e39c6ef5cfde6a90a650343b47ba57d3e8e92ca7 *Qubes-R3.1-x86_64.iso
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1

    iQIcBAEBCAAGBQJW4AqUAAoJEMsRyh0D+lCCo+cP/A/96SmGSPmnMxIor0ODsZNh
    HtGCfFPhB2KnpLMOVUMRidoMWTzL1+J7HpWYdOS7hPhlcbDfX4A0C4QCs4b0Wkc7
    npha/GabQuek0HSi2uKt2YQtADq9yPjpqhc3Q2crbnL9UPmKv/XdECfpnK9zSRAE
    RKl7Uj5RAPuLQ7ee4uQ8lIXWUm6IljpHnm4cG+WP2QYLCkS8BWq18Bl9s0fKdj47
    JzIkhpyc6Vr9a7UBBxghF+Cb9WrPy22sTtE7eQYHRibh38xdMPOw0tb9F6AMAVeC
    hK6+xJVz+7xERtRWTQPk4LOPeHIU21xJyVipkwb+T0SrQgsNwSXsSGPe0PiNU9Xk
    khMbKGcbA+rnQiCS/9EKORNyULRAHvD6WXUqNyIS9trhcx49fxU8taPXKze947p1
    XvWbqBWHIcCvKVQ3t/okmNN7OXfUCIDJ9bx+qyoLsIU2BF/aZZv+5ijK26D3H+xQ
    G+2DMIynDMOlHSioCM3I1M0Ml5sB21G0VMJF9r9r8RrDop5cVGdgksie0JvpZ/ep
    N/L7ozf1gvrO2euVslelMOUJcBjeisT214g6/DNjQ9Ox5SkDWIXrS2ZtR/zToApg
    x3T0IusOQQhdpC8I0nnXPL/tgyRV8UFNBhxIec7IKnGwvQlVYMFYVomPh7vJhfdl
    GMMP3JlFAaxghZWU14+F
    =FiJ5
    -----END PGP SIGNATURE-----

Four digests have been computed for this ISO. The hash functions used, in order
from top to bottom, are MD5, SHA1, SHA256, and SHA512. One way to verify that
the ISO you downloaded matches any of these hash values is by using the
respective `*sum` programs:

    $ md5sum -c Qubes-R3.1-x86_64.iso.DIGESTS
    Qubes-R3.1-x86_64.iso: OK
    md5sum: WARNING: 23 lines are improperly formatted
    $ sha1sum -c Qubes-R3.1-x86_64.iso.DIGESTS
    Qubes-R3.1-x86_64.iso: OK
    sha1sum: WARNING: 23 lines are improperly formatted
    $ sha256sum -c Qubes-R3.1-x86_64.iso.DIGESTS
    Qubes-R3.1-x86_64.iso: OK
    sha256sum: WARNING: 23 lines are improperly formatted
    $ sha512sum -c Qubes-R3.1-x86_64.iso.DIGESTS
    Qubes-R3.1-x86_64.iso: OK
    sha512sum: WARNING: 23 lines are improperly formatted

The `OK` response tells us that the hash value for that particular hash
function matches. The program also warns us that there are 23 improperly
formatted lines, but this is to be expected. This is because each file contains
lines for several different hash values (as mentioned above), but each `*sum`
program verifies only the line for its own hash function. In addition, there
are lines for the PGP signature which the `*sum` programs do not know how to
read.

Another way is to use `openssl` to compute each hash value, then compare them
to the contents of the `.DIGESTS` file.:

    $ openssl dgst -md5 Qubes-R3.1-x86_64.iso
    MD5(Qubes-R3.1-x86_64.iso)= f99634b05d15f6bb2ac02ee03e4338a0
    $ openssl dgst -sha1 Qubes-R3.1-x86_64.iso
    SHA1(Qubes-R3.1-x86_64.iso)= 990b7765ee209b42b3cad78673463daae769c729
    $ openssl dgst -sha256 Qubes-R3.1-x86_64.iso
    SHA256(Qubes-R3.1-x86_64.iso)= 2d82a684d507ad5789ed83272af4311fd04375e782364d5dd9df4b3d7118cc28
    $ openssl dgst -sha512 Qubes-R3.1-x86_64.iso
    SHA512(Qubes-R3.1-x86_64.iso)=
    083d6cfc3fb5dc97fd91d8f9f70301c154e3674114ff1727b0415c2c663b233c22e0830d0bfc1f7a532549d7e39c6ef5cfde6a90a650343b47ba57d3e8e92ca7

(Notice that the outputs match the values from the `.DIGESTS` file.)

However, it is possible that an attacker replaced `Qubes-R3.1-x86_64.iso` with
a malicious ISO, computed the hash values for that ISO, and replaced the values
in `Qubes-R3.1-x86_64.iso.DIGESTS` with his own set of values. Therefore,
ideally, we should also verify the authenticity of the listed hash values.
Since `Qubes-R3.1-x86_64.iso.DIGESTS` is a clearsigned PGP file, we can use
`gpg` to verify it from the command line:

    $ gpg -v --verify Qubes-R3.1-x86_64.iso.DIGESTS
    gpg: armor header: Hash: SHA256
    gpg: armor header: Version: GnuPG v1
    gpg: original file name=''
    gpg: Signature made Wed 09 Mar 2016 03:35:48 AM PST using RSA key ID 03FA5082
    gpg: using PGP trust model
    gpg: Good signature from "Qubes OS Release 3 Signing Key"
    gpg: textmode signature, digest algorithm SHA256

The signature is good. Assuming our copy of the `Qubes OS Release 3 Signing
Key` is also authentic (see above), we can be confident that these hash values
came from the Qubes devs.

Verifying Qubes Code
--------------------

Developers who fetch code from our Git server should always verify tags on the
latest commit. Any commits that are not followed by a signed tag should not be
trusted!

To verify a signature on a git tag, you can use:

    $ git tag -v <tag name>


[Qubes Master Signing Key]: https://keys.qubes-os.org/keys/qubes-master-signing-key.asc
[keyserver]: https://en.wikipedia.org/wiki/Key_server_%28cryptographic%29#Keyserver_examples
[Qubes Security Pack]: /doc/security-pack/
[devel-master-key-msg]: https://groups.google.com/d/msg/qubes-devel/RqR9WPxICwg/kaQwknZPDHkJ
[user-master-key-msg]: https://groups.google.com/d/msg/qubes-users/CLnB5uFu_YQ/ZjObBpz0S9UJ
[mailing lists]: /mailing-lists/
[Release 3 Signing Key]: https://keys.qubes-os.org/keys/qubes-release-3-signing-key.asc
[Qubes OS Keyserver]: https://keys.qubes-os.org/keys/

