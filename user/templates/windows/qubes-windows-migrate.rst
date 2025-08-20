=======================================
Migrating Windows qubes to Qubes OS 4.1
=======================================


For Windows 7, 10, and 11, there is a way to migrate backups created under Qubes R4.1 to R4.2. For this, a backup must be created under R4.1, and this backup has to be restored under Qubes R4.2, resulting in a VM well integrated into Qubes R4.2. If ``qvm-features <VMname> audio-model ich6`` is set, Windows will even have audio, although for Windows 10 and 11, it is somewhat scratchy.


Preparation
-----------


While this is somewhat straightforward, things get difficult if QWT 4.1.68-1 (or earlier) was installed in the VM. Prior to creating the backup, this old version has to be removed, which can be quite tricky for Windows 10 and 11. Otherwise, the restored backup will probably not start or run under Qubes R4.2, because this QWT version is incompatible with R4.2.

To uninstall the installed QWT version, proceed as described in the :doc:`QWT installation documentation for R4.2 </user/templates/windows/qubes-windows-tools-4-1#Uninstalling Qubes Windows Tools (QWT) in a Windows VM>`


Transferring the Windows Qube
-----------------------------


- Now, the backup for R4.2 may be created.

- This backup can be installed in Qubes R4.2 and will (probably) work.

- If Qubes Windows Tools was installed under R4.1, the new version for R4.2 can then be installed as described in the documentation.


**Note:** The Qubes application menus for the newly restored Windows qubes will be empty, but can be easily restored vai the Qube Meanager or by issuing the command ``qubes-sync-appmenus`` in ``dom0``.


Migration to Qubes R4.3
-----------------------


As the current new QWT version was developed primarily for Qubes R4.3, it is compatible with the version of Qubes. So, a Windows VM running under Qubes R4.2 should be transferrable to R4.3 via backup/restore, without the need to remove and reinstall Qubes Windows Tools. At least, for the current pre-release of Qubes R4.3-rc1, this is possible. Currently, however, the new Qubes graphics driver is still very buggy, especially for Windows 11, so it is better not to use it there, since seamless mode is quite unreliable there, and changing the screen resolution may put the VM into an unusable state.

Performing an in-place upgrade of Qubes itself from R4.2.4 to R4.3-rc1 preserves the functionality of Windows 7, 10, and 11 qubes including Qubes Windows Tools; so there is no need to perform an upgrade of these qubes.
