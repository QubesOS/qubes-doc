---
layout: doc
title: Fetchmail
redirect_to: https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/fetchmail.md
redirect_from:
- /doc/fetchmail/
- /en/doc/fetchmail/
- /doc/Fetchmail/
- /wiki/Fetchmail/
---

Fetchmail
=========

Fetchmail is standalone MRA (Mail Retrieval Agent) aka "IMAP/POP3 client". Its sole purpose is to fetch your messages and store it locally or feed to local MTA (Message Transfer Agent). It cannot "read" messages — for that, use a MUA like Thunderbird or [Mutt](/doc/mutt/).

Installation
------------

`dnf install fetchmail`

Configuration
-------------

Assuming you have more than one account (safe assumption these days), you need to spawn multiple fetchmail instances, one for each IMAP/POP3 server (though one instance can watch over several accounts on one server). The easiest way is to create template systemd unit and start it several times. Fedora does not supply any, so we have to write one anyway.

**NOTE:** this assumes you use [Postfix](/doc/postfix/) or Exim4 as your local MTA.

In TemplateVM create `/etc/systemd/system/fetchmail@.service`:

~~~
[Unit]
Description=Mail Retrieval Agent
After=network.target
Requires=postfix.service

[Service]
User=user
ExecStart=/bin/fetchmail -f /usr/local/etc/fetchmail/%I.rc -d 60 -i /usr/local/etc/fetchmail/.%I.fetchids --pidfile /usr/local/etc/fetchmail/.%I.pid
RestartSec=1
~~~

Alternatively, in Debian with Exim4:

~~~
[Unit]
Description=Mail Retrieval Agent
After=network.target
Requires=exim4.service

[Service]
User=user
ExecStart=/usr/bin/fetchmail -f /usr/local/etc/fetchmail/%I.rc -d 60 -i /usr/local/etc/fetchmail/.%I.fetchids --pidfile /usr/local/etc/fetchmail/.%I.pid
RestartSec=1
~~~

Then shutdown TemplateVM, start AppVM and create directory `/usr/local/etc/fetchmail`. In it, create one `.rc` file for each instance of fetchmail, ie. `personal1.rc` and `personal2.rc`. Sample configuration file:

~~~
set syslog
set no bouncemail
#set daemon 600

poll mailserver1.com proto imap
    no dns
    uidl
    tracepolls
user woju pass supersecret
    ssl
    sslproto "TLS1"
    sslcertfile "/etc/pki/ca-trust/extracted/openssl/ca-bundle.trust.crt"
    sslcertck
    mda "/usr/sbin/sendmail -i -f %F -- user"
    fetchall
    idle

# vim: ft=fetchmail
~~~

Then `chown -R user:user /usr/local/etc/fetchmail` and `chmod 600 /usr/local/etc/fetchmail/*.rc`. **This is important**, fetchmail will refuse to run with wrong permissions on its rc-file.

Next, add this to `/rw/config/rc.local`:

~~~
#!/bin/sh

for rc in /usr/local/etc/fetchmail/*.rc; do
        instance=${rc%.*}
        instance=${instance##*/}
        systemctl --no-block start fetchmail@${instance}
done
~~~

Make sure the folder '/rw/config/qubes-bind-dirs.d' exists.

~~~
sudo mkdir -p /rw/config/qubes-bind-dirs.d
~~~

Create the file '/rw/config/qubes-bind-dirs.d/50_user.conf' with root rights.

Now edit it to append the '/var/spool/mail/' directory to the binds variable.

~~~
binds+=( '/var/spool/mail' )
~~~

Now reboot your AppVM and you are done.
