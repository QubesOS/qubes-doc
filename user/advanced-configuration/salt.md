---
lang: en
layout: doc
permalink: /doc/salt/
ref: 185
title: Management stack
---

# Management Infrastructure

Since the Qubes R3.1 release we have included the Salt (also called SaltStack)
management engine in dom0 as default (with some states already configured).
Salt allows administrators to easily configure their systems.
In this guide we will show how it is set up and how you can modify it for your
own purpose.

In the current form the **API is provisional** and subject to change between
*minor* releases.

## Understanding Salt

This document is not meant to be comprehensive Salt documentation; however,
before writing anything it is required you have at least *some* understanding of
basic Salt-related vocabulary.
For more exhaustive documentation, visit [official site](https://docs.saltstack.com/en/latest/), though we
must warn you that it is not easy to read if you just start working with Salt
and know nothing.

### The Salt Architecture

Salt is a client-server model, where the server (called *master*) manages
its clients (called *minions*).
In typical situations, it is intended that the administrator interacts only
with the master and keeps the configurations there.
In Qubes, we don't have a master.
Instead we have one minion which resides in `dom0` and manages domains from
there.
This setup is also supported by Salt.

Salt is a management engine (similar to Ansible, Puppet, and Chef), that
enforces a particular state of a minion system.
A *state* is an end effect *declaratively* expressed by the administrator.
This is the most important concept in the entire engine.
All configurations (i.e., the states) are written in YAML.

A *pillar* is a data back-end declared by the administrator.
When states become repetitive, instead of pure YAML they can be written using a
template engine (preferably Jinja2); which can use data structures specified in
pillars.

A *formula* is a ready to use, packaged solution that combines a state and a
pillar (possibly with some file templates and other auxiliary files).
There are many formulas made by helpful people all over the Internet.

A *grain* is some data that is also available in templates, but its value is not
directly specified by administrator.
For example, the distribution (e.g., `"Debian"` or `"Gentoo"`) is a value of
the grain `"os"`. It also contains other information about the kernel,
hardware, etc.

A *module* is a Python extension to Salt that is responsible for actually
enforcing the state in a particular area.
It exposes some *imperative* functions for the administrator.
For example, there is a `system` module that has a `system.halt` function that,
when issued, will immediately halt a domain.
There is another function called `state.highstate` which will synchronize the
state of the system with the administrator's configuration/desires.

### Configuration

#### States

The smallest unit of configuration is a state.
A state is written in YAML and looks like this:

```
stateid:
  cmd.run:  #this is the execution module. in this case it will execute a command on the shell
  - name: echo 'hello world' #this is a parameter of the state.
```

The stateid has to be unique throughout all states running for a minion and can
be used to order the execution of the references state.
`cmd.run` is an execution module.
It executes a command on behalf of the administrator.
`name: echo 'hello world'` is a parameter for the execution module `cmd.run`.
The module used defines which parameters can be passed to it.

There is a list of [officially available states](https://docs.saltstack.com/en/latest/ref/states/all/).
There are many very useful states:

- For [managing files](https://docs.saltstack.com/en/latest/ref/states/all/salt.states.file.html): Use this to create files or
  directories and change them (append lines, replace text, set their content etc.)
- For [installing and uninstalling](https://docs.saltstack.com/en/latest/ref/states/all/salt.states.pkg.html) packages.
- For [executing shell commands](https://docs.saltstack.com/en/latest/ref/states/all/salt.states.file.html).

With these three states you can define most of the configuration of a VM.

You can also [order the execution](https://docs.saltstack.com/en/latest/ref/states/ordering.html) of your states:

```
D:
  cmd.run:
  - name: echo 1
  - order: last
C:
  cmd.run:
  - name: echo 1
B:
  cmd.run:
  - name: echo 1
  - require:
    - cmd: A
  - require_in:
    - cmd:C
A:
  cmd.run:
  - name: echo 1
  - order: 1
```

The order of execution will be `A, B, C, D`.
The official documentation has more details on the
[require](https://docs.saltstack.com/en/latest/ref/states/requisites.html) and [order](https://docs.saltstack.com/en/latest/ref/states/ordering.html#the-order-option) arguments.

#### State Files

When configuring a system you will write one or more state files (`*.sls`) and
put (or symlink) them into the main Salt directory `/srv/salt/`.
Each state file contains multiple states and should describe some unit of
configuration (e.g., a state file `mail.sls` could setup a VM for e-mail).

#### Top Files

After you have several state files, you need something to assign them to a VM.
This is done by `*.top` files ([official documentation](https://docs.saltstack.com/en/latest/ref/states/top.html)).
Their structure looks like this:

```
environment:
  target_matching_clause:
  - statefile1
  - folder2.statefile2
```

In most cases, the environment will be called `base`.
The `target_matching_clause` will be used to select your minions (VMs).
It can be either the name of a VM or a regular expression.
If you are using a regular expressions, you need to give Salt a hint you are
doing so:

```
environment:
  ^app-(work|(?!mail).*)$:
  - match: pcre
  - statefile
```

For each target you can write a list of state files.
Each line is a path to a state file (without the `.sls` extension) relative to
the main directory.
Each `/` is exchanged with a `.`, so you can't reference files or directories
with a `.` in their name.

### Enabling Top Files and Applying the States

Now, because we use custom extensions to manage top files (instead of just
enabling them all), to enable a particular top file you should issue command:

```
$ qubesctl top.enable my-new-vm
```

To list all enabled top files:

```
$ qubesctl top.enabled
```

And to disable one:

```
$ qubesctl top.disable my-new-vm
```

To apply the states to dom0 and all VMs:

```
$ qubesctl --all state.highstate
```

(More information on the `qubesctl` command further down.)

### Template Files

You will sometimes find yourself writing repetitive states.
To solve this, there is the ability to template files or states.
This is most commonly done with [Jinja](http://jinja.pocoo.org/).
Jinja is similar to Python and in many cases behaves in a similar fashion, but
there are sometimes differences when, for example, you set some variable inside
a loop: the variable outside will not get changed.
Instead, to get this behavior, you would use a `do` statement.
So you should take a look at the [Jinja API documentation](http://jinja.pocoo.org/docs/2.9/templates/).
Documentation about using Jinja to directly call Salt functions and get data
about your system can be found in the official
[Salt documentation](https://docs.saltstack.com/en/getstarted/config/jinja.html#get-data-using-salt).

## Salt Configuration, QubesOS layout

All Salt configuration files are in the `/srv/` directory, as usual.
The main directory is `/srv/salt/` where all state files reside.
States are contained in `*.sls` files.
However, the states that are part of the standard Qubes distribution are mostly
templates and the configuration is done in pillars from formulas.

The formulas are in `/srv/formulas`, including stock formulas for domains in
`/srv/formulas/dom0/virtual-machines-formula/qvm`, which are used by firstboot.

Because we use some code that is not found in older versions of Salt, there is
a tool called `qubesctl` that should be run instead of `salt-call --local`.
It accepts all the same arguments of the vanilla tool.

## Configuring a VM's System from Dom0

Salt in Qubes can be used to configure VMs from dom0.
Simply set the VM name as the target minion name in the top file.
You can also use the `qubes` pillar module to select VMs with a particular
property (see below).
If you do so, then you need to pass additional arguments to the `qubesctl` tool:

```
usage: qubesctl [-h] [--show-output] [--force-color] [--skip-dom0]
                [--targets TARGETS | --templates | --app | --all]
                ...

positional arguments:
  command            Salt command to execute (e.g., state.highstate)

optional arguments:
  -h, --help         show this help message and exit
  --show-output      Show output of management commands
  --force-color      Force color output, allow control characters from VM,
                     UNSAFE
  --skip-dom0        Skip dom0 configuration (VM creation etc)
  --targets TARGETS  Coma separated list of VMs to target
  --templates        Target all templates
  --app              Target all AppVMs
  --all              Target all non-disposable VMs (TemplateVMs and AppVMs)
```

To apply a state to all templates, call `qubesctl --templates state.highstate`.

The actual configuration is applied using `salt-ssh` (running over `qrexec`
instead of `ssh`).
Which means you don't need to install anything special in a VM you want to
manage.
Additionally, for each target VM, `salt-ssh` is started from a temporary VM.
This way dom0 doesn't directly interact with potentially malicious target VMs;
and in the case of a compromised Salt VM, because they are temporary, the
compromise cannot spread from one VM to another.

Beginning with Qubes 4.0 and after [QSB #45](/news/2018/12/03/qsb-45/), we implemented two changes:

1. Added the `management_dispvm` VM property, which specifies the DVM
   Template that should be used for management, such as Salt
   configuration.  TemplateBasedVMs inherit this property from their
   parent TemplateVMs.  If the value is not set explicitly, the default
   is taken from the global `management_dispvm` property. The
   VM-specific property is set with the `qvm-prefs` command, while the
   global property is set with the `qubes-prefs` command.

2. Created the `default-mgmt-dvm` DisposableVM Template, which is hidden from
   the menu (to avoid accidental use), has networking disabled, and has
   a black label (the same as TemplateVMs). This VM is set as the global
   `management_dispvm`. Keep in mind that this DVM template has full control
   over the VMs it's used to manage.

## Writing Your Own Configurations

Let's start with a quick example:

```
my new and shiny VM:
  qvm.present:
    - name: salt-test # can be omitted when same as ID
    - template: fedora-21
    - label: yellow
    - mem: 2000
    - vcpus: 4
    - flags:
      - proxy
```

It uses the Qubes-specific `qvm.present` state, which ensures that the domain is
present (if not, it creates it).

- The `name` flag informs Salt that the domain should be named `salt-test` (not
  `my new and shiny VM`).
- The `template` flag informs Salt which template should be used for the domain.
- The `label` flag informs Salt what color the domain should be.
- The `mem` flag informs Salt how much RAM should be allocated to the domain.
- The `vcpus` flag informs Salt how many Virtual CPUs should be allocated to the
  domain
- The `proxy` flag informs Salt that the domain should be a ProxyVM.

As you will notice, the options are the same (or very similar) to those used in
`qvm-prefs`.

This should be put in `/srv/salt/my-new-vm.sls` or another `.sls` file.
A separate `*.top` file should be also written:

```
base:
  dom0:
    - my-new-vm
```

**Note** The third line should contain the name of the previous state file,
without the `.sls` extension.

To enable the particular top file you should issue the command:

```
$ qubesctl top.enable my-new-vm
```

To apply the state:

```
$ qubesctl state.highstate
```

### Example of Configuring a VM's System from Dom0

Lets make sure that the `mc` package is installed in all templates.
Similar to the previous example, you need to create a state file
(`/srv/salt/mc-everywhere.sls`):

```
mc:
  pkg.installed: []
```

Then the appropriate top file (`/srv/salt/mc-everywhere.top`):

```
base:
 qubes:type:template:
    - match: pillar
    - mc-everywhere
```

Now you need to enable the top file:

```
$ qubesctl top.enable mc-everywhere
```

And apply the configuration:

```
$ qubesctl --all state.highstate
```

## All Qubes-specific States

### `qvm.present`

As in the example above, it creates a domain and sets its properties.

### `qvm.prefs`

You can set properties of an existing domain:

```
my preferences:
  qvm.prefs:
    - name: salt-test2
    - netvm: sys-firewall
```

***Note*** The `name:` option will not change the name of a domain, it will only
be used to match a domain to apply the configurations to it.

### `qvm.service`

```
services in my domain:
  qvm.service:
    - name: salt-test3
    - enable:
      - service1
      - service2
    - disable:
      - service3
      - service4
    - default:
      - service5
```

This enables, disables, or sets to default, services as in `qvm-service`.

### `qvm.running`

Ensures the specified domain is running:

```
domain is running:
  qvm.running:
    - name: salt-test4
```

## Virtual Machine Formulae

You can use these formulae to download, install, and configure VMs in Qubes.
These formulae use pillar data to define default VM names and configuration details.
The default settings can be overridden in the pillar data located in:

```
/srv/pillar/base/qvm/init.sls
```

In dom0, you can apply a single state with `sudo qubesctl state.sls STATE_NAME`.
For example, `sudo qubesctl state.sls qvm.personal` will create a `personal` VM (if it does not already exist) with all its dependencies (TemplateVM, `sys-firewall`, and `sys-net`).

### Available states

#### `qvm.sys-net`

System NetVM

#### `qvm.sys-usb`

System USB VM

#### `qvm.sys-net-with-usb`

System USB VM bundled into NetVM. Do not enable together with `qvm.sys-usb`.

#### `qvm.usb-keyboard`

Enable USB keyboard together with USB VM, including for early system boot (for LUKS passhprase).
This state implicitly creates a USB VM (`qvm.sys-usb` state), if not already done.

#### `qvm.sys-firewall`

System firewall ProxyVM

#### `qvm.sys-whonix`

Whonix gateway ProxyVM

#### `qvm.personal`

Personal AppVM

#### `qvm.work`

Work AppVM

#### `qvm.untrusted`

Untrusted AppVM

#### `qvm.vault`

Vault AppVM with no NetVM enabled.

#### `qvm.default-dispvm`

Default DisposableVM template - fedora-26-dvm AppVM

#### `qvm.anon-whonix`

Whonix workstation AppVM.

#### `qvm.whonix-ws-dvm`

Whonix workstation AppVM for Whonix DisposableVMs.

#### `qvm.updates-via-whonix`

Setup UpdatesProxy to route all templates updates through Tor (sys-whonix here).

#### `qvm.template-fedora-21`

Fedora-21 TemplateVM

#### `qvm.template-fedora-21-minimal`

Fedora-21 minimal TemplateVM

#### `qvm.template-debian-7`

Debian 7 (wheezy) TemplateVM

#### `qvm.template-debian-8`

Debian 8 (jessie) TemplateVM

#### `qvm.template-whonix-gw`

Whonix Gateway TemplateVM

#### `qvm.template-whonix-ws`

Whonix Workstation TemplateVM

#### `update.qubes-dom0`

Updates dom0

#### `update.qubes-vm`

Updates domUs. Example to update all TemplateVMs:

```
sudo qubesctl --skip-dom0 --templates state.sls update.qubes-vm
```

Useful options:

- `--max-concurrency` --- Limits how many templates are updated at the same time.
  Adjust to your available RAM.
  The default is 4, and the GUI updater sets it to 1.
- `--targets=vm1,vm2,...` --- Limit to specific VMs, instead of all of them.
  (Use instead of `--templates` or `--standalones`.)
- `--show-output` --- Show an update summary instead of just OK/FAIL.

For other options, see `qubesctl --help`.

## The `qubes` Pillar Module

Additional pillar data is available to ease targeting configurations (for example all templates).

**Note:** This list is subject to change in future releases.

### `qubes:type`

VM type. Possible values:

- `admin` - Administration domain (`dom0`)
- `template` - Template VM
- `standalone` - Standalone VM
- `app` - Template based AppVM

### `qubes:template`

Template name on which a given VM is based (if any).

### `qubes:netvm`

VM which provides network to the given VM

## Debugging

The output for each VM is logged in `/var/log/qubes/mgmt-VM_NAME.log`.

If the log does not contain useful information:
1. Run `sudo qubesctl --skip-dom0 --target=VM_NAME state.highstate`
2. When your VM is being started (yellow) press Ctrl-z on qubesctl.
3. Open terminal in disp-mgmt-VM_NAME.
4. Look at /etc/qubes-rpc/qubes.SaltLinuxVM - this is what is
   executed in the management VM.
5. Get the last two lines:

    ```shell_session
    $ export PATH="/usr/lib/qubes-vm-connector/ssh-wrapper:$PATH"
    $ salt-ssh "$target_vm" $salt_command
    ```

  Adjust $target_vm (VM_NAME) and $salt_command (state.highstate).
6. Execute them, fix problems, repeat.

## Known Pitfalls

### Using fedora-24-minimal

The fedora-24-minimal package is missing the `sudo` package.
You can install it via:

```shell_session
$ qvm-run -p -u root fedora-24-minimal-template 'dnf install -y sudo'
```

The `-p` will cause the execution to wait until the package is installed.
Having the `-p` flag is important when using a state with `cmd.run`.

### Disk Quota Exceeded (When Installing Templates)

If you install multiple templates you may encounter this error.
The solution is to shut down the updateVM between each install:

```
install template and shutdown updateVM:
  cmd.run:
  - name: sudo qubes-dom0-update -y fedora-24; qvm-shutdown {% raw %}{{ salt.cmd.run(qubes-prefs updateVM) }}{% endraw %}
```

## Further Reading

- [Salt documentation](https://docs.saltstack.com/en/latest/)
- [Salt states](https://docs.saltstack.com/en/latest/ref/states/all/) ([files](https://docs.saltstack.com/en/latest/ref/states/all/salt.states.file.html), [commands](https://docs.saltstack.com/en/latest/ref/states/all/salt.states.file.html),
  [packages](https://docs.saltstack.com/en/latest/ref/states/all/salt.states.pkg.html), [ordering](https://docs.saltstack.com/en/latest/ref/states/ordering.html))
- [Top files](https://docs.saltstack.com/en/latest/ref/states/top.html)
- [Jinja templates](http://jinja.pocoo.org/)
- [Qubes specific modules](https://github.com/QubesOS/qubes-mgmt-salt-dom0-qvm/blob/master/README.rst)
- [Formulas for default Qubes VMs](https://github.com/QubesOS/qubes-mgmt-salt-dom0-virtual-machines/tree/master/qvm)

