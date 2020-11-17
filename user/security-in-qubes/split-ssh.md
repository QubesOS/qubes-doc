---
layout: doc
title: Split SSH
permalink: /doc/split-ssh/
redirect_from:

---

# Qubes Split SSH

This Qubes setup allows you to keep SSH private keys in a vault VM (`vault`) and SSH Client VM (`ssh-client`) to use them only after being authorized. This is done by using Qubes's [qrexec][qrexec] framework to connect a local SSH Agent socket from an AppVM to the SSH Agent socket within the vault VM. 

## Overview

1. Make sure the TemplateVM you plan to use is up to date and `nmap` and `ncat` is installed.
2. Create `vault` and `ssh-client` AppVMs.
3. Create an ssh key in your `vault` AppVM and set up automatic key adding prompt.
4. Set up VM interconnection
5. (Strongly Encouraged) Create a KeePassXC Database and set up SSH Agent Integration in KeePassXC.


## Prepare Your System
0. (Optional) Take a system snapshot before you start tuning your system or do any major installations. To perform a Qubes OS backup please read and follow this guide in the [User Documentation][CreateBackup].

1. Make sure the TemplateVM you plan to use is [up to date][update].

   For Fedora templates:<br/>
   ```
   [user@fedora-32 ~]$ sudo dnf update && sudo dnf upgrade -y
   ```
   
   For Debian templates:<br/>
   ```
   user@debian-10:~$ sudo apt-get update && sudo apt-get upgrade
   ```
   
2. Make sure `nmap` and `ncat` is installed in your TemplateVM

   For Fedora templates:<br/>
   ```
   [user@fedora-32 ~]$ sudo dnf install nmap-ncat
   ```

   For Debian templates:<br/>
   ```
   user@debian-10:~$ sudo apt-get install nmap ncat
   ```
   
3. If you *don't* plan to use KeePassXC, install `ssh-askpass`.

   For Fedora templates:<br/>
   ```
   [user@fedora-32 ~]$ sudo dnf install openssh-askpass
   ```

   For Debian templates:<br/>
   ```
   user@debian-10:~$ sudo apt-get install ssh-askpass
   ```

## [Creating AppVMs][appvm create]

If you’ve installed Qubes OS using the default options, a few qubes including a vault AppVM has been created for you. Skip the first step if you don't wish to create another vault.

1. Create a new vault AppVM (`vault`) based on your chosen template. Set networking to `(none)`.

   ![vault creation](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/80fad13c2d72b4f6ac4c03cd30d15ebd2c08a927.png)
   
2. Create a SSH Client AppVM (`ssh-client`). This VM will be used to make the SSH connection to your remote machine.

   ![ssh-client creation](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/ff7c5d239b53906b8d1396381810b291d4364900.png)

## Setting up SSH

Perform the next steps in a vault VM terminal.

1. Generate an SSH key pair. Skip this step if you already have your keys.

      ```shell_prompt
      [user@vault ~]$ ssh-keygen -t ed25519 -a 500
      Generating public/private ed25519 key pair.
      Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
      Created directory '/home/user/.ssh'.
      Enter passphrase (empty for no passphrase): 
      Enter same passphrase again: 
      Your identification has been saved in /home/user/.ssh/id_ed25519
      Your public key has been saved in /home/user/.ssh/id_ed25519.pub
      The key fingerprint is:
      SHA256:DBxSxZcp16d1NSVSid3m8HRipUDM2INghQ4Sx3jPEDo user@vault
      The key's randomart image is:
      +--[ED25519 256]--+
      |    o==+++.@++o=*|
      |    o==o+ B BoOoB|
      |    Eoo* +   *.O.|
      |     . o+   .   o|
      |        S        |
      |                 |
      |                 |
      |                 |
      |                 |
      +----[SHA256]-----+
    ```
    **-t**: type<br/>
    **-a**: num_trials<br/>
    
    Please note that the key fingerprint and the randomart image will differ.
    
    For more information about `ssh-keygen`, run `man ssh-keygen`.
    
**Notice:** You can skip the following steps if you plan on using KeePassXC.  

2. Make a new directory `~/.config/autostart`

3. Create the file `ssh-add.desktop` in `~/.config/autostart`

      - Open the file with e.g. `nano`

        ```shell_prompt
        [user@fedora-32 ~]$ nano ~/.config/autostart/ssh-add.desktop
        ```

      - Paste the following contents:

        ```shell_prompt
        [Desktop Entry]
        Name=ssh-add
        Exec=ssh-add
        Type=Application
        ```
        
      - Save and exit.
      
      **Note:** If you've specified a custom name for your key using *-f*, you should adjust `Exec=ssh-add` to `Exec=ssh-add <path-to-your-key-file>`.

With this configuration you'll be prompted for a password the first time you start your vault VM to  be able to make use of your SSH key. 

## Setting Up VM Interconnection

