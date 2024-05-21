==========================
Salt (management software)
==========================


Since the Qubes R3.1 release we have included the Salt (also called
SaltStack) management engine in dom0 as default (with some states
already configured). Salt allows administrators to easily configure
their systems. In this guide we will show how it is set up and how you
can modify it for your own purpose.

In the current form the **API is provisional** and subject to change
between *minor* releases.

Understanding Salt
------------------


This document is not meant to be comprehensive Salt documentation;
however, before writing anything it is required you have at least *some*
understanding of basic Salt-related vocabulary. For more exhaustive
documentation, visit `official site <https://docs.saltproject.io/en/latest/>`__, though we must warn
you that it is not easy to read if you just start working with Salt and
know nothing.

The Salt Architecture
^^^^^^^^^^^^^^^^^^^^^


Salt is a client-server model, where the server (called *master*)
manages its clients (called *minions*). In typical situations, it is
intended that the administrator interacts only with the master and keeps
the configurations there. In Qubes, we don’t have a master. Instead we
have one minion which resides in ``dom0`` and manages qubes from there.
This setup is also supported by Salt.

Salt is a management engine (similar to Ansible, Puppet, and Chef), that
enforces a particular state of a minion system. A *state* is an end
effect *declaratively* expressed by the administrator. This is the most
important concept in the entire engine. All configurations (i.e., the
states) are written in YAML.

A *pillar* is a data back-end declared by the administrator. When states
become repetitive, instead of pure YAML they can be written using a
template engine (preferably Jinja2); which can use data structures
specified in pillars.

A *formula* is a ready to use, packaged solution that combines a state
and a pillar (possibly with some file templates and other auxiliary
files). There are many formulas made by helpful people all over the
Internet.

A *grain* is some data that is also available in templates, but its
value is not directly specified by administrator. For example, the
distribution (e.g., ``"Debian"`` or ``"Gentoo"``) is a value of the
grain ``"os"``. It also contains other information about the kernel,
hardware, etc.

A *module* is a Python extension to Salt that is responsible for
actually enforcing the state in a particular area. It exposes some
*imperative* functions for the administrator. For example, there is a
``system`` module that has a ``system.halt`` function that, when issued,
will immediately halt a domain.

In salt, there are different levels of functionality. The lowest level
is a single state function, called like this
``state.single pkg.installed name=firefox-esr`` When the system compiles
data from sls formulas, it generates *chunks* - low chunks are at the
bottom of the compiler . You can call them with ``state.low`` Next up is
the *lowstate* level - this is the list of all low chunks in order. - To
see them you have ``state.show_lowstate``, and use ``state.lowstate`` to
apply them. At the top level is *highstate* - this is an interpretation
of **all** the data represented in YAML in sls files. You can view it
with ``state.show_highstate``.

When you want to apply a configuration, you can use
``qubesctl state.highstate.`` This will apply all the states you have
included in highstate.

There is another function, ``state.apply``; ``state.apply`` has two
uses. When used on its own, it will apply *highstate* - all the
configuration that has been enabled. It can also be used to apply a
specific state, like this: ``state.apply browser`` - this will apply the
state specified in ``browser.sls``.

For simplicity we will use ``state.apply`` through this page, when we
want to apply all configured states.

Configuration
^^^^^^^^^^^^^


States
^^^^^^


The smallest unit of configuration is a state. A state is written in
YAML and looks like this:

.. code:: bash

      stateid:
        cmd.run:  #this is the execution module. in this case it will execute a command on the shell
        - name: echo 'hello world' #this is a parameter of the state.



The stateid has to be unique throughout all states running for a minion
and can be used to order the execution of the references state.
``cmd.run`` is an execution module. It executes a command on behalf of
the administrator. ``name: echo 'hello world'`` is a parameter for the
execution module ``cmd.run``. The module used defines which parameters
can be passed to it.

There is a list of `officially available states <https://docs.saltproject.io/en/latest/ref/states/all/>`__. There
are many very useful states:

- For `managing files <https://docs.saltproject.io/en/latest/ref/states/all/salt.states.file.html>`__:
  Use this to create files or directories and change them (append
  lines, replace text, set their content etc.)

