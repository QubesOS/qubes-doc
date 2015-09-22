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

Every file published by the Qubes Project (ISO, RPM, TGZ files and git repositories) is digitally signed by one of the developer or release signing keys. Each such key is signed by the Qubes Master Signing Key ([`0x36879494`](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc)).

The public portion of the Qubes Master Signing Key can be imported directly from a [ keyserver](https://en.wikipedia.org/wiki/Key_server_%28cryptographic%29#Keyserver_examples) (specified on first use with --keyserver URI, keyserver saved in `~/.gnupg/gpg.conf`), e.g.,

    gpg --keyserver pool.sks-keyservers.net --recv-keys 0x427F11FD0FAA4B080123F01CDDFA1A3E36879494

or downloaded [here](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc) and imported with gpg,

    $ gpg --import ./qubes-master-signing-key.asc 

or fetched directly with gpg.

    $ gpg --fetch-keys https://keys.qubes-os.org/keys/qubes-master-signing-key.asc

For additional security we also publish the fingerprint of the Qubes Master Signing Key ([`0x36879494`](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc)) here in this document:

    pub   4096R/36879494 2010-04-01
          Key fingerprint = 427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494
    uid   Qubes Master Signing Key

There should also be a copy of this key at the project's main website, in the [Qubes Security Pack](/doc/SecurityPack/), and in the archives of the project's [developer](https://groups.google.com/forum/#!msg/qubes-devel/RqR9WPxICwg/kaQwknZPDHkJ) and [user](https://groups.google.com/d/msg/qubes-users/CLnB5uFu_YQ/ZjObBpz0S9UJ) mailing lists.

Once you have obtained the Qubes Master Signing Key ([`0x36879494`](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc)), you should verify the fingerprint of this key very carefully by obtaining copies of the fingerprint from trustworthy independent sources and comparing them to the downloaded key's fingerprint to ensure they match. Then set its trust level to "ultimate" (oh, well), so that it can be used to automatically verify all the keys signed by the Qubes Master Signing Key:


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

Now you can easily download any of the developer or release signing keys that happen to be used to sign particular ISO, RPM, TGZ files or git tags.

For example: Qubes OS Release 2 Signing Key ([`0x0A40E458`](https://keys.qubes-os.org/keys/qubes-release-2-signing-key.asc)) is used for all Release 2 ISO images.

    $ gpg --recv-keys 0x3F01DEF49719158EF86266F80C73B9D40A40E458
    gpg: requesting key 0A40E458 from hkp server keys.gnupg.net
    gpg: key 0A40E458: public key "Qubes OS Release 2 Signing Key" imported
    gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
    gpg: depth: 0  valid:   1  signed:   1  trust: 0-, 0q, 0n, 0m, 0f, 1u
    gpg: depth: 1  valid:   1  signed:   0  trust: 1-, 0q, 0n, 0m, 0f, 0u
    gpg: Total number processed: 1
    gpg:               imported: 1  (RSA: 1)

You can also download all the currently used developers' signing keys and current and older release signing keys (and also a copy of the Qubes Master Signing Key) from the [keys directory on our server](https://keys.qubes-os.org/keys/) and from the [Qubes Security Pack](/doc/SecurityPack/).

The developer signing keys are set to be valid for 1 year only, while the Qubes Master Signing Key ([`0x36879494`](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc)) has no expiration date. This latter key was generated and is kept only within a dedicated, air-gapped "vault" machine, and the private portion will (hopefully) never leave this isolated machine.

You can now verify the ISO image (`Qubes-R2-x86_64-DVD.iso`) matches its signature (`Qubes-R2-x86_64-DVD.iso.asc`):

    $ gpg -v --verify Qubes-R2-x86_64-DVD.iso.asc
    gpg: armor header: Version: GnuPG v1
    gpg: assuming signed data in `Qubes-R2-x86_64-DVD.iso'
    gpg: Signature made Tue Sep 23 08:38:40 2014 UTC using RSA key ID 0A40E458
    gpg: using PGP trust model
    gpg: Good signature from "Qubes OS Release 2 Signing Key"
    gpg: binary signature, digest algorithm SHA1

The Release 2 Signing Key ([`0x0A40E458`](https://keys.qubes-os.org/keys/qubes-release-2-signing-key.asc)) used to sign this ISO image should be signed by the Qubes Master Signing Key ([`0x36879494`](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc)):

    $ gpg --list-sig 0A40E458
    pub   4096R/0A40E458 2012-11-15
    uid                  Qubes OS Release 2 Signing Key
    sig          36879494 2012-11-15  Qubes Master Signing Key
    sig 3        0A40E458 2012-11-15  Qubes OS Release 2 Signing Key

Having problems verifying the ISO images? Make sure you have the corresponding release signing key and see this thread:

[https://groups.google.com/group/qubes-devel/browse\_thread/thread/4bdec1cd19509b38/9f8e219c41e1b232](https://groups.google.com/group/qubes-devel/browse_thread/thread/4bdec1cd19509b38/9f8e219c41e1b232)

Verifying Digests
-----------------

Each ISO is accompanied by a plain text file ending in `.DIGESTS`. This file contains the output of running several different crytographic hash functions on the ISO in order to obtain alphanumeric outputs known as "digests." For example, `Qubes-R2-x86_64-DVD.iso` is accompanied by `Qubes-R2-x86_64-DVD.iso.DIGESTS` which has the following content:

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA256
    
    6f6ff24f2edec3a7607671001e694d8e *Qubes-R2-x86_64-DVD.iso
    0344e04a98b741c311936f3e2bb67fcebfc2be08 *Qubes-R2-x86_64-DVD.iso
    1fa056b73d8e2e93acdf3dcaface2515d61335e723d1d7d338241209119c10a3 *Qubes-R2-x86_64-DVD.iso
    a49ff19c1ad8c51a50198ac51670cf7c71972b437fa59f2e9fc9432cce76f4529f10de1d576ac777cdd49b9325eb2f32347fd13e0f9b04f823a73e84c6ddd772 *Qubes-R2-x86_64-DVD.iso
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1
    
    iQIcBAEBCAAGBQJVvUfGAAoJEAxzudQKQORYhj0P/1TTtDn0WtlfwvSOQ5m3ybeT
    CiEv/wWZmZR2hfTOs1chlwt5PZFUCkAk6hbr7+AbJU3HurnmyK97ORtak0WcuBiO
    3MWKGiDaBGjKfYcv7YZWDcMRCjN69I4gq7lhXB2JC5pSnOkciD8xzSMAnyFz8Dnh
    sHSGJIrOIeLhj0Jt90NGm2CKeQgKrbCGQWWqn/BRf40GXjkyGDSAj+Bsbnpn3LjE
    kWOblX631PRi8eclD27/b5hsK/ur7RlpA0KKn7dJoTO2PikEZRoT7QgcIMxYWOja
    GZhDi/5gWyttVmF1EszkwaYLAH3uqkZbgKHIsLwweTwXYxMqjobQ5dFkm0RCaXXg
    wf/ayfyAIHCWYK0GvyHyAe7hs30UQ4Ssw0LDnnTsOwJYzxZpZqWhcg89EBMGdNgu
    5sghcj97VHjDI/zpRyTOAi1+8ZoG1FMsvmnlpghojXPcFGM1nldKs2k1XfGHdVrH
    ucJfhQilhsGo65EiN+v9VS6tz5dDtX5+NnkkpR5mOx1+xwUf4n+F6cWyIiLKY6Se
    byIN0dPtErZpq47w6bhLZ3Dd/frReG8Egmr7yLAqGHKmuwvmEUA6w6a2VzWQy5G4
    Smcj5kPHKWJ9SvAQHc7SoUmYqt2GEAKBi6CYb5Oeknf3vc4QUSPxF8KRiebUhTxc
    ruycSbLkLklsDjfH0caD
    =NVWj
    -----END PGP SIGNATURE-----

Four digests have been computed for this ISO. The hash functions used, in order from top to bottom, are MD5, SHA1, SHA256, and SHA512. One way to verify that the ISO you downloaded matches any of these is by using `openssl` from the command line:

    $ openssl dgst -md5 Qubes-R2-x86_64-DVD.iso
    MD5(Qubes-R2-x86_64-DVD.iso)= 6f6ff24f2edec3a7607671001e694d8e
    $ openssl dgst -sha1 Qubes-R2-x86_64-DVD.iso
    SHA1(Qubes-R2-x86_64-DVD.iso)= 0344e04a98b741c311936f3e2bb67fcebfc2be08
    $ openssl dgst -sha256 Qubes-R2-x86_64-DVD.iso
    SHA256(Qubes-R2-x86_64-DVD.iso)= 1fa056b73d8e2e93acdf3dcaface2515d61335e723d1d7d338241209119c10a3
    $ openssl dgst -sha512 Qubes-R2-x86_64-DVD.iso
    SHA512(Qubes-R2-x86_64-DVD.iso)= a49ff19c1ad8c51a50198ac51670cf7c71972b437fa59f2e9fc9432cce76f4529f10de1d576ac777cdd49b9325eb2f32347fd13e0f9b04f823a73e84c6ddd772

(Notice that the outputs match the values from the `.DIGESTS` file.)

However, it is possible that an attacker replaced `Qubes-R2-x86_64-DVD.iso` with a malicious ISO, computed the hash values for that ISO, and replaced the values in `Qubes-R2-x86_64-DVD.iso.DIGESTS` with his own set of values. Therefore, ideally, we should also verify the authenticity of the listed hash values. Since `Qubes-R2-x86_64-DVD.iso.DIGESTS` is a clearsigned PGP file, we can use `gpg` to verify it from the command line:

    $ gpg -v --verify Qubes-R2-x86_64-DVD.iso.DIGESTS
    gpg: armor header: Hash: SHA256
    gpg: armor header: Version: GnuPG v1
    gpg: original file name=''
    gpg: Signature made 2015-08-01T22:27:18 UTC using RSA key ID 0A40E458
    gpg: using PGP trust model
    gpg: Good signature from "Qubes OS Release 2 Signing Key"
    gpg: textmode signature, digest algorithm SHA256

The signature is good. Assuming our copy of the `Qubes OS Release 2 Signing Key` is also authentic (see above), we can be confident that these hash values came from the Qubes devs.

Verifying Qubes Code
--------------------

Developers who fetch code from our Git server should always verify tags on the latest commit. Any commits that are not followed by a signed tag should not be trusted!

To verify a signature on a git tag, you can use:

    $ git tag -v <tag name>
