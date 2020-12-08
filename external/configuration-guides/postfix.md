---
layout: doc
title: Postfix
redirect_to: https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/postfix.md
redirect_from:
- /doc/postfix/
- /en/doc/postfix/
- /doc/Postfix/
- /wiki/Postfix/
---

Postfix
=======

Postfix is full featured MTA (Message Transfer Agent). Here we will configure it in smarthost mode as part of common [Mutt](/doc/mutt/)+Postfix+[Fetchmail](/doc/fetchmail/) stack.

Installation
------------

`dnf install postfix procmail make cyrus-sasl cyrus-sasl-plain`

Cyrus-sasl is installed to authenticate to remote servers. Procmail is not strictly necessary, but is useful to sort your incoming mail, for example to put each mailing list in its own directory. Make is also not necessary, but is used to keep Postfix lookup tables.

You should also check `alternatives` command, to see if it is the default `mta`. It probably is not. You may need to `dnf remove ssmtp` or something

Configuration
-------------

In TemplateVM open `/etc/aliases` and add line:

~~~
root: user
~~~

and run `newaliases`.

This is the only thing to do in TemplateVM, as MTA configuration is AppVM specific, so we will keep it in `/usr/local` (ie. `/rw/usrlocal`) in each AppVM.

Now shutdown TemplateVM, start AppVM. Create directory `/usr/local/etc/postfix` and copy `/etc/postfix/master.cf` and `/etc/postfix/postfix-files` there.

### Makefile

Postfix keeps its lookup tables in bdb hash databases. They need to be compiled from source files. Postfix admins like to keep track of them by means of `/usr/local/etc/postfix/Makefile`:

~~~
all: $(addsuffix .db,$(shell sed -n -e '/^[^#].*hash:\/etc\/postfix/s:.*/::p' main.cf))
    newaliases
clean:
    $(RM) *.db
.PHONY: all clean

%.db: %
    /usr/sbin/postmap hash:$<
~~~

### Postfix main configuration

`/usr/local/etc/postfix/main.cf` (`/etc/postfix` is intentional, don't correct it):

~~~
mydestination = $myhostname, $myhostname.$mydomain, $myhostname.localdomain, localhost, localhost.$mydomain, localhost.localdomain, $mydomain, localdomain
mynetworks_style = host

inet_protocols = ipv4

smtp_generic_maps = hash:/etc/postfix/generic
local_header_rewrite_clients =

smtp_sender_dependent_authentication = yes
sender_dependent_relayhost_maps = hash:/etc/postfix/sender_relay
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/saslpass
smtp_sasl_security_options =
smtp_tls_security_level = encrypt
smtp_sasl_mechanism_filter = plain, login
smtpd_relay_restrictions = permit_mynetworks,permit_sasl_authenticated,defer_unauth_destination
smtpd_sender_restrictions = check_sender_access hash:/etc/postfix/sender_access

home_mailbox = .maildir/
setgid_group = postdrop
mail_owner = postfix

html_directory = no
manpage_directory = /usr/share/man
queue_directory = /var/spool/postfix
readme_directory = no

mailbox_command = /usr/bin/procmail
sendmail_path = /usr/sbin/sendmail
newaliases_path = /usr/bin/newaliases
mailq_path = /usr/bin/mailq
alias_maps = hash:/etc/aliases
~~~

### Lookup tables

`/usr/local/etc/postfix/generic` (put there your primary address):

~~~
@localhost your.mail@example.com
~~~

`/usr/local/etc/postfix/sender_relay`. This is an important file. Put all your SMTP servers there. Pay attention to port (smtp/submission). Square brackets have their special meaning, they are almost certainly needed. For more info consult Postfix manual.

~~~
your.mail@exmaple.com         [mail.example.com]:submission
your.other@mail.com         [smtp.mail.com]:smtp
~~~

`/usr/local/etc/postfix/saslpass`. Here you put passwords to above mentioned servers. It depends on your provider if you need to put whole email as username or just the part before `@`.

~~~
[mail.example.com]:submission     your.mail:y0urP4ssw0rd
[smtp.mail.com]:smtp            your.other@mail.com:supers3cret
~~~

`/usr/local/etc/postfix/sender_access`. I use it to nullroute known spam domains. If you do not need it, comment respective line in `main.cf`.

~~~
spamdomain1.com       DISCARD
spamdomain2.com     DISCARD
~~~

Now run `make` in `/usr/local/etc/postfix`. It will hopefully compile four above mentioned lookup tables (`generic.db`, `sender_relay.db`, `saslpass.db` and `sender_access`).

### procmail

Don't start postfix or fetchmail yet, first create `/home/user/.procmailrc`:

~~~
MAILDIR = "${HOME}/.maildir"
ORGMAIL = "${MAILDIR}/"
DEFAULT = "${MAILDIR}/"

:0
* ^List-Id:.*qubes-users\.googlegroups\.com
list/qubes-users/

:0
* ^List-Id:.*qubes-devel\.googlegroups\.com
list/qubes-devel/
~~~

Run
---

Open `/rw/config/rc.local` and add those two lines (before fetchmail lines, if you have them):

~~~
#!/bin/sh

mount --bind /usr/local/etc/postfix /etc/postfix
systemctl --no-block start postfix
~~~

Make sure `/rw/config/rc.local` is executable (i.e., `chmod a+x /rw/config/rc.local`).  Reboot your AppVM and you are done.