- For `installing and uninstalling <https://docs.saltproject.io/en/latest/ref/states/all/salt.states.pkg.html>`__
  packages.

- For `executing shell commands <https://docs.saltproject.io/en/latest/ref/states/all/salt.states.cmd.html>`__.



With these three states you can define most of the configuration of a
VM.

You can also `order the execution <https://docs.saltproject.io/en/latest/ref/states/ordering.html>`__
of your states:

.. code:: bash

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



The order of execution will be ``A, B, C, D``. The official
documentation has more details on the
`require <https://docs.saltproject.io/en/latest/ref/states/requisites.html>`__
and
`order <https://docs.saltproject.io/en/latest/ref/states/ordering.html#the-order-option>`__
arguments.

State Files
^^^^^^^^^^^


When configuring a system you will write one or more state files
(``*.sls``) and put (or symlink) them into the main Salt directory
``/srv/salt/``. Each state file contains multiple states and should
describe some unit of configuration (e.g., a state file ``mail.sls``
could setup a qube for e-mail).

Top Files
^^^^^^^^^


After you have several state files, you need something to assign them to
a qube. This is done by ``*.top`` files (`official documentation <https://docs.saltproject.io/en/latest/ref/states/top.html>`__).
Their structure looks like this:

.. code:: bash

      environment:
        target_matching_clause:
        - statefile1
        - folder2.statefile2



In most cases, the environment will be called ``base``. The
``target_matching_clause`` will be used to select your minions
(Templates or qubes). It can be either the name of a qube or a regular
expression. If you are using a regular expressions, you need to give
Salt a hint you are doing so:

.. code:: bash

      environment:
        ^app-(work|(?!mail).*)$:
        - match: pcre
        - statefile



For each target you can write a list of state files. Each line is a path
to a state file (without the ``.sls`` extension) relative to the main
directory. Each ``/`` is exchanged with a ``.``, so you can’t reference
files or directories with a ``.`` in their name.

Enabling Top Files and Applying the States
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Now, because we use custom extensions to manage top files (instead of
just enabling them all), to enable a particular top file you should
issue command:

.. code:: bash

      $ qubesctl top.enable my-new-vm



To list all enabled top files:

.. code:: bash

      $ qubesctl top.enabled



And to disable one:

.. code:: bash

      $ qubesctl top.disable my-new-vm



To apply the states to dom0 and all VMs:

.. code:: bash

      $ qubesctl --all state.apply



(More information on the ``qubesctl`` command further down.)

Template Files
^^^^^^^^^^^^^^


You will sometimes find yourself writing repetitive states. To solve
this, there is the ability to template files or states. This is most
commonly done with `Jinja <https://palletsprojects.com/p/jinja/>`__.
Jinja is similar to Python and in many cases behaves in a similar
fashion, but there are sometimes differences when, for example, you set
some variable inside a loop: the variable outside will not get changed.
Instead, to get this behavior, you would use a ``do`` statement. So you
should take a look at the `Jinja API documentation <https://jinja.palletsprojects.com/templates/>`__.
Documentation about using Jinja to directly call Salt functions and get
data about your system can be found in the official `Salt documentation <https://docs.saltproject.io/en/getstarted/config/jinja.html#get-data-using-salt>`__.

Salt Configuration, QubesOS layout
----------------------------------


All Salt configuration files are in the ``/srv/`` directory, as usual.
The main directory is ``/srv/salt/`` where all state files reside.
States are contained in ``*.sls`` files. However, the states that are
part of the standard Qubes distribution are mostly templates and the
configuration is done in pillars from formulas.

The formulas are in ``/srv/formulas``, including stock formulas for
domains in ``/srv/formulas/dom0/virtual-machines-formula/qvm``, which
are used by first boot.

Because we use some code that is not found in older versions of Salt,
there is a tool called ``qubesctl`` that should be run instead of
``salt-call --local``. It accepts all the same arguments of the vanilla
tool.

Configuring a qube's System from Dom0
-------------------------------------


Salt can be used to configure qubes from dom0. Simply set the qube name
as the target minion name in the top file. You can also use the
``qubes`` pillar module to select qubes with a particular property (see
below). If you do so, then you need to pass additional arguments to the
``qubesctl`` tool:

.. code:: bash

      usage: qubesctl [-h] [--show-output] [--force-color] [--skip-dom0]
                      [--targets TARGETS | --templates | --app | --all]
                      ...
      
      positional arguments:
        command            Salt command to execute (e.g., state.apply)
      
      optional arguments:
        -h, --help         show this help message and exit
        --show-output      Show output of management commands
        --force-color      Force color output, allow control characters from VM,
                           UNSAFE
        --skip-dom0        Skip dom0 configuration (VM creation etc)
        --targets TARGETS  Coma separated list of VMs to target
        --templates        Target all templates
        --app              Target all app qubes
        --all              Target all non-disposables (templates and app qubes)



To apply a state to all templates, call
``qubesctl --templates state.apply``.

The actual configuration is applied using ``salt-ssh`` (running over
``qrexec`` instead of ``ssh``). Which means you don’t need to install
anything special in a qube you want to manage. Additionally, for each
target qube, ``salt-ssh`` is started from a temporary qube. This way
dom0 doesn’t directly interact with potentially malicious target qubes;
and in the case of a compromised Salt qube, because they are temporary,
the compromise cannot spread from one qube to another.

Beginning with Qubes 4.0 and after `QSB #45 <https://www.qubes-os.org/news/2018/12/03/qsb-45/>`__, we implemented two changes:

1. Added the ``management_dispvm`` qube property, which specifies the
   disposable Template that should be used for management, such as Salt
   configuration. App qubes inherit this property from their parent
   templates. If the value is not set explicitly, the default is taken
   from the global ``management_dispvm`` property. The qube-specific
   property is set with the ``qvm-prefs`` command, while the global
   property is set with the ``qubes-prefs`` command.

2. Created the ``default-mgmt-dvm`` disposable template, which is hidden
   from the menu (to avoid accidental use), has networking disabled, and
   has a black label (the same as templates). This qube is set as the
   global ``management_dispvm``. Keep in mind that this disposable
   template has full control over the qubes it’s used to manage.



Writing Your Own Configurations
-------------------------------


Let’s start with a quick example:

.. code:: bash

      my new and shiny VM:
        qvm.present:
          - name: salt-test # can be omitted when same as ID
          - template: fedora-21
          - label: yellow
          - mem: 2000
          - vcpus: 4
          - flags:
            - proxy



It uses the Qubes-specific ``qvm.present`` state, which ensures that the
qube is present (if not, it creates it).

- The ``name`` flag informs Salt that the qube should be named
  ``salt-test`` (not ``my new and shiny VM``).

- The ``template`` flag informs Salt which template should be used for
  the qube.

- The ``label`` flag informs Salt what color the qube should be.

- The ``mem`` flag informs Salt how much RAM should be allocated to the
  qube.

- The ``vcpus`` flag informs Salt how many Virtual CPUs should be
  allocated to the qube

- The ``proxy`` flag informs Salt that the qube should be a ProxyVM.



As you will notice, the options are the same (or very similar) to those
used in ``qvm-prefs``.

This should be put in ``/srv/salt/my-new-vm.sls`` or another ``.sls``
file. A separate ``*.top`` file should be also written:

.. code:: bash

      base:
        dom0:
          - my-new-vm



**Note** The third line should contain the name of the previous state
file, without the ``.sls`` extension.

To enable the particular top file you should issue the command:

.. code:: bash

      $ qubesctl top.enable my-new-vm



To apply the state:

.. code:: bash

      $ qubesctl state.apply



Example of Configuring Templates from Dom0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Lets make sure that the ``mc`` package is installed in all templates.
Similar to the previous example, you need to create a state file
(``/srv/salt/mc-everywhere.sls``):

.. code:: bash

      mc:
        pkg.installed: []



Then the appropriate top file (``/srv/salt/mc-everywhere.top``):

.. code:: bash

      base:
       qubes:type:template:
          - match: pillar
          - mc-everywhere



Now you need to enable the top file:

.. code:: bash

      $ qubesctl top.enable mc-everywhere



And apply the configuration:

