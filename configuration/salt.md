---
layout: doc
title: Management stack
permalink: /doc/salt/
---
# Management infrastructure

Since Qubes R3.1 release we have included `salt` (also called SaltStack)
management engine in dom0 as default with some states already configured. salt
allows administrators to easily configure their systems. In this guide we will
show how it is set up and how you can modify it for your own purpose.

In the current form the **API is provisional** and subject to change between
*minor* releases.

## Understanding `salt`

This document is not meant to be comprehensive salt documentation, however
before writing anything it is required you have at least *some* understanding of
basic salt-related vocabulary. For more exhaustive documentation, visit
[official site][salt-doc], though we must warn you that it is not easy to read
if you just start working with salt and know nothing.

### The architecture

Salt has client-server architecture, where server (called *master*) manages its
clients (called *minions*). In typical situation it is intended that
administrator interacts only with master and keeps the configuration there. In
Qubes OS we don't have master though, since we have only one minion, which
resides in `dom0` and manages domains from there. This is also supported by
salt.

Salt is a management engine, that enforces particular state of the system, where
minion runs. A *state* is an end effect *declaratively* expressed by the
administrator. This is the most important concept in the whole package. All
configuration (ie. the states) are written in YAML.

A *pillar* is a data back-end declared by administrator. When states became
repetitive, instead of pure YAML they can be written with help of some template
engine (preferably jinja2), which can use data structures specified in pillars.

A *formula* is a ready to use, packaged solution that combines state and pillar,
possibly with some file templates and other auxiliary files. There are many of
those made by helpful people all over the Internet.

A *grain* is some data that is also available in templates, but its value is not
directly specified by administrator. For example the distribution (like
`"Debian"` or `"Gentoo"`) is a value of the grain `"os"`. It also contains other
info about kernel, hardware etc.

A *module* is a Python extension to salt that is responsible for actually
enforcing the state in a particular area. It exposes some *imperative* functions
for administrator. For example there is `system` module that has `system.halt`
function that, when issued, will immediately halt the computer. There is another
function called `state.highstate` which will synchronize the state of the system
with the administrator's will.

### Configuration

#### States

The smallest unit of configuration is a state.
A state is written in yaml and looks like this:

    stateid:
      cmd.run:  #this is the execution module. in this case it will execute a command on the shell
      - name: echo 'hello world' #this is a parameter of the state. 

The stateid has to be unique over all states running for a minion and can be used
to order the execution of states.
`cmd.run` is the execution module. It decides which action will be executed.
`name: echo 'hello world'` is a parameter for the execution module. It depends on
the module which parameters are accepted.

There is list of [officially available states][salt-doc-states].
There are many very useful states:

* For [managing files][salt-doc-states-file]: Use this to create files or 
  directories and change them (append lines, replace text, set their content etc.)
* For [installing and uninstalling][salt-doc-states-pkg] packages.
* To [execute shell commands][salt-doc-states-cmd].

With these three states you can do most of the configuration inside of a vm.

You also can [order the execution][salt-doc-states-order] of your states:

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

The order of execution will be `A, B, C, D`.
The official documentation has more details on the [require][salt-doc-states-req] and
[order][salt-doc-states-ord] arguments.

#### State files

When configuring a system you will write one or several state files (`*.sls`) and
put (or symlink) them in the salt main directory `/srv/salt/`.
Each state file contains one multiple states and should describe some unit of 
configuration (e.g.: A state file `mail.sls` could setup a vm for mailing).

#### Top files

After you have state several state files, you need something to assign them to a
vm. This is done by `*.top` files ([official documentation][salt-doc-top]).
Their structure looks like this:

    environment:
      target_matching_clause:
      - statefile1
      - folder2.statefile2

The environment will be in most cases `base`.
The `target_matching_clause` will be used to select your minions (vms).
It can be just the name of a vm or a regular expression.
If you are using a regular expression, you need to give salt a hint you are doing
so:

    environment:
      ^app-(work|(?!mail).*)$:
      - match: pcre
      - statefile

For each target you can write a list of state files.
Each line is a path to a state file (without the `.sls`) relative to the main 
directory. Each `/` is exchanged by a dot, so you can't reference files or 
directories with a dot in their name.

### Enabling top files and applying the configuration

Now because we use custom extension to manage top files (instead of just
enabling them all) to enable the particular top file you should issue command:

    qubesctl top.enable my-new-vm

