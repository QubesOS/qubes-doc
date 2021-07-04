---
lang: en
layout: doc
permalink: /doc/guivm-configuration/
ref: 184
title: GuiVM Configuration
---

## Gui domain

In this section, we describe how to setup `GuiVM` in several case as described in [GUI Domain](https://www.qubes-os.org/news/2020/03/18/gui-domain/). In all the cases, the base underlying TemplateVM used is `Fedora` with `XFCE` flavor to match current desktop choice in `dom0`. That can be adapted very easily for other desktops and templates. By default, the configured `GuiVM` is a management qube with global admin permissions `rwx` but can be adjusted to `ro` (see [Introducing the Qubes Admin API](https://www.qubes-os.org/news/2017/06/27/qubes-admin-api/)) in pillar data of the corresponding `GuiVM` to setup. Please note that each `GuiVM` has no `NetVM`.

> Note: The setup is done using `SaltStack` formulas with the `qubesctl` tool. When executing it, apply step can take time because it needs to download latest Fedora XFCE TemplateVM and install desktop dependencies.


### Hybrid GuiVM `sys-gui`

Here, we describe how to setup `sys-gui` that we call *hybrid mode* or referenced as a *compromised solution* in [GUI Domain](https://www.qubes-os.org/news/2020/03/18/gui-domain/#the-compromise-solution).

[![sys-gui](/attachment/posts/guivm-hybrid.png)](/attachment/posts/guivm-hybrid.png)

In `dom0`, enable the formula for `sys-gui` with pillar data:

```bash
sudo qubesctl top.enable qvm.sys-gui
sudo qubesctl top.enable qvm.sys-gui pillar=True
```

then, execute it:

```bash
sudo qubesctl --all state.highstate
```

You can now disable the `sys-gui` formula:
```bash
sudo qubesctl top.disable qvm.sys-gui
```

At this point, you need to shutdown all your running qubes as the `default_guivm` qubes global property has been set to `sys-gui`. In order to use `sys-gui` as GuiVM, you need to logout and select `lightdm` session to *Gui Domain (sys-gui)*. Once logged, you are running `sys-gui` as fullscreen window and you can perform any operation as if you would be in `dom0` desktop.

> Note: In order to go back to `dom0` desktop, you need to logout and then, select `lightdm` session to *Session Xfce*.

### GPU GuiVM `sys-gui-gpu`

Here, we describe how to setup `sys-gui-gpu` which is a `GuiVM` with *GPU passthrough* in [GUI Domain](https://www.qubes-os.org/news/2020/03/18/gui-domain/#gpu-passthrough-the-perfect-world-desktop-solution).

[![sys-gui-gpu](/attachment/posts/guivm-gpu.png)](/attachment/posts/guivm-gpu.png)

In `dom0`, enable the formula for `sys-gui-gpu` with pillar data:

```bash
sudo qubesctl top.enable qvm.sys-gui-gpu
sudo qubesctl top.enable qvm.sys-gui-gpu pillar=True
```

then, execute it:

```bash
sudo qubesctl --all state.highstate
```

You can now disable the `sys-gui-gpu` formula:

```bash
sudo qubesctl top.disable qvm.sys-gui-gpu
```

At this point, you need to reboot your Qubes OS machine in order to boot into `sys-gui-gpu`.

> None: For some platforms, it can be sufficient to shutdown all the running qubes and starting `sys-gui-gpu`. Unfortunately, it has been observed that detaching and attaching some GPU cards from `dom0` to `sys-gui-gpu` can freeze computer. We encourage reboot to prevent any data loss.

Once, `lightdm` is started, you can log as `user` where `user` refers to the first `dom0` user in `qubes` group and with corresponding `dom0` password.

### VNC GuiVM `sys-gui-vnc`

Here, we describe how to setup `sys-gui-vnc` that we call a *remote* `GuiVM` or referenced as *with a virtual server* in [GUI Domain](https://www.qubes-os.org/news/2020/03/18/gui-domain/#virtual-server-the-perfect-remote-solution).

[![sys-gui-vnc](/attachment/posts/guivm-vnc.png)](/attachment/posts/guivm-vnc.png)

In `dom0`, enable the formula for `sys-gui-vnc` with pillar data:

```bash
sudo qubesctl top.enable qvm.sys-gui-vnc
sudo qubesctl top.enable qvm.sys-gui-vnc pillar=True
```

then, execute it:

```bash
sudo qubesctl --all state.highstate
```

You can now disable the `sys-gui-vnc` formula:

```bash
sudo qubesctl top.disable qvm.sys-gui-vnc
```

At this point, you need to shutdown all your running qubes as the `default_guivm` qubes global property has been set to `sys-gui-vnc`. Then, you can start `sys-gui-vnc`:

```bash
qvm-start sys-gui-vnc
```

A VNC server session is running on `localhost:5900` in `sys-gui-vnc`. In order to reach the `VNC` server, we encourage to not connect `sys-gui-vnc` to a `NetVM` but rather to use another qube for remote access, say `sys-remote`. First, you need to bind port 5900 of `sys-gui-vnc` into a `sys-remote` local port (you may want to use another port than 5900 to reach `sys-remote` from the outside). For that, use `qubes.ConnectTCP` RPC service (see [Firewall](/doc/firewall). Then, you can use any `VNC` client to connect to you `sys-remote` on the chosen local port (5900 if you kept the default one). For the first connection, you will reach `lightdm` for which you can log as `user` where `user` refers to the first `dom0` user in `qubes` group and with corresponding `dom0` password.

> Note: `lightdm` session remains logged even if you disconnect your `VNC` client. Ensure to lock or log out before disconnecting your `VNC` client session.

### Troobleshooting

#### Delete GuiVM

The following commands have to be run in `dom0`.

> Note: For the case of `sys-gui-gpu`, you need to prevent Qubes OS autostart of any qube to reach `dom0`. For that, you need to boot Qubes OS with [`qubes.skip_autostart`](/doc/skip-qubes-autostart/) GRUB parameter.

Set `default_guivm` as `dom0`:

```bash
qubes-prefs default_guivm dom0
```

and for every selected qubes not using default value for `guivm` property, for example with a qube `personal`:

```bash
qvm-prefs personal guivm dom0
```

You are now able to delete the GuiVM, for example `sys-gui-gpu`:

```bash
qvm-remove -y sys-gui-gpu
```
