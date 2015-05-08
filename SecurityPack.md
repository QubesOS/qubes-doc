---
layout: doc
title: SecurityPack
permalink: /doc/SecurityPack/
redirect_from: /wiki/SecurityPack/
---

Qubes Security Pack
===================

1.  [Qubes Security Pack](#QubesSecurityPack)
    1.  [Introduction](#Introduction)
    2.  [History and Rationale](#HistoryandRationale)
    3.  [How to Obtain, Verify, and Read](#HowtoObtainVerifyandRead)

Introduction
------------

The **Qubes Security Pack (QSP)** is a Git repository which contains:

-   [All Qubes Security Bulletins (QSBs)](/wiki/SecurityBulletins)
-   [All PGP keys](https://keys.qubes-os.org/keys/)
-   [Warrant canaries](https://en.wikipedia.org/wiki/Warrant_canary)
-   Other security-related information and announcements (such as key revocations)

The QSP is located here:

> [https://github.com/QubesOS/qubes-secpack](https://github.com/QubesOS/qubes-secpack)

History and Rationale
---------------------

On 2013-01-05, Joanna Rutkowska announced the QSP and explained its rationale in an [email](https://groups.google.com/d/msg/qubes-devel/twkOEaMLtNI/lZyGx6_jFCEJ) to the Qubes mailing lists:

{% highlight trac-wiki %}
Hello,

A new Qubes Security Bulletin has been just released and is available here:

https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-013-2015.txt

As per the previous discussions about recent problems with verifying
digital signatures on messages sent to Google Groups (thanks to
automatic footer addition by Google), we have decided to change the way
we publish Qubes Security Bulletins, as well as other security-related
info pertinent to the Qubes Project.

Starting today, we will be maintain a Git repository -- "Qubes Security
Pack" -- which will contain all the QSBs released so far, all the keys,
warrant canaries [1], and potentially some additional info or
announcements (e.g. key revocations). The whole repo can be found here:

https://github.com/QubesOS/qubes-secpack

Note that all the keys distributed there should be signed by Qubes
Master Key. The Master Key is also attached in the repo, but should
really be obtained/verified using a different channel.

Additionally, most of the files are signed by core Qubes
developers (currently by Marek and myself) via detached signatures as
well as git tag signatures.

The are several advantages of using Git to distribute all these information:

1) Git repo is a collection of files, some of which can be detached GPG
signatures for other files and we can ensure all these files are
distributed together.

2) Git makes it easy for people to clone and redistribute these
collection of files, as well as to easily host them and view on the Web.

3) Git provides for signed tags mechanisms which is another mean we
utilize to ensure integrity of the distributed files.

A few words about the Warrant Canary which we've just introduced today,
and which can be seen here:

https://github.com/QubesOS/qubes-secpack/blob/master/canaries/canary-001-2015.txt

Even though we're not providing any kind of services (such as e.g. email
hosting), that could be searched or tapped by authorities, there are
other possibilities that worry us [2], in the light of various recent
law "developments", such as those that might be coercing people to hand
over their private keys to authorities.

Until we fully decentralize the root of trust for Qubes, something that
requires the move to deterministic builds [3], and so won't happen
very soon, the possibility of having to disclose any of the Qubes
signing keys to anybody might have pretty serious consequences for those
who decided to entrust Qubes with anything serious. And we would like to
somehow minimize these consequences with this canary thing.

Additionally the canary is a nice way of ensuring "freshness" of our
messaging to the community.

Of course the canary doesn't solve all the problems. E.g. if my signing
keys were somehow stolen without our knowledge, it wouldn't help.
Neither it could help in case me being or becoming a miscreant. And
probably it doesn't address many other potential problems, which could
only be solved one day with a multi-signature scheme. But anyway, until
that time, this is the best we can do, I think.

And congrats to Jann for the very interesting clipboard attack (even
though mostly theoretical, still very cool)!

Thanks,
joanna.

--
The Qubes Security Team
http://wiki.qubes-os.org/trac/wiki/SecurityPage


[1] http://en.wikipedia.org/wiki/Warrant_canary

[2] Especially myself, because I'm currently the Root Of Trust for all
Qubes binaries :/

[3] Deterministic builds are required because it's the only way we can
implement multiple signature scheme for distributed binaries.
{% endhighlight %}

How to Obtain, Verify, and Read
-------------------------------

The following example demonstrates one method of obtaining the QSP, verifying its contents, and reading them.

1.  Clone the QSP repo.

    {% highlight trac-wiki %}
    [user@qubes ~]$ git clone https://github.com/QubesOS/qubes-secpack.git
    Cloning into 'qubes-secpack'...
    remote: Counting objects: 195, done.
    remote: Total 195 (delta 0), reused 0 (delta 0)
    Receiving objects: 100% (195/195), 130.94 KiB | 207.00 KiB/s, done.
    Resolving deltas: 100% (47/47), done.
    Checking connectivity... done.
    {% endhighlight %}

2.  Import the included PGP keys.

    {% highlight trac-wiki %}
    [user@qubes ~]$ gpg --import qubes-secpack/keys/*/*
    gpg: directory `/home/user/.gnupg' created
    gpg: new configuration file `/home/user/.gnupg/gpg.conf' created
    gpg: WARNING: options in `/home/user/.gnupg/gpg.conf' are not yet active during this run
    gpg: keyring `/home/user/.gnupg/secring.gpg' created
    gpg: keyring `/home/user/.gnupg/pubring.gpg' created
    gpg: /home/user/.gnupg/trustdb.gpg: trustdb created
    gpg: key C37BB66B: public key "Joanna Rutkowska (Qubes OS signing key) <joanna@invisiblethingslab.com>" imported
    gpg: key 1E30A75D: public key "Joanna Rutkowska (Qubes OS signing key) <joanna@invisiblethingslab.com>" imported
    gpg: key 74EADABC: public key "Joanna Rutkowska (Qubes OS signing key) <joanna@invisiblethingslab.com>" imported
    gpg: key 65EF29CA: public key "Joanna Rutkowska (Qubes OS Signing Key) <joanna@invisiblethingslab.com>" imported
    gpg: key 34898310: public key "Joanna Rutkowska (Qubes OS Signing Key) <joanna@invisiblethingslab.com>" imported
    gpg: key B298547C: public key "Marek Marczykowski (Qubes OS signing key) <marmarek@mimuw.edu.pl>" imported
    gpg: key AB5EEF90: public key "Marek Marczykowski (Qubes OS signing key) <marmarek@invisiblethingslab.com>" imported
    gpg: key A603BCB6: public key "Marek Marczykowski (Qubes OS signing key) <marmarek@invisiblethingslab.com>" imported
    gpg: key 42CFA724: public key "Marek Marczykowski-G�recki (Qubes OS signing key) <marmarek@invisiblethingslab.com>" imported
    gpg: key 15CE40BF: public key "Wojciech Zygmunt Porczyk (Qubes OS signing key) <woju@invisiblethingslab.com>" imported
    gpg: key 36879494: public key "Qubes Master Signing Key" imported
    gpg: key 211093A7: public key "Qubes OS Release 1 Signing Key" imported
    gpg: key 0A40E458: public key "Qubes OS Release 2 Signing Key" imported
    gpg: key 03FA5082: public key "Qubes OS Release 3 Signing Key" imported
    gpg: key 92C7B3DC: public key "Joanna Rutkowska (Qubes Security Pack Signing Key) <joanna@invisiblethingslab.com>" imported
    gpg: key 1830E06A: public key "Marek Marczykowski-G�recki (Qubes security pack) <marmarek@invisiblethingslab.com>" imported
    gpg: key 3F48CB21: public key "Qubes OS Security Team <security@qubes-os.org>" imported
    gpg: Total number processed: 17
    gpg:               imported: 17  (RSA: 17)
    gpg: no ultimately trusted keys found
    {% endhighlight %}

3.  Verify and trust the Qubes Master Signing Key.

    {% highlight trac-wiki %}
    [user@qubes ~]$ gpg --edit-key 36879494
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

> **Important!**

> In order to verify the authenticity of the Qubes Master Signing Key prior to trusting it, you should obtain the Qubes Master Signing Key fingerprint from a trustworthy source (ideally, multiple sources) *other than* this website and visually compare it (them) to the fingerprint displayed in the preceding step, ensuring they match. You can read more about digital signatures and key verification [here](/wiki/VerifyingSignatures).

1.  Verify and read the canaries.

    {% highlight trac-wiki %}
    [user@qubes ~]$ cd qubes-secpack/canaries/                                     
    [user@qubes canaries]$ gpg --verify canary-001-2015.txt.sig.joanna canary-001-2015.txt
    gpg: Signature made Mon Jan  5 20:21:40 2015 UTC using RSA key ID 92C7B3DC
    gpg: Good signature from "Joanna Rutkowska (Qubes Security Pack Signing Key) <joanna@invisiblethingslab.com>"
    [user@qubes canaries]$ gpg --verify canary-001-2015.txt.sig.marmarek canary-001-2015.txt
    gpg: Signature made Mon Jan  5 20:13:37 2015 UTC using RSA key ID 1830E06A
    gpg: Good signature from "Marek Marczykowski-G�recki (Qubes security pack) <marmarek@invisiblethingslab.com>"
    [user@qubes canaries]$ cat canary-001-2015.txt


                        ---===[ Qubes Canary #1 ]===---

                                     [...]
    {% endhighlight %}

2.  Verify and read the QSBs.

    {% highlight trac-wiki %}
    [user@qubes canaries]$ cd ../QSBs/
    [user@qubes QSBs]$ gpg --verify qsb-013-2015.txt.sig.joanna qsb-013-2015.txt
    gpg: Signature made Mon Jan  5 21:22:14 2015 UTC using RSA key ID 92C7B3DC
    gpg: Good signature from "Joanna Rutkowska (Qubes Security Pack Signing Key) <joanna@invisiblethingslab.com>"
    [user@qubes QSBs]$ gpg --verify qsb-013-2015.txt.sig.marmarek qsb-013-2015.txt
    gpg: Signature made Mon Jan  5 21:38:11 2015 UTC using RSA key ID 1830E06A
    gpg: Good signature from "Marek Marczykowski-G�recki (Qubes security pack) <marmarek@invisiblethingslab.com>"
    [user@qubes QSBs]$ cat qsb-013-2015.txt


                 ---===[ Qubes Security Bulletin #13 ]===---

                                    [...]
    {% endhighlight %}