.. code:: bash

      $ qubesctl --all state.apply



All Qubes-specific States
-------------------------


``qvm.present``
^^^^^^^^^^^^^^^


As in the example above, it creates a qube and sets its properties.

``qvm.prefs``
^^^^^^^^^^^^^


You can set properties of an existing qube:

.. code:: bash

      my preferences:
        qvm.prefs:
          - name: salt-test2
          - netvm: sys-firewall



**Note** The ``name:`` option will not change the name of a qube, it
will only be used to match a qube to apply the configurations to it.

``qvm.service``
^^^^^^^^^^^^^^^


.. code:: bash

      services in my qube:
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



This enables, disables, or sets to default, services as in
``qvm-service``.

``qvm.running``
^^^^^^^^^^^^^^^


Ensures the specified qube is running:

.. code:: bash

      qube is running:
        qvm.running:
          - name: salt-test4



Virtual Machine Formulae
------------------------


You can use these formulae to download, install, and configure qubes in
Qubes. These formulae use pillar data to define default qube names and
configuration details. The default settings can be overridden in the
pillar data located in:

.. code:: bash

      /srv/pillar/base/qvm/init.sls



In dom0, you can apply a single state with
``sudo qubesctl state.sls STATE_NAME``. For example,
``sudo qubesctl state.sls qvm.personal`` will create a ``personal`` qube
(if it does not already exist) with all its dependencies (template,
``sys-firewall``, and ``sys-net``).

Available states
^^^^^^^^^^^^^^^^


``qvm.sys-net``
^^^^^^^^^^^^^^^


System NetVM

``qvm.sys-usb``
^^^^^^^^^^^^^^^


System USB qube

``qvm.sys-net-as-usbvm``
^^^^^^^^^^^^^^^^^^^^^^^^


System USB qube bundled into NetVM. Do not enable together with
``qvm.sys-usb``.

``qvm.usb-keyboard``
^^^^^^^^^^^^^^^^^^^^


Enable USB keyboard together with USB qube, including for early system
boot (for LUKS passhprase). This state implicitly creates a USB qube
(``qvm.sys-usb`` state), if not already done.

``qvm.sys-firewall``
^^^^^^^^^^^^^^^^^^^^


System firewall ProxyVM

``qvm.sys-whonix``
^^^^^^^^^^^^^^^^^^


Whonix gateway ProxyVM

``qvm.personal``
^^^^^^^^^^^^^^^^


Personal app qube

``qvm.work``
^^^^^^^^^^^^


Work app qube

``qvm.untrusted``
^^^^^^^^^^^^^^^^^


Untrusted app qube

``qvm.vault``
^^^^^^^^^^^^^


Vault app qube with no NetVM enabled.

``qvm.default-dispvm``
^^^^^^^^^^^^^^^^^^^^^^


Default disposable template - fedora-26-dvm app qube

``qvm.anon-whonix``
^^^^^^^^^^^^^^^^^^^


Whonix workstation app qube.

``qvm.whonix-ws-dvm``
^^^^^^^^^^^^^^^^^^^^^


Whonix workstation app qube for Whonix disposables.

``qvm.updates-via-whonix``
^^^^^^^^^^^^^^^^^^^^^^^^^^


Setup UpdatesProxy to route all templates updates through Tor
(sys-whonix here).

``qvm.template-fedora-21``
^^^^^^^^^^^^^^^^^^^^^^^^^^


Fedora-21 template

``qvm.template-fedora-21-minimal``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Fedora-21 minimal template

``qvm.template-debian-7``
^^^^^^^^^^^^^^^^^^^^^^^^^


Debian 7 (wheezy) template

``qvm.template-debian-8``
^^^^^^^^^^^^^^^^^^^^^^^^^


Debian 8 (jessie) template

``qvm.template-whonix-gw``
^^^^^^^^^^^^^^^^^^^^^^^^^^


Whonix Gateway template

``qvm.template-whonix-ws``
^^^^^^^^^^^^^^^^^^^^^^^^^^


Whonix Workstation template

``update.qubes-dom0``
^^^^^^^^^^^^^^^^^^^^^


Updates dom0. Example (executed in dom0):

