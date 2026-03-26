====================
Verifying signatures
====================


The Qubes OS Project uses `digital signatures <https://en.wikipedia.org/wiki/Digital_signature>`__ to guarantee the authenticity and integrity of certain important assets. This page explains how to verify those signatures. It is extremely important for your security to understand and apply these practices.

What digital signatures can and cannot prove
--------------------------------------------


Most people — even programmers — are confused about the basic concepts underlying digital signatures. Therefore, most people should read this section, even if it looks trivial at first sight.

Digital signatures can prove both **authenticity** and **integrity** to a reasonable degree of certainty. **Authenticity** ensures that a given file was indeed created by the person who signed it (i.e., that a third party did not forge it). **Integrity** ensures that the contents of the file have not been tampered with (i.e., that a third party has not undetectably altered its contents *en route*).

Digital signatures **cannot** prove, e.g., that the signed file is not malicious. In fact, there is nothing that could stop someone from signing a malicious program (and it happens from time to time in reality).

The point is that we must decide who we will trust (e.g., Linus Torvalds, Microsoft, or the Qubes Project) and assume that if a trusted party signed a given file, then it should not be malicious or negligently buggy. The decision of whether to trust any given party is beyond the scope of digital signatures. It’s more of a social and political decision.

Once we decide to trust certain parties, digital signatures are useful, because they make it possible for us to limit our trust only to those few parties we choose and not to worry about all the bad things that can happen between them and us, e.g., server compromises (qubes-os.org will surely be compromised one day, so :ref:`don’t blindly trust the live version of this site <introduction/faq:should i trust this website?>`), dishonest IT staff at the hosting company, dishonest staff at the ISPs, Wi-Fi attacks, etc. We call this philosophy :ref:`distrusting the infrastructure <introduction/faq:what does it mean to "distrust the infrastructure"?>`.

By verifying all the files we download that purport to be authored by a party we’ve chosen to trust, we eliminate concerns about the bad things discussed above, since we can easily detect whether any files have been tampered with (and subsequently choose to refrain from executing, installing, or opening them).

However, for digital signatures to make sense, we must ensure that the public keys we use for signature verification are the original ones. Anybody can generate a cryptographic key that purports to belong to “The Qubes OS Project,” but of course only the keys that we (the real Qubes developers) generate are the genuine ones. The rest of this page explains how to verify the authenticity of the various keys used in the project and how to use those keys to verify certain important assets.

OpenPGP software
----------------


We use `PGP <https://en.wikipedia.org/wiki/Pretty_Good_Privacy>`__ (specifically, the `OpenPGP <https://en.wikipedia.org/wiki/Pretty_Good_Privacy#OpenPGP>`__ standard). Before we begin, you’ll need software that can manage PGP keys and verify PGP signatures. Any program that complies with the OpenPGP standard will do, but here are some examples for popular operating systems:

**Linux:** `GnuPG <https://gnupg.org/download/index.html>`__ (`documentation <https://www.gnupg.org/documentation/>`__). Open a terminal and use the ``gpg2`` command. If you don’t already have GnuPG installed, install it via your distro’s package manager or from the GnuPG website.

**Mac:** `GPG Suite <https://gpgtools.org/>`__ (`documentation <https://gpgtools.tenderapp.com/kb>`__). Open a terminal to enter commands.

**Windows:** `Gpg4win <https://gpg4win.org/download.html>`__ (`documentation <https://www.gpg4win.org/documentation.html>`__). Use the Windows command line (``cmd.exe``) to enter commands.

Throughout this page, we’ll use GnuPG via the ``gpg2`` command. If that doesn’t work for you, try ``gpg`` instead. If that still doesn’t work, please consult the documentation for your specific program (see links above) and the :ref:`project-security/verifying-signatures:troubleshooting faq` below.

.. _how-to-import-QMSK:

How to import and authenticate the Qubes Master Signing Key
-----------------------------------------------------------


Many important Qubes OS Project assets (e.g., ISOs, RPMs, TGZs, and Git objects) are digitally signed by an official team member’s key or by a release signing key (RSK). Each such key is, in turn, signed by the `Qubes Master Signing Key (QMSK) <https://keys.qubes-os.org/keys/qubes-master-signing-key.asc>`__ (``0x427F11FD0FAA4B080123F01CDDFA1A3E36879494``). In this way, the QMSK is the ultimate root of trust for the Qubes OS Project.

