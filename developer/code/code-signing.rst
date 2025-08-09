============
Code signing
============


All contributions to the Qubes OS :doc:`source code </developer/code/source-code>` must be cryptographically signed by the author’s PGP key.

Generating a Key
----------------


(**Note:** If you already have a PGP key, you may skip this step.)

Alex Cabal has written an excellent `guide <https://alexcabal.com/creating-the-perfect-gpg-keypair/>`__ on creating a PGP keypair. Below, we reproduce just the minimum steps in generating a keypair using GnuPG. Please read Cabal’s full guide for further important details.

.. code:: console

      $ gpg --gen-key
      gpg (GnuPG) 2.2.27; Copyright (C) 2021 Free Software Foundation, Inc.
      This is free software: you are free to change and redistribute it.
      There is NO WARRANTY, to the extent permitted by law.

      gpg: directory '/home/user/.gnupg' created
      gpg: keybox '/home/user/.gnupg/pubring.kbx' created
      **Note:** Use "gpg --full-generate-key" for a full featured key generation dialog.

      GnuPG needs to construct a user ID to identify your key.

      Real name: Bilbo Baggins
      Email address: bilbo@shire.org
      You selected this USER-ID:
          "Bilbo Baggins <bilbo@shire.org>"

      Change (N)ame, (E)mail, or (O)kay/(Q)uit? O
      We need to generate a lot of random bytes. It is a good idea to perform
      some other action (type on the keyboard, move the mouse, utilize the
      disks) during the prime generation; this gives the random number
      generator a better chance to gain enough entropy.

      <type your passphrase>

      We need to generate a lot of random bytes. It is a good idea to perform
      some other action (type on the keyboard, move the mouse, utilize the
      disks) during the prime generation; this gives the random number
      generator a better chance to gain enough entropy.
      gpg: /home/user/.gnupg/trustdb.gpg: trustdb created
      gpg: key 6E2F4E7AF50A5827 marked as ultimately trusted
      gpg: directory '/home/user/.gnupg/openpgp-revocs.d' created
      gpg: revocation certificate stored as '/home/user/.gnupg/openpgp-revocs.d/87975838063F97A968D503266E2F4E7AF50A5827.rev'
      public and secret key created and signed.

      pub   rsa3072 2021-12-30 [SC] [expires: 2023-12-30]
            87975838063F97A968D503266E2F4E7AF50A5827
      uid                      Bilbo Baggins <bilbo@shire.org>
      sub   rsa3072 2021-12-30 [E] [expires: 2023-12-30]



Upload the Key
--------------


For others to find the public key, please upload it to a server.

Currently, `these <https://github.com/marmarek/signature-checker/blob/master/check-git-signature#L133-L135>`__ are the recognized servers.

In the example below, we will use ``keyserver.ubuntu.com``.

Replace 6E2F4E7AF50A5827 with your key ID, preferably the **long keyID** which is the last 16 hex digits of the long number in the second line of the output above:

.. code:: output

      pub   rsa3072 2021-12-30 [SC] [expires: 2023-12-30]
            87975838063F97A968D503266E2F4E7AF50A5827



.. code:: console

      $ gpg --send-keys --keyserver hkps://keyserver.ubuntu.com 6E2F4E7AF50A5827
      gpg: sending key 6E2F4E7AF50A5827 to hkps://keyserver.ubuntu.com


Using PGP with Git
------------------


If you’re submitting a patch via GitHub (or a similar Git server), please sign your Git commits.

1. Set up Git to use your key:

   .. code:: console

         git config --global user.signingkey <KEYID>



2. Set up Git to sign your commits with your key:

   .. code:: console

         git config --global commit.gpgsign true


   Alternatively, manually specify when a commit is to be signed:

   .. code:: console

         git commit -S



3. (Optional) Create signed tags. Signed commits are totally sufficient to contribute to Qubes OS. However, if you have commits which are not signed and you do not want to change them, you can create a signed tag for the commit and push it before the check.
   This is useful for example, if you have a commit back in the git history which you like to sign now without rewriting the history.

   .. code:: console

         git tag -s <tag_name> -m "<tag_message>"


   You can also create an alias to make this easier. Edit your ``~/.gitconfig`` file. In the ``[alias]`` section, add ``stag`` to create signed tags and ``spush`` to create signed tags and push them.

   .. code:: ini

         [alias]
         stag = "!bash -c 'id=\"`git rev-parse --verify HEAD`\"; tag_name="signed_tag_for_${id:0:8}"; git tag -s "$tag_name" -m \"Tag for commit $id\"; echo \"$tag_name\"'"
         spush = "!bash -c 'git push origin `git stag`'"


   You may also find it convenient to have an alias for verifying the tag on the latest commit:

   .. code:: ini

         vtag = !git tag -v `git describe`





GitHub Signature Verification (optional)
----------------------------------------


GitHub shows a green ``Verified`` label indicating that the GPG signature could be verified using any of the contributor’s GPG keys uploaded to GitHub. You can upload your public key on GitHub by adding your public GPG key on the `New GPG key <https://github.com/settings/gpg/new>`__ under the `SSH GPG keys page <https://github.com/settings/keys>`__.

Code Signature Checks
---------------------


The `signature-checker <https://github.com/marmarek/signature-checker>`__ checks if code contributions are signed. Although GitHub adds a little green ``Verified`` button next to the commit, the `signature-checker <https://github.com/marmarek/signature-checker>`__ uses this algorithm to check if a commit is correctly signed:

1. Is the commit signed? If the commit is not signed, you can see the message

      ``policy/qubesos/code-signing — No signature found``

2. If the commit is signed, the key is downloaded from a GPG key server. If you can see the following error message, please check if you have uploaded the key to a key server.

      ``policy/qubesos/code-signing — Unable to verify (no valid key found)``



No Signature Found
^^^^^^^^^^^^^^^^^^


   ``policy/qubesos/code-signing — No signature found``

In this case, you have several options to sign the commit:

1. Amend the commit and replace it with a signed commit. You can use this command to create a new signed commit:

   .. code:: console

         git commit --amend -S


   This also rewrites the commit so you need to push it forcefully:

   .. code:: console

         git push -f



2. Create a signed tag for the unsigned commit. If the commit is back in history and you do not want to change it, you can create a signed tag for this commit and push the signature. You can use the alias from above:

   .. code:: console

         git checkout <commit>
         git spush


   Now, the signature checker needs to re-check the signature. Please comment on the pull request that you would like to have the signatures checked again.



Unable To Verify
^^^^^^^^^^^^^^^^


   ``policy/qubesos/code-signing — Unable to verify (no valid key found)``

This means that the `signature-checker <https://github.com/marmarek/signature-checker>`__ has found a signature for the commit but is not able to verify it using the any key available. This might be that you forgot to upload the key to a key server. Please upload it.

Using PGP with Email
--------------------


If you’re submitting a patch by emailing the :ref:`developer mailing list <introduction/support:qubes-devel>`, simply sign your email with your PGP key. One good way to do this is with a program like `Enigmail <https://www.enigmail.net/>`__. Enigmail is a security addon for the Mozilla Thunderbird email client that allows you to easily digitally encrypt and sign your emails.