### In the TemplateVM to your vault VM:

1. Create the file `qubes.SshAgent` in `/etc/qubes-rpc`

   - Open the file with e.g. `nano`

     ```shell_prompt
     [user@fedora-32 ~]$ sudo nano /etc/qubes-rpc/qubes.SshAgent
     ```

   - Paste the following contents:

     ```shell_prompt
     #!/bin/sh
     # Qubes App Split SSH Script
     
     # safeguard - Qubes notification bubble for each ssh request
     notify-send "[`qubesdb-read /name`] SSH agent access from: $QREXEC_REMOTE_DOMAIN"
     
     # SSH connection
     ncat -U $SSH_AUTH_SOCK
     ```

   - Save and exit.

2. Shutdown the template VM.

### In `dom0`:

1. Create the file `qubes.SshAgent` in `/etc/qubes-rpc`

   - Open the file with your editor of choice (e.g. `nano`).

     ```shell_prompt
     [user@fedora-32 ~]$ sudo nano /etc/qubes-rpc/qubes.SshAgent
     ```

   - If you want to explicitly allow only this connection, add the following line:

     ```shell_prompt
     ssh-client vault ask
     ```

   - If you want to allow all VMs to connect, add the following line:

     ```shell_prompt
     @anyvm @anyvm ask
     ```

   - If you want the input field to be "prefilled" by your `vault` VM, append `default_target=vault` so it looks like for example:

     ```shell_prompt
     @anyvm @anyvm ask,default_target=vault
     ```

   - Save and exit.

2. Close the terminal. **Do not shutdown `dom0`.**

### In a Client SSH AppVM terminal

1. Edit `/rw/config/rc.local`

   - Open the file with your editor of choice (e.g. `nano`).

     ```shell_prompt
     [user@ssh-client ~]$ sudo nano /rw/config/rc.local
     ```

   - Add the following to the bottom of the file:

     ```shell_prompt
     # SPLIT SSH CONFIGURATION >>>
     # replace "vault" with your AppVM name which stores the ssh private key(s)
     SSH_VAULT_VM="vault"
     
     if [ "$SSH_VAULT_VM" != "" ]; then
       export SSH_SOCK="/home/user/.SSH_AGENT_$SSH_VAULT_VM"
       rm -f "$SSH_SOCK"
       sudo -u user /bin/sh -c "umask 177 && ncat -k -l -U '$SSH_SOCK' -c 'qrexec-client-vm $SSH_VAULT_VM qubes.SshAgent' &"
     fi
     # <<< SPLIT SSH CONFIGURATION
     ```

   - Save and exit.

2. Edit `~/.bashrc`

   - Open the file with your editor of choice (e.g. `nano`).

     ```shell_prompt
     [user@ssh-client ~]$ nano ~/.bashrc
     ```

   - Add the following to the bottom of the file:

     ```shell_prompt
     # SPLIT SSH CONFIGURATION >>>
     # replace "vault" with your AppVM name which stores the ssh private key(s)
     SSH_VAULT_VM="vault"
     
     if [ "$SSH_VAULT_VM" != "" ]; then
         export SSH_AUTH_SOCK="/home/user/.SSH_AGENT_$SSH_VAULT_VM"
     fi
     # <<< SPLIT SSH CONFIGURATION
     ```

   - Save and exit.

## Using [KeePassXC][KeePassXC]

**Warning:** This part is for setting up *KeePassXC*, not KeePassX or KeePass. See the [KeePassXC FAQ][KeePassXC FAQ].

0. KeePassXC should be installed by default in both Fedora and Debian TemplateVMs. If this changes in the future and you find that it isn't, it can be installed with:
   
   For Fedora templates:<br/>
   ```shell_prompt
   [user@fedora-32 ~]$ sudo dnf install keepassxc
   ```
   For Debian templates:<br/>
   ```shell_prompt
   user@vault-deb:~$ sudo apt-get install keepassxc
   ```
   
   If you have another template check the [KeePassXC download page][KeePassXC download page] for instructions.

1. Add KeepasXC to the Applications menu of the newly created AppVM for ease of access.

   ![vault adding keepass](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/optimized/1X/e20e988e356ea63feda6760dca6a88fcd2a650c6_2_602x500.png)

**Note:** Since the vault VM has no internet connection, you can safely deny automatic updates.

2. Create a new database.

   ![create database](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/a25e16fca7d5a394e9a9acdc017c9a02f7e6f4f4.png)

3. Enter a name for your database and continue.

   ![naming screen](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/0925cd8e469b6194f80b1e46e51d7f137a01dd74.png)

4. Adjust the encryption settings. Check the [KeePassXC User Guide][KeePassXC User Guide] for more information about these settings.

   ![encryption settings](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/optimized/1X/8537b07f453a0950d72cb51b9b5339e0f7bfc3c4_2_690x472.png)
   
