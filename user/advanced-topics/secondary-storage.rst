=================
Secondary storage
=================

.. warning::

      This page is intended for advanced users.

Storing qubes on Secondary Drives
---------------------------------


Suppose you have a fast but small primary SSD and a large but slow secondary HDD. You may want to store a subset of your qubes on the HDD. Or if you install a second SSD, you may want to use *that* for storage of some qubes. This page explains how to use that second drive.

Instructions
^^^^^^^^^^^^


Qubes 4.0 is more flexible than earlier versions about placing different VMs on different disks. For example, you can keep templates on one disk and app qubes on another, without messy symlinks.

You can query qvm-pool to list available storage drivers:

.. code:: console

      qvm-pool --help-drivers


qvm-pool driver explanation:

.. code:: text

      <file> refers to using a simple file for image storage and lacks a few features.
      <file-reflink> refers to storing images on a filesystem supporting copy on write.
      <linux-kernel> refers to a directory holding kernel images.
      <lvm_thin> refers to LVM managed pools.



In theory, you can still use file-based disk images (“file” pool driver), but they will lack some features: for example, you won’t be able to do backups without shutting down the qube.

Additional storage can also be added on a Btrfs filesystem. A unique feature of Btrfs is that data can be compressed transparently. The subvolume can also be backed up using snapshots for an additional layer of protection; Btrfs supports differents level of redundancy; it has parity checksum; Btrfs volumes can be expanded or shrunk. Starting or stopping a VM has less impact and less chance of causing slowdown of the system as some users have noted with LVM. Relevant information for general btrfs configuration will be provided after the section on LVM storage.

LVM storage
^^^^^^^^^^^


These steps assume you have already created a separate `volume group <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/logical_volume_manager_administration/vg_admin#VG_create>`__ and `thin pool <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/logical_volume_manager_administration/thinly_provisioned_volume_creation>`__ (not thin volume) for your second drive.. See also `this example <https://www.linux.com/blog/how-full-encrypt-your-linux-system-lvm-luks>`__ if you would like to create an encrypted LVM pool (but note you can use a single logical volume if preferred, and to use the ``-T`` option on ``lvcreate`` to specify it is thin). You can find the commands for this example applied to Qubes at the bottom of this R4.0 section.

First, collect some information in a dom0 terminal:

.. code:: console

      sudo pvs
      sudo lvs


Take note of the VG and thin pool names for your second drive., then register it with Qubes:

.. code:: console

      # <pool_name> is a freely chosen pool name
      # <vg_name> is LVM volume group name
      # <thin_pool_name> is LVM thin pool name
      qvm-pool --add <pool_name> lvm_thin -o volume_group=<vg_name>,thin_pool=<thin_pool_name>,revisions_to_keep=2



BTRFS storage
^^^^^^^^^^^^^


Theses steps assume you have already created a separate Btrfs filesystem for your second drive., that it is encrypted with LUKS and it is mounted. It is recommended to use a subvolume as it enables compression and excess storage can be use for other things.

It is possible to use an existing Btrfs storage if it is configured. In dom0, available Btrfs storage can be displayed using:

.. code:: console

      mount -t btrfs
      btrfs show filesystem


To register the storage to qubes:

.. code:: console

      # <pool_name> is a freely chosen pool name
      # <dir_path> is the mounted path to the second btrfs storage
      qvm-pool --add <pool_name> file-reflink -o dir_path=<dir_path>,revisions_to_keep=2


Using the new pool
^^^^^^^^^^^^^^^^^^


Now, you can create qubes in that pool:

.. code:: console

      qvm-create -P <pool_name> --label red <vmname>


It isn’t possible to directly migrate an existing qube to the new pool, but you can clone it there, then remove the old one:

.. code:: console

      qvm-clone -P <pool_name> <sourceVMname> <cloneVMname>
      qvm-remove <sourceVMname>


If that was a template, or other qube referenced elsewhere (netVM or such), you will need to adjust those references manually after moving. For example:

.. code:: console

      qvm-prefs <appvmname_based_on_old_template> template <new_template_name>


Example setup of second drive.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Assuming the secondary hard disk is at /dev/sdb , you can encrypt the drive as follows. Note that the drive contents will be completely erased, In a dom0 terminal run this command - use the same passphrase as the main Qubes disk to avoid a second password prompt at boot:

.. code:: console

      sudo cryptsetup luksFormat --sector-size=512 /dev/sdb
      sudo blkid /dev/sdb



(The ``--sector-size=512`` argument can sometimes work around an incompatibility of storage hardware with LVM thin pools on Qubes. If this does not apply to your hardware, the argument will make no difference.)

Note the device’s UUID (in this example “b209…”), we will use it as its luks name for auto-mounting at boot, by editing ``/etc/crypttab``, and adding this line to crypttab (replacing both “b209…” entries with your device’s UUID taken from blkid) :

.. code:: text

      luks-b20975aa-8318-433d-8508-6c23982c6cde UUID=b20975aa-8318-433d-8508-6c23982c6cde none


Reboot the computer so the new luks device appears at /dev/mapper/luks-b209… You can then create the new pool by running this command in a dom0 terminal (substitute the b209… UUIDs with your UID):

For LVM
^^^^^^^


First create the physical volume:

.. code:: console

      sudo pvcreate /dev/mapper/luks-b20975aa-8318-433d-8508-6c23982c6cde


Then create the LVM volume group, we will use for example “qubes” as the :

.. code:: console

      sudo vgcreate qubes /dev/mapper/luks-b20975aa-8318-433d-8508-6c23982c6cde


And then use “poolhd0” as the (LVM thin pool name):

.. code:: console

      sudo lvcreate -T -n poolhd0 -l +100%FREE qubes


Finally we will tell Qubes to add a new pool on the just created thin pool:

.. code:: console

      qvm-pool --add poolhd0_qubes lvm_thin -o volume_group=qubes,thin_pool=poolhd0,revisions_to_keep=2


For Btrfs
^^^^^^^^^


First create the physical volume:

.. code:: console

      # <label> Btrfs Label
      sudo mkfs.btrfs -L <label> /dev/mapper/luks-b20975aa-8318-433d-8508-6c23982c6cde


Then mount the new Btrfs to a temporary path:

.. code:: console

      sudo mkdir -p /mnt/new_qube_storage
      sudo mount /dev/mapper/luks-b20975aa-8318-433d-8508-6c23982c6cde /mnt/new_qube_storage


Create a subvolume to hold the data:

.. code:: console

      sudo btrfs subvolume create /mnt/new_qube_storage/qubes



Unmount the temporary Btrfs filesystem:

.. code:: console

      sudo umount /mnt/new_qube_storage
      rmdir /mnt/new_qube_storage


Mount the subvolume with compression enabled if desired:

.. code:: console

      # <compression> zlib|lzo|zstd
      # <subvol> btrfs subvolume "qubes" in this example
      sudo mount /dev/mapper/luks-b20975aa-8318-433d-8508-6c23982c6cde /var/lib/qubes_newpool -o compress=<compression>,subvol=qubes


Finally we will tell Qubes to add a new pool on the just created Btrfs subvolume:

.. code:: console

      qvm-pool --add poolhd0_qubes file-reflink -o dir_path=/var/lib/qubes_newpool,revisions_to_keep=2


By default VMs will be created on the main Qubes disk (i.e. a small SSD), to create them on this secondary drive do the following on a dom0 terminal:

.. code:: console

      qvm-create -P poolhd0_qubes --label red unstrusted-hdd


Verify that corresponding lines were added to /etc/fstab and /etc/cryptab to enable auto mounting of the new pool.
