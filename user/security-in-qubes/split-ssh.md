---
layout: doc
title: Split SSH
permalink: /doc/split-ssh/
redirect_from:

---

# Qubes Split SSH with KeePassXC

**Warning:** This guide is for setting up *KeePassXC*, not KeePassX or KeePass. See the [KeePassXC FAQ][KeePassXC FAQ].

These Qubes setup allows you to keep ssh private keys in a vault VM and the Client SSH VM to use them only after being authorized. This is done by using Qubes's qrexec framework to connect a local SSH Agent socket from an AppVM to the SSH Agent socket within the vault VM. 

## Prepare Your System
0. (Optional) Take a system snapshot before you start tuning your system or do any major installations. To perform a Qubes OS backup please read and follow this guide the [User Documentation][CreateBackup]

1. Fedora 32 has been used for this guide but is should also work with updated version of Fedora. Make sure your **Fedora Template VM** (Template: fedora-32) is up to date.

   `[user@fedora-32 ~]$ sudo dnf update && sudo dnf upgrade -y`

## Creating the Vault  AppVM

If you’ve installed Qubes OS using the default options, a few qubes including a vault AppVM has been created for you. Skip this part if you don't wish to create another vault.

1. Create a new vault AppVM based on your chosen template. Set networking to `(none)`.

   ![vault creation](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/72bd43ce6a17475c5e356bcd351b8b4ad86370a5.png)

## Generating an SSH key pair

1. Add KeepasXC to the Applications menu of the newly created AppVM for ease of access.

   ![vault adding keepass](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/optimized/1X/b98c57e05e304414567e87d694f4b7890b65531a_2_598x500.png)
   
2. Open the vaultVM Terminal and generate an SSH key pair. Skip this step if you already have your keys.

      ```shell_prompt
      user@vault-keepassxc:~$ ssh-keygen -t ed25519 -a 500 -f ~/.ssh/myssh_key
      Generating public/private ed25519 key pair.
      Created directory '/home/user/.ssh'.
      Enter passphrase (empty for no passphrase): 
      Enter same passphrase again: 
      Your identification has been saved in /home/user/.ssh/myssh_key.
      Your public key has been saved in /home/user/.ssh/myssh_key.pub.
      The key fingerprint is:
      SHA256:faJ3kBECVKMwNERj2t5ZVE2yz9YqsFGI3uE3vq7JeRI user@vault-keepassxc
      The key's randomart image is:
      +--[ED25519 256]--+
      |   +X.oo=.+o.    |
      |   + = + + +.    |
      |  . . o + +      |
      |   . o = + = .   |
      |    . + S B = .  |
      |        EB * .   |
      |        o.+ o    |
      |       ..+.+     |
      |        ==o      |
      +----[SHA256]-----+
      ```
    **-t**: type<br/>
    **-a**: num_trials<br/>
    **-f**: file<br/>
    
    Please note that the key fingerprint and the randomart image will differ.
    
    For more information about `ssh-keygen`, run `man ssh-keygen`.
    
## Setting up KeePassXC.

1. Deny auto updates since there is no network active.

   ![deny auto update](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/38d8cede2df66e68f2aea6f6f07605677d5a45bc.png)

2. Follow the wizard and adjust security settings.

   ![continue](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/0f8584bc907e7f18b44f1fc51233f2d45613e1c2.png)

3. Set password to your ssh key passphrase.

   ![setting passphrase](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/optimized/1X/21a2a38f54852126adefb4f6170b7e77b59863bf_2_594x500.png)

4. Go into "Advanced" and add your keys.  

   ![add keys](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/0f4a9b160ab40773c5341d6437acb6b7b4666e6d.png)

Remarks: You only need to add the private key (here myssh_key) but if you want to use it to simple backup all-in-one you can also add the public key (myssh_key.pub). 

5. Enable "SSH Agent Integration" within the Application Settings.

   ![enable ssh agent integration](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/optimized/1X/ad4700e7ed11682dfe9278d088af2f5381b0f286_2_594x500.png)

6. Restart KeePassXC and check the SSH Agent Integration status.

   ![checking](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/77103ff4f1088efa4664f2c4cedd6fcf819e5fbd.png)

7. Select your private key in the "SSH Agent" section. 

   ![select private key](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/optimized/1X/e24ed462d471d4b8a5bdb47be1278d246de7d208_2_537x500.png)

## Testing KeePassXC Setup

1. Close your KeePassXC database and run `ssh-add -L`. It should output `The agent has no identities.`

    ```shell_prompt
    [user@vault-keepassxc ~]$ ssh-add -L
    The agent has no identities.
    ```

2. Unlock your KeePassXC database and run `ssh-add -L` again. This time it should output your public key.

    ```shell_prompt
    [user@vault-keepassxc ~]$ ssh-add -L
    ssh-ed25519 <public key here> user@vault-keepassxc
    ```
## Setting Up VM Interconnection

1. Create a client SSH AppVM. This VM will be used to make the SSH connection to your remote machine.

   ![server-connector creation](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/e390f796135eb964c9c70dc962a23197d87defe7.png)

### In the Template VM to your Client SSH AppVM

1. Make sure `nmap-ncat` is installed.

    ```shell_prompt
    [user@vault-keepassxc ~]$ sudo dnf install nmap-ncat
    Fedora bla bla
    ```

