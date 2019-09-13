---
layout: doc
title: Removing TemplateVM Packages
redirect_from:
- /doc/removing-templatevm-packages/
---

# Removing TemplateVM Packages
When removing any packages from a default TemplateVM, be sure to check what's being removed by `apt autoremove` or `dnf`. 
When removing certain packages, for instance Thunderbird, `apt` and `dnf` will attempt to remove many packages required by qubes for the template to function correctly under qubes.

As an example from a terminal in a TemplateVM:
```shell_session
$ sudo apt remove thunderbird
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

Note all of the qubes packages are tracked as dependencies that will no longer be required. `apt remove` will only remove the packages listed, which is ok. 
If, however you also run `apt autoremove` the other qubes packages necessary for TemplateVMs will be removed.

If you'd still like to remove one of these applications without breaking your TemplateVM you have a couple different options. 

## Removing Only Packages Not Needed for a Qubes TemplateVM

### Debian
 1. In your TemplateVM terminal run:
 ```shell_session $ apt remove package-name```
 Note the packages "no longer required"
 2. If the list of "no longer required" packages includes anything beginning with `qubes-` or `salt-` make a note to yourself to **never** run `$ sudo apt autoremove` on this TemplateVM

**Recommended but optional:** Use `apt-mark` to make `apt autoremove` safe again. 
```shell_session
$ sudo apt mark-manual package-name package-name
```

Replace package-names with actual `qubes-*` and `salt-*` packages you'd like to retain. 

For example, still in your TemplateVM terminal: 
```shell_session
$ sudo apt-mark manual qubes-core-agent-dom0-updates qubes-core-agent-passwordless-root qubes-gpg-split qubes-img-converter qubes-input-proxy-sender qubes-mgmt-salt-vm-connector qubes-pdf-converter salt-common salt-ssh qubes-usb-proxy
```

`$ apt autoremove` should now be safe to use.

### Fedora
In your TemplateVM terminal, run:
```shell_session
$ dnf remove --noautoremove package-name
```

 
## Recovering A TemplateVM which you've already removed needed qubes-* packages
If you've already removed packages, run `apt autoremove` and restarted your VM you've lost passwordless sudo access. 
You can login as root, open a terminal in dom0 and run: 
```shell_session
$ qvm-run -u root vmname xterm
```
This will open an xterm terminal in the TemplateVM named `vmname`

Once you're logged in as root, reinstall these packages & their dependencies: 

### Debian
```shell_session
$ sudo apt install qubes-core-agent-dom0-updates qubes-core-agent-passwordless-root qubes-gpg-split qubes-img-converter qubes-input-proxy-sender qubes-mgmt-salt-vm-connector qubes-pdf-converter salt-common salt-ssh
```

### Fedora
Similar to Debian for example (package names may vary):
```shell_session
$ sudo dnf install qubes-core-agent-dom0-updates qubes-core-agent-passwordless-root qubes-gpg-split qubes-img-converter qubes-input-proxy-sender qubes-mgmt-salt-vm-connector qubes-pdf-converter salt-common salt-ssh
```
