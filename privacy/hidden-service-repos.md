---
layout: doc
title: Hidden Service Repos
permalink: /doc/hidden-service-repos/
---

Hidden Service Repos
====================

Run the following commands in dom0 in order to use Qubes' Tor hidden service
repos for each type of VM.

**Note:** The `cat`s are optional, for confirmation only.

Dom0
----

    sudo sed -i 's/yum.qubes-os.org/qubes-yum.kkkkkkkkkk63ava6.onion/' /etc/yum.repos.d/qubes-dom0.repo && cat /etc/yum.repos.d/qubes-dom0.repo
    sudo sed -i 's/yum.qubes-os.org/qubes-yum.kkkkkkkkkk63ava6.onion/' /etc/yum.repos.d/qubes-templates.repo && cat /etc/yum.repos.d/qubes-templates.repo

Fedora
------

    qvm-run -a --nogui -p -u root $FedoraTemplateVM 'sed -i "s/yum.qubes-os.org/qubes-yum.kkkkkkkkkk63ava6.onion/" /etc/yum.repos.d/qubes-r3.repo && cat /etc/yum.repos.d/qubes-r3.repo'

Debian and Whonix
-----------------

    qvm-run -a --nogui -p -u root $DebianTemplateVM 'sed -i "s/deb.qubes-os.org/qubes-deb.kkkkkkkkkk63ava6.onion/" /etc/apt/sources.list.d/qubes-r3.list && cat /etc/apt/sources.list.d/qubes-r3.list'

