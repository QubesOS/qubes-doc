---
lang: en
layout: doc
permalink: /doc/how-to-use-disposables/
redirect_from:
- /doc/how-to-use-disposablevms/
- /doc/disposable/
- /doc/dispvm/
- /en/doc/dispvm/
- /doc/DisposableVms/
- /wiki/disposables/
ref: 203
title: How to Use Disposables
---

A **disposable** is a lightweight VM that can be created quickly and will disappear when closed.
disposables are usually created in order to host a single application, like a viewer, editor, or web browser.

From inside an app qube, choosing the `Open in disposable` option on a file will launch a disposable for just that file.
Changes made to a file opened in a disposable are passed back to the originating VM.
This means that you can safely work with untrusted files without risk of compromising your other VMs.
disposables can be launched either directly from dom0's Start Menu or terminal window, or from within app qubes.
While running, disposables will appear in Qubes VM Manager with the name `disp####`.

[![disposablevm-example.png](/attachment/wiki/DisposableVms/disposablevm-example.png)](/attachment/wiki/DisposableVms/disposablevm-example.png)

This diagram provides a general example of how disposables can be used to safely open untrusted links and attachments in disposables. See [this article](https://blog.invisiblethings.org/2010/06/01/disposable-vms.html) for more on why one would want to use a disposable.

## Security

If a [disposable template](/doc/glossary/#disposable-template) becomes compromised, then any disposable based on that disposable template could be compromised.
In particular, the *default* disposable template is important because it is used by the "Open in disposable" feature.
This means that it will have access to everything that you open with this feature.
For this reason, it is strongly recommended that you base the default disposable template on a trusted TemplateVM.

### Disposables and Local Forensics

At this time, disposables should not be relied upon to circumvent local forensics, as they do not run entirely in RAM.
For details, see [this thread](https://groups.google.com/d/topic/qubes-devel/QwL5PjqPs-4/discussion).

When it is essential to avoid leaving any trace, consider using [Tails](https://tails.boum.org/).

## Disposables and Networking

Similarly to how app qubes are based on their underlying [TemplateVM](/doc/glossary/#templatevm), disposables are based on their underlying [disposable template](/doc/glossary/#disposable-template).
R4.0 introduces the concept of multiple disposable templates, whereas R3.2 was limited to only one.

On a fresh installation of Qubes, the default disposable template is called `fedora-XX-dvm` (where `XX` is the Fedora version of the default TemplateVM).
If you have included the Whonix option in your install, there will also be a `whonix-ws-dvm` disposable template available for your use.

You can set any app qube to have the ability to act as a disposable template with:

```
qvm-prefs <vmname> template_for_dispvms True
```

The default system wide disposable template can be changed with `qubes-prefs default_dispvm`.
By combining the two, choosing `Open in disposable` from inside an app qube will open the document in a disposable based on the default disposable template you specified.

You can change this behaviour for individual VMs: in the Application Menu, open Qube Settings for the VM in question and go to the "Advanced" tab.
Here you can edit the "Default disposable" setting to specify which disposable template will be used to launch disposables from that VM.
This can also be changed from the command line with:

```
qvm-prefs <VM> default_dispvm <DISPOSABLEVM_TEMPLATE>
```

For example, `anon-whonix` has been set to use `whonix-ws-dvm` as its `default_dispvm`, instead of the system default.
You can even set an app qube that has also been configured as a disposable template to use itself, so disposables launched from within the app qube/disposable template would inherit the same settings.

NetVM and firewall rules for disposable templates can be set as they can for a normal VM.
By default a disposable will inherit the NetVM and firewall settings of the disposable template on which it is based.
This is a change in behaviour from R3.2, where disposables would inherit the settings of the app qube from which they were launched.
Therefore, launching a disposable from an app qube will result in it using the network/firewall settings of the disposable template on which it is based.
For example, if an app qube uses sys-net as its NetVM, but the default system disposable uses sys-whonix, any disposable launched from this app qube will have sys-whonix as its NetVM.

**Warning:** The opposite is also true.
This means if you have changed anon-whonix's `default_dispvm` to use the system default, and the system default disposable uses sys-net, launching a disposable from inside anon-whonix will result in the disposable using sys-net.

A disposable launched from the Start Menu inherits the NetVM and firewall settings of the disposable template on which it is based.
Note that changing the "NetVM" setting for the system default disposable template *does* affect the NetVM of disposables launched from the Start Menu.
Different disposable templates with individual NetVM settings can be added to the Start Menu.

**Important Notes:**
Some disposable templates will automatically create a menu item to launch a disposable, if you do not see an entry and want to add one please use the command:

```
qvm-features <DISPOSABLE> appmenus-dispvm 1
```

To launch a disposable template from the command line, in dom0 please type the following:

```
qvm-run --dispvm=<DISPOSABLE_TEMPLATE> --service qubes.StartApp+NameOfApp
```

## Opening a file in a disposable via GUI

In an app qube's file manager, right click on the file you wish to open in a disposable, then choose "View in disposable" or "Edit in disposable".
Wait a few seconds and the default application for this file type should appear displaying the file content.
This app is running in its own dedicated VM -- a disposable created for the purpose of viewing or editing this very file.
Once you close the viewing application the whole disposable will be destroyed.
If you have edited the file and saved the changes, the changed file will be saved back to the original app qube, overwriting the original.

![r4.0-open-in-dispvm-1.png](/attachment/wiki/DisposableVms/r4.0-open-in-dispvm-1.png) ![r4.0-open-in-dispvm-2.png](/attachment/wiki/DisposableVms/r4.0-open-in-dispvm-2.png)


## Opening a fresh web browser instance in a new disposable

Sometimes it is desirable to open an instance of Firefox within a new fresh disposable.
This can be done easily using the Start Menu: just go to **Application Menu -\> disposable -\> disposable:Firefox web browser**.
Wait a few seconds until a web browser starts.
Once you close the viewing application the whole disposable will be destroyed.

![r4.0-open-in-dispvm-3.png](/attachment/wiki/DisposableVms/r4.0-open-in-dispvm-3.png)


## Opening a file in a disposable via command line (from app qube)

Use the `qvm-open-in-dvm` command from a terminal in your app qube:

~~~
[user@work-pub ~]$ qvm-open-in-dvm Downloads/apple-sandbox.pdf
~~~

Note that the `qvm-open-in-dvm` process will not exit until you close the application in the disposable.

## Starting an arbitrary program in a disposable from an app qube

Sometimes it can be useful to start an arbitrary program in a disposable.
The disposable will stay running so long as the process which started the disposable has not exited.
Some applications, such as GNOME Terminal, do not wait for the application to close before the process exits (details [here](https://github.com/QubesOS/qubes-issues/issues/2581#issuecomment-272664009)).
Starting an arbitrary program can be done from an app qube by running

~~~
[user@vault ~]$ qvm-run '@dispvm' xterm
~~~

The created disposable can be accessed via other tools (such as `qvm-copy-to-vm`) using its `disp####` name as shown in the Qubes Manager or `qvm-ls`.

## Starting an arbitrary application in a disposable via command line from dom0

The Application Launcher has shortcuts for opening a terminal and a web browser in dedicated disposables, since these are very common tasks.
The disposable will stay running so long as the process which started the disposable has not exited.
Some applications, such as GNOME Terminal, do not wait for the application to close before the process exits (details [here](https://github.com/QubesOS/qubes-issues/issues/2581#issuecomment-272664009)).
It is possible to start an arbitrary application in a disposable directly from dom0 by running:

~~~
$ qvm-run --dispvm=<DISPOSABLE_TEMPLATE> --service qubes.StartApp+xterm
~~~

The label color will be inherited from `<DISPOSABLE_TEMPLATE>`.
(The disposable Application Launcher shortcut used for starting programs runs a very similar command to the one above.)

### Opening a link in a disposable based on a non-default disposable template from a qube

Suppose that the default disposable template for your `email` qube has no networking (e.g., so that untrusted attachments can't phone home).
However, sometimes you want to open email links in disposables.
Obviously, you can't use the default disposable template, since it has no networking, so you need to be able to specify a different disposable template.
You can do that with this command from the `email` qube (as long as your RPC policies allow it):

~~~
$ qvm-open-in-vm @dispvm:<ONLINE_DISPOSABLE_TEMPLATE> https://www.qubes-os.org
~~~

This will create a new disposable based on `<ONLINE_DISPOSABLE_TEMPLATE>`, open the default web browser in that disposable, and navigate to `https://www.qubes-os.org`.

#### Example of RPC policies to allow this behavior

In dom0, add the following line at the beginning of the file `/etc/qubes-rpc/policy/qubes.OpenURL`

~~~
@anyvm @dispvm:<ONLINE_DISPOSABLE_TEMPLATE> allow
~~~

This line means:
- FROM: Any VM
- TO: A disposable based on `<ONLINE_DISPOSABLE_TEMPLATE>`
- WHAT: Allow sending an "Open URL" request

In other words, any VM will be allowed to create a new disposable based on `<ONLINE_DISPOSABLE_TEMPLATE>` and open a URL inside of that disposable.

More information about RPC policies for disposables can be found [here](/doc/qrexec/#qubes-rpc-administration).

## Customizing disposables

You can change the template used to generate the disposables, and change settings used in the disposable savefile.
These changes will be reflected in every new disposable based on that template.
Full instructions can be found [here](/doc/disposable-customization/).

