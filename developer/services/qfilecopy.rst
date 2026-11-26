===================================
Inter-qube file copying (qfilecopy)
===================================


There are two cases when we need a mechanism to copy files between VMs:

- “regular” file copy - when user instructs file manager to copy a given files/directories to a different qube

- “disposable” copy - user selects :guilabel:`View in disposable qube` on a file or use :program:`qvm-open-in-dvm`; this file must be copied to a :term:`disposable`, edited by user, and possibly a modified file copied back from the disposable to the source qube.



In the early days of Qubes OS, for both cases, a block device (backed by a file in dom0 with a vfat filesystem on it) was attached to a qube, file(s) copied there, and then the device was detached and attached to target qube. In the disposable case, if a edited file has been modified, another block device is passed to requester qube in order to update the source file.

This has the following disadvantages:

- performance - dom0 has to prepare and attach/detach block devices, which is slow because of hotplug scripts involvement.

- security - qube kernel parses partition table and filesystem metadata from the block device; they are controlled by (potentially untrusted) sender qube.



In modern Qubes OS releases, we have reimplemented inter-qube file copy using :doc:`qrexec </developer/services/qrexec>`, which addresses the above mentioned disadvantages. Nowadays, even more generic solution (Qubes RPC) is used. In a nutshell, the file sender and the file receiver just read/write from stdin/stdout, and the Qubes RPC layer passes data properly - so, no block devices are used.

The RPC action for regular file copy is :ref:`qubes.Filecopy <qubes.Filecopy>`, the RPC client is named *qfile-agent*, the RPC server is named *qfile-unpacker*. For disposable copy, the RPC action is :ref:`qubes.OpenInVM <qubes.OpenInVM>`, the RPC client is named *qopen-in-vm*, RPC server is named *vm-file-editor*. Note that the *qubes.OpenInVM* action can be done on a normal app qube, too.

Being a RPC server, *qfile-unpacker* must be coded securely, as it processes potentially untrusted data format. Particularly, we do not want to use external :command:`tar` or :command:`cpio` and be prone to all vulnerabilities in them; we want a simplified, small utility, that handles only directory/file/symlink file type, permissions, mtime/atime, and assume user/user ownership. In the current implementation, the code that actually parses the data from source qube has ca 100 lines of code and executes chrooted to the destination directory. The latter is hardcoded to :samp:`~user/QubesIncoming/{<SOURCE_QUBE>}`; because of chroot, there is no possibility to alter files outside of this directory.
