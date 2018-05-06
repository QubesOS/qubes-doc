---
layout: security
title: Verifying Signatures
permalink: /security/verifying-signatures/
redirect_from:
- /doc/verifying-signatures/
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
copies of the fingerprint from multiple independent sources and comparing
them to the downloaded key's fingerprint to ensure they match. Here are some
ideas:

 * Use the PGP Web of Trust.
 * Check the key against different keyservers.
 * Use different search engines to search for the fingerprint.
 * Use Tor to view and search for the fingerprint on various websites.
 * Use various VPNs and proxy servers.
 * Use different Wi-Fi networks (work, school, internet cafe, etc.).
 * Ask people to post the fingerprint in various forums and chat rooms.
 * Check against PDFs and photographs in which the fingerprint appears
   (e.g., slides from a talk or on a T-shirt).
 * Repeat all of the above from different computers and devices.

In addition, some operating systems have built-in keyrings containing keys
capable of validating the Qubes Master Signing Key. For example, if you have
a Debian system, then your debian-keyring may already contain the necessary
keys.

Once you're confident that you have the legitimate Qubes Master Signing Key,
set its trust level to "ultimate" (oh, well), so that it can be used to
automatically verify all the keys signed by the Qubes Master Signing Key:


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

You can now verify the ISO image (`Qubes-R3.2-x86_64.iso`) matches its
signature (`Qubes-R3.2-x86_64.iso.asc`):

    $ gpg -v --verify Qubes-R3.2-x86_64.iso.asc Qubes-R3.2-x86_64.iso
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


Verifying Digests
-----------------

Each ISO is also accompanied by a plain text file ending in `.DIGESTS`. This
file contains the output of running several different crytographic hash
functions on the ISO in order to obtain alphanumeric outputs known as "digests"
or "hash values." These hash values are provided as an alternative verification
method to PGP signatures (though the `.DIGESTS` file is itself also PGP-signed
--- see below). If you've already verified the signatures on the ISO directly,
then verifying digests is not necessary. You can always find all the `.DIGESTS`
files for every Qubes ISO in the [Qubes Security Pack].

As an example, `Qubes-R3.2-x86_64.iso` is accompanied by
`Qubes-R3.2-x86_64.iso.DIGESTS` which has the following content:

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA256
    
    3c951138b8b9867d8657f173c1b58b82 *Qubes-R3.2-x86_64.iso
    1fc9508160d7c4cba6cacc3025165b0f996c843f *Qubes-R3.2-x86_64.iso
    6b998045a513dcdd45c1c6e61ace4f1b4e7eff799f381dccb9eb0170c80f678a *Qubes-R3.2-x86_64.iso
    de1eb2e76bdb48559906f6fe344027ece20658d4a7f04ba00d4e40c63723171c62bdcc869375e7a4a4499d7bff484d7a621c3acfe9c2b221baee497d13cd02fe *Qubes-R3.2-x86_64.iso
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v2
    
    iQIcBAEBCAAGBQJX4XO/AAoJEMsRyh0D+lCCL9sP/jlZ26zhvlDEX/eaA/ANa/6b
    Dpsh/sqZEpz1SWoUxdm0gS+anc8nSDoCQSMBxnafuBbmwTChdHI/P7NvNirCULma
    9nw+EYCsCiNZ9+WCeroR8XDFSiDjvfkve0R8nwfma1XDqu1bN2ed4n/zNoGgQ8w0
    t5LEVDKCVJ+65pI7RzOSMbWaw+uWfGehbgumD7a6rfEOqOTONoZOjJJTnM0+NFJF
    Qz5yBg+0FQYc7FmfX+tY801AwSyevj3LKGqZN1GVcU9hhoHH7f2BcbdNk9I5WHHq
    doKMnZtcdyadQGwMNB68Wu9+0CWsXvk6E00QfW69M4d6w0gbyoJyUL1uzxgixb5O
    qodxrqeitXQSZZvU4kom5zlSjqZs4dGK+Ueplpkr8voT8TSWer0Nbh/VMfrNSt1z
    0/j+e/KMjor7XxehR+XhNWa2YLjA5l5H9rP+Ct/LAfVFp4uhsAnYf0rUskhCStxf
    Zmtqz4FOw/iSz0Os+IVcnRcyTYWh3e9XaW56b9J/ou0wlwmJ7oJuEikOHBDjrUph
    2a8AM+QzNmnc0tDBWTtT2frXcotqL+Evp/kQr5G5pJM/mTR5EQm7+LKSl7yCPoCj
    g8JqGYYptgkxjQdX3YAy9VDsCJ/6EkFc2lkQHbgZxjXqyrEMbgeSXtMltZ7cCqw1
    3N/6YZw1gSuvBlTquP27
    =e9oD
    -----END PGP SIGNATURE-----
    