To list all enabled tops:

    qubesctl top.enabled

And to disable one:

    qubesctl top.disable my-new-vm

To actually apply the states to dom0 and all vms:

    qubesctl --all state.highstate

(More information on the command is further down.)

### Templating files

You will sometimes find your self writing repetitive states. To solve this,
there is the ability to template files or states.
This can be done with [jinja][jinja].
Jinja is similar to python and behaves in many cases similar, but there 
sometimes are differences (e.g. If you set some variable inside a loop,
the variable outside will not get changed. Unless you use a do statement).
So you should take a look at the [jinja api documentation][jinja-tmp].
How you can use jinja to directly call salt functions and get data about
your system is documented in the [salt documentation][jinja-call-salt-functions].

## Salt configuration, Qubes OS layout

All salt configuration in `/srv/` directory, as usual. The main directory is
`/srv/salt/` where all state files reside. States are contained in `*.sls`
files. However the states that are part of standard Qubes distribution are
mostly templates and the configuration is done in pillars from formulas.

The formulas are in `/srv/formulas`, including stock formula for domains in
`/srv/formulas/dom0/virtual-machines-formula/qvm`, which are used by firstboot.

Because we use some code that is not found in older versions of salt, there is
a tool called `qubesctl` that should be run instead of `salt-call --local`. It
accepts all arguments of the vanilla tool.


## Configuring system inside of VMs

Starting with Qubes 3.2, Salt in Qubes can be used to configure VMs. Salt
formulas can be used normal way. Simply set VM name as target minion name in
top file. You can also use `qubes` pillar module to select VMs with a
particular property (see below). Then you need to pass additional arguments to
`qubesctl` tool:

    usage: qubesctl [-h] [--show-output] [--force-color] [--skip-dom0]
                    [--targets TARGETS | --templates | --app | --all]
                    ...

    positional arguments:
      command            Salt command to execute (for example: state.highstate)

    optional arguments:
      -h, --help         show this help message and exit
      --show-output      Show output of management commands
      --force-color      Force color output, allow control characters from VM,
                         UNSAFE
      --skip-dom0        Skip dom0 condifuration (VM creation etc)
      --targets TARGETS  Coma separated list of VMs to target
      --templates        Target all templates
      --app              Target all AppVMs
      --all              Target all non-disposable VMs (TemplateVMs and AppVMs)


To apply the configuration to all the templates, call `qubesctl --templates
state.highstate`.

Actual configuration is applied using `salt-ssh` (running over `qrexec` instead
of `ssh`). Which means you don't need to install anything special in a VM you
want to manage. Additionally for each target VM, `salt-ssh` is started from a
temporary VM. This way dom0 doesn't directly interact with potentially
malicious target VM.

## Writing your own configuration

Let's start with quick example:

    my new and shiny vm:
      qvm.present:
        - name: salt-test # can be omitted when same as ID
        - template: fedora-21
        - label: yellow
        - mem: 2000
        - vcpus: 4
        - flags:
          - proxy

It uses Qubes-specific `qvm.present` state, which ensures that domain is
created. The name should be `salt-test` (and not `my new and shiny vm`),
the rest are domains properties, same as in `qvm-prefs`. `proxy` flag informs
salt that the domain should be a ProxyVM.

This should be put in `/srv/salt/my-new-vm.sls` or another `.sls` file. Separate
`*.top` file should be also written:

    base:
      dom0:
        - my-new-vm

The third line should contain the name of the previous file, without `.sls`.

To enable the particular top file you should issue command:

    qubesctl top.enable my-new-vm

To actually apply the state:

    qubesctl state.highstate


### Example of VM system configuration

It is also possible to configure system inside the VM. Lets make sure that `mc`
package is installed in all the templates. Similar to previous example, you
need to create state file (`/srv/salt/mc-everywhere.sls`):

    mc:
      pkg.installed: []

Then appropriate top file (`/srv/salt/mc-everywhere.top`):

    base:
     qubes:type:template:
        - match: pillar
        - mc-everywhere

Now you need to enable the configuration:

    qubesctl top.enable mc-everywhere

And apply the configuration:

    qubesctl --all state.highstate


## All Qubes-specific states


### qvm.present

As in example above, it creates domain and sets its properties.

### qvm.prefs

You can set properties of existing domain:

    my preferences:
      qvm.prefs:
        - name: salt-test2
        - netvm: sys-firewall

