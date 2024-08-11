---
lang: en
layout: doc
permalink: /doc/templates/windows/migrate-to-4-1/
redirect_from:
- /doc/templates/windows/windows-migrate41/
- /user/templates/windows/windows-migrate41/
- /doc/windows-migrate41/
title: Migrating Windows qubes to Qubes OS 4.1
---

For Windows 7, 10 and 11, there is a way to migrate backups created under Qubes R4.0 to R4.1. For this, the version of Qubes Windows Tools (QWT) 4.1-68, available from [tabit-pro/qubes-windows-tools-cross](https://github.com/tabit-pro/qubes-windows-tools-cross/releases), has to be installed under Qubes R4.0, selecting the option to install the Xen PV disk driver, which emulates SCSI disks. For template VMs, the option to move user profiles may be selected, too. Then, the backup may be created, and this backup can be restored under Qubes R4.1, resulting in a VM well integrated into Qubes R4.1. If `qvm-features <VMname> audio-model ich6` is set, Windows even will have audio, although for Windows 10 and 11 somewhat scratchy.
 
While this is somewhat straightforward, things get difficult if QWT 4.0.1.3 was installed in the VM. Prior to installing version 4.1-68, the old version has to be removed, which can be quite tricky for Windows 10 and 11.

## Preparation for Windows 7

 - Uninstall QWT 4.0.1.3, using the standard procedure from the system control panel of Windows. This will most likely result in a crash.
 - Restart Windows again, hitting the F8 key, select the restart menu, and there select a start in safe mode.
 - The system will start gain, but in a rather useless way. Just shut it down, and reboot again.
 - Now Windows will start normally. Check in the control panel, if there are any Xen drivers left. If so, uninstall them.
 - In the Windows device manager, check if there is still a (probably non working) Xen PV disk device. If so, uninstall it. Otherwise, QWT 4.1-68 will not install.
 - In the control panel, check again, if the Xen drivers are removed. A Xen Bus Package (version 8.2.1.8) may remain and cannot be removed, but does no harm. Any other Xen drivers should have disappeared.
 - There probably will be a drive `D:` containing the private user data. For Qubes, R4.1, QWT will expect this drive to be called `Q:`, so it has to be renamed:
	 - Start the command prompt as administrator, i.e. right click on the Command Prompt icon (All Programs -> Accessories) and choose "Run as administrator"
	 - In the command prompt type `diskmgmt.msc`
	 - In the disk manager, select the volume `Private (D:)`
	 - Select the option `Change Drive Letter and Path`
	 - Select option `Change...`
	 - Select the letter `Q`
	 - Click `OK` in all still open windows of the disk manager and terminate it.

## Preparation for Windows 10 and 11

If there is a drive `D:` from this earlier installation of Qubes Windows Tools, it will probably contain incomplete private data; especially the folder `AppData` containing program configuration data will be missing. In this situation, it may be better to perform a new Windows installation, because repair may be difficult and trouble-prone.

- First, be sure that the automatic repair function is disabled. In a command window, execute `bcdedit /set recoveryenabled NO`, and check that this worked by issuing the command `bcdedit`, without parameters, again.
- Now, uninstall QWT 4.0.1.3, using the Apps and Features function of Windows. This will most likely result in a crash.
- Restart Windows again, possibly two or three times, until repair options are offered. By hitting the F8 key, select the restart menu, and there select a start in safe mode (in German, it's option number 4).
- The system will start gain, but in a rather useless way. Just shut it down, and reboot again.
- Now Windows will start normally. Check in the Apps and Features display, if there are any Xen drivers left. If so, uninstall them.
- In the Windows device manager, check if there is still a (probably non working) Xen PV disk device. If so, uninstall it. Otherwise, QWT 4.1-68 will not install.
- In the Apps and Features display, check again, if the Xen drivers are removed. A Xen Bus Package (version 8.2.1.8) may remain and cannot be removed, but does no harm. Any other Xen drivers should have disappeared.
  
## Transferring the Windows Qube

- Now, finally, after one additional reboot, Qubes Windows Tools 4.1-68 can be installed. The option `Move user profiles` should be used **if and only if** there was **no** separate drive `D:` in the earlier Windows installation.
- After one more reboot, the backup for R4.1 may be created.
- This backup can be installed in Qubes R4.1 and will (probably) work.
 
The PV disk drivers used for migration can be removed after successful installation of the VM under Qubes R4.1. For this, the QWT installation has to be started, the option Change has to be selected, and the PV disk driver must be unselected. After completion, the VM has to be rebooted. For Windows 10 and 11, the VM will crash with the error INACCESSIBLE BOOT DEVICE, which can be repaired as described above.

After successful uninstallation of the PV disk drivers, the disks will appear as QEMU ATA disks.

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  **Caution:** This change may lead Windows to declare that the hardware has changed and that in consequence, the activation is no longer valid, possibly complaining that the use of the software is no longer lawful. It should be possible to reactivate the software if a valid product key is provided.
</div>