The developer signing keys are set to expire after one year, while the QMSK and RSKs have no expiration date. The QMSK was generated on and is kept only on a dedicated, air-gapped “vault” machine, and the private portion will (hopefully) never leave this isolated machine.

.. hint::

   Before we proceed, you must first complete the prerequisite step of :ref:`installing OpenPGP software <project-security/verifying-signatures:openpgp software>`.

Once you have appropriate OpenPGP software installed, there are several ways to get the QMSK.

- **If you’re on Qubes OS**, it’s available in every qube (`except dom0 <https://github.com/QubesOS/qubes-issues/issues/2544>`__):

  .. code:: console

        $ gpg2 --import /usr/share/qubes/qubes-master-key.asc


- **If you’re on Fedora**, you can get it in the `distribution-gpg-keys <https://github.com/xsuchy/distribution-gpg-keys>`__ package:

  .. code:: console

        $ dnf install distribution-gpg-keys
        $ gpg2 --import /usr/share/distribution-gpg-keys/qubes/*


- **If you’re on Debian**, it may already be included in your keyring.

- You can also **fetch it with GPG**:

  .. code:: console

        $ gpg2 --fetch-keys https://keys.qubes-os.org/keys/qubes-master-signing-key.asc


- Get it from a public `keyserver <https://en.wikipedia.org/wiki/Key_server_%28cryptographic%29#Keyserver_examples>`__ (specified on first use with ``--keyserver <URI>`` along with keyserver options to include key signatures), e.g.:

  .. code:: console

        $ gpg2 --keyserver-options no-self-sigs-only,no-import-clean --keyserver hkp://keyserver.ubuntu.com --recv-keys 0x427F11FD0FAA4B080123F01CDDFA1A3E36879494


- Or **download it as a file**, then import the file. Here are some example download locations:

  - :doc:`Qubes security pack </project-security/security-pack>`

  - `Qubes keyserver <https://keys.qubes-os.org/keys/qubes-master-signing-key.asc>`__

  - `Email to qubes-devel <https://groups.google.com/d/msg/qubes-devel/RqR9WPxICwg/kaQwknZPDHkJ>`__

  - `Email to qubes-users <https://groups.google.com/d/msg/qubes-users/CLnB5uFu_YQ/ZjObBpz0S9UJ>`__


  Once you have the key as a file, **import it**:

  .. code:: console

        $ gpg2 --import /<PATH_TO_FILE>/qubes-master-signing-key.asc




Once you’ve obtained the QMSK, you must verify that it’s authentic rather than a forgery. Anyone can create a PGP key with the name “Qubes Master Signing Key” and the short key ID ``0x36879494``, so you cannot rely on these alone. You also should not rely on any single website, not even over HTTPS.

So, what *should* you do? One option is to use the PGP `Web of Trust <https://en.wikipedia.org/wiki/Web_of_trust>`__. In addition, some operating systems include the means to acquire the QMSK securely. For example, on Fedora, ``dnf install distribution-gpg-keys`` will get you the QMSK along with several other Qubes keys. On Debian, your keyring may already contain the necessary keys.

Perhaps the most common route is to rely on the key’s fingerprint, which is a string of 40 alphanumeric characters, like this:

.. code:: text

      427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494



Every PGP key has one of these fingerprints, which uniquely identifies it among all PGP keys. (On the command line, you can view a key’s fingerprint with the ``gpg2 --fingerprint <KEY_ID>`` command.) Therefore, if you know the genuine QMSK fingerprint, then you always have an easy way to confirm whether any purported copy of it is authentic, simply by comparing the fingerprints.

But how do you know which fingerprint is the real one? After all, :ref:`this website could be compromised <introduction/faq:should i trust this website?>`, so the fingerprint you see here may not be genuine. That’s why we strongly suggest obtaining the fingerprint from *multiple independent sources in several different ways*, then comparing the strings of letters and numbers to make sure they match.

For the purpose of convincing yourself that you know the authentic QMSK fingerprint, spaces and capitalization don’t matter. In other words, all of these fingerprints are considered the same:

.. code:: text

      427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494
      427f 11fd 0faa 4b08 0123  f01c ddfa 1a3e 3687 9494
      427F11FD0FAA4B080123F01CDDFA1A3E36879494
      427f11fd0faa4b080123f01cddfa1a3e36879494



Instead, what matters is that *all* the characters are present in *exactly* the same order. If even one character is different, the fingerprints should not be considered the same. Even if two fingerprints have all the same characters, if any of those characters are in a different order, sequence, or position, then the fingerprints should not be considered the same.

However, for the purpose of *searching for*, *looking up*, or *entering* keys, spaces and capitalization can matter, depending on the software or tool you’re using. You may need to try different variations (e.g., with and without spaces). You may also sometimes see (or need to enter) the entire fingerprint prefixed with ``0x``, as in:

.. code:: text

      0x427F11FD0FAA4B080123F01CDDFA1A3E36879494
      0x427f11fd0faa4b080123f01cddfa1a3e36879494



The ``0x`` prefix is sometimes used to indicate that the string following it is a hexadecimal value, and some PGP-related tools may require this prefix. Again, for the purpose of convincing yourself that you know the authentic QMSK fingerprint, you may safely ignore the ``0x`` prefix, as it is not part of the fingerprint. As long as the 40-character string after the ``0x`` matches exactly, the fingerprint is considered the same. The ``0x`` prefix only matters if the software or tool you’re using cares about it.

The general idea of “comparing fingerprints” is to go out into the world (whether digitally, physically, or both) and find other 40-character strings purporting to be the QMSK fingerprint, then compare them to your own purported QMSK fingerprint to ensure that the sequence of alphanumeric characters is exactly the same (again, regardless of spaces or capitalization). If any of the characters do not match or are not in the same order, then at least one of the fingerprints is a forgery. Here are some ideas to get you started:

- Check the fingerprint on various websites (e.g., `mailing lists <https://groups.google.com/g/qubes-devel/c/RqR9WPxICwg/m/kaQwknZPDHkJ>`__, `discussion forums <https://forum.qubes-os.org/t/1441/9>`__, `social <https://twitter.com/rootkovska/status/496976187491876864>`__ `media <https://www.reddit.com/r/Qubes/comments/5bme9n/fingerprint_verification/>`__, `personal websites <https://andrewdavidwong.com/fingerprints.txt>`__).

- Check against PDFs, photographs, and videos in which the fingerprint appears (e.g., `slides from a talk <https://hyperelliptic.org/PSC/slides/psc2015_qubesos.pdf>`__, on a `T-shirt <https://twitter.com/legind/status/813847907858337793/photo/2>`__, or in the `recording of a presentation <https://youtu.be/S0TVw7U3MkE?t=2563>`__).

- Ask people to post the fingerprint on various mailing lists, forums, and chat rooms.

- Download old Qubes ISOs from different sources and check the included Qubes Master Signing Key.

- Repeat the above over Tor.

- Repeat the above over various VPNs and proxy servers.

- Repeat the above on different networks (work, school, internet cafe, etc.).

- Text, email, call, video chat, snail mail, or meet up with people you know to confirm the fingerprint.

- Repeat the above from different computers and devices.



Once you’ve observed enough matching fingerprints from enough independent sources in enough different ways that you feel confident that you have the genuine fingerprint, keep it in a safe place. Every time you need to check whether a key claiming to be the QMSK is authentic, compare that key’s fingerprint to your trusted copy and confirm they match.

Now that you’ve imported the authentic QMSK, set its trust level to “ultimate” so that it can be used to automatically verify all the keys signed by the QMSK (in particular, RSKs).

.. code:: console

      $ gpg2 --edit-key 0x427F11FD0FAA4B080123F01CDDFA1A3E36879494
      gpg (GnuPG) 1.4.18; Copyright (C) 2014 Free Software Foundation, Inc.
      This is free software: you are free to change and redistribute it.
      There is NO WARRANTY, to the extent permitted by law.

      pub  4096R/36879494  created: 2010-04-01  expires: never       usage: SC
                           trust: unknown       validity: unknown
      [ unknown] (1). Qubes Master Signing Key

      $ gpg> fpr
      pub   4096R/36879494 2010-04-01 Qubes Master Signing Key
      Primary key fingerprint: 427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494

      $ gpg> trust
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

      $ gpg> q


Now, when you import any of the release signing keys and many Qubes team member keys, they will already be trusted in virtue of being signed by the QMSK.

As a final sanity check, make sure the QMSK is in your keyring with the correct trust level.

.. code:: console
      :emphasize-lines: 4

      $ gpg2 -k "Qubes Master Signing Key"
      pub   rsa4096 2010-04-01 [SC]
            427F11FD0FAA4B080123F01CDDFA1A3E36879494
      uid           [ultimate] Qubes Master Signing Key



If you don’t see the QMSK here with a trust level of “ultimate,” go back and follow the instructions in this section carefully and consult the :ref:`project-security/verifying-signatures:troubleshooting faq` below.

.. _how-to-import-RSK:

How to import and authenticate release signing keys
---------------------------------------------------


Every Qubes OS release is signed by a **release signing key (RSK)**, which is, in turn, signed by the Qubes Master Signing Key (QMSK).

.. hint::

   Before we proceed, you must first complete the following prerequisite steps:

   1. :ref:`Install OpenPGP software. <project-security/verifying-signatures:openpgp software>`

   2. :ref:`Import and authenticate the QMSK. <how-to-import-QMSK>`



After you have completed these two prerequisite steps, the next step is to obtain the correct RSK. The filename pattern for RSKs is :file:`qubes-release-{*}-signing-key.asc`, where :samp:`{*}` is either a major or minor Qubes release number, such as :samp:`4` or :samp:`4.3`. There are several ways to get the RSK for your Qubes release.

- **If you have access to an existing Qubes installation**, the release keys are available **in dom0** or **in the official Fedora templates** (and qubes based on them), in :file:`/etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-{*}`.

  These can be :doc:`copied from dom0 </user/how-to-guides/how-to-copy-from-dom0>` or :doc:`any qube based on fedora </user/how-to-guides/how-to-copy-and-move-files>` into other qubes for further use.

  If you wish to use one of these keys, **make sure to import it into your keyring**, e.g.:

  .. code:: console

     [user@fedora-based-qube] $ gpg2 --import /etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-*


- **Fetch it with GPG**:

  .. code:: console

        [user@any-online-qube] $ gpg2 --keyserver-options no-self-sigs-only,no-import-clean --fetch-keys https://keys.qubes-os.org/keys/qubes-release-X-signing-key.asc


- **Download it as a file**. You can find the RSK for your Qubes release on the `downloads <https://www.qubes-os.org/downloads/>`__ page. You can also download all the currently used developers’ signing keys, RSKs, and the Qubes Master Signing Key from the :doc:`Qubes security pack </project-security/security-pack>` and the `Qubes keyserver <https://keys.qubes-os.org/keys/>`__. Once you’ve downloaded your RSK, **import it with GPG**:

  .. code:: console

        [user@any-qube] $ gpg2 --keyserver-options no-self-sigs-only,no-import-clean --import ./qubes-release-X-signing-key.asc




Now that you have the correct RSK, you simply need to verify that it is signed by the QMSK:

.. code:: console
      :emphasize-lines: 6

      $ gpg2 --check-signatures "Qubes OS Release X Signing Key"
      pub   rsa4096 YYYY-MM-DD [SC]
            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      uid           [  full  ] Qubes OS Release X Signing Key
      sig!3        XXXXXXXXXXXXXXXX YYYY-MM-DD  Qubes OS Release X Signing Key
      sig!         DDFA1A3E36879494 YYYY-MM-DD  Qubes Master Signing Key

      gpg: 2 good signatures


This is just an example, so the output you receive may not look exactly the same (:samp:`{X}` will be replaced by the release number). What matters is the line with a ``sig!`` prefix showing that the QMSK has signed this key. This verifies the authenticity of the RSK. Note that the ``!`` flag after the ``sig`` tag is important because it means that the key signature is valid. A ``sig-`` prefix would indicate a bad signature, and ``sig%`` would mean that gpg encountered an error while verifying the signature. It is not necessary to independently verify the authenticity of the RSK, since you already verified the authenticity of the QMSK.

As a final sanity check, make sure the RSK is in your keyring with the correct trust level:

.. code:: console
      :emphasize-lines: 4

      $ gpg2 -k "Qubes OS Release X Signing Key"
      pub   rsa4096 YYYY-MM-DD [SC]
            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      uid           [  full  ] Qubes OS Release X Signing Key


If you don’t see the correct RSK here with a trust level of “full” or higher, go back and follow the instructions in this section carefully, and consult the :ref:`project-security/verifying-signatures:troubleshooting faq` below.

How to obtain and authenticate other signing keys
-------------------------------------------------


Please see the :doc:`Qubes security pack </project-security/security-pack>` documentation.

How to verify detached PGP signatures on Qubes ISOs
---------------------------------------------------

.. hint::

   Before we proceed, you must first complete the following prerequisite steps:

   1. :ref:`Install OpenPGP software. <project-security/verifying-signatures:openpgp software>`

   2. :ref:`Import and authenticate the Qubes Master Signing Key. <how-to-import-QMSK>`

   3. :ref:`Import and authenticate your release signing key. <how-to-import-RSK>`



Every Qubes ISO is released with a **detached PGP signature** file, which you can find on the `downloads <https://www.qubes-os.org/downloads/>`__ page alongside the ISO. If the filename of your ISO is :file:`Qubes-R{X}-86_64.iso`, then the name of the signature file for that ISO is :file:`Qubes-R{X}-86_64.iso.asc`, where :samp:`{X}` is a specific release of Qubes. The signature filename is always the same as the ISO filename followed by ``.asc``.

**Download both the ISO and its signature file**. Put both of them **in the same directory**, then navigate to that directory. Now, you can verify the ISO by executing this GPG command in the directory that contains both files, make sure to replace :samp:`Qubes-R{X}` by the correct release number (i.e.: :samp:`Qubes-R{4.3}`):

.. code:: console
   :emphasize-lines: 5

   $ gpg2 -v --verify Qubes-RX-x86_64.iso.asc Qubes-RX-x86_64.iso
   gpg: armor header: Version: GnuPG v1
   gpg: Signature made <TIME> using RSA key ID 03FA5082
   gpg: using PGP trust model
   gpg: Good signature from "Qubes OS Release X Signing Key"
   gpg: binary signature, digest algorithm SHA256


This is just an example, so the output you receive will not look exactly the same. What matters is the line that says ``Good signature from "Qubes OS Release X Signing Key"``. This confirms that the signature on the ISO is good.

If you don’t see a good signature here, go back and follow the instructions in this section carefully, and consult the :ref:`project-security/verifying-signatures:troubleshooting faq` below.

How to re-verify installation media after writing
-------------------------------------------------

.. note:: This is an optional section intended for advanced users.

**Why would you want to re-verify the data that has been written when you’ve already verified the original ISO?** Well, it’s conceivable that a sufficiently sophisticated adversary might allow your initial ISO verification to succeed (so as not to alert you that your machine has been compromised, for example), then surreptitiously modify the data as it is being written onto your installation medium, resulting in a compromised Qubes installer. This might increase the odds that the attack goes undetected. One way to mitigate this risk is to re-verify the installer after writing it onto an installation medium that cannot be altered, such as a USB drive with a properly implemented physical write-protect switch and firmware that is either unflashable or cryptographically signed (or both), as discussed in our :doc:`installation security considerations </user/downloading-installing-upgrading/install-security>`.

.. hint:: Before we proceed, you must have:

   * :ref:`an authentic RSK <how-to-import-RSK>`
   * :ref:`written a Qubes ISO onto your desired medium <user/downloading-installing-upgrading/installation-guide:copying the iso onto the installation medium>` (such as a USB drive or optical disc)

**First**, unplug your USB drive and flip the write protect switch so that the data on the drive can no longer be altered.

Then, you have two options:

* **If you have a different computer** from the one you used to create the installation medium, consider using that computer, preferably an offline computer that has never seen the original ISO.
* **If not**, try to at least use a fresh VM (e.g., a new qube if it’s a Qubes system), preferably offline and with a storage space that is too small to hold the original ISO

The idea is that the original system may have been compromised, and using a different one for re-verification forces your hypothetical adversary to compromise an additional system in order to succeed. After all, if your adversary knows the answer you’re looking for — namely, a match to the genuine ISO — and has access to that very ISO in the same re-verification environment, then there is little to prevent them from simply reading the original ISO and feeding you that result (perhaps while also reading from the USB drive and piping it into ``/dev/null`` so that you see the light on the USB drive blinking to support the illusion that the data is being read from the USB drive).

Now, our goal is to perform **the same verification steps as we did with the original ISO**, except, this time, we’ll be reading the installer data directly from the write-protected USB drive instead of from the original ISO file.

In order to do this, **we have to know the exact size, in bytes, of the original ISO**. There are two ways to get this information:

* **from the Qubes website**, by hovering over any ISO download button on the `downloads page <https://www.qubes-os.org/downloads/>`__. You can also view these values directly in the `downloads page’s source data <https://github.com/QubesOS/qubesos.github.io/blob/master/_data/downloads.yml>`__.
* **from the ISO itself**:

.. code:: console

      $ stat -c %s Qubes-RX-x86_64.iso
      8176568320

Where :file:`Qubes-R{X}-x86_64.iso` is your Qubes ISO (with :samp:`{X}` replaced by the release number). Note that your actual byte number will depend on which Qubes ISO you’re using. This is just an example.

You can now use :program:`gpg` to verify the detached PGP signature directly against the data on the USB drive. The following command reads the exact number of bytes from your USB drive and pipes them into :program:`gpg`: 

.. code:: console
      :emphasize-lines: 8

      $ dd if=/dev/sdX bs=1M count=<SIZE> iflag=count_bytes | gpg -v --verify Qubes-RX-x86_64.iso.asc -
      7797+1 records in
      7797+1 records out
      8176568320 bytes (8.2 GB, 7.6 GiB) copied, 277.332 s, 29.5 MB/s
      gpg: Signature made <TIME>
      gpg:                using RSA key XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      gpg: using pgp trust model
      gpg: Good signature from "Qubes OS Release X Signing Key" [full]
      gpg: binary signature, digest algorithm SHA256, key algorithm rsa4096

Where :file:`/dev/{sdX}` is your USB drive, :samp:`<SIZE>` is the exact size in bytes of the original ISO and ``Qubes-RX-x86_64.iso.asc`` is the detached PGP signature file of the original ISO.

.. note:: The usual form of a :program:`gpg` verification command is ``gpg --verify <SIGNATURE> <SIGNED_DATA>``. Our command is using shell redirection in order to use data from your USB drive as the ``<SIGNED_DATA>``, which is why the ``-`` at the end of the command is required.


**The output you receive will not look exactly the same**, what matters is that you should receive a ``Good signature`` message for the :ref:`appropriate RSK <how-to-import-RSK>`, which should be signed by a copy of the :ref:`genuine QMSK <how-to-import-QMSK>`.

How to verify signatures on Git repository tags and commits
-----------------------------------------------------------

.. hint::

   Before we proceed, you must first complete the following prerequisite steps:

   1. :ref:`Install OpenPGP software. <project-security/verifying-signatures:openpgp software>`

   2. :ref:`Import and authenticate the Qubes Master Signing Key. <how-to-import-QMSK>`

   3. :doc:`Import and authenticate keys from the Qubes security pack (qubes-secpack). </project-security/security-pack>` Please see our :ref:`PGP key policies <project-security/security-pack:pgp key policies>` for important information about these keys.



Whenever you use one of the `Qubes repositories <https://github.com/QubesOS>`__, you should use Git to verify the PGP signature in a tag on the latest commit or on the latest commit itself. (One or both may be present, but only one is required.) If there is no trusted signed tag or commit on top, any commits after the latest trusted signed tag or commit should **not** be trusted. If you come across a repo with any unsigned commits, you should not add any of your own signed tags or commits on top of them unless you personally vouch for the trustworthiness of the unsigned commits. Instead, ask the person who pushed the unsigned commits to sign them.

You should always perform this verification on a trusted local machine with properly authenticated keys rather than relying on a third party, such as GitHub. While the GitHub interface may claim that a commit has a verified signature from a member of the Qubes team, this is only trustworthy if GitHub has performed the signature check correctly, the account identity is authentic, an admin has not replaced the user’s key, GitHub’s servers have not been compromised, and so on. Since there’s no way for you to be certain that all such conditions hold, you’re much better off verifying signatures yourself. (Also see: :ref:`distrusting the infrastructure <introduction/faq:what does it mean to "distrust the infrastructure"?>`.)

How to verify a signature on a Git tag
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. code:: console

      $ git tag -v <tag name>


or

.. code:: console

      $ git verify-tag <tag name>


How to verify a signature on a Git commit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. code:: console

      $ git log --show-signature <commit ID>


or

.. code:: console

      $ git verify-commit <commit ID>


Troubleshooting FAQ
-------------------


Why am I getting "Can't check signature: public key not found"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


You don’t have the correct :ref:`release signing key <how-to-import-RSK>`.

Why am I getting "BAD signature from ‘Qubes OS Release X Signing Key'"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The problem could be one or more of the following:

- You’re trying to verify the wrong file(s). Reread this page carefully.

- You’re using the wrong GPG command. Follow the provided examples carefully, or try using ``gpg`` instead of ``gpg2`` (or vice versa).

- The ISO or :ref:`detached PGP signature file <project-security/verifying-signatures:how to verify detached pgp signatures on qubes isos>` is bad (e.g., incomplete or corrupt download). Try downloading the signature file again from a different source, then try verifying again. If you still get the same result, try downloading the ISO again from a different source, then try verifying again.



Why am I getting "bash: gpg2: command not found"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


You don’t have ``gpg2`` installed. Please install it using the method appropriate for your environment (e.g., via your package manager), or try using ``gpg`` instead.

Why am I getting "No such file or directory"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Your working directory does not contain the required files. Go back and follow the instructions more carefully, making sure that you put all required files in the same directory *and* navigate to that directory.

Why am I getting "can't open signed data ‘Qubes-RX-x86_64.iso'" / "no signed data" / "can't hash datafile: No data"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The correct ISO is not in your working directory.

Why am I getting "can't open ‘Qubes-RX-x86_64.iso.asc' / verify signatures failed: file open error"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The correct :ref:`detached PGP signature file <project-security/verifying-signatures:how to verify detached pgp signatures on qubes isos>` is not in your working directory.

Why am I getting "no valid OpenPGP data found"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Either you don’t have the correct :ref:`detached PGP signature file <project-security/verifying-signatures:how to verify detached pgp signatures on qubes isos>`, or you inverted the arguments to ``gpg2``. (The signature file goes first.)

Why am I getting "WARNING: This key is not certified with a trusted signature! There is no indication that the signature belongs to the owner."?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


There are several possibilities:

- You don’t have the :ref:`Qubes Master Signing Key <how-to-import-QMSK>`.

- You have not :ref:`set the Qubes Master Signing Key’s trust level correctly. <how-to-import-QMSK>`

- In the case of a key that is not directly signed by the Qubes Master Signing Key, you have not :ref:`set that key’s trust level correctly. <project-security/verifying-signatures:how to verify signatures on git repository tags and commits>`



Why am I getting "X signature not checked due to a missing key"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


You don’t have the keys that created those signatures in your keyring. For the purpose of verifying a Qubes ISO, you don’t need them as long as you have the :ref:`Qubes Master Signing Key <how-to-import-QMSK>` and the :ref:`release signing key <how-to-import-RSK>` for your Qubes release.

Why am I seeing additional signatures on a key with "[User ID not found]" or from a revoked key?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


This is just a fundamental part of how OpenPGP works. Anyone can sign anyone else’s public key and upload the signed public key to keyservers. Everyone is also free to revoke their own keys at any time (assuming they possess or can create a revocation certificate). This has no impact on verifying Qubes ISOs, code, or keys.

Why am I getting "verify signatures failed: unexpected data"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


You’re not verifying against the correct :ref:`detached PGP signature file <project-security/verifying-signatures:how to verify detached pgp signatures on qubes isos>`.

Why am I getting "not a detached signature"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


You’re not verifying against the correct :ref:`detached PGP signature file <project-security/verifying-signatures:how to verify detached pgp signatures on qubes isos>`.

Why am I getting "CRC error; […] no signature found […]"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


You’re not verifying against the correct :ref:`detached PGP signature file <project-security/verifying-signatures:how to verify detached pgp signatures on qubes isos>`, or the signature file has been modified. Try downloading it again or from a different source.

Why am I getting "WARNING: 1 listed file could not be read"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The correct ISO is not in your working directory.

I have another problem that isn't mentioned here.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Carefully reread this page to be certain that you didn’t skip any steps. In particular, make sure you have the :ref:`Qubes Master Signing Key <how-to-import-QMSK>`, the :ref:`release signing key <how-to-import-RSK>` for your Qubes release, *and* the :ref:`detached PGP signature file <project-security/verifying-signatures:how to verify detached pgp signatures on qubes isos>`, all for the *correct* Qubes OS release. If your question is about GPG, please see the `GnuPG documentation <https://www.gnupg.org/documentation/>`__. Still have question? Please see :doc:`help, support, mailing lists, and forum </introduction/support>` for places where you can ask!