5. Enter a password for your database. Take your time make a secure but also rememberable password. ([hint][Hint])

   ![password screen](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/413a9bbe68395ae07d1e2989735c9af53409071f.png)

6. Add a new entry.

   ![adding new entry](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/a5a6c74aac781f95db2909ce43058971e08e5407.png)
   
7. Set password to your SSH key passphrase.

   ![enter passphrase](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/881340d19c2e78e10374555a1a8867040b713cd2.png)
   
8. Go into the Advanced section and add your keys.

   ![adding keys](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/ff4a1197826ee69740251dbf8204d90b6cf4c6c8.png)

   **Note:** You only need to add the private key (`id_25519` here) but if you want to be able to simply back up both your private and public key (myssh_key.pub) by backing up your KeePassXC database (\*.kdbx file) you can add that too.

9. Enable "SSH Agent Integration" within the Application Settings.

   ![enable ssh agent integration](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/optimized/1X/29dba9a7d44729cd8dce261cfecbbb63db3f4a70_2_594x500.png)
   
10. Restart KeePassXC

11. Check the SSH Agent Integration status.

   ![check integration status](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/2ef14b195947d2190306b500298379458d6194da.png)

12. Select your private key in the "SSH Agent" section.

   ![select private key](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/optimized/1X/0d19ae6f3545a154823a8b3f8c89d52f6e0d6b68_2_594x500.png)

### Testing the KeePassXC Setup

1. Close your KeePassXC database and run `ssh-add -L`. It should return `The agent has no identities.`

    ```shell_prompt
    [user@vault ~]$ ssh-add -L
    The agent has no identities.
    ```

2. Unlock your KeePassXC database and run `ssh-add -L` again. This time it should return your public key.

    ```shell_prompt
    [user@vault ~]$ ssh-add -L
    ssh-ed25519 <public key string> user@vault-keepassxc
    ```

## Test Your Configuration

1. Shutdown your vaultVM.

2. Try fetching your identities on the SSH Client VM. 

    ```shell_prompt
    [user@ssh-client ~]$ ssh-add -L
    ```

3. Allow operation execution

    ![operation execution](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/a4c234f61064d16820a21e1ddaf305bf959735c1.png)

Check if it returns `error fetching identities: communication with agent failed`

4. Start your vaultVM and unlock your KeePassXC database.

5. Try fetching your identities on the SSH Client VM. 

   ```shell_prompt
   [user@ssh-client ~]$ ssh-add -L
   ```

6. Allow operation execution

   ![operation execution](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/a4c234f61064d16820a21e1ddaf305bf959735c1.png)

Check if it returns `ssh-ed25519 <public key string>`

## (Optional) Backing Up the Configuration
### System Backup
Start a system backup as per the [User Documentation][CreateBackup].
### KeePassXC Database Backup
You can also only back up your \*.kdbx file.

Depending on your threat model you can:
* Hide the \*.kdbx file by simply renaming the file extension (e.g. \*.zip)
* Add an additional security layer by adding a second encryption layer (e.g. VeraCrypt, \*.7z with password)
* Upload the \*.kdbx to an end-to-end-encrypted email box (e.g. Tutanota, ProtonMail)

Want more Qubes split magic?
Check out [Split-GPG:][Split-GPG].

-------------------------------

This guide has been inspired by:

Qubes Split SSH (Github: Jason Hennessey - henn)
https://github.com/henn/qubes-app-split-ssh

Using split ssh in QubesOS 4.0 (Kushal Das)
https://kushaldas.in/posts/using-split-ssh-in-qubesos-4-0.html

Using Split-SSH in Qubes 4 (Denis Zanin)
https://deniszanin.com/using-split-ssh-gpg-in-qubes-os/

R.I.S.K.S.
https://19hundreds.github.io/risks-workflow/ssh-split-setup

Qubes Community: Phil (phl), deeplow, whoami, santorihelix
https://qubes-os.discourse.group/


[CreateBackup]:https://www.qubes-os.org/doc/backup-restore/#creating-a-backup
[KeePassXC]: https://keepassxc.org/project
[KeePassXCFedoraPackageSource]:https://src.fedoraproject.org/rpms/keepassxc
[KeePassXC download page]: https://keepassxc.org/download/
[KeePassXC FAQ]: https://keepassxc.org/docs
[Hint]:https://xkcd.com/936
[PolicyFilesQubesOS]:https://www.qubes-os.org/doc/qrexec/#policy-files
[Split-GPG]:https://www.qubes-os.org/doc/split-gpg

[qrexec]: https://www.qubes-os.org/doc/qrexec/
[update]: https://www.qubes-os.org/doc/software-update-domu/#updating-software-in-templatevms
[appvm create]: https://www.qubes-os.org/doc/getting-started/#adding-removing-and-listing-qubes
[KeePassXC User Guide]: https://keepassxc.org/docs/KeePassXC_UserGuide.html#_database_settings
