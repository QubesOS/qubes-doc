========================
Qubes R3.1 release notes
========================


New features since 3.0
----------------------


- Management Stack based of Salt Stack in dom0 -
  :doc:`documentation </user/advanced-topics/salt>`

- Out of the box Whonix setup

- UEFI support

- LIVE edition (still alpha, not part of R3.1-rc1)

- Updated GPU drivers in dom0

- Colorful window application icons (instead of just colorful lock
  icon)

- PV Grub support (:doc:`documentation </user/advanced-topics/managing-vm-kernels>`)

- Out of the box USB VM setup, including `handling USB mouse <https://github.com/QubesOS/qubes-app-linux-input-proxy/blob/master/README.md>`__

- Xen upgraded to 4.6, for better hardware support (especially Skylake
  platform)

- Improve updates proxy flexibility - especially repositories served
  over HTTPS



You can get detailed description in `completed github issues <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+sort%3Aupdated-desc+milestone%3A%22Release+3.1%22+label%3Arelease-notes+is%3Aclosed>`__

Known issues
------------


- Installation image does not fit on DVD, requires either DVD DL, or
  USB stick (5GB or more)

- Windows Tools: ``qvm-block`` does not work

- Some icons in the Qubes Manager application might not be drawn
  correctly when using the Xfce4 environment in Dom0. If this bothers
  you, please use the KDE environment instead.

- USB mouse (in the case of USB VM) does not work at first system
  startup (just after completing firstboot). Workaround: restart the
  system.

- For other known issues take a look at `our tickets <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Release+3.1%22+label%3Abug>`__



It is advised to install updates just after system installation to apply
bug fixes for (some of) the above problems.

Downloads
---------


See :doc:`Qubes Downloads </user/downloading-installing-upgrading/downloads>`.

Installation instructions
-------------------------


See :doc:`Installation Guide </user/downloading-installing-upgrading/installation-guide>`.

Upgrading
---------


From R3.0
^^^^^^^^^


The easiest and safest way to upgrade to Qubes R3.1 is to install it
from scratch and use :doc:`qubes backup and restore tools </user/how-to-guides/how-to-back-up-restore-and-migrate>` for migrating of all of the user VMs.

Users of Qubes R3.0 can upgrade using :doc:`experimental procedure </user/downloading-installing-upgrading/upgrade/3_1>`.

From R2 or earlier
^^^^^^^^^^^^^^^^^^


When upgrading from earlier versions the easiest and safest way is to
install it from scratch and use :doc:`qubes backup and restore tools </user/how-to-guides/how-to-back-up-restore-and-migrate>` for migrating of all of the user VMs.

Alternatively you can :ref:`upgrade to R3.0 using <developer/releases/3_0/release-notes:upgrading>` first, then follow
the instructions above. This will be time consuming process.