2. Generate the file `qubes.SshAgent` in `/etc/qubes-rpc`

   - Open the file with e.g. `nano`

      ```shell_prompt
      [user@fedora-32] sudo nano /etc/qubes-rpc/qubes.SshAgent
      ```
      
   - Paste the following content:
  
      ```shell_prompt
      #!/bin/sh
      # Qubes App Split SSH Script

      # safeguard - Qubes notification bubble for each ssh request
      notify-send "[`qubesdb-read /name`] SSH agent access from: $QREXEC_REMOTE_DOMAIN"

      # SSH connection
      ncat -U $SSH_AUTH_SOCK
      ```
      
   - Save and exit.

     
3. Shutdown the template VM.

### In a `dom0` Terminal

1. Generate the file `qubes.SshAgent` in `/etc/qubes-rpc`

   - Open the file with your editor of choice (e.g. `nano`).

      ```shell_prompt
      [user@fedora-32] sudo nano /etc/qubes-rpc/qubes.SshAgent
      ```
      
   - If you want to explicitly allow only this connection, paste the following content:
  
      ```shell_prompt
      # explicitly allow only this connection
      server-connector vault-keepassxc ask
      ```
   - If you want to allow all VMs to connect, paste the following content:
      
      ```shell_prompt
      $anyvm $anyvm ask
      ```
   - Save and exit.

2. Close the terminal. **Do not shutdown `dom0`.**

### In a Client SSH AppVM terminal

1. Edit `/rw/config/rc.local`

   - Open the file with your editor of choice (e.g. `nano`).
   
      ```shell_prompt
      [user@server-connector ~]$ sudo nano /rw/config/rc.local
      ```
     
   - Add the following to the bottom of the file:
   
      ```shell_prompt
      # SPLIT SSH CONFIGURATION >>>
      # replace "vault-keepassxc" with your AppVM name which stores the ssh private key(s)
      SSH_VAULT_VM="vault-keepassxc"

      if [ "$SSH_VAULT_VM" != "" ]; then
        export SSH_SOCK=~user/.SSH_AGENT_$SSH_VAULT_VM
        rm -f "$SSH_SOCK"
       sudo -u user /bin/sh -c "umask 177 && ncat -k -l -U '$SSH_SOCK' -c 'qrexec-client-vm $SSH_VAULT_VM qubes.SshAgent' &"
      fi
      # <<< SPLIT SSH CONFIGURATION
      ```
      
   - Save and exit.

2. Edit `~/.bashrc`

   - Open the file with your editor of choice (e.g. `nano`).
   
      ```shell_prompt
      [user@server-connector ~]$ sudo nano ~/.bashrc
      ```

   - Add the following to the bottom of the file:
   
      ```shell_prompt
      # SPLIT SSH CONFIGURATION >>>
      # replace "vault-keepassxc" with your AppVM name which stores the ssh private key(s)
      SSH_VAULT_VM="vault-keepassxc"

      if [ "$SSH_VAULT_VM" != "" ]; then
          export SSH_AUTH_SOCK=~user/.SSH_AGENT_$SSH_VAULT_VM
      fi
      # <<< SPLIT SSH CONFIGURATION
      ```
      
   - Save and exit.
   
### Test your configuration
 
 1. Shutdown your vaultVM.
 
 2. Try fetching your identities on the Client SSH VM. 
 
     ```shell_prompt
     [user@server-connector ~]$ ssh-add -L
     ```
 3. Allow operation execution
 
    ![operation execution](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/a4c234f61064d16820a21e1ddaf305bf959735c1.png)
 
 Check if it returns `error fetching identities: communication with agent failed`
 
 4. Start your vaultVM and unlock your KeePassXC database.
 
5. Try fetching your identities on the Client SSH VM. 
 
    ```shell_prompt
    [user@server-connector ~]$ ssh-add -L
    ```
 
6. Allow operation execution
 
    ![operation execution](https://aws1.discourse-cdn.com/free1/uploads/qubes_os/original/1X/a4c234f61064d16820a21e1ddaf305bf959735c1.png)
 
Check if it returns `ssh-ed25519 <public key string>`

## (Optional) Backing Up the Configuration
### System Backup
Start a system backup as per the [User Documentation][CreateBackup].
### KeePassXC Database Backup
You can also only back up your \*.kdbx-file.

Depending on your threat model you can:
* Hide the \*.kdbx file by simply renaming the file extension (e.g. \*.zip)
* Add an additional security layer by adding a second encryption layer (e.g. VeraCrypt, \*.7z with password)
* Upload the \*.kdbx to an end-to-end-encrypted email box (e.g. Tutanota, ProtonMail)

Want more Qubes split magic?
Check this out: [Split-GPG:][Split-GPG]

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

Qubes Community: Phil (phl), deeplow, whoami
https://qubes-os.discourse.group/


[CreateBackup]:https://www.qubes-os.org/doc/backup-restore/#creating-a-backup
[KeePassXC]: https://keepassxc.org/project
[KeePassXCFedoraPackageSource]:https://src.fedoraproject.org/rpms/keepassxc
[KeePassXC FAQ]: https://keepassxc.org/docs
[Password]:https://xkcd.com/936
[PolicyFilesQubesOS]:[https://www.qubes-os.org/doc/qrexec/#policy-files]
[Split-GPG]:https://www.qubes-os.org/doc/split-gpg