.. code:: bash

      $ sudo qubesctl --show-output state.sls update.qubes-dom0



``update.qubes-vm``
^^^^^^^^^^^^^^^^^^^


Updates domUs. Example to update all templates (executed in dom0):

.. code:: bash

      $ sudo qubesctl --show-output --skip-dom0 --templates state.sls update.qubes-vm



Useful options:

- ``--max-concurrency`` — Limits how many templates are updated at the
  same time. Adjust to your available RAM. The default is 4, and the
  GUI updater sets it to 1.

- ``--targets=vm1,vm2,...`` — Limit to specific qubes, instead of all
  of them. (Use instead of ``--templates`` or ``--standalones``.)

- ``--show-output`` — Show an update summary instead of just OK/FAIL.



For other options, see ``qubesctl --help``.

The ``qubes`` Pillar Module
---------------------------


Additional pillar data is available to ease targeting configurations
(for example all templates).

**Note:** This list is subject to change in future releases.

``qubes:type``
^^^^^^^^^^^^^^


qube type. Possible values:

- ``admin`` - Administration qube (``dom0``)

- ``template`` - template

- ``standalone`` - Standalone qube

- ``app`` - Template based app qube



``qubes:template``
^^^^^^^^^^^^^^^^^^


Template name on which a given qube is based (if any).

``qubes:netvm``
^^^^^^^^^^^^^^^


qube which provides network to the given qube

Debugging
---------


The output for each qube is logged in
``/var/log/qubes/mgmt-VM_NAME.log``.

If the log does not contain useful information: 1. Run
``sudo qubesctl --skip-dom0 --target=VM_NAME state.apply`` 2. When your
qube is being started (yellow) press Ctrl-z on qubesctl. 3. Open
terminal in disp-mgmt-qube_NAME. 4. Look at
/etc/qubes-rpc/qubes.SaltLinuxVM - this is what is executed in the
management qube. 5. Get the last two lines:

.. code:: bash

      ```
      $ export PATH="/usr/lib/qubes-vm-connector/ssh-wrapper:$PATH"
      $ salt-ssh "$target_vm" $salt_command
      ```


Adjust $target_vm (VM_NAME) and $salt_command (state.apply). 6. Execute
them, fix problems, repeat.

Known Pitfalls
--------------


Using fedora-24-minimal
^^^^^^^^^^^^^^^^^^^^^^^


The fedora-24-minimal package is missing the ``sudo`` package. You can
install it via:

.. code:: bash

      $ qvm-run -p -u root fedora-24-minimal-template 'dnf install -y sudo'


The ``-p`` will cause the execution to wait until the package is
installed. Having the ``-p`` flag is important when using a state with
``cmd.run``.

Disk Quota Exceeded (When Installing Templates)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If you install multiple templates you may encounter this error. The
solution is to shut down the updateVM between each install:

.. code:: bash

      install template and shutdown updateVM:
        cmd.run:
        - name: sudo qubes-dom0-update -y fedora-24; qvm-shutdown {% raw %}{{ salt.cmd.run(qubes-prefs updateVM) }}{% endraw %}



Further Reading
---------------


- `Salt documentation <https://docs.saltproject.io/en/latest/>`__

- `Salt states <https://docs.saltproject.io/en/latest/ref/states/all/>`__
  (`files <https://docs.saltproject.io/en/latest/ref/states/all/salt.states.file.html>`__,
  `commands <https://docs.saltproject.io/en/latest/ref/states/all/salt.states.cmd.html>`__,
  `packages <https://docs.saltproject.io/en/latest/ref/states/all/salt.states.pkg.html>`__,
  `ordering <https://docs.saltproject.io/en/latest/ref/states/ordering.html>`__)

- `Top files <https://docs.saltproject.io/en/latest/ref/states/top.html>`__

- `Jinja templates <https://palletsprojects.com/p/jinja/>`__

- `Qubes specific modules <https://github.com/QubesOS/qubes-mgmt-salt-dom0-qvm/blob/master/README.rst>`__

- `Formulas for default Qubes qubes <https://github.com/QubesOS/qubes-mgmt-salt-dom0-virtual-machines/tree/master/qvm>`__


