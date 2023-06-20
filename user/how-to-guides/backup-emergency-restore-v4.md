---
lang: en
layout: doc
permalink: /doc/backup-emergency-restore-v4/
redirect_from:
- /en/doc/backup-emergency-restore-v4/
- /doc/BackupEmergencyRestoreV4/
ref: 192
title: Emergency backup recovery (v4)
---

This page describes how to perform an emergency restore of a backup created on
Qubes R4.X (which uses backup format version 4).

The Qubes backup system is designed with emergency disaster recovery in mind. No
special Qubes-specific tools are required to access data backed up by Qubes. In
the event a Qubes system is unavailable, you can access your data on any
GNU/Linux system by following the instructions on this page.

**Important:** You may wish to store a copy of these instructions with your
Qubes backups. All Qubes documentation, including this page, is available in
plain text format in the [qubes-doc](https://github.com/QubesOS/qubes-doc) Git
repository.

## Required `scrypt` utility

In Qubes 4.X, backups are encrypted and integrity-protected with
[scrypt](https://www.tarsnap.com/scrypt.html). You will need a copy of this
utility in order to access your data.  Since `scrypt` is not pre-installed on
every GNU/Linux system, it is strongly recommended that you store a copy of it
with your backups. If your distribution has `scrypt` packaged (e.g., Debian),
you can install the package in the standard way using your distribution's
package manager. Otherwise, you'll need to obtain a compiled binary
(instructions below) or compile the program from source yourself. (Don't forget
to [verify signatures](/security/verifying-signatures) first!) Note that
versions of `scrypt` up to 1.2.0 (inclusive) do not support the `-P` option for
easier scripting, which means you'll need to enter the passphrase for each file
separately, instead of using `echo ... | scrypt`.

Here are instructions for obtaining a compiled `scrypt` binary. This example
uses an RPM-based system (Fedora), but the same general procedure should work on
any GNU/Linux system.

 1. If you're not on Qubes 4.X, [import and authenticate the Release 4 Signing
    Key](/security/verifying-signatures/#how-to-import-and-authenticate-release-signing-keys).

        [user@restore ~]$ sudo rpm --import qubes-release-4-signing-key.asc

 2. Download the `scrypt` RPM.

        [user@restore ~]$ dnf download scrypt

    Or, if that doesn't work:

        [user@restore ~]$ curl -O https://yum.qubes-os.org/r4.0/current/vm/fc28/rpm/scrypt-1.2.1-1.fc28.x86_64.rpm

 3. Verify the signature on the `scrypt` RPM.

        [user@restore ~]$ rpm -K scrypt-*.rpm
        scrypt-*.rpm: digests signatures OK

    The message `digests signatures OK` means that both the digest (i.e., the
    output of a hash function) and PGP signature verification were successful.

 4. Install `rpmdevtools`.

        [user@restore ~]$ sudo dnf install rpmdevtools

 5. Extract the `scrypt` binary from the RPM and make it conveniently
    available.

        [user@restore ~]$ rpmdev-extract scrypt-*.rpm
        [user@restore ~]$ alias scrypt="$PWD/scrypt-*/usr/bin/scrypt"

## Emergency recovery instructions

**Note:** In the following example, the backup file is both *encrypted* and
*compressed*.

 1. Untar the backup metadata from the main backup file.

        [user@restore ~]$ tar -i -xvf qubes-backup-2023-04-05T123456 \
            backup-header backup-header.hmac qubes.xml.000.enc
        backup-header
        backup-header.hmac
        qubes.xml.000.enc

 2. Set the backup passphrase environment variable. While this isn't strictly
    required, it will be handy later and will avoid saving the passphrase in the
    shell's history.

        [user@restore ~]$ read -r backup_pass

    Type in your passphrase (it will be visible on screen!) and press Enter.

 3. Verify the integrity of `backup-header` using `backup-header.hmac` (an
    encrypted *and integrity protected* version of `backup-header`).

        [user@restore ~]$ set +H
        [user@restore ~]$ echo "backup-header!$backup_pass" |\
            scrypt dec -P backup-header.hmac backup-header.verified && \
            diff -qs backup-header backup-header.verified
        Files backup-header and backup-header.verified are identical

    **Note:** If this command fails, it may be that the backup was tampered with
    or is in a different format. In the latter case, look inside `backup-header`
    at the `version` field. If it contains a value other than `version=4`, go to
    the instructions for that format version:
    - [Emergency Backup Recovery without Qubes (v2)](/doc/backup-emergency-restore-v2/)
    - [Emergency Backup Recovery without Qubes (v3)](/doc/backup-emergency-restore-v3/)

 4. Read `backup-header`.

        [user@restore ~]$ cat backup-header
        version=4
        encrypted=True
        compressed=True
        compression-filter=gzip
        hmac-algorithm=scrypt
        backup-id=20230405T123455-1234

 5. Set `backup_id` to the value in the last line of `backup-header`. (Note that
    there is a hyphen in `backup-id` in the file, whereas there is an underscore
    in `backup_id` in the variable you're setting.)

        [user@restore ~]$ backup_id=20230405T123455-1234

 6. Verify and decrypt, decompress, and extract the `qubes.xml` file.

        [user@restore ~]$ echo "$backup_id!qubes.xml.000!$backup_pass" |\
            scrypt dec -P qubes.xml.000.enc | gzip -d | tar -xv
        qubes.xml

    If this pipeline fails, it is likely that the backup is corrupted or has
    been tampered with.

    **Note:** If your backup was compressed with a program other than `gzip`,
    you must substitute the correct compression program in the command above.
    This information is contained in `backup-header` (see step 4). For example,
    if your backup is compressed with `bzip2`, use `bzip2 -d` instead of `gzip
    -d` in the command above. You might need to install a package of the same
    name (in this example, `bzip2`) through your distribution's package manager.

 7. Search inside of the `qubes.xml` file for the `backup-path` of the qube
    whose data you wish to restore. If you install the `xmlstarlet` package, the
    following command will convert `qubes.xml` to a friendlier listing for this
    purpose:

        [user@restore ~]$ xmlstarlet sel -T -t -m //domain \
            -v 'concat(.//property[@name="name"], " ", .//feature[@name="backup-path"])' \
            -n qubes.xml
        
        anon-whonix
        debian-11
        default-mgmt-dvm
        disp2345
        fedora-37
        fedora-37-dvm
        personal vm123/
        sys-firewall
        sys-net
        sys-usb
        sys-whonix
        untrusted
        vault vm321/
        whonix-gw-16
        whonix-ws-16
        whonix-ws-16-dvm
        work

    The example output above shows that the backup file includes a qube named
    `personal` and a qube named `vault`, with `backup-path` values of `vm123/`
    and `vm321/` respectively. (Every other listed qube was not selected to be
    included in the backup file.) Use the corresponding value to untar the
    necessary data files of the qube:

        [user@restore ~]$ tar -i -xvf qubes-backup-2023-04-05T123456 vm123/

 8. Verify and decrypt the backed up data, decompress it, and extract it.

        [user@restore ~]$ find vm123/ -name 'private.img.*.enc' | sort -V | while read f_enc; do \
            f_dec=${f_enc%.enc}; \
            echo "$backup_id!$f_dec!$backup_pass" | scrypt dec -P $f_enc || break; \
            done | gzip -d | tar -xv
        vm123/private.img

    If this pipeline fails, it is likely that the backup is corrupted or has
    been tampered with.

    Also see the note in step 6 about substituting a different compression
    program for `gzip`.

 9. Mount `private.img` and access your data.

        [user@restore ~]$ sudo mkdir /mnt/img
        [user@restore ~]$ sudo mount -o loop vm123/private.img /mnt/img/
        [user@restore ~]$ cat /mnt/img/home/user/your_data.txt
        This data has been successfully recovered!

Success! If you wish to recover data from more than one qube in your backup,
simply repeat steps 7, 8, and 9 for each additional qube.
