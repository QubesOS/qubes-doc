---
layout: wiki
title: Mutt
permalink: /wiki/Mutt/
---

Mutt
====

Mutt is a fast, standards-compliant, efficient MUA (Mail User Agent). In some areas it works better than Thunderbird+Enigmail, and is certainly faster and more responsive.

Mutt lacks true MTA (Message Transfer Agent aka "SMTP client") and MRA (Mail Retrieval Agent aka "IMAP/POP3 client"), thus there are some provisions built-in. In principle it is only mail reader and composer. You may install true MTA such as [Postfix](/wiki/Postfix) or Exim and MRA such as [Fetchmail](/wiki/Fetchmail).

Installation
------------

`yum install mutt`

Configuration
-------------

Mutt generally works out of the box. This configuration guide discusses only Qubes-specific setup. In this example we will have one TemplateVM and several AppVMs. It also takes advantage of [SplitGPG?](/wiki/SplitGPG), which is assumed to be already working.

**NOTE:** this requires `qubes-gpg-split >= 2.0.9`. 2.0.8 and earlier contains bug which causes this setup to hang in specific situations and does not allow to list keys.

First, paste this to `/etc/Muttrc.local` in TemplateVM:

``` {.wiki}
# specify your key or override in ~/.mutt/muttrc in AppVM
set pgp_sign_as="0xDEADBEEF"

set pgp_use_gpg_agent = no

# this needs qubes-gpg-split >= 2.0.8; 2.0.7 end earlier has had a deadlock on this
set pgp_decode_command="qubes-gpg-client-wrapper --status-fd=2 --batch %f"
#set pgp_decode_command="gpg --status-fd=2 %?p?--passphrase-fd=0? --no-verbose --quiet --batch --output - %f"

set pgp_decrypt_command="$pgp_decode_command"

set pgp_verify_command="qubes-gpg-client-wrapper --status-fd=2 --no-verbose --quiet --batch --output - --verify %s %f"

set pgp_sign_command="qubes-gpg-client-wrapper --batch --armor --detach-sign --textmode %?a?-u %a? %f"
set pgp_clearsign_command="qubes-gpg-client-wrapper --batch --armor --textmode --clearsign %?a?-u %a? %f"

# I found no option to add Charset armor header when it is UTF-8, since this is
# default (as specified in RFC4880). This is needed to workaround bug in
# Enigmail, which ignores RFC and without this header Thunderbird interprets
# plaintext as us-ascii. See http://sourceforge.net/p/enigmail/bugs/38/.
set pgp_encrypt_only_command="pgpewrap qubes-gpg-client-wrapper --batch --textmode --armor --always-trust %?a?--encrypt-to %a? --encrypt -- -r %r -- %f | sed -e '2iCharset: UTF-8'"
set pgp_encrypt_sign_command="pgpewrap qubes-gpg-client-wrapper --batch --textmode --armor --always-trust %?a?--encrypt-to %a? --encrypt --sign %?a?-u %a? -- -r %r -- %f | sed -e '2iCharset: UTF-8'"

# we need to import both into vault and locally wrt $pgp_verify_command
set pgp_import_command="qubes-gpg-import-key %f; gpg --no-verbose --import %f"

# those are unsupported by split-gpg
set pgp_export_command="gpg --no-verbose --export --armor %r"
set pgp_verify_key_command="gpg --no-verbose --batch --fingerprint --check-sigs %r"

# read in the public key ring
set pgp_list_pubring_command="qubes-gpg-client-wrapper --no-verbose --batch --quiet --with-colons --list-keys %r"

# read in the secret key ring
set pgp_list_secring_command="qubes-gpg-client-wrapper --no-verbose --batch --quiet --with-colons --list-secret-keys %r"

# this set the number of seconds to keep in memory the passpharse used to encrypt/sign
# the more the less secure it will be
set pgp_timeout=600

# it's a regexp used against the GPG output: if it matches some line of the output
# then mutt considers the message a good signed one (ignoring the GPG exit code)
#set pgp_good_sign="^gpg: Good signature from"
set pgp_good_sign="^\\[GNUPG:\\] GOODSIG"

# mutt uses by default PGP/GPG to sign/encrypt messages
# if you want to use S-mime instead set the smime_is_default variable to yes

# automatically sign all outcoming messages
set crypt_autosign=yes
# sign only replies to signed messages
#set crypt_replysign

# automatically encrypt outcoming messages
#set crypt_autoencrypt=yes
# encrypt only replies to signed messages
set crypt_replyencrypt=yes
# encrypt and sign replies to encrypted messages
set crypt_replysignencrypted=yes

# automatically verify the sign of a message when opened
set crypt_verify_sig=yes

send-hook "~A" set pgp_autoinline=no crypt_autoencrypt=no
send-hook "~t @invisiblethingslab\.com" set crypt_autoencrypt=yes

# vim:ft=muttrc
```

Then shutdown your TemplateVM. Next open your AppVM, create file `/home/user/.mutt/muttrc` and adjust for your needs:

``` {.wiki}
#
# accounts
#
set from = "Wojciech Zygmunt Porczyk <woju@invisiblethingslab.com>"
alternates '^woju@invisiblethingslab\.com$'
alternates '^wojciech@porczyk\.eu$'

#
# crypto
#
set pgp_sign_as = "0xDEADBEEF"
send-hook "~t @my\.family\.com" set crypt_autoencrypt=no

#
# lists
#

# google groups
lists .*@googlegroups\.com

subscribe (qubes-(users|devel)|othergroup)@googlegroups\.com
fcc-save-hook qubes-users@googlegroups\.com =list/qubes-users/
fcc-save-hook qubes-devel@googlegroups\.com =list/qubes-devel/
fcc-save-hook othergroup@googlegroups\.com =list/othergroup/
```

You may also create `/home/user/.signature`:

``` {.wiki}
regards,
Wojciech Porczyk
```
