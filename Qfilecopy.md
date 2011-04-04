---
layout: wiki
title: Qfilecopy
permalink: /wiki/Qfilecopy/
---

InterVM file copy design
========================

There are two cases when we need a mechanism to copy files between VMs:

-   "regular" file copy - when user instructs file manager to copy a given files/directories to a different VM
-   DVM copy - user selects "open in DVM" on a file; this file must be copied to DVM, edited by user, and possibly a modified file copied back from DVM to VM.

Prior to Qubes Beta1, for both cases, a block device (backed by a file in dom0 with a vfat filesystem on it) was attached to VM, file(s) copied there, and then the device was detached and attached to target VM. In the DVM case, if a edited file has been modified, another block device is passed to requester VM in order to update the source file.

This has the following disadvantages:

-   performance - dom0 has to attach/detach block devices, which is slow because of hotplug scripts involvement.
-   security - VM kernel parses partition table and filesystem metadata from the block device.

The current solution is based on the "qrexec" mechanism. Dom0 can call *qrexec\_client* program, which will execute a given program in a given VM, passing stdin/stdout/stderr/exit code over vchan connection; possibly attaching the remote stdin/stdout to a local program. In the latter case, the syntax is *qrexec\_client peer\_vm command\_in\_vm -l command\_in\_dom0*

In order to support qrexec, there are two permanent processes: *qrexec-daemon* in dom0 and *qrexec-agent* in VM, connected over vchan. These processes are started when a domain is created. All data exchanged by pairs of processes created by *qrexec\_client DestVM command\_in\_vm* pass via the vchan connecting qrexec-daemon and qrexec-agent.

Notably, qrexec-agent possess ability to signal its qrexec-daemon peer to execute a predefined command. This way, VM-side code can initiate setup of *vm process \<-\> vchan \<-\> dom0 process* structure. As the range of dom0 commands will be predefined, there is no "arbitrary code execution" vulnerability here.

In Qubes Beta1, we have reimplemented interVM file copy using qrexec, which addresses the abovementioned disadvantages.

Note, the qrexec mechanism works over vchan, and vchan is a channel between VM and dom0 (not between two VMs). We could imagine vchan extension, in which instead of using facilities available for dom0 only (like *xc\_map\_foreign\_range*), the channel would be setup over granted pages, between two AppVMs. Reimplementing vchan this way is nontrivial. Also, it creates some security design questions; currently, everything is mediated via dom0, which has the ability to allow/deny communication, possibly asking user via dialog popups.

"Regular" file copy would be implemented as follows:

-   in srcVM, qvm-copy-to-vm utility
    -   stores the information on the files\_to\_be\_copied to *\~/.filecopyspool* directory
    -   tells *qrexec-agent* (by writing to its command fifo) to send "EXECUTE\_FILE\_COPY" command to qrexec-daemon
-   *qrexec-daemon* sees EXECUTE\_FILE\_COPY command, executes
     *qrexec\_client srcVM qfile-agent -l qfile-daemon*
-   qfile-agent inspects *\~/.filecopyspool*, sees the description about the file copy request. *qfile-agent* walks the directory tree, sends destination vmname, sends file metadata and data, then exits
-   qfile-daemon gets the first 32 characters from stdin (copy destination vmname), then executes (execve, really turn into new process)
     *qrexec\_client dstVM qfile-unpacker*
     At this point, two *qrexec\_client* processes running in dom0 just pass data between srcVM and dstVM. When the one connected to srcVM sees incoming EOF, it just closes input to the other qrexec\_client.

DVM copy would be implemented as follows:

-   in source\_VM, *qvm-open-in-dvm* utility
    -   stores the information on file\_to\_be\_edited in *\~/.dvmspool* directory
    -   tells *qrexec-agent* (by writing to qrexec-agent command fifo) to send "EXECUTE\_FILE\_COPY\_FOR\_DISPVM" command to *qrexec-daemon*
-   qrexec-daemon sees EXECUTE\_FILE\_COPY\_FOR\_DISPVM command, executes
     *qrexec\_client srcVM qfile-agent-dvm -l qfile-daemon-dvm*
-   *qfile-agent-dvm* inspects *\~/.dvmspool*, sees the description about file\_to\_be\_edited, sends data about it to its peer, closes stdout
-   *qfile-daemon-dvm* creates DispVM, then forks
     *qrexec\_client DVM dvm\_file\_editor*
     at this point, two qrexec\_client processes running in dom0 just pass data between srcVM and DispVM. *qfile-daemon-dvm* just waits for its child qrexec\_client process termination.
-   *dvm\_file\_editor* gets file contents (end of transfer signalled by EOF), spawns mime handler, if the file has changed, sends modified file to its stdout, closes stdout
-   the response from *dvm\_file\_editor* (terminated by EOF) is passed (via two qrexec\_client processes in dom0) to *qfile-agent-dvm*. When *qfile-daemon-dvm* sees its child qrexec\_client has exited (because of EOFs in both directions), it kills DVM.
-   *qfile-agent-dvm* retrieves response (terminated by EOF), if nonempty, it updates the edited file.

Note that *qfile-unpacker* must be coded securely, as it processes potentially untrusted data format. Particularly, we do not want to use external tar or cpio and be prone to all vulnerabilities in them; we want a simplified, small utility, that handles only directory/file/symlink file type, permissions, mtime/atime, and assume user/user ownership. In the current implementation, the code that actually parses the data from srcVM has ca 100 lines of code and executes chrooted to the destination directory.
