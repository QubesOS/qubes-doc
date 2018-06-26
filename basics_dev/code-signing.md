---
layout: doc
title: Code Signing
permalink: /doc/code-signing/
---

Code Signing
============

All contributions to the Qubes OS [source code] must be cryptographically signed by the author's PGP key.


Generating a Key
----------------

(Note: If you already have a PGP key, you may skip this step.)

Alex Cabal has written an excellent [guide] on creating a PGP keypair.
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


Using PGP with Git
------------------
[Using PGP with Git]: #using-pgp-with-git

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
   commit -S
   ~~~

3. Create signed tags:

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

How to Contribute Signed Code
-----------------------------

The [signature-checker] checks if code contributions are signed.
Although GitHub adds a little green `Verified` button next to the commit, the [signature-checker] uses another algorithm.
You may see this message:

> policy/qubesos/code-signing — Unable to verify (no valid key found) - [signature-checker/check-git-signature line 392](https://github.com/marmarek/signature-checker/blob/d143b8f2b4da828a9a93b91eb972dddb7e28b4f0/check-git-signature#L392)

Which means that the following correct flow was not done in order or is missing steps:

1. Create a signed commit.
   If you have configured your git as in [Using PGP with Git], your commits are signed automatically.
2. Create a new signed tag for the commit.
   The optional part of [Using PGP with Git] uses the `stag` alias to create the signed commit.
   ```
   $ git stag
   signed_tag_for_a8beed54
   ```
3. Push the newly created tag to your repository.
   ```
   git push origin signed_tag_for_a8beed54
   ```
   You can do this and the step before using `git spush` if you added the alias.
4. Push the commit to the repository.
   ```
   git push origin branch-name
   ```
   This triggers the check if the commit is signed in the pull request.
5. Then, the tag is already existent and the [signature-checker] can find it.
   You can see a message like this:
   > policy/qubesos/code-signing — Signed with 9BBAB2DEB1488C99 

### Error Handling

Now, if you get

> Unable to verify (no valid key found)

chances are, you did already push a commit and wonder how to sign it properly.
You can do the following to re-trigger the signature check:

1. Create a new signed commit with the same message. Add `-S` if you did not enable automatic signatures.
   ```
   git commit --amend
   ```
2. Create a tag and push it.
   ```
   git spush
   ```
4. Push the new commit replacing the old one.
   ```
   git push -f
   ```

[signature-checker]: https://github.com/marmarek/signature-checker

Using PGP with Email
--------------------

If you're submitting a patch by emailing the [developer mailing list], simply sign your email with your PGP key. 
One good way to do this is with a program like [Enigmail]. 
Enigmail is a security addon for the Mozilla Thunderbird email client that allows you to easily digitally encrypt and sign your emails.


[guide]: https://alexcabal.com/creating-the-perfect-gpg-keypair/
[source code]: /doc/source-code/
[developer mailing list]: /support/#qubes-devel
[Enigmail]: https://www.enigmail.net/

