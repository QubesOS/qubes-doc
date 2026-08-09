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

.. _qfilecopy-security:

Security
--------

The inter-qube file copy system is secure because it doesn’t allow other qubes to steal the files that are being copied, and it doesn’t allow the source qube to overwrite arbitrary files on the destination qube. Moreover, this system doesn’t use any sort of virtual block device for file copy. Instead, we use Xen shared memory, which eliminates a lot of processing of untrusted data. For example, the receiving qube is *not* forced to parse untrusted partitions or file systems. In this respect, the inter-qube file copy system provides even more security than file copy between two physically separated (air-gapped) machines!

However, one should keep in mind that performing a data transfer from *less trusted* to *more trusted* qubes is always potentially insecure if the data will be parsed in the target qube. This is because the data that we copy could try to exploit some hypothetical bug in software running in the target qube. For example, a seemingly-innocent JPEG that we copy from an untrusted qube might contain a specially-crafted exploit for a bug in a JPEG-parsing application in the target qube. This is a general problem and applies to any data transfer from *less trusted* to *more trusted* qubes. It even applies to the scenario of copying files between air-gapped machines. Therefore, you should always copy data only from *more trusted* to *less trusted* qubes.

.. seealso::

   :download:`Software compartmentalization vs. physical separation (PDF, 1.8MB) <https://invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf>`
      ..

         "Many people believe the Holy Grail of secure isolation is to use two or more physically separate machines. This belief seems so natural, that we often don't give it much thought. After all, what better isolation could we possible get than physical "airgap"?"

         -- Joanna Rutkowska

   `Partitioning my digital life into security domains <https://blog.invisiblethings.org/2011/03/13/partitioning-my-digital-life-into.html>`__
      For more information on this topic, and some ideas of how we might solve this problem in some future version of Qubes.
