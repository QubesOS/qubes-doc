===================================
Qubes security pack (qubes-secpack)
===================================


The **Qubes security pack (qubes-secpack)** is a Git repository that contains:

- `Qubes security bulletins (QSBs) <https://www.qubes-os.org/security/qsb/>`__

- `Qubes canaries <https://www.qubes-os.org/security/canary/>`__

- :ref:`Qubes ISO cryptographic hash values <project-security/verifying-signatures:how to verify the cryptographic hash values of qubes isos>`

- `Qubes fund information <https://github.com/QubesOS/qubes-secpack/tree/master/fund>`__

- `Qubes PGP keys <https://keys.qubes-os.org/keys/>`__

- Security-related information and announcements (e.g., key revocations)



While qubes-secpack itself is independent of any particular host, its current official location is:

https://github.com/QubesOS/qubes-secpack

How to obtain and authenticate
------------------------------


The following example demonstrates one method of obtaining the qubes-secpack and verifying its authenticity. This requires Git and :ref:`OpenPGP software <project-security/verifying-signatures:openpgp software>`.

1. Use Git to clone the qubes-secpack repo.

   .. code:: console

         $ git clone https://github.com/QubesOS/qubes-secpack.git
         Cloning into 'qubes-secpack'...
         remote: Counting objects: 195, done.
         remote: Total 195 (delta 0), reused 0 (delta 0)
         Receiving objects: 100% (195/195), 130.94 KiB | 207.00 KiB/s, done.
         Resolving deltas: 100% (47/47), done.
         Checking connectivity... done.


2. Import the included PGP keys. See our `PGP key policies <#pgp-key-policies>`__ for important information about these keys.

   .. code:: console

         $ gpg --import qubes-secpack/keys/*/*
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
         gpg: key 42CFA724: public key "Marek Marczykowski-Górecki (Qubes OS signing key) <marmarek@invisiblethingslab.com>" imported
         gpg: key 15CE40BF: public key "Wojciech Zygmunt Porczyk (Qubes OS signing key) <woju@invisiblethingslab.com>" imported
         gpg: key 36879494: public key "Qubes Master Signing Key" imported
         gpg: key 211093A7: public key "Qubes OS Release 1 Signing Key" imported
         gpg: key 0A40E458: public key "Qubes OS Release 2 Signing Key" imported
         gpg: key 03FA5082: public key "Qubes OS Release 3 Signing Key" imported
         gpg: key 92C7B3DC: public key "Joanna Rutkowska (Qubes Security Pack Signing Key) <joanna@invisiblethingslab.com>" imported
         gpg: key 1830E06A: public key "Marek Marczykowski-Górecki (Qubes security pack) <marmarek@invisiblethingslab.com>" imported
         gpg: key 3F48CB21: public key "Qubes OS Security Team <security@qubes-os.org>" imported
         gpg: Total number processed: 17
         gpg:               imported: 17  (RSA: 17)
         gpg: no ultimately trusted keys found


3. :ref:`Authenticate and set the trust level of the Qubes Master Signing Key (QMSK). <project-security/verifying-signatures:how to import and authenticate the qubes master signing key>`

4. Verify signed Git tags.

   .. code:: console

         $ cd qubes-secpack/
         $ git tag -v `git describe`
         object 2bb7f0b966593d8ed74e140a04d60c68b96b164e
         type commit
         tag joanna_sec_2bb7f0b9
         tagger Joanna Rutkowska <joanna@invisiblethingslab.com> 1468335706 +0000

         Tag for commit 2bb7f0b966593d8ed74e140a04d60c68b96b164e
         gpg: Signature made 2016-07-12T08:01:46 PDT
         gpg:                using RSA key 0x4E6829BC92C7B3DC
         gpg: Good signature from "Joanna Rutkowska (Qubes Security Pack Signing Key) <joanna@invisiblethingslab.com>" [full]

   The final line of output confirms that the signature is good.

5. Verify detached PGP signatures.

   .. code:: console

         $ cd canaries/
         $ gpg --verify canary-001-2015.txt.sig.joanna canary-001-2015.txt
         gpg: Signature made Mon Jan  5 20:21:40 2015 UTC using RSA key ID 92C7B3DC
         gpg: Good signature from "Joanna Rutkowska (Qubes Security Pack Signing Key) <joanna@invisiblethingslab.com>"
         $ gpg --verify canary-001-2015.txt.sig.marmarek canary-001-2015.txt
         gpg: Signature made Mon Jan  5 20:13:37 2015 UTC using RSA key ID 1830E06A
         gpg: Good signature from "Marek Marczykowski-Górecki (Qubes security pack) <marmarek@invisiblethingslab.com>"

   The fourth and final lines of output confirm that the two signatures are good.



The same procedures can be applied to any directory or file in the qubes-secpack. Two methods of verification (signed Git tags and detached PGP signatures) are provided to ensure that the system is robust (e.g., against a potential failure in Git tag-based verification) and to give users more options to verify the files.

PGP key policies
----------------


- **Inclusion criteria.** The qubes-secpack generally includes only those PGP keys used to sign some kind of official project asset, such as Qubes release ISOs (release signing keys), Git tags and commits (code signing, doc signing, and security team keys), and the qubes-secpack’s own files and Git tags (security team keys again). This means that email keys are generally not included, even for official project email addresses. There is one exception to this rule: the official :ref:`Qubes security team <project-security/security:qubes security team>` email address, which is used to report security vulnerabilities in Qubes OS to our security team.

- **Key signing (certification).** Only some keys in the qubes-secpack are signed by the QMSK. Keys that are not signed directly by the QMSK are still signed indirectly by virtue of being included in the qubes-secpack, which is itself signed (via Git tags and/or commits) by keys that are in turn signed by the QMSK.



History and rationale
---------------------


On 2013-01-05, Joanna Rutkowska announced the qubes-secpack and explained its rationale in an `email <https://groups.google.com/d/msg/qubes-devel/twkOEaMLtNI/lZyGx6_jFCEJ>`__ to the Qubes mailing lists:

.. code:: text

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
      https://www.qubes-os.org/doc/SecurityPage


      [1] http://en.wikipedia.org/wiki/Warrant_canary

      [2] Especially myself, because I'm currently the Root Of Trust for all
      Qubes binaries :/

      [3] Deterministic builds are required because it's the only way we can
      implement multiple signature scheme for distributed binaries.


