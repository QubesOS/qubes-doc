---
layout: doc
title: Removing TemplateVM Packages
permalink: /doc/removing-template-vm-packages/
redirect_from:
- /doc/removing-thunderbird-from-template-vm/
---

# Removing Template VM Packages
When removing any packages from a default TemplateVM, be sure to check what's being autoremoved by apt or dnf. Some applications, for instance Thunderbird, when being removed, apt and dnf will attempt to autoremove many packages required by qubes for the template to function correctly under qubes.

As an example see the output of the following:
```
sudo apt remove thunderbird
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  debugedit libjs-sphinxdoc libjs-underscore librpm3 librpmbuild3 librpmio3
  librpmsign3 libsqlite0 linux-headers-4.9.0-6-amd64
  linux-headers-4.9.0-6-common linux-image-4.9.0-6-amd64 python-backports-abc
  python-cffi-backend python-concurrent.futures python-croniter
  python-cryptography python-dateutil python-enum34 python-idna
  python-iniparse python-ipaddress python-jinja2 python-libxml2 python-lzma
  python-markupsafe python-msgpack python-openssl python-pyasn1 python-pycurl
  python-requests python-rpm python-singledispatch python-six python-sqlite
  python-sqlitecachec python-tornado python-tz python-urlgrabber
  python-urllib3 python-xpyb python-yaml qubes-core-agent-dom0-updates
  qubes-core-agent-passwordless-root qubes-gpg-split qubes-img-converter
  qubes-input-proxy-sender qubes-mgmt-salt-vm-connector qubes-pdf-converter
  qubes-usb-proxy rpm rpm-common rpm2cpio salt-common salt-ssh usbutils yum
  yum-utils
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  icedove lightning qubes-thunderbird qubes-vm-recommended thunderbird
0 upgraded, 0 newly installed, 5 to remove and 0 not upgraded.
After this operation, 151 MB disk space will be freed.
Do you want to continue? [Y/n]
```

Note all of the qubes packages are tracked as dependancies that will no longer be required. With apt continuing will only remove the 5 packages listed, which is ok. If, however you also run ``apt autoremove`` the other qubes packages necessary for TemplateVMs will be removed.

If you'd still like to remove one of these applications without breaking your TemplateVM you have a couple different options. 

## Removing Without Autoremove

### Debian
 1. Run ``apt remove package-name`` noting the packages "no longer required"
 1. If the list of "no longer required" packages includes anything beginning with ``qubes-`` or ``salt-`` make a note to yourself to never run ``apt autoremove`` on this TemplateVM

**Recommended but optional:** Use apt-mark to make autoremove safe again. ``apt mark-manual package-name package-name`` 

Replace package-names with actual ``qubes-*`` and ``salt-*`` packages you'd like to retain. 

For example: 
```sudo apt-mark manual qubes-core-agent-dom0-updates qubes-core-agent-passwordless-root qubes-gpg-split qubes-img-converter qubes-input-proxy-sender qubes-mgmt-salt-vm-connector qubes-pdf-converter salt-common salt-ssh qubes-usb-proxy```

``apt autoremove`` should now be safe to use.
### Fedora
 1. Run ``dnf remove --noautoremove package-name``

 
 ## Recovering A TemplateVM which you've already removed thunderbird and qubes-* packages
If you've already removed packages, autoremoved and restarted your VM you've lost passwordless sudo access. You can login as root through dom0: 
```qvm-run -u root vmname xterm```

Once you're logged in as root or if you're using debian and haven't rebooted the TemplateVM after the initial removal of these packages, reinstall these packages & their dependancies (use ``sudo`` if you haven't rebooted yet): 

### Debian
```apt install qubes-core-agent-dom0-updates qubes-core-agent-passwordless-root qubes-gpg-split qubes-img-converter qubes-input-proxy-sender qubes-mgmt-salt-vm-connector qubes-pdf-converter salt-common salt-ssh```

### Fedora
Similar to Debian for example (package names may vary):
```dnf install qubes-core-agent-dom0-updates qubes-core-agent-passwordless-root qubes-gpg-split qubes-img-converter qubes-input-proxy-sender qubes-mgmt-salt-vm-connector qubes-pdf-converter salt-common salt-ssh```
