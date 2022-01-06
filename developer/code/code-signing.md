---
lang: en
layout: doc
permalink: /doc/code-signing/
ref: 51
title: Code signing
---

All contributions to the Qubes OS [source code](/doc/source-code/) must be cryptographically signed by the author's PGP key.

## Generating a Key

(Note: If you already have a PGP key, you may skip this step.)

Alex Cabal has written an excellent [guide](https://alexcabal.com/creating-the-perfect-gpg-keypair/) on creating a PGP keypair.
Below, we reproduce just the minimum steps in generating a keypair using GnuPG.
Please read Cabal's full guide for further important details.

~~~
$ gpg --gen-key
gpg (GnuPG) 1.4.11; Copyright (C) 2010 Free Software Foundation, Inc.
This is free software: you are free to change and  redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
    (1) RSA and RSA (default)
    (2) DSA and Elgamal
    (3) DSA (sign only)
    (4) RSA (sign only)
Your selection? 1

RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 4096

Requested keysize is 4096 bits
Please specify how long the key should be valid.
    0 = key does not expire
    <n>  = key expires in n days
    <n>w = key expires in n weeks
    <n>m = key expires in n months
    <n>y = key expires in n years
Key is valid for? (0) 0

Key does not expire at all
Is this correct? (y/N) y


You need a user ID to identify your key; the software constructs the user ID
from the Real Name, Comment and E-mail Address in this form:
    "Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"

Real name: Bilbo Baggins

E-mail address: bilbo@shire.org

Comment:
You selected this USER-ID:
    "Bilbo Baggins <bilbo@shire.org>"

Change (N)ame, (C)omment, (E)-mail or (O)kay/(Q)uit? O

You need a Passphrase to protect your secret key.

<type your passphrase>

gpg: key 488BA441 marked as ultimately trusted
public and secret key created and signed.

gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
pub   4096R/488BA441 2013-03-13
      Key fingerprint = B878 1FB6 B187 B94C 3E52  2AFA EB1D B79A 488B A441
uid                  Bilbo Baggins <bilbo@shire.org>
sub   4096R/69B0EA85 2013-03-13
~~~

## Upload the Key

For others to find the public key, please upload it to a server.

```
$ gpg --send-keys --keyserver pool.sks-keyservers.net 69B0EA85
gpg: sending key 488BA441 to hkp server pool.sks-keyservers.net
```

## Using PGP with Git

If you're submitting a patch via GitHub (or a similar Git server), please sign
your Git commits.

1. Set up Git to use your key:

   ~~~
   git config --global user.signingkey <KEYID>
   ~~~

2. Set up Git to sign your commits with your key:

   ~~~
   git config --global commit.gpgsign true
   ~~~

   Alternatively, manually specify when a commit is to be signed:

   ~~~
   git commit -S
   ~~~

3. (Optional) Create signed tags.
   Signed commits are totally sufficient to contribute to Qubes OS.
   However, if you have commits which are not signed and you do not want to change them,
   you can create a signed tag for the commit and push it before the check.

   This is useful for example, if you have a commit back in the git history which
   you like to sign now without rewriting the history.

   ~~~
   git tag -s <tag_name> -m "<tag_message>"
   ~~~

   You can also create an alias to make this easier.
   Edit your `~/.gitconfig` file.
   In the `[alias]` section, add `stag` to create signed tags and `spush` to create signed tags and push them.

   ~~~
   [alias]
   stag = "!bash -c 'id=\"`git rev-parse --verify HEAD`\"; tag_name="signed_tag_for_${id:0:8}"; git tag -s "$tag_name" -m \"Tag for commit $id\"; echo \"$tag_name\"'"
   spush = "!bash -c 'git push origin `git stag`'"
   ~~~

   You may also find it convenient to have an alias for verifying the tag on the
   latest commit:

   ~~~
   vtag = !git tag -v `git describe`
   ~~~

## GitHub Signature Verification (optional)

GitHub shows a green `Verified` label indicating that the GPG signature could be
verified using any of the contributor’s GPG keys uploaded to GitHub. You can
upload your public key on GitHub by adding your public GPG key on the [New GPG
key](https://github.com/settings/gpg/new) under the [SSH GPG keys page](https://github.com/settings/keys).

## Code Signature Checks

The [signature-checker](https://github.com/marmarek/signature-checker) checks if code contributions are signed.
Although GitHub adds a little green `Verified` button next to the commit, the [signature-checker](https://github.com/marmarek/signature-checker) uses this algorithm to check if a commit is correctly signed:

1. Is the commit signed?
   If the commit is not signed, you can see the message
   > policy/qubesos/code-signing — No signature found
2. If the commit is signed, the key is downloaded from a GPG key server.
   If you can see the following error message, please check if you have uploaded the key to a key server.
   > policy/qubesos/code-signing — Unable to verify (no valid key found)

### No Signature Found

> policy/qubesos/code-signing — No signature found

In this case, you have several options to sign the commit:

1. Amend the commit and replace it with a signed commit.
   You can use this command to create a new signed commit:

   ```
   git commit --amend -S
   ```

   This also rewrites the commit so you need to push it forcefully:

   ```
   git push -f
   ```

2. Create a signed tag for the unsigned commit.
   If the commit is back in history and you do not want to change it,
   you can create a signed tag for this commit and push the signature.
   You can use the alias from above:

   ```
   git checkout <commit>
   git spush
   ```

   Now, the signature checker needs to re-check the signature.
   Please comment on the pull request that you would like to have the signatures checked again.

### Unable To Verify

> policy/qubesos/code-signing — Unable to verify (no valid key found)

This means that the [signature-checker](https://github.com/marmarek/signature-checker) has found a signature for the commit
but is not able to verify it using the any key available.
This might be that you forgot to upload the key to a key server.
Please upload it.

## Using PGP with Email

If you're submitting a patch by emailing the [developer mailing list](/support/#qubes-devel), simply sign your email with your PGP key.
One good way to do this is with a program like [Enigmail](https://www.enigmail.net/).
Enigmail is a security addon for the Mozilla Thunderbird email client that allows you to easily digitally encrypt and sign your emails.