Note that `name:` is a matcher, ie. it says the domain which properties will be
manipulated is called `salt-test2`. The implies that you currently cannot rename
domains this way.

### qvm.service

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

This enables, disables, or sets to default, the services as in qvm-service.

### qvm.running


Ensures the domain is running:

    domain is running:
      qvm.running:
        - name: salt-test4

## qubes pillar module

Additional pillar data is available to ease targeting configuration (for
example all the templates). List here may be subject to changes in future
releases.

### qubes:type

VM type. Possible values:

 - `admin` - administration domain (`dom0`)
 - `template` - Template VM
 - `standalone` - Standalone VM
 - `app` - template based AppVM

### qubes:template

Template name on which given VM is based (if any).

### qubes:netvm

VM which provides network to the given VM

## Debugging
The output for each vm is logged in `/var/log/qubes/mgmt-VM_NAME.log`.

If the log does not contain useful information, you can stop `qubesctl` by 
pressing `ctrl+z`.

You need to:
1. run `sudo qubesctl --skip-dom0 --target=VM_NAME state.highstate`
2. When your vm is being started (yellow) press Ctrl-Z on qubesctl.
3. Open terminal in disp-mgmt-VM_NAME.
4. Look at /etc/qubes-rpc/qubes.SaltLinuxVM - this is what is 
   executed in the management vm.
5. Get the last two lines:

    export PATH="/usr/lib/qubes-vm-connector/ssh-wrapper:$PATH"
    salt-ssh "$target_vm" $salt_command

  Adjust $target_vm (VM_NAME) and $salt_command (state.highstate).
6. Execute them, fix problems, repeat.

## Known pitfalls

### Using fedora-24-minimal
The fedora-24-minimal package is missing the sudo package.
You can install it via:

    qvm-run -p vmname 'dnf install -y sudo'
    
The `-p` is will cause the execution to wait until the package is installed.
This is important when using a state with `cmd.run`.

### Disk quota exceeded (when installing templates)
If you install multiple templates you may encounter this error.
The solution is to shut down the updatevm between each install.
E.g.:

{% raw %}
    install template and shutdown updatevm:
      cmd.run:
      - name: sudo qubes-dom0-update -y fedora-24; qvm-shutdown {{salt.cmd.run(qubes-prefs updatevm) }}
{% endraw %}

## Further reading

* [Salt documentation][salt-doc]
* [Salt states][salt-doc-states] ([files][salt-doc-states-file], [commands][salt-doc-states-cmd], 
  [packages][salt-doc-states-pkg], [ordering][salt-doc-states-order])
* [Top files][salt-doc-top]
* [Jinja templates][jinja]
* [Qubes specific modules][salt-qvm-doc]
* [Formula for default Qubes VMs][salt-virtual-machines-doc] ([and actual states][salt-virtual-machines-states])

[salt-doc]: https://docs.saltstack.com/en/latest/
[salt-qvm-doc]: https://github.com/QubesOS/qubes-mgmt-salt-dom0-qvm/blob/master/README.rst
[salt-virtual-machines-doc]: https://github.com/QubesOS/qubes-mgmt-salt-dom0-virtual-machines/blob/master/README.rst
[salt-virtual-machines-states]: https://github.com/QubesOS/qubes-mgmt-salt-dom0-virtual-machines/tree/master/qvm
[salt-doc-states]: https://docs.saltstack.com/en/latest/ref/states/all/
[salt-doc-states-file]: https://docs.saltstack.com/en/latest/ref/states/all/salt.states.file.html
[salt-doc-states-pkg]: https://docs.saltstack.com/en/latest/ref/states/all/salt.states.pkg.html
[salt-doc-states-cmd]: https://docs.saltstack.com/en/latest/ref/states/all/salt.states.file.html
[salt-doc-states-order]: https://docs.saltstack.com/en/latest/ref/states/ordering.html
[salt-doc-states-req]: https://docs.saltstack.com/en/latest/ref/states/requisites.html
[salt-doc-states-ord]: https://docs.saltstack.com/en/latest/ref/states/ordering.html#the-order-option
[salt-doc-top]:https://docs.saltstack.com/en/latest/ref/states/top.html
[jinja]: http://jinja.pocoo.org/
[jinja-tmp]: http://jinja.pocoo.org/docs/2.9/templates/
[jinja-call-salt-functions]: https://docs.saltstack.com/en/getstarted/config/jinja.html#get-data-using-salt
