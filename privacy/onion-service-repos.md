---
layout: doc
title: Onion Service Repos
permalink: /doc/onion-service-repos/
redirect_from: /doc/hidden-service-repos/
---

Onion Service Repos
====================

Run the following commands in dom0 in order to use Qubes' Tor onion service
(aka "hidden service") repos for each type of VM.

**Note:** The `cat`s are optional, for confirmation only.

Dom0
----

    sudo sed -i 's/yum.qubes-os.org/yum.qubesos4rrrrz6n4.onion/' /etc/yum.repos.d/qubes-dom0.repo && cat /etc/yum.repos.d/qubes-dom0.repo
    sudo sed -i 's/yum.qubes-os.org/yum.qubesos4rrrrz6n4.onion/' /etc/yum.repos.d/qubes-templates.repo && cat /etc/yum.repos.d/qubes-templates.repo

Fedora
------

    qvm-run -a --nogui -p -u root $FedoraTemplateVM 'sed -i "s/yum.qubes-os.org/yum.qubesos4rrrrz6n4.onion/" /etc/yum.repos.d/qubes-r3.repo && cat /etc/yum.repos.d/qubes-r3.repo'

Debian and Whonix
-----------------

    qvm-run -a --nogui -p -u root $DebianTemplateVM 'sed -i "s/deb.qubes-os.org/deb.qubesos4rrrrz6n4.onion/" /etc/apt/sources.list.d/qubes-r3.list && cat /etc/apt/sources.list.d/qubes-r3.list'

