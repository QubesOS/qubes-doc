=========================================
How to upgrade a Fedora template in-place
=========================================

.. warning::

      This page is intended for advanced users.

.. DANGER::

      **Warning:** This page is intended for advanced users only. Most users seeking to upgrade should instead :ref:`install a new Fedora template <user/templates/fedora/fedora:installing>`      . Learn more about the two options :ref:`here <user/templates/fedora/fedora:upgrading>`      .

This page provides instructions for performing an in-place upgrade of an installed :doc:`Fedora Template </user/templates/fedora/fedora>`. If you wish to install a new, unmodified Fedora template instead of upgrading a template that is already installed in your system, please see the :doc:`Fedora Template </user/templates/fedora/fedora>` page instead. (:ref:`Learn more about the two options. <user/templates/fedora/fedora:upgrading>`)

Summary instructions for standard Fedora templates
--------------------------------------------------


**Note:** The prompt on each line indicates where each command should be entered: ``dom0``, ``fedora-<old>``, or ``fedora-<new>``, where ``<old>`` is the Fedora version number *from* which you are upgrading, and ``<new>`` is the Fedora version number *to* which you are upgrading.

.. code:: console

      [user@dom0 ~]$ qvm-clone fedora-<old> fedora-<new>
      [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
      [user@dom0 ~]$ qvm-run -a fedora-<new> gnome-terminal
      [user@dom0 ~]$ dev=$(sudo losetup -f --show /var/tmp/template-upgrade-cache.img)
      [user@dom0 ~]$ qvm-block attach fedora-<new> dom0:${dev##*/}
      [user@fedora-<new> ~]$ sudo mkfs.ext4 /dev/xvdi
      [user@fedora-<new> ~]$ sudo mount /dev/xvdi /mnt/removable
      [user@fedora-<new> ~]$ sudo dnf clean all
      [user@fedora-<new> ~]$ sudo dnf --releasever=<new> --setopt=cachedir=/mnt/removable --best distro-sync --allowerasing
      [user@dom0 ~]$ qvm-shutdown fedora-<new>
      [user@dom0 ~]$ sudo losetup -d $dev
      [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img
      [user@dom0 ~]$ qvm-features fedora-<new> template-name fedora-<new>


**Recommended:** :ref:`Switch everything that was set to the old template to the new template. <user/templates/templates:switching>`

Detailed instructions for standard Fedora templates
---------------------------------------------------


These instructions will show you how to upgrade the standard Fedora template. The same general procedure may be used to upgrade any template based on the standard Fedora template.

**Note:** The prompt on each line indicates where each command should be entered: ``dom0``, ``fedora-<old>``, or ``fedora-<new>``, where ``<old>`` is the Fedora version number *from* which you are upgrading, and ``<new>`` is the Fedora version number *to* which you are upgrading.

1. Ensure the existing template is not running.

   .. code:: console

         [user@dom0 ~]$ qvm-shutdown fedora-<old>


2. Clone the existing template and start a terminal in the new template.

   .. code:: console

         [user@dom0 ~]$ qvm-clone fedora-<old> fedora-<new>
         [user@dom0 ~]$ qvm-run -a fedora-<new> gnome-terminal


3. Attempt the upgrade process in the new template.

   .. code:: console

         [user@fedora-<new> ~]$ sudo dnf clean all
         [user@fedora-<new> ~]$ sudo dnf --releasever=<new> distro-sync --best --allowerasing


   **Note:** ``dnf`` might ask you to approve importing a new package signing key. For example, you might see a prompt like this one:

   .. code:: output

         warning: /mnt/removable/updates-0b4cc238d1aa4ffe/packages/example-package.fc<new>.x86_64.rpm: Header V3 RSA/SHA256 Signature, key ID XXXXXXXX: NOKEY
         Importing GPG key 0xXXXXXXXX:
          Userid     : "Fedora <new> (<new>) <fedora-<new>@fedoraproject.org>"
          Fingerprint: XXXX XXXX XXXX XXXX XXXX  XXXX XXXX XXXX XXXX XXXX
          From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-<new>-x86_64
         Is this ok [y/N]: y


   This key was already checked when it was installed (notice that the “From” line refers to a location on your local disk), so you can safely say yes to this prompt.

   - **Note:** If you encounter no errors, proceed to step 4. If you do encounter errors, see the next two points first.

   - If ``dnf`` reports that you do not have enough free disk space to proceed with the upgrade process, create an empty file in dom0 to use as a cache and attach it to the template as a virtual disk.

     .. code:: console

           [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
           [user@dom0 ~]$ dev=$(sudo losetup -f --show /var/tmp/template-upgrade-cache.img)
           [user@dom0 ~]$ qvm-block attach fedora-<new> dom0:${dev##*/}

     Then reattempt the upgrade process, but this time use the virtual disk as a cache.

     .. code:: console

           [user@fedora-<new> ~]$ sudo mkfs.ext4 /dev/xvdi
           [user@fedora-<new> ~]$ sudo mount /dev/xvdi /mnt/removable
           [user@fedora-<new> ~]$ sudo dnf clean all
           [user@fedora-<new> ~]$ sudo dnf --releasever=<new> --setopt=cachedir=/mnt/removable --best distro-sync --allowerasing


     If this attempt is successful, proceed to step 4.

   - ``dnf`` may error with the text: ``At least X MB more space needed on the / filesystem.``
     In this case, one option is to :doc:`resize the template’s disk image </user/advanced-topics/resize-disk-image>` before reattempting the upgrade process. (See `Additional Information <#additional-information>`__ below for other options.)



4. Check that you are on the correct (new) Fedora release. Do this check only after completing the upgrade process. This is *not* a troubleshooting procedure for fixing download issues from the repository. This check simply verifies that your clone has successfully been upgraded.

   .. code:: console

         [user@fedora-<new> ~]$ cat /etc/fedora-release



5. (Optional) Trim the new template. (This should :ref:`no longer be necessary <user/templates/templates:important notes>`, but it does not hurt. Some users have `reported <https://github.com/QubesOS/qubes-issues/issues/5055>`__ that it makes a difference.)

   .. code:: console

         [user@fedora-<new> ~]$ sudo fstrim -av
         [user@dom0 ~]$ qvm-shutdown fedora-<new>
         [user@dom0 ~]$ qvm-start fedora-<new>
         [user@fedora-<new> ~]$ sudo fstrim -av


6. Shut down the new template.

   .. code:: console

         [user@dom0 ~]$ qvm-shutdown fedora-<new>


7. Remove the cache file, if you created one.

   .. code:: console

         [user@dom0 ~]$ sudo losetup -d $dev
         [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img


8. Set the template-name, which is used by the Qubes updater.

   .. code:: console

         [user@dom0 ~]$ qvm-features fedora-<new> template-name fedora-<new>


9. (Recommended) :ref:`Switch everything that was set to the old template to the new template. <user/templates/templates:switching>`

10. (Optional) Make the new template the global default.

    .. code:: console

          [user@dom0 ~]$ qubes-prefs --set default_template fedora-<new>


11. (Optional) :ref:`Uninstall the old template. <user/templates/templates:uninstalling>` Make sure that the template you’re uninstalling is the old one, not the new one!



Summary instructions for Fedora Minimal templates
-------------------------------------------------


**Note:** The prompt on each line indicates where each command should be entered: ``dom0``, ``fedora-<old>``, or ``fedora-<new>``, where ``<old>`` is the Fedora version number *from* which you are upgrading, and ``<new>`` is the Fedora version number *to* which you are upgrading.

.. code:: console

      [user@dom0 ~]$ qvm-clone fedora-<old>-minimal fedora-<new>-minimal
      [user@dom0 ~]$ qvm-run -u root -a fedora-<new>-minimal xterm
      [root@fedora-<new>-minimal ~]# dnf clean all
      [user@fedora-<new>-minimal ~]# dnf --releasever=<new> --best distro-sync --allowerasing
      [user@fedora-<new>-minimal ~]# fstrim -v /
      [user@dom0 ~]$ qvm-features fedora-<new>-minimal template-name fedora-<new>


(Shut down template by any normal means.)

(If you encounter insufficient space issues, you may need to use the methods described for the standard template above.)

Standalones
-----------


The procedure for upgrading a Fedora :doc:`standalone </user/advanced-topics/standalones-and-hvms>` is the same as for a template.

Release-specific notes
----------------------


See the `news <https://www.qubes-os.org/news/>`__ announcement for each specific template release for any important notices about that particular release.

End-of-life (EOL) releases
^^^^^^^^^^^^^^^^^^^^^^^^^^


We strongly recommend against using any Fedora release that has reached `end-of-life (EOL) <https://fedoraproject.org/wiki/End_of_life>`__. Also see :doc:`supported releases </user/downloading-installing-upgrading/supported-releases>`.

Additional information
----------------------


As mentioned above, you may encounter the following ``dnf`` error:

.. code:: output

      At least X MB more space needed on the / filesystem.



In this case, you have several options:

1. :doc:`Increase the template’s disk image size </user/advanced-topics/resize-disk-image>`. This is the solution mentioned in the main instructions above.

2. Delete files in order to free up space. One way to do this is by uninstalling packages. You may then reinstall them again after you finish the upgrade process, if desired). However, you may end up having to increase the disk image size anyway (see previous option).

3. Do the upgrade in parts, e.g., by using package groups. (First upgrade ``@core`` packages, then the rest.)

4. Do not perform an in-place upgrade, see :ref:`Upgrading Fedora templates <user/templates/fedora/fedora:upgrading>`.


