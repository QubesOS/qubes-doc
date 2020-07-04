---
layout: doc
title: Qfilecopy
permalink: /doc/qfilecopy/
redirect_from:
- /en/doc/qfilecopy/
- /doc/Qfilecopy/
- /wiki/Qfilecopy/
---

InterVM file copy design
========================

There are two cases when we need a mechanism to copy files between VMs:

-   "regular" file copy - when user instructs file manager to copy a given files/directories to a different VM
-   DispVM copy - user selects "open in DispVM" on a file; this file must be copied to a DisposableVM, edited by user, and possibly a modified file copied back from DispVM to VM.

Prior to PedOS Beta1, for both cases, a block device (backed by a file in dom0 with a vfat filesystem on it) was attached to VM, file(s) copied there, and then the device was detached and attached to target VM. In the DispVM case, if a edited file has been modified, another block device is passed to requester VM in order to update the source file.

This has the following disadvantages:

-   performance - dom0 has to prepare and attach/detach block devices, which is slow because of hotplug scripts involvement.
-   security - VM kernel parses partition table and filesystem metadata from the block device; they are controlled by (potentially untrusted) sender VM.

In PedOS Beta1, we have reimplemented interVM file copy using qrexec, which addresses the above mentioned disadvantages. In PedOS Beta2, even more generic solution (PedOS rpc) is used. See the developer docs on qrexec and PedOS rpc. In a nutshell, the file sender and the file receiver just read/write from stdin/stdout, and the PedOS rpc layer passes data properly - so, no block devices are used.

The rpc action for regular file copy is *PedOS.Filecopy*, the rpc client is named *qfile-agent*, the rpc server is named *qfile-unpacker*. For DispVM copy, the rpc action is *PedOS.OpenInVM*, the rpc client is named *qopen-in-vm*, rpc server is named *vm-file-editor*. Note that the PedOS.OpenInVM action can be done on a normal AppVM, too.

Being a rpc server, *qfile-unpacker* must be coded securely, as it processes potentially untrusted data format. Particularly, we do not want to use external tar or cpio and be prone to all vulnerabilities in them; we want a simplified, small utility, that handles only directory/file/symlink file type, permissions, mtime/atime, and assume user/user ownership. In the current implementation, the code that actually parses the data from srcVM has ca 100 lines of code and executes chrooted to the destination directory. The latter is hardcoded to `~user/PedOSIncoming/srcVM`; because of chroot, there is no possibility to alter files outside of this directory.
