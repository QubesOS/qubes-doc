:orphan:

===========
Split GPG-2
===========


Split GPG implements a concept similar to having a smart card with your private GPG keys, except that the role of the “smart card” is played by another Qubes app qube. This way one not-so-trusted domain, e.g. the one where Thunderbird is running, can delegate all crypto operations – such as encryption/decryption and signing – to another, more trusted, network-isolated domain. This way the compromise of your domain where Thunderbird or another client app is running – arguably a not-so-unthinkable scenario – does not allow the attacker to automatically also steal all your keys. (We should make a rather obvious comment here that the so-often-used passphrases on private keys are pretty meaningless because the attacker can easily set up a simple backdoor which would wait until the user enters the passphrase and steal the key then.)

|split-gpg-diagram.png|

This diagram presents an overview of the Split GPG architecture.

Advantages of Split GPG vs. traditional GPG with a smart card
-------------------------------------------------------------


It is often thought that the use of smart cards for private key storage guarantees ultimate safety. While this might be true (unless the attacker can find a usually-very-expensive-and-requiring-physical-presence way to extract the key from the smart card) but only with regards to the safety of the private key itself. However, there is usually nothing that could stop the attacker from requesting the smart card to perform decryption of all the user documents the attacker has found or need to decrypt. In other words, while protecting the user’s private key is an important task, we should not forget that ultimately it is the user data that are to be protected and that the smart card chip has no way of knowing the requests to decrypt documents are now coming from the attacker’s script and not from the user sitting in front of the monitor. (Similarly the smart card doesn’t make the process of digitally signing a document or a transaction in any way more secure – the user cannot know what the chip is really signing. Unfortunately this problem of signing reliability is not solvable by Split GPG.)

With Qubes Split GPG this problem is drastically minimized, because each time the key is to be used the user is asked for consent (with a definable time out, 5 minutes by default), plus is always notified each time the key is used via a tray notification from the domain where GPG backend is running. This way it would be easy to spot unexpected requests to decrypt documents.

Configuration
-------------


Create/Edit ``/etc/qubes/policy.d/30-user-gpg2.policy`` in dom0, and add a line like this:

.. code:: console

      qubes.Gpg2 + gpg-client-vm @default allow target=gpg-server-vm



Import/Generate your secret keys in the server domain. For example:

.. code:: console

      gpg-server-vm$ gpg --import /path/to/my/secret-keys-export
      gpg-server-vm$ gpg --import-ownertrust /path/to/my/ownertrust-export



or

.. code:: console

      gpg-server-vm$ gpg --gen-key



In dom0 enable the ``split-gpg2-client`` service in the client domain, for example via the command-line:

.. code:: console

      dom0$ qvm-service <SPLIT_GPG2_CLIENT_DOMAIN_NAME> split-gpg2-client on


To verify if this was done correctly:

.. code:: console

      dom0$ qvm-service <SPLIT_GPG2_CLIENT_DOMAIN_NAME>


Output should be:

.. code:: console

      split-gpg2-client on


Restart the client domain.

Export the **public** part of your keys and import them in the client domain. Also import/set proper “ownertrust” values. For example:

.. code:: console

      gpg-server-vm$ gpg --export > public-keys-export
      gpg-server-vm$ gpg --export-ownertrust > ownertrust-export
      gpg-server-vm$ qvm-copy public-keys-export ownertrust-export

      gpg-client-vm$ gpg --import ~/QubesIncoming/gpg-server-vm/public-keys-export
      gpg-client-vm$ gpg --import-ownertrust ~/QubesIncoming/gpg-server-vm/ownertrust-export



This should be enough to have it running:

.. code:: console

      gpg-client-vm$ gpg -K
      /home/user/.gnupg/pubring.kbx
      -----------------------------
      sec#  rsa2048 2019-12-18 [SC] [expires: 2021-12-17]
            50C2035AF57B98CD6E4010F1B808E4BB07BA9EFB
      uid           [ultimate] test
      ssb#  rsa2048 2019-12-18 [E]



If you want change some server option copy ``/usr/share/doc/split-gpg2/examples/qubes-split-gpg2.conf.example`` to ``~/.config/qubes-split-gpg2/qubes-split-gpg2.conf`` and change it as desired, it will take precedence over other loaded files, such as the drop-in configuration files with the suffix ``.conf`` in ``~/.config/qubes-split-gpg2/conf.d/``.

If you have a passphrase on your keys and ``gpg-agent`` only shows the “keygrip” (something like the fingerprint of the private key) when asking for the passphrase, then make sure that you have imported the public key part in the server domain.

Subkeys vs primary keys
-----------------------


split-gpg2 only knows a hash of the data being signed. Therefore, it cannot differentiate between e.g. signatures of a piece of data or signatures of another key. This means that a client can use split-gpg2 to sign other keys, which split-gpg1 did not allow.

To prevent this, split-gpg2 creates a new GnuPG home directory and imports the secret subkeys (**not** the primary key!) to it. Clients will be able to use the secret parts of the subkeys, but not of the primary key. If your primary key is able to sign data and certify other keys, and your only subkey can only perform encryption, this means that all signing will fail. To make signing work again, generate a subkey that is capable of signing but **not** certification. split-gpg2 does not generate this key for you, so you need to generate it yourself. If you want to generate a key in software, use the ``addkey`` command of ``gpg2 --edit-key``. If you want to generate a key on a smartcard or other hardware token, use ``addcardkey`` instead.

Advanced usage
--------------


There are a few option not described in this README. See the comments in the example `config and the source code <https://github.com/QubesOS/qubes-app-linux-split-gpg2/blob/main/qubes-split-gpg2.conf.example>`__.

Similar to a smartcard, split-gpg2 only tries to protect the private key. For advanced usages, consider if a specialized RPC service would be better. It could do things like checking what data is singed, detailed logging, exposing the encrypted content only to a VM without network, etc.

Using split-gpg2 as the “backend” for split-gpg1 is known to work.

Allow key generation
--------------------


By setting ``allow_keygen = yes`` in ``qubes-split-gpg2.conf`` you can allow the client to generate new keys. Normal usage should not need this.

**Warning**: This feature is new and not much tested. Therefore it’s not security supported!

Copyright
---------

| Copyright (C) 2014 HW42 `hw42@ipsumj.de <mailto:hw42@ipsumj.de>`__
| Copyright (C) 2019 Marek Marczykowski-Górecki `marmarek@invisiblethingslab.com <mailto:marmarek@invisiblethingslab.com>`__


This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

.. |split-gpg-diagram.png| image:: /attachment/doc/split-gpg-diagram.png

