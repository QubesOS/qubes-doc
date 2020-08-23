---
layout: doc
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

Most people --- even programmers --- are confused about the basic concepts underlying digital signatures.
Therefore, most people should read this section, even if it looks trivial at first sight.

Digital signatures can prove both **authenticity** and **integrity** to a reasonable degree of certainty.
**Authenticity** ensures that a given file was indeed created by the person who signed it (i.e., that it was not forged by a third party).
**Integrity** ensures that the contents of the file have not been tampered with (i.e., that a third party has not undetectably altered its contents *en route*).

Digital signatures **cannot** prove any other property, e.g., that the signed file is not malicious.
In fact, there is nothing that could stop someone from signing a malicious program (and it happens from time to time in reality).

The point is that we must decide who we will trust (e.g., Linus Torvalds, Microsoft, or the Qubes Project) and assume that if a given file was signed by a trusted party, then it should not be malicious or negligently buggy.
The decision of whether to trust any given party is beyond the scope of digital signatures.
It's more of a sociological and political decision.

Once we make the decision to trust certain parties, digital signatures are useful, because they make it possible for us to limit our trust only to those few parties we choose and not to worry about all the bad things that can happen between us and them, e.g., server compromises (qubes-os.org will surely be compromised one day, so [don't blindly trust the live version of this site][website-trust]), dishonest IT staff at the hosting company, dishonest staff at the ISPs, Wi-Fi attacks, etc.
We call this philosophy [Distrusting the Infrastructure].

By verifying all the files we download that purport to be authored by a party we've chosen to trust, we eliminate concerns about the bad things discussed above, since we can easily detect whether any files have been tampered with (and subsequently choose to refrain from executing, installing, or opening them).

However, for digital signatures to make any sense, we must ensure that the public keys we use for signature verification are indeed the original ones.
Anybody can generate a GPG key pair that purports to belong to "The Qubes Project," but of course only the key pair that we (i.e., the Qubes developers) generated is the legitimate one.
The next section explains how to verify the validity of the Qubes signing keys in the process of verifying a Qubes ISO.
(However, the same general principles apply to all cases in which you may wish to verify a PGP signature, such as [verifying repos], not just verifying ISOs.)


How to Verify Qubes ISO Signatures
----------------------------------

This section will guide you through the process of verifying a Qubes ISO by checking its PGP signature.
There are three basic steps in this process:

 1. [Get the Qubes Master Signing Key and verify its authenticity][QMSK]
 2. [Get the Release Signing Key][RSK]
 3. [Verify your Qubes ISO][signature file]

If you run into any problems, please consult the [Troubleshooting FAQ] below.

### 1. Get the Qubes Master Signing Key and verify its authenticity

Every file published by the Qubes Project (ISO, RPM, TGZ files and Git repositories) is digitally signed by one of the developer keys or Release Signing Keys.
Each such key is signed by the [Qubes Master Signing Key] (`0xDDFA1A3E36879494`).
The developer signing keys are set to expire after one year, while the Qubes Master Signing Key and Release Signing Keys have no expiration date.
This Qubes Master Signing Key was generated on and is kept only on a dedicated, air-gapped "vault" machine, and the private portion will (hopefully) never leave this isolated machine.

There are several ways to get the Qubes Master Signing Key.

 - If you have access to an existing Qubes installation, it's available in every VM ([except dom0]):

       $ gpg2 --import /usr/share/qubes/qubes-master-key.asc

 - Fetch it with GPG:

       $ gpg2 --fetch-keys https://keys.qubes-os.org/keys/qubes-master-signing-key.asc

 - Download it as a [file][Qubes Master Signing Key], then import it with GPG:

       $ gpg2 --import ./qubes-master-signing-key.asc 

 - Get it from a public [keyserver] (specified on first use with `--keyserver <URI>`, then saved in `~/.gnupg/gpg.conf`), e.g.:

       $ gpg2 --keyserver pool.sks-keyservers.net --recv-keys 0x427F11FD0FAA4B080123F01CDDFA1A3E36879494

The Qubes Master Signing Key is also available in the [Qubes Security Pack] and in the archives of the project's [developer][devel-master-key-msg] and [user][user-master-key-msg] [mailing lists].

Once you have obtained the Qubes Master Signing Key, you should verify the fingerprint of this key very carefully by obtaining copies of the fingerprint from multiple independent sources and comparing them to the downloaded key's fingerprint to ensure they match.
Here are some ideas:

 - Use the PGP Web of Trust.
 - Check the key against different keyservers.
 - Use different search engines to search for the fingerprint.
 - Use Tor to view and search for the fingerprint on various websites.
 - Use various VPNs and proxy servers.
 - Use different Wi-Fi networks (work, school, internet cafe, etc.).
 - Ask people to post the fingerprint in various forums and chat rooms.
 - Check against PDFs and photographs in which the fingerprint appears
   (e.g., slides from a talk or on a T-shirt).
 - Repeat all of the above from different computers and devices.

In addition, some operating systems have built-in keyrings containing keys capable of validating the Qubes Master Signing Key.
For example, if you have a Debian system, then your keyring may already contain the necessary keys.

For additional security, we also publish the fingerprint of the Qubes Master Signing Key here (but [remember not to blindly trust the live version of this website][website-trust]):

    pub   4096R/36879494 2010-04-01
          Key fingerprint = 427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494
    uid   Qubes Master Signing Key

Once you're confident that you have the legitimate Qubes Master Signing Key, set its trust level to "ultimate" so that it can be used to automatically verify all the keys signed by the Qubes Master Signing Key (in particular, Release Signing Keys).

    $ gpg2 --edit-key 0x36879494
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

Now, when you import any of the legitimate Qubes developer keys and Release Signing Keys used to sign ISOs, RPMs, TGZs, Git tags, and Git commits, they will already be trusted in virtue of being signed by the Qubes Master Signing Key.


### 2. Get the Release Signing Key

The filename of the Release Signing Key for your version is `qubes-release-X-signing-key.asc`, where `X` is the major version number of your Qubes release.
There are several ways to get the Release Signing Key for your Qubes release.

 - If you have access to an existing Qubes installation, the release keys are available in dom0 in `/etc/pki/rpm-gpg/`.
   These can be [copied][copy-from-dom0] into other VMs for further use.
   In addition, every other VM contains the release key corresponding to that installation's release in `/etc/pki/rpm-gpg/`.

 - Fetch it with GPG:

       $ gpg2 --keyserver-options no-self-sigs-only,no-import-clean --fetch-keys https://keys.qubes-os.org/keys/qubes-release-X-signing-key.asc

 - Download it as a file.
   You can find the Release Signing Key for your Qubes version on the [Downloads] page.
   You can also download all the currently used developers' signing keys, Release Signing Keys, and the Qubes Master Signing Key from the [Qubes Security Pack] and the [Qubes OS Keyserver].
   Once you've downloaded your Release Signing Key, import it with GPG:

       $ gpg2 --keyserver-options no-self-sigs-only,no-import-clean --import ./qubes-release-X-signing-key.asc 

The Release Signing Key should be signed by the Qubes Master Signing Key:

    $ gpg2 --check-signatures "Qubes OS Release X Signing Key"
    pub   rsa4096 2017-03-06 [SC]
          5817A43B283DE5A9181A522E1848792F9E2795E9
    uid           [  full  ] Qubes OS Release X Signing Key
    sig!3        1848792F9E2795E9 2017-03-06  Qubes OS Release X Signing Key
    sig!         DDFA1A3E36879494 2017-03-08  Qubes Master Signing Key

    gpg: 2 good signatures

This is just an example, so the output you receive will not look exactly the same.
What matters is the line that shows that this key is signed by the Qubes Master
Signing Key with a `sig!` prefix.  This verifies the authenticity of the
Release Signing Key.  Note that the `!` flag after the `sig` tag is important
because it means that the key signature is valid.  A `sig-` prefix would
indicate a bad signature and `sig%` would mean that gpg encountered an error
while verifying the signature.
It is not necessary to independently verify the authenticity of the Release Signing Key.


### 3. Verify your Qubes ISO

Every Qubes ISO is released with a detached PGP signature file, which you can find on the [Downloads] page alongside the ISO.
If the filename of your ISO is `Qubes-RX-x86_64.iso`, then the name of the signature file for that ISO is `Qubes-RX-x86_64.iso.asc`, where `X` is a specific version of Qubes.
The signature filename is always the same as the ISO filename followed by `.asc`.

Once you've downloaded both the ISO and its signature file, you can verify the ISO using GPG:

    $ gpg2 -v --verify Qubes-RX-x86_64.iso.asc Qubes-RX-x86_64.iso
    gpg: armor header: Version: GnuPG v1
    gpg: Signature made Tue 08 Mar 2016 07:40:56 PM PST using RSA key ID 03FA5082
    gpg: using PGP trust model
    gpg: Good signature from "Qubes OS Release X Signing Key"
    gpg: binary signature, digest algorithm SHA256

This is just an example, so the output you receive will not look exactly the same.
What matters is the line that says `Good signature from "Qubes OS Release X Signing Key"`.
This confirms that the signature on the ISO is good.


How to Verify Qubes ISO Digests
-------------------------------

Each Qubes ISO is also accompanied by a plain text file ending in `.DIGESTS`.
This file contains the output of running several different cryptographic hash functions on the ISO in order to obtain alphanumeric outputs known as "digests" or "hash values."
These hash values are provided as an alternative verification method to PGP signatures (though the digest file is itself also PGP-signed --- see below).
If you've already verified the signatures on the ISO directly, then verifying digests is not necessary.
You can find the `.DIGESTS` for your ISO on the [Downloads] page, and you can always find all the digest files for every Qubes ISO in the [Qubes Security Pack].

If the filename of your ISO is `Qubes-RX-x86_64.iso`, then the name of the digest file for that ISO is `Qubes-RX-x86_64.iso.DIGESTS`, where `X` is a specific version of Qubes.
The digest filename is always the same as the ISO filename followed by `.DIGESTS`.
Since the digest file is a plain text file, you can open it with any text editor.
Inside, you should find text that looks similar to this:

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA256
    
    3c951138b8b9867d8657f173c1b58b82 *Qubes-RX-x86_64.iso
    1fc9508160d7c4cba6cacc3025165b0f996c843f *Qubes-RX-x86_64.iso
    6b998045a513dcdd45c1c6e61ace4f1b4e7eff799f381dccb9eb0170c80f678a *Qubes-RX-x86_64.iso
    de1eb2e76bdb48559906f6fe344027ece20658d4a7f04ba00d4e40c63723171c62bdcc869375e7a4a4499d7bff484d7a621c3acfe9c2b221baee497d13cd02fe *Qubes-RX-x86_64.iso
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
    
Four digests have been computed for this ISO.
The hash functions used, in order from top to bottom, are MD5, SHA1, SHA256, and SHA512.
One way to verify that the ISO you downloaded matches any of these hash values is by using the respective `*sum` programs:

    $ md5sum -c Qubes-RX-x86_64.iso.DIGESTS
    Qubes-RX-x86_64.iso: OK
    md5sum: WARNING: 23 lines are improperly formatted
    $ sha1sum -c Qubes-RX-x86_64.iso.DIGESTS
    Qubes-RX-x86_64.iso: OK
    sha1sum: WARNING: 23 lines are improperly formatted
    $ sha256sum -c Qubes-RX-x86_64.iso.DIGESTS
    Qubes-RX-x86_64.iso: OK
    sha256sum: WARNING: 23 lines are improperly formatted
    $ sha512sum -c Qubes-RX-x86_64.iso.DIGESTS
    Qubes-RX-x86_64.iso: OK
    sha512sum: WARNING: 23 lines are improperly formatted

The `OK` response tells us that the hash value for that particular hash function matches.
The program also warns us that there are 23 improperly formatted lines, but this is to be expected.
This is because each file contains lines for several different hash values (as mentioned above), but each `*sum` program verifies only the line for its own hash function.
In addition, there are lines for the PGP signature that the `*sum` programs do not know how to read.
Therefore, it is safe to ignore these warning lines.

Another way is to use `openssl` to compute each hash value, then compare them to the contents of the digest file.:

    $ openssl dgst -md5 Qubes-RX-x86_64.iso
    MD5(Qubes-RX-x86_64.iso)= 3c951138b8b9867d8657f173c1b58b82
    $ openssl dgst -sha1 Qubes-RX-x86_64.iso
    SHA1(Qubes-RX-x86_64.iso)= 1fc9508160d7c4cba6cacc3025165b0f996c843f
    $ openssl dgst -sha256 Qubes-RX-x86_64.iso
    SHA256(Qubes-RX-x86_64.iso)= 6b998045a513dcdd45c1c6e61ace4f1b4e7eff799f381dccb9eb0170c80f678a
    $ openssl dgst -sha512 Qubes-RX-x86_64.iso
    SHA512(Qubes-RX-x86_64.iso)= de1eb2e76bdb48559906f6fe344027ece20658d4a7f04ba00d4e40c63723171c62bdcc869375e7a4a4499d7bff484d7a621c3acfe9c2b221baee497d13cd02fe

(Notice that the outputs match the values from the digest file.)

However, it is possible that an attacker replaced `Qubes-RX-x86_64.iso` with a malicious ISO, computed the hash values for that ISO, and replaced the values in `Qubes-RX-x86_64.iso.DIGESTS` with his own set of values.
Therefore, ideally, we should also verify the authenticity of the listed hash values.
Since `Qubes-RX-x86_64.iso.DIGESTS` is a clearsigned PGP file, we can use GPG to verify it from the command line:

 1. [Get the Qubes Master Signing Key and verify its authenticity][QMSK]
 2. [Get the Release Signing Key][RSK]
 3. Verify the signature in the digest file:

        $ gpg2 -v --verify Qubes-RX-x86_64.iso.DIGESTS 
        gpg: armor header: Hash: SHA256
        gpg: armor header: Version: GnuPG v2
        gpg: original file name=''
        gpg: Signature made Tue 20 Sep 2016 10:37:03 AM PDT using RSA key ID 03FA5082
        gpg: using PGP trust model
        gpg: Good signature from "Qubes OS Release X Signing Key"
        gpg: textmode signature, digest algorithm SHA256
    
The signature is good.
If our copy of the `Qubes OS Release X Signing Key` is being validated by the authentic Qubes Master Signing Key (see [above][QMSK]), we can be confident that these hash values came from the Qubes devs.


How to Verify Qubes Repos
-------------------------

Whenever you use one of the [Qubes repositories], you should verify the PGP signature in a tag on the latest commit or on the latest commit itself.
(One or both may be present, but only one is required.)
If there is no trusted signed tag or commit on top, any commits after the latest trusted signed tag or commit should **not** be trusted.
If you come across a repo with any unsigned commits, you should not add any of your own signed tags or commits on top of them unless you personally vouch for the trustworthiness of the unsigned commits.
Instead, ask the person who pushed the unsigned commits to sign them.

To verify a signature on a Git tag:

    $ git tag -v <tag name>

or

    $ git verify-tag <tag name>

To verify a signature on a Git commit:

    $ git log --show-signature <commit ID>

or

    $ git verify-commit <commit ID>

You should always perform this verification on a trusted local machine with properly validated keys (which are available in the [Qubes Security Pack]) rather than relying on a third party, such as GitHub.
While the GitHub interface may claim that a commit has a verified signature from a member of the Qubes team, this is only trustworthy if GitHub has performed the signature check correctly, the account identity is authentic, the user's key has not been replaced by an admin, GitHub's servers have not been compromised, and so on.
Since there's no way for you to be certain that all such conditions hold, you're much better off verifying signatures yourself.

Also see: [Distrusting the Infrastructure]


Troubleshooting FAQ
-------------------


### Why am I getting "Can't check signature: public key not found"?

You don't have the correct [Release Signing Key][RSK].


### Why am I getting "BAD signature from 'Qubes OS Release X Signing Key'"?

The problem could be one or more of the following:

 - You're trying to verify the wrong file(s).
   Read this page again carefully.
 - You're using the wrong GPG command.
   Follow the examples in [Verify your Qubes ISO][signature file] carefully.
 - The ISO or [signature file] is bad (e.g., incomplete or corrupt download).
   Try downloading the signature file again from a different source, then try verifying again.
   If you still get the same result, try downloading the ISO again from a different source, then try verifying again.


### I'm getting "bash: gpg2: command not found"

You don't have `gpg2` installed.
Please install it using the method appropriate for your environement (e.g., via your package manager).


### Why am I getting "can't open signed data `Qubes-RX-x86_64.iso' / can't hash datafile: file open error"?

The correct ISO is not in your working directory.


### Why am I getting "can't open `Qubes-RX-x86_64.iso.asc' / verify signatures failed: file open error"?

The correct [signature file] is not in your working directory.


### Why am I getting "no valid OpenPGP data found"?

Either you don't have the correct [signature file], or you inverted the arguments to `gpg2`.
([The signature file goes first.][signature file])


### Why am I getting "WARNING: This key is not certified with a trusted signature! There is no indication that the signature belongs to the owner."?

Either you don't have the [Qubes Master Signing Key][QMSK], or you didn't [set its trust level correctly][QMSK].


### Why am I getting "X signature not checked due to a missing key"?

You don't have the keys that created those signatures in your keyring.
For present purposes, you don't need them as long as you have the [Qubes Master Signing Key][QMSK] and the [Release Signing Key][RSK] for your Qubes version.


### Why am I seeing additional signatures on a key with "[User ID not found]" or from a revoked key?

This is just a basic part of how OpenPGP works.
Anyone can sign anyone else's public key and upload the signed public key to keyservers.
Everyone is also free to revoke their own keys at any time (assuming they possess or can create a revocation certificate). 
This has no impact on verifying Qubes ISOs, code, or keys.


### Why am I getting "verify signatures failed: unexpected data"?

You're not verifying against the correct [signature file].


### Why am I getting "not a detached signature"?

You're not verifying against the correct [signature file].


### Why am I getting "CRC error; [...] no signature found [...]"?

You're not verifying against the correct [signature file], or the signature file has been modified.
Try downloading it again or from a different source.


### Do I have to verify the ISO against both the [signature file] and the [digest file]?

No, either method is sufficient by itself.


### Why am I getting "no properly formatted X checksum lines found"?

You're not checking the correct [digest file].


### Why am I getting "WARNING: X lines are improperly formatted"?

Read [How to Verify Qubes ISO Digests][digest file] again.


### Why am I getting "WARNING: 1 listed file could not be read"?

The correct ISO is not in your working directory.


### I have another problem that isn't mentioned here.

Carefully read this page again to be certain that you didn't skip any steps.
In particular, make sure you have the [Qubes Master Signing Key][QMSK], the [Release Signing Key][RSK], *and* the [signature file] and/or [digest file] all for the *correct* Qubes OS version.
If your question is about GPG, please see the [GPG documentation].
Still have question?
Please see [Help, Support, Mailing Lists, and Forum] for places where you can ask!


[website-trust]: /faq/#should-i-trust-this-website
[Distrusting the Infrastructure]: /faq/#what-does-it-mean-to-distrust-the-infrastructure
[verifying repos]: #how-to-verify-qubes-repos
[Qubes Master Signing Key]: https://keys.qubes-os.org/keys/qubes-master-signing-key.asc
[keyserver]: https://en.wikipedia.org/wiki/Key_server_%28cryptographic%29#Keyserver_examples
[Downloads]: /downloads/
[Qubes Security Pack]: /security/pack/
[Qubes OS Keyserver]: https://keys.qubes-os.org/keys/
[devel-master-key-msg]: https://groups.google.com/d/msg/qubes-devel/RqR9WPxICwg/kaQwknZPDHkJ
[user-master-key-msg]: https://groups.google.com/d/msg/qubes-users/CLnB5uFu_YQ/ZjObBpz0S9UJ
[mailing lists]: /support/
[Troubleshooting FAQ]: #troubleshooting-faq
[QMSK]: #1-get-the-qubes-master-signing-key-and-verify-its-authenticity
[RSK]: #2-get-the-release-signing-key
[copy-from-dom0]: /doc/copy-from-dom0/#copying-from-dom0
[signature file]: #3-verify-your-qubes-iso
[digest file]: #how-to-verify-qubes-iso-digests
[Qubes repositories]: https://github.com/QubesOS
[GPG documentation]: https://www.gnupg.org/documentation/
[Help, Support, Mailing Lists, and Forum]: /support/
[except dom0]: https://github.com/QubesOS/qubes-issues/issues/2544

