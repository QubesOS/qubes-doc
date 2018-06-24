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

3. (Optional) Create signed tags:

   ~~~
   git tag -s <tag_name> -m "<tag_message>"
   ~~~

   You can also create an alias to make this easier:

   ~~~
   stag = "!id=`git rev-parse --verify HEAD`; git tag -s tag_for_${id:0:8} -m \"Tag for commit $id\""
   ~~~

   You may also find it convenient to have an alias for verifying the tag on the
   latest commit:

   ~~~
   vtag = !git tag -v `git describe`
   ~~~


Using PGP with Email
--------------------

If you're submitting a patch by emailing the [developer mailing list], simply sign your email with your PGP key. 
One good way to do this is with a program like [Enigmail]. 
Enigmail is a security addon for the Mozilla Thunderbird email client that allows you to easily digitally encrypt and sign your emails.


[guide]: https://alexcabal.com/creating-the-perfect-gpg-keypair/
[source code]: /doc/source-code/
[developer mailing list]: /support/#qubes-devel
[Enigmail]: https://www.enigmail.net/