Four digests have been computed for this ISO. The hash functions used, in order
from top to bottom, are MD5, SHA1, SHA256, and SHA512. One way to verify that
the ISO you downloaded matches any of these hash values is by using the
respective `*sum` programs:

    $ md5sum -c Qubes-R3.2-x86_64.iso.DIGESTS
    Qubes-R3.2-x86_64.iso: OK
    md5sum: WARNING: 23 lines are improperly formatted
    $ sha1sum -c Qubes-R3.2-x86_64.iso.DIGESTS
    Qubes-R3.2-x86_64.iso: OK
    sha1sum: WARNING: 23 lines are improperly formatted
    $ sha256sum -c Qubes-R3.2-x86_64.iso.DIGESTS
    Qubes-R3.2-x86_64.iso: OK
    sha256sum: WARNING: 23 lines are improperly formatted
    $ sha512sum -c Qubes-R3.2-x86_64.iso.DIGESTS
    Qubes-R3.2-x86_64.iso: OK
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

    $ openssl dgst -md5 Qubes-R3.2-x86_64.iso
    MD5(Qubes-R3.2-x86_64.iso)= 3c951138b8b9867d8657f173c1b58b82
    $ openssl dgst -sha1 Qubes-R3.2-x86_64.iso
    SHA1(Qubes-R3.2-x86_64.iso)= 1fc9508160d7c4cba6cacc3025165b0f996c843f
    $ openssl dgst -sha256 Qubes-R3.2-x86_64.iso
    SHA256(Qubes-R3.2-x86_64.iso)= 6b998045a513dcdd45c1c6e61ace4f1b4e7eff799f381dccb9eb0170c80f678a
    $ openssl dgst -sha512 Qubes-R3.2-x86_64.iso
    SHA512(Qubes-R3.2-x86_64.iso)= de1eb2e76bdb48559906f6fe344027ece20658d4a7f04ba00d4e40c63723171c62bdcc869375e7a4a4499d7bff484d7a621c3acfe9c2b221baee497d13cd02fe

(Notice that the outputs match the values from the `.DIGESTS` file.)

However, it is possible that an attacker replaced `Qubes-R3.2-x86_64.iso` with
a malicious ISO, computed the hash values for that ISO, and replaced the values
in `Qubes-R3.2-x86_64.iso.DIGESTS` with his own set of values. Therefore,
ideally, we should also verify the authenticity of the listed hash values.
Since `Qubes-R3.2-x86_64.iso.DIGESTS` is a clearsigned PGP file, we can use
`gpg` to verify it from the command line:

    $ gpg -v --verify Qubes-R3.2-x86_64.iso.DIGESTS 
    gpg: armor header: Hash: SHA256
    gpg: armor header: Version: GnuPG v2
    gpg: original file name=''
    gpg: Signature made Tue 20 Sep 2016 10:37:03 AM PDT using RSA key ID 03FA5082
    gpg: using PGP trust model
    gpg: Good signature from "Qubes OS Release 3 Signing Key"
    gpg: textmode signature, digest algorithm SHA256
    
The signature is good. Assuming our copy of the `Qubes OS Release 3 Signing
Key` is also authentic (see above), we can be confident that these hash values
came from the Qubes devs.

Verifying Qubes Code
--------------------

Developers who fetch code from our Git server should always verify the PGP signature of the tag on the latest commit.
In some cases, commits themselves may also be signed.
Any unsigned commit that is not followed by a signed tag should not be trusted!

To verify a signature on a git tag:

    $ git tag -v <tag name>

or

    $ git verify-tag <tag name>

To verify a signature on a git commit:

    $ git log --show-signature <commit ID>

or

    $ git verify-commit <commit ID>


[Qubes Master Signing Key]: https://keys.qubes-os.org/keys/qubes-master-signing-key.asc
[keyserver]: https://en.wikipedia.org/wiki/Key_server_%28cryptographic%29#Keyserver_examples
[Qubes Security Pack]: /security/pack/
[devel-master-key-msg]: https://groups.google.com/d/msg/qubes-devel/RqR9WPxICwg/kaQwknZPDHkJ
[user-master-key-msg]: https://groups.google.com/d/msg/qubes-users/CLnB5uFu_YQ/ZjObBpz0S9UJ
[mailing lists]: /support/
[Release 3 Signing Key]: https://keys.qubes-os.org/keys/qubes-release-3-signing-key.asc
[Qubes OS Keyserver]: https://keys.qubes-os.org/keys/

