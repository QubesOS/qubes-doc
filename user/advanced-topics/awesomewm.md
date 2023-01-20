---
lang: en
layout: doc
permalink: /doc/awesomewm/
redirect_from:
- /doc/awesome/
- /en/doc/awesome/
ref: 179
title: AwesomeWM (window manager)
---

## Qubes-specific features

* support for the Qubes OS window colors
* rudimentary support for the Qubes application menu entries following the freedesktop standard
* support for custom filters and menu entries

## Installation

AwesomeWM can be installed with the standard dom0 installation mechanisms.

```shell_session
$ sudo qubes-dom0-update awesome
```

That's it. After logging out, you can select AwesomeWM in the login manager.

## Development

To [contribute code](/doc/contributing/) you may clone the AwesomeWM repository as follows:

```shell_session
$ git clone https://github.com/QubesOS/qubes-desktop-linux-awesome
```

For build instructions please check the repository _README_.

The repository attempts to follow the upstream Fedora repository.
