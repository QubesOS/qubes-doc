---
layout: doc
title: Ubuntu Template
redirect_to: https://github.com/Qubes-Community/Contents/blob/master/docs/os/templates/ubuntu.md
redirect_from:
- /doc/templates/ubuntu/
- /doc/ubuntu/
- /en/doc/templates/ubuntu/
- /doc/Templates/Ubuntu/
- /wiki/Templates/Ubuntu/
---

Ubuntu template(s)
==================

If you would like to use Ubuntu Linux distribution in your AppVMs, you can build and install one of the available Ubuntu templates.
These templates are currently not provided by Qubes in ready to use binary packages, because Canonical does not allow redistribution of a modified Ubuntu.
The redistribution is not allowed by their [Intellectual property rights policy][IP].

Building the Template
-------

Templates can be built using [Qubes Builder][builder]  
(You can also access documentation in the [source code repository][repo].)

Please carefully read the [instructions][builder] for setting up and using Qubes Builder.  
To quickly prepare the builder configuration, you can use the `setup` script available in the repository - it will interactively ask you which templates you want to build.  
Select one of the Ubuntu version options.  
On the "Choose Pre-Built Packages Repositories" page you must not select either option.  
This is because Qubes does not provide offical Pre-Built packages for Ubuntu.  

Once you have completed setup, in the qubes-builder directory, run:
```
make qubes-vm
make template
```

The build for Ubuntu 16.04 LTS (Xenial) is straightforward.

The build for Ubuntu 18.04 LTS (Bionic) is straightforward.



Installing the template
-------

You must copy the template you have built in to dom0 and install it there.  
Rather than do this manually, there is a script you can use.  

In dom0, run :
```
qvm-run -p <build_qube> 'cat /home/user/qubes-builder/qubes-src/linux-template-builder/rpm/install-templates.sh ' > install-templates.sh
```
If you have built other templates, edit the `install-templates.sh` to ensure you only retain the templates you want to install.  
Then run `./install-templates.sh`

----------
If you want to help in improving the template, feel free to [contribute][contrib].

[IP]: https://www.ubuntu.com/legal/terms-and-policies/intellectual-property-policy  
[repo]: https://github.com/QubesOS/qubes-builder/blob/master/README.md
[builder]: /doc/qubes-builder/
[contrib]: /doc/contributing/
