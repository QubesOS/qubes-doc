# How to connect to Microsoft Exchange with Qubes OS

## Introduction
This Howto describes how you can connect to your Exchange Server with Qubes OS.
It is based on using a Exchange-to-IMAP-Gateway which is named Davmail.

The howto covers:

- Installation/Configuration of Davmail
- Configuration to use Thunderbird
- Configuration to use neomutt

the following VMs will be mentioned in this howto:

- t-mail = TemplateVM
- my-vault = ApppVM which is used for SplitGPG
- my-workmail = AppVM

TODO:

- Howto use SplitGPG with neomutt
- Howto work with attachments (PDF/Pictures) and HTML mails in neomutt

## Davmail

install required packages for Davmail

`sudo dnf install java-9-openjdk`

Download Davmail in an AppVM and qvm-copy-to-vm it over to the mail template vm
in the AppVM which has internet access:

`wget https://kent.dl.sourceforge.net/project/davmail/davmail/4.8.3/davmail-linux-x86_64-4.8.3-2554.tgz`
`qvm-copy-to-vm t-mail davmail-linux-x86_64-4.8.3-2554.tgz`  

In the TemplateVM:

`sudo tar -xvzf ~/QubesIncoming/<AppVM>/davmail.*.tgz -C /opt`
`sudo mv /opt/davmail* /opt/davmail`

tell your template VM where to find the GPG Vault VM 

`export QUBES_GPG_DOMAIN=my-vault`

test access via SplitGPG (this command should list your secret-keys in the Vault-AppVM)

`qubes-gpg-client -K` 


Shutdown TemplateVM and create a new AppVM based on the TemplateVM
in dom0

`qvm-shutdown --wait t-mail`
`qvm-create --template t-mail --label blue my-workmail`

Open Qubes Setting for the new AppVM and increase storage capacity
Private storage max. size: 20480 MiB

Start AppVM and continue configuration there

`qvm-run --auto my-workmail gnome-terminal`

Start davmail

`/opt/davmail/davmail.sh &`

- Main Tab: Echange Protocol: Auto
- Main Tab: OWA (Exchange) URL: https://owa.domain.com/owa/
- Main Tab: [ ] Local POP port
- Advanced Tab: Default windows domain: <YOUR-DOMAIN>
- Advanced Tab: [x] Disable Update Check

tell your AppVM VM where to find the GPG Vault VM 

`echo "export QUBES_GPG_DOMAIN=my-vault" >> /home/user/.bashrc`

allow TemplateVM to acces SplitGPG Vault-AppVM
in dom0

`echo "my-workmail my-vault allow" >> /etc/qubes-rpc/policy/qubes.Gpg`

Test SpliGPG in the AppVM
Close and restart Terminal, so that the variable QUBES_GPG_DOMAIN will be set
Check if connection via SplitGPG works

`qubes-gpg-client --list-secret-keys`


## Setting up Thunderbird with Davmail
Start Thunderbird in the AppVM

`thunderbird &`

- Create new account (use existing mail)
- choose manual config
- IMAP localhost 1143 Autodetect Autodetect
- SMTP localhost 1025 Autodetect Autodetect
- Username: <YOUR-USERNAME>
- Click on Re-Test and accept any certificate warning
- (Checking the fingerprints!)
- Click on Re-Test, then Done
- Warning about unencrypted transfer from localhost
- [x] I understand the risks


## Setting up neomutt and offlineimap with Davmail
See also: https://hobo.house/2015/09/09/take-control-of-your-email-with-mutt-offlineimap-notmuch/ assuming that you have installed and configured Davmail (see above)

### Install packages in the TemplateVM
install neomutt and offlineimap in the Template VM
dom0:

`qvm-run --auto t-mail gnome-terminal`

in the Template VM:
```
sudo dnf install dnf-plugins-core
sudo dnf copr enable flatcap/neomutt
sudo dnf install neomutt dialog offlineimap git notmuch
```
additional tools for a good neomutt experience

`sudo dnf -y install w3m qutebrowser mupdf`
`shutdown -h now`

restart AppVM if it was running before and you installed new packages in the Template VM
dom0:

`qvm-shutdown --wait --quiet my-workmail`
`qvm-run --auto my-workmail gnome-terminal`

Start & configure davmail (see above)

`/opt/davmail/davmail.sh &`

### Setting up neomutt
Clone mutt-wizard

`git clone https://github.com/LukeSmithxyz/mutt-wizard.git ~/.config/mutt`

Launch mutt-wizard and choose add new account

`.config/mutt/mutt-wizard.sh`

- 1 Add an email account
- start with adding something like user@qubes when asked for a GPG key
- we will manually overwrite the config-file
- fill out all entries, it's Ok if the last steps fails
- verify if the account has been created:
- 0 List all email accounts configured
- 6 Exit this wizard

Fix the configuration of offlineimap
the configuration which has been created by mutt-wizard has to be changed in order to work with Davmail
(Offlineimap will connect to davmail (localhost) and download emails)

Create directory where offlineimap will store its mail

`mkdir ~/.mail`

Create a basic configuration file
Change YOUR-USERNAME and YOUR-PASSWORD to your settings ;-)

`nano ~/.offlineimaprc`

Paste (overwrite the existing settings) the following lines into this file
```
[general]
accounts = work
starttls = no
ssl = no
sslcacertfile = /etc/ssl/certs/ca-certificates.crt

[Account work]
localrepository = work-local
remoterepository = work-remote

[Repository work-remote]
type = IMAP
remoteuser = YOUR-USERNAME
sslcacerfile = /etc/ssl/cets/ca-certificates.crt
remotepass = YOUR-PASSWORD
remotehost = localhost
remoteport = 1143
sslcacertfile = /etc/ssl/certs/ca-certificates.crt
ssl=no

[Repository work-local]
type = Maildir
localfolders = ~/.mail/work
```

Create a link to the certfiles
you could also put the correct path to the certfiles into .offlineimaprc but we're using the default paths which are also configures via mutt-wizard

`cd /etc/ssl/certs/`
`sudo ln -s ca-bundle.trust.crt ca-certificates.crt`  

Check if offlineimap connects to your Exchange Server and downloads email
Run offlineimap once (-o) and only for the Inbox folder (to see if it is working)

`offlineimap -f INBOX,Sent,Drafts -o`

if some mails has been synchronized, you can abort (Ctrl+C)
continue with mutt-wizard:

`.config/mutt/mutt-wizard.sh` 

- 2 Auto-detect mailboxes for an account
- 6 Exit this wizard

Launch neomutt

`neomutt`

### Configure notmuch search
See also: https://notmuchmail.org/

configure notmuch
`notmuch setup`

initial run

`notmuch new`


--- offtopic ---

Download and import an own Root CA-certificate

`sudo cp vsrv-mail-3.pem /etc/pki/ca-trust/source`
`sudo update-ca-trust`

