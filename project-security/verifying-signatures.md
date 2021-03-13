---
layout: doc
permalink: /security/verifying-signatures/
redirect_from:
- /doc/verifying-signatures/
- /en/doc/verifying-signatures/
- /doc/VerifyingSignatures/
- /wiki/VerifyingSignatures/
title: Verifying Signatures
---

# On Digital Signatures and Key Verification

## What Digital Signatures Can and Cannot Prove

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

## How to Verify Qubes ISO Signatures

This section will guide you through the process of verifying a Qubes ISO by checking its PGP signature.
There are three basic steps in this process:

1. [Get the Qubes Master Signing Key and verify its authenticity][QMSK]
2. [Get the Release Signing Key][RSK]
3. [Verify your Qubes ISO][signature file]

If you run into any problems, please consult the [Troubleshooting FAQ] below.

### Preparation

Before we begin, you'll need a program that can verify PGP signatures.
Any such program will do, but here are some examples for popular operating systems:

**Windows:** [Gpg4win](https://gpg4win.org/download.html) ([documentation](https://www.gpg4win.org/documentation.html)).
Use the Windows command line (`cmd.exe`) to enter commands.

**Mac:** [GPG Suite](https://gpgtools.org/) ([documentation](https://gpgtools.tenderapp.com/kb)).
Open a terminal to enter commands.

**Linux:** `gpg2` from your package manager or from [gnupg.org](https://gnupg.org/download/index.html) ([documentation](https://www.gnupg.org/documentation/)).
Open a terminal to enter commands.

The commands below will use `gpg2`, but if that doesn't work for you, try `gpg` instead.
If that still doesn't work, please consult the documentation for your specific program (see links above).

### 1. Get the Qubes Master Signing Key and verify its authenticity

Every file published by the Qubes Project (ISO, RPM, TGZ files and Git repositories) is digitally signed by one of the developer keys or Release Signing Keys.
Each such key is signed by the [Qubes Master Signing Key] (`0xDDFA1A3E36879494`).
The developer signing keys are set to expire after one year, while the Qubes Master Signing Key and Release Signing Keys have no expiration date.
This Qubes Master Signing Key was generated on and is kept only on a dedicated, air-gapped "vault" machine, and the private portion will (hopefully) never leave this isolated machine.

There are several ways to get the Qubes Master Signing Key.

- If you have access to an existing Qubes installation, it's available in every VM ([except dom0]):

    ```shell_session
    $ gpg2 --import /usr/share/qubes/qubes-master-key.asc
    ```

- If you're on Fedora, you can get it in the `distribution-gpg-keys` package:
    
    ```shell_session
    $ dnf install distribution-gpg-keys
    ```

- If you’re on Debian, it may already be included in your keyring.

- Fetch it with GPG:

    ```shell_session
    $ gpg2 --fetch-keys https://keys.qubes-os.org/keys/qubes-master-signing-key.asc
    ```

- Download it as a [file][Qubes Master Signing Key], then import it with GPG:

    ```shell_session
    $ gpg2 --import ./qubes-master-signing-key.asc
    ```

- Get it from a public [keyserver] (specified on first use with `--keyserver <URI>` along with keyserver options to include key signatures), e.g.:

    ```shell_session
    $ gpg2 --keyserver-options no-self-sigs-only,no-import-clean --keyserver hkp://pool.sks-keyservers.net:11371 --recv-keys 0x427F11FD0FAA4B080123F01CDDFA1A3E36879494
    ```

The Qubes Master Signing Key is also available in the [Qubes Security Pack] and in the archives of the project's [developer][devel-master-key-msg] and [user][user-master-key-msg] [mailing lists].

Once you have obtained the Qubes Master Signing Key, you must verify that it is authentic rather than a forgery.
Anyone can create a PGP key with the name "Qubes Master Signing Key," so you cannot rely on the name alone.
You also should not rely on any single website, not even over HTTPS.

So, what *should* you do?
One option is to use the PGP [Web of Trust](https://en.wikipedia.org/wiki/Web_of_trust).
In addition, some operating systems include the means to acquire the Qubes Master Signing Key in a secure way.
For example, on Fedora, `dnf install distribution-gpg-keys` will get you the Qubes Master Signing Key along with several other Qubes keys.
On Debian, your keyring may already contain the necessary keys.

Another option is to rely on the key's fingerprint.
Every PGP key has a fingerprint that uniquely identifies it among all PGP keys (viewable with `gpg2 --fingerprint <KEY_ID>`).
Therefore, if you know the genuine Qubes Master Signing Key fingerprint, then you always have an easy way to confirm whether any purported copy of it is authentic, simply by comparing the fingerprints.

For example, here is the Qubes Master Signing Key fingerprint:

```
pub   4096R/36879494 2010-04-01
      Key fingerprint = 427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494
uid   Qubes Master Signing Key
```

But how do you know that this is the real fingerprint?
After all, [this website could be compromised][website-trust], so the fingerprint you see here may not be genuine.
That's why we strongly suggest obtaining the fingerprint from *multiple, independent sources in several different ways*.

Here are some ideas for how to do that:

- Check the fingerprint on various websites (e.g., [mailing lists](https://groups.google.com/g/qubes-devel/c/RqR9WPxICwg/m/kaQwknZPDHkJ), [discussion forums](https://qubes-os.discourse.group/t/there-is-no-way-to-validate-qubes-master-signing-key/1441/9?u=adw), [social](https://twitter.com/rootkovska/status/496976187491876864) [media](https://www.reddit.com/r/Qubes/comments/5bme9n/fingerprint_verification/), [personal websites](https://andrewdavidwong.com/fingerprints.txt)).
- Check against PDFs, photographs, and videos in which the fingerprint appears
   (e.g., [slides from a talk](https://hyperelliptic.org/PSC/slides/psc2015_qubesos.pdf), on a [T-shirt](https://twitter.com/legind/status/813847907858337793/photo/2), or in the [recording of a presentation](https://youtu.be/S0TVw7U3MkE?t=2563)).
- Download old Qubes ISOs from different sources and check the included Qubes Master Signing Key.
- Ask people to post the fingerprint on various mailing lists, forums, and chat rooms.
- Repeat the above over Tor.
- Repeat the above over various VPNs and proxy servers.
- Repeat the above on different networks (work, school, internet cafe, etc.).
- Text, email, call, video chat, snail mail, or meet up with people you know to confirm the fingerprint.
- Repeat the above from different computers and devices.

Once you've obtained the fingerprint from enough independent sources in enough different ways that you feel confident that you know the genuine fingerprint, keep it in a safe place.
Every time you need to check whether a key claiming to be the Qubes Master Signing Key is authentic, compare that key's fingerprint to your trusted copy and confirm they match.

Now that you've imported the authentic Qubes Master Signing Key, set its trust level to "ultimate" so that it can be used to automatically verify all the keys signed by the Qubes Master Signing Key (in particular, Release Signing Keys).

```
$ gpg2 --edit-key 0x427F11FD0FAA4B080123F01CDDFA1A3E36879494
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
```

Now, when you import any of the legitimate Qubes developer keys and Release Signing Keys used to sign ISOs, RPMs, TGZs, Git tags, and Git commits, they will already be trusted in virtue of being signed by the Qubes Master Signing Key.

Before proceeding to the next step, make sure the Qubes Master Signing Key is in your keyring with the correct trust level.
(Note: We have already verified the authenticity of the key, so this final check is not about security.
Rather, it's just a sanity check to make sure that we've imported the key into our keyring correctly.)

```
$ gpg2 -k "Qubes Master Signing Key"
pub   rsa4096 2010-04-01 [SC]
      427F11FD0FAA4B080123F01CDDFA1A3E36879494
uid           [ultimate] Qubes Master Signing Key
```

If you don't see the Qubes Master Signing Key here with a trust level of "ultimate," go back and follow the instructions in this section carefully.

### 2. Get the Release Signing Key

The filename of the Release Signing Key for your version is usually `qubes-release-X-signing-key.asc`, where `X` is the major version number of your Qubes release.
There are several ways to get the Release Signing Key for your Qubes release.

- If you have access to an existing Qubes installation, the release keys are available in dom0 in `/etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-*`.
  These can be [copied][copy-from-dom0] into other VMs for further use.
  In addition, every other VM contains the release key corresponding to that installation's release in `/etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-*`.
  If you wish to use one of these keys, make sure to import it into your keyring, e.g.:

    ```
    $ gpg2 --import /etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-*
    ```

- Fetch it with GPG:

    ```shell_session
    $ gpg2 --keyserver-options no-self-sigs-only,no-import-clean --fetch-keys https://keys.qubes-os.org/keys/qubes-release-X-signing-key.asc
    ```

- Download it as a file.
  You can find the Release Signing Key for your Qubes version on the [Downloads] page.
  You can also download all the currently used developers' signing keys, Release Signing Keys, and the Qubes Master Signing Key from the [Qubes Security Pack] and the [Qubes OS Keyserver].
  Once you've downloaded your Release Signing Key, import it with GPG:

    ```shell_session
    $ gpg2 --keyserver-options no-self-sigs-only,no-import-clean --import ./qubes-release-X-signing-key.asc
    ```

The Release Signing Key should be signed by the Qubes Master Signing Key:

```shell_session
$ gpg2 --check-signatures "Qubes OS Release X Signing Key"
pub   rsa4096 2017-03-06 [SC]
      5817A43B283DE5A9181A522E1848792F9E2795E9
uid           [  full  ] Qubes OS Release X Signing Key
sig!3        1848792F9E2795E9 2017-03-06  Qubes OS Release X Signing Key
sig!         DDFA1A3E36879494 2017-03-08  Qubes Master Signing Key

gpg: 2 good signatures
```

This is just an example, so the output you receive will not look exactly the same.
What matters is the line that shows that this key is signed by the Qubes Master Signing Key with a `sig!` prefix.
This verifies the authenticity of the Release Signing Key.
Note that the `!` flag after the `sig` tag is important because it means that the key signature is valid.
A `sig-` prefix would indicate a bad signature and `sig%` would mean that gpg encountered an error while verifying the signature.
It is not necessary to independently verify the authenticity of the Release Signing Key, since you already verified the authenticity of the Qubes Master Signing Key.
Before proceeding to the next step, make sure the Release Signing Key is in your keyring:

```
$ gpg2 -k "Qubes OS Release"
pub   rsa4096 2017-03-06 [SC]
      5817A43B283DE5A9181A522E1848792F9E2795E9
uid           [  full  ] Qubes OS Release X Signing Key
```

If you don't see the correct Release Signing Key here, go back and follow the instructions in this section carefully.

### 3. Verify your Qubes ISO

Every Qubes ISO is released with a detached PGP signature file, which you can find on the [Downloads] page alongside the ISO.
If the filename of your ISO is `Qubes-RX-x86_64.iso`, then the name of the signature file for that ISO is `Qubes-RX-x86_64.iso.asc`, where `X` is a specific version of Qubes.
The signature filename is always the same as the ISO filename followed by `.asc`.

Download both the ISO and its signature file.
Put both of them in the same directory, then navigate to that directory.
Now, you can verify the ISO by executing this GPG command in the directory that contains both files:

```shell_session
$ gpg2 -v --verify Qubes-RX-x86_64.iso.asc Qubes-RX-x86_64.iso
gpg: armor header: Version: GnuPG v1
gpg: Signature made Tue 08 Mar 2016 07:40:56 PM PST using RSA key ID 03FA5082
gpg: using PGP trust model
gpg: Good signature from "Qubes OS Release X Signing Key"
gpg: binary signature, digest algorithm SHA256
```

This is just an example, so the output you receive will not look exactly the same.
What matters is the line that says `Good signature from "Qubes OS Release X Signing Key"`.
This confirms that the signature on the ISO is good.

## How to Verify Qubes ISO Digests

Each Qubes ISO is also accompanied by a plain text file ending in `.DIGESTS`.
This file contains the output of running several different cryptographic hash functions on the ISO in order to obtain alphanumeric outputs known as "digests" or "hash values."
These hash values are provided as an alternative verification method to PGP signatures (though the digest file is itself also PGP-signed --- see below).
If you've already verified the signatures on the ISO directly, then verifying digests is not necessary.
You can find the `.DIGESTS` for your ISO on the [Downloads] page, and you can always find all the digest files for every Qubes ISO in the [Qubes Security Pack].

If the filename of your ISO is `Qubes-RX-x86_64.iso`, then the name of the digest file for that ISO is `Qubes-RX-x86_64.iso.DIGESTS`, where `X` is a specific version of Qubes.
The digest filename is always the same as the ISO filename followed by `.DIGESTS`.
Since the digest file is a plain text file, you can open it with any text editor.
Inside, you should find text that looks similar to this:

```
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
```

Four digests have been computed for this ISO.
The hash functions used, in order from top to bottom, are MD5, SHA1, SHA256, and SHA512.
One way to verify that the ISO you downloaded matches any of these hash values is by using the respective `*sum` programs:

```shell_session
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
```

The `OK` response tells us that the hash value for that particular hash function matches.
The program also warns us that there are 23 improperly formatted lines, but this is to be expected.
This is because each file contains lines for several different hash values (as mentioned above), but each `*sum` program verifies only the line for its own hash function.
In addition, there are lines for the PGP signature that the `*sum` programs do not know how to read.
Therefore, it is safe to ignore these warning lines.

Another way is to use `openssl` to compute each hash value, then compare them to the contents of the digest file.:

```shell_session
$ openssl dgst -md5 Qubes-RX-x86_64.iso
MD5(Qubes-RX-x86_64.iso)= 3c951138b8b9867d8657f173c1b58b82
$ openssl dgst -sha1 Qubes-RX-x86_64.iso
SHA1(Qubes-RX-x86_64.iso)= 1fc9508160d7c4cba6cacc3025165b0f996c843f
$ openssl dgst -sha256 Qubes-RX-x86_64.iso
SHA256(Qubes-RX-x86_64.iso)= 6b998045a513dcdd45c1c6e61ace4f1b4e7eff799f381dccb9eb0170c80f678a
$ openssl dgst -sha512 Qubes-RX-x86_64.iso
SHA512(Qubes-RX-x86_64.iso)= de1eb2e76bdb48559906f6fe344027ece20658d4a7f04ba00d4e40c63723171c62bdcc869375e7a4a4499d7bff484d7a621c3acfe9c2b221baee497d13cd02fe
```

(Notice that the outputs match the values from the digest file.)

However, it is possible that an attacker replaced `Qubes-RX-x86_64.iso` with a malicious ISO, computed the hash values for that malicious ISO, and replaced the values in `Qubes-RX-x86_64.iso.DIGESTS` with his own set of values.
Therefore, we should also verify the authenticity of the listed hash values.
Since `Qubes-RX-x86_64.iso.DIGESTS` is a clearsigned PGP file, we can use GPG to verify it from the command line:

1. [Get the Qubes Master Signing Key and verify its authenticity][QMSK]
2. [Get the Release Signing Key][RSK]
3. Verify the signature in the digest file:

    ```shell_session
    $ gpg2 -v --verify Qubes-RX-x86_64.iso.DIGESTS
    gpg: armor header: Hash: SHA256
    gpg: armor header: Version: GnuPG v2
    gpg: original file name=''
    gpg: Signature made Tue 20 Sep 2016 10:37:03 AM PDT using RSA key ID 03FA5082
    gpg: using PGP trust model
    gpg: Good signature from "Qubes OS Release X Signing Key"
    gpg: textmode signature, digest algorithm SHA256
    ```

The signature is good.
If our copy of the `Qubes OS Release X Signing Key` is being validated by the authentic Qubes Master Signing Key (see [above][QMSK]), we can be confident that these hash values came from the Qubes devs.

## How to Verify Qubes Repos

Whenever you use one of the [Qubes repositories], you should verify the PGP signature in a tag on the latest commit or on the latest commit itself.
(One or both may be present, but only one is required.)
If there is no trusted signed tag or commit on top, any commits after the latest trusted signed tag or commit should **not** be trusted.
If you come across a repo with any unsigned commits, you should not add any of your own signed tags or commits on top of them unless you personally vouch for the trustworthiness of the unsigned commits.
Instead, ask the person who pushed the unsigned commits to sign them.

To verify a signature on a Git tag:

```shell_session
$ git tag -v <tag name>
```

or

```shell_session
$ git verify-tag <tag name>
```

To verify a signature on a Git commit:

```shell_session
$ git log --show-signature <commit ID>
```

or

```shell_session
$ git verify-commit <commit ID>
```

You should always perform this verification on a trusted local machine with properly validated keys (which are available in the [Qubes Security Pack]) rather than relying on a third party, such as GitHub.
While the GitHub interface may claim that a commit has a verified signature from a member of the Qubes team, this is only trustworthy if GitHub has performed the signature check correctly, the account identity is authentic, the user's key has not been replaced by an admin, GitHub's servers have not been compromised, and so on.
Since there's no way for you to be certain that all such conditions hold, you're much better off verifying signatures yourself.

Also see: [Distrusting the Infrastructure]

## Troubleshooting FAQ

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

### Why am I getting "bash: gpg2: command not found"?

You don't have `gpg2` installed.
Please install it using the method appropriate for your environment (e.g., via your package manager).

### Why am I getting "No such file or directory"?

Your working directory does not contain the required files.
Go back and follow the instructions more carefully, making sure that you put all required files in the same directory *and* navigate to that directory.

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
