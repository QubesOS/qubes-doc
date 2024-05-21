==============================================
How to mount a Qubes partition from another OS
==============================================


When a Qubes OS install is unbootable or booting it is otherwise
undesirable, this process allows for the recovery of files stored within
the system.

These functions are manual and do not require any Qubes specific tools.
All steps assume the default Qubes install with the following
components: - LUKS encrypted disk - LVM based VM storage

Before beginning, if attempting to access one Qubes system from another,
it is recommended to pass the entire encrypted Qubes disk to an isolated
app qube. This can be done with the command
``qvm-block attach <isolated vm> dom0:<disk>`` in dom0.

Decrypting the Disk
-------------------


1. Find the disk to be accessed:

   1. Open a Linux terminal in either dom0 or the app qube the disk was
      passed through to and enter ``lsblk``, which will result in an
      output similar to the following. In this example, the currently
      booted Qubes system is installed on ``sda`` and the qubes system
      to be accessed is on ``nvme0n1p2``.

      .. code:: bash

            sda                                                                   8:0    0 111.8G  0 disk
            ├─sda1                                                                8:1    0   200M  0 part  /boot/efi
            ├─sda2                                                                8:2    0     1G  0 part  /boot
            └─sda3                                                                8:3    0 110.6G  0 part
              └─luks-fed62fc2-2674-266d-2667-2667259cbdec                       253:0    0 110.6G  0 crypt
                ├─qubes_dom0-pool00_tmeta                                       253:1    0    88M  0 lvm
                │ └─qubes_dom0-pool00-tpool                                     253:3    0  84.4G  0 lvm
                │   ├─qubes_dom0-root                                           253:4    0  84.4G  0 lvm   /
                │   ├─qubes_dom0-pool00                                         253:6    0  84.4G  0 lvm
                ├─qubes_dom0-vm--fedora--30--dvm--private--1576749131--back 253:7    0     2G  0 lvm
                ├─qubes_dom0-pool00_tdata                                       253:2    0  84.4G  0 lvm
                │ └─qubes_dom0-pool00-tpool                                     253:3    0  84.4G  0 lvm
                │   ├─qubes_dom0-root                                           253:4    0  84.4G  0 lvm   /
                │   ├─qubes_dom0-pool00                                         253:6    0  84.4G  0 lvm
                │   ├─qubes_dom0-vm--fedora--30--dvm--private--1576749131--back 253:7    0     2G  0 lvm
                └─qubes_dom0-swap                                               253:5    0     4G  0 lvm   [SWAP]
            sdb                                                                   8:16   0 447.1G  0 disk
            ├─sdb1                                                                8:17   0   549M  0 part
            └─sdb2                                                                8:18   0 446.6G  0 part
            sr0                                                                  11:0    1  1024M  0 rom
            nvme0n1                                                             259:0    0 465.8G  0 disk
            ├─nvme0n1p1                                                         259:1    0     1G  0 part
            └─nvme0n1p2                                                         259:2    0 464.8G  0 part





2. Decrypt the disk using the command
   ``cryptsetup luksOpen /dev/<disk>``.



Accessing LVM Logical Volumes
-----------------------------


3. If using an app qube or standard Linux, LVM should automatically
   discover the Qubes LVM configuration. In this case, continue to step
   4.

   1. Qubes uses the default name ``qubes_dom0`` for it’s LVM VG. This
      will conflict with the name of the VG of the currently installed
      system. To read both, you will have to rename the VG. *Note:* If
      this is not reversed, the Qubes install being accessed will not be
      bootable.

   2. Find the UUID of the vg to be accessed using the command
      ``vgdisplay``. This will be the VG named ``qubes_dom0`` which is
      not marked active.

   3. The command ``vgrename <UUID> other_install`` will rename the VG.



4. Run the command ``vgscan`` to add any new VGs to the device list.





Mounting the disk
-----------------


5. Find the disk to be accessed. The ``lsblk`` command above may be of
   use. The following rules apply by default:





.. list-table:: 
   :widths: 22 22 22 
   :align: center
   :header-rows: 1

   * - Disk name
     - Data type
     - Explanation
   * - other_install/root
     - dom0 root
     - The root partition of dom0.
   * - ot her_install/-private
     - VM
     - The /rw partition of the named VM.
   * - other_install/-root
     - template root
     - The root partition of the named template.
   * - other install/pool00_tmeta
     - LVM Metadata
     - The metadata LV of this disk.
   


6. Mount the disk using the command
   ``mount /dev/other_install/<lv name> <mountpoint>``. *Note:* Any
   compromised data which exists in the volume to be mounted will be
   accessible here. Do not mount untrusted partitions in dom0.





At this point, all files are available in the chosen mountpoint.

Reverting Changes
-----------------


Any changes which were made to the system in the above steps will need
to be reverted before the disk will properly boot. However, LVM will not
allow an VG to be renamed to a name already in use. Thes steps must
occur either in an app qube or using recovery media.

1. Unmount any disks that were accessed.

2. Rename the VG back to qubes_dom0 using the command
   ``vgrename other_install qubes_dom0``.


