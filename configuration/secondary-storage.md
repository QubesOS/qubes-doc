---
layout: doc
title: Secondary Storage
permalink: /doc/secondary-storage/
redirect_from:
- /en/doc/secondary-storage/
- /doc/SecondaryStorage/
- /wiki/SecondaryStorage/
---

Storing AppVMs on Secondary Drives
==================================

Suppose you have a fast but small primary SSD and a large but slow secondary HDD.
You want to store a subset of your AppVMs on the HDD.

### R4.0 ###

Qubes 4.0 is more flexible than earlier versions about placing different VMs on different disks. 
For example, you can keep templates on one disk and AppVMs on another, without messy symlinks.

These steps assume you have already created a separate [volume group](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/logical_volume_manager_administration/vg_admin#VG_create) and [thin pool](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/logical_volume_manager_administration/thinly_provisioned_volume_creation) (not thin volume) for your HDD.
See also [this example](https://www.linux.com/blog/how-full-encrypt-your-linux-system-lvm-luks) if you would like to create an encrypted LVM pool (but note you can use a single logical volume if preferred, and to use the `-T` option on `lvcreate` to specify it is thin).

First, collect some information in a dom0 terminal:

    sudo pvs
    sudo lvs

Take note of the VG and thin pool names for your HDD, then register it with Qubes:

    # <pool_name> is a freely chosen pool name
    # <vg_name> is LVM volume group name
    # <thin_pool_name> is LVM thin pool name
    qvm-pool --add <pool_name> lvm_thin -o volume_group=<vg_name>,thin_pool=<thin_pool_name>,revisions_to_keep=2
    
Now, you can create qubes in that pool:

    qvm-create -P <pool_name> --label red <vmname>

It isn't possible to directly migrate an existing qube to the new pool, but you can clone it there, then remove the old one:

    qvm-clone -P <pool_name> <sourceVMname> <cloneVMname>
    qvm-remove <sourceVMname>

If that was a template, or other qube referenced elsewhere (NetVM or such), you will need to adjust those references manually after moving.
For example:

    qvm-prefs <appvmname_based_on_old_template> template <new_template_name>

In theory, you can still use file-based disk images ("file" pool driver), but it lacks some features such as you won't be able to do backups without shutting down the qube.

### R3.2 ###

In dom0:

    mv /var/lib/qubes/appvms/<my-new-appvm> /path/to/secondary/drive/<my-new-appvm>
    ln -s /path/to/secondary/drive/<my-new-appvm> /var/lib/qubes/appvms/

Now, `my-new-appvm` will behave as if it were still stored on the primary SSD (except that it will probably be slower, since it's actually stored on the secondary HDD).

 * The above procedure does **not** interfere with [Qubes Backup][].
   However, attempting to symlink a `private.img` file (rather than the whole AppVM directory) is known to prevent the `private.img` file from being backed up.
   The same problem may occur if the above procedure is attempted on a [TemplateVM][]. [[1]]

 * After implementing the above procedure, starting `my-new-appvm` will cause dom0 notifications to occur stating that loop devices have been attached to dom0.
   This is normal. 
   (No untrusted devices are actually being mounted to dom0.)
   Do not attempt to detach these disks.
   (They will automatically be detached when you shut down the AppVM.) [[2]]

[Qubes Backup]: /doc/BackupRestore/
[TemplateVM]: /doc/Templates/
[1]: https://groups.google.com/d/topic/qubes-users/EITd1kBHD30/discussion
[2]: https://groups.google.com/d/topic/qubes-users/nDrOM7dzLNE/discussion
