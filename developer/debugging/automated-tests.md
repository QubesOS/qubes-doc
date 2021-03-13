---
layout: doc
permalink: /doc/automated-tests/
redirect_from:
- /en/doc/automated-tests/
- /doc/AutomatedTests/
title: Automated Tests
---

# Automated Tests

## Unit and Integration Tests

Starting with Qubes R3 we use [python unittest][unittest] to perform automatic tests of Qubes OS.
Despite the name, we use it for both [unit tests](https://en.wikipedia.org/wiki/Unit_tests) and [integration tests](https://en.wikipedia.org/wiki/Integration_tests).
The main purpose is, of course, to deliver much more stable releases.

The integration tests must be run in dom0, but some unit tests can run inside a VM as well.

### Integration & unit testing in dom0

Integration tests are written with the assumption that they will be executed on dedicated hardware and must be run in dom0. All other unit tests can also be run in dom0.

**Do not run the tests on installations with important data, because you might lose it.**

All the VMs with a name starting with `test-` on the installation are removed during the process, and all the tests are recklessly started from dom0, even when testing (& possibly breaking) VM components.

First you need to build all packages that you want to test. Please do not mix branches as this will inevitably lead to failures. Then setup Qubes OS with these packages installed.

For testing you'll have to stop the `qubesd` service as the tests will use its own custom variant of the service:
`sudo systemctl stop qubesd`

Don't forget to start it after testing again.

To start testing you can then use the standard python unittest runner:

`sudo -E python3 -m unittest -v qubes.tests`

Alternatively, use the custom Qubes OS test runner:

`sudo -E python3 -m qubes.tests.run -v`

Our test runner runs mostly the same as the standard one, but it has some nice additional features like colored output and not needing the "qubes.test" prefix.

You can use `python3 -m qubes.tests.run -h` to get usage information:

```
    [user@dom0 ~]$ python3 -m qubes.tests.run -h
    usage: run.py [-h] [--verbose] [--quiet] [--list] [--failfast] [--no-failfast]
                  [--do-not-clean] [--do-clean] [--loglevel LEVEL]
                  [--logfile FILE] [--syslog] [--no-syslog] [--kmsg] [--no-kmsg]
                  [TESTNAME [TESTNAME ...]]

    positional arguments:
      TESTNAME              list of tests to run named like in description
                            (default: run all tests)

    optional arguments:
      -h, --help            show this help message and exit
      --verbose, -v         increase console verbosity level
      --quiet, -q           decrease console verbosity level
      --list, -l            list all available tests and exit
      --failfast, -f        stop on the first fail, error or unexpected success
      --no-failfast         disable --failfast
      --loglevel LEVEL, -L LEVEL
                            logging level for file and syslog forwarding (one of:
                            NOTSET, DEBUG, INFO, WARN, WARNING, ERROR, CRITICAL;
                            default: DEBUG)
      --logfile FILE, -o FILE
                            if set, test run will be also logged to file
      --syslog              reenable logging to syslog
      --no-syslog           disable logging to syslog
      --kmsg, --very-brave-or-very-stupid
                            log most important things to kernel ring-buffer
      --no-kmsg, --i-am-smarter-than-kay-sievers
                            do not abuse kernel ring-buffer
      --allow-running-along-qubesd
                            allow running in parallel with qubesd; this is
                            DANGEROUS and WILL RESULT IN INCONSISTENT SYSTEM STATE
      --break-to-repl       break to REPL after tests

    When running only specific tests, write their names like in log, in format:
    MODULE+"/"+CLASS+"/"+FUNCTION. MODULE should omit initial "qubes.tests.".
    Example: basic/TC_00_Basic/test_000_create
```

For instance, to run only the tests for the fedora-21 template, you can use the `-l` option, then filter the list:

```
    [user@dom0 ~]$ python3 -m qubes.tests.run -l | grep fedora-21
    network/VmNetworking_fedora-21/test_000_simple_networking
    network/VmNetworking_fedora-21/test_010_simple_proxyvm
    network/VmNetworking_fedora-21/test_020_simple_proxyvm_nm
    network/VmNetworking_fedora-21/test_030_firewallvm_firewall
    network/VmNetworking_fedora-21/test_040_inter_vm
    vm_qrexec_gui/TC_00_AppVM_fedora-21/test_000_start_shutdown
    vm_qrexec_gui/TC_00_AppVM_fedora-21/test_010_run_gui_app
    vm_qrexec_gui/TC_00_AppVM_fedora-21/test_050_qrexec_simple_eof
    vm_qrexec_gui/TC_00_AppVM_fedora-21/test_051_qrexec_simple_eof_reverse
    vm_qrexec_gui/TC_00_AppVM_fedora-21/test_052_qrexec_vm_service_eof
    vm_qrexec_gui/TC_00_AppVM_fedora-21/test_053_qrexec_vm_service_eof_reverse
    vm_qrexec_gui/TC_00_AppVM_fedora-21/test_060_qrexec_exit_code_dom0
    vm_qrexec_gui/TC_00_AppVM_fedora-21/test_065_qrexec_exit_code_vm
    vm_qrexec_gui/TC_00_AppVM_fedora-21/test_100_qrexec_filecopy
    vm_qrexec_gui/TC_00_AppVM_fedora-21/test_110_qrexec_filecopy_deny
    vm_qrexec_gui/TC_00_AppVM_fedora-21/test_120_qrexec_filecopy_self
    vm_qrexec_gui/TC_20_DispVM_fedora-21/test_000_prepare_dvm
    vm_qrexec_gui/TC_20_DispVM_fedora-21/test_010_simple_dvm_run
    vm_qrexec_gui/TC_20_DispVM_fedora-21/test_020_gui_app
    vm_qrexec_gui/TC_20_DispVM_fedora-21/test_030_edit_file
    [user@dom0 ~]$ sudo -E python3 -m qubes.tests.run -v `python3 -m qubes.tests.run -l | grep fedora-21`
```

Example test run:

![snapshot-tests2.png](/attachment/wiki/developers/snapshot-tests2.png)

Tests are also compatible with nose2 test runner, so you can use this instead:

```bash
    sudo systemctl stop qubesd; sudo -E nose2 -v --plugin nose2.plugins.loader.loadtests qubes.tests; sudo systemctl start qubesd
```

This may be especially useful together with various nose2 plugins to store tests results (for example `nose2.plugins.junitxml`), to ease presenting results. This is what we use on [OpenQA].

### Unit testing inside a VM

Many unit tests will also work inside a VM. However all of the tests requiring a dedicated VM to be run (mostly the integration tests) will be skipped.

Whereas integration tests are mostly stored in the [qubes-core-admin](https://github.com/QubesOS/qubes-core-admin) repository, unit tests can be found in each of the Qubes OS repositories.

To for example run the `qubes-core-admin` unit tests, you currently have to clone at least [qubes-core-admin](https://github.com/QubesOS/qubes-core-admin) and
its dependency [qubes-core-qrexec](https://github.com/QubesOS/qubes-core-qrexec) repository in the branches that you want to test.

The below example however will assume that you set up a build environment as described in the [Qubes Builder documentation](/doc/qubes-builder/).

Assuming you cloned the `qubes-builder` repository to your home directory inside a fedora VM, you can use the following commands to run the unit tests:

```{.bash}
cd ~
sudo dnf install python3-pip lvm2 python35 python3-virtualenv
virtualenv -p /usr/bin/python35 python35
source python35/bin/activate
python3 -V
cd ~/qubes-builder/qubes-src/core-admin
pip3 install -r ci/requirements.txt
export PYTHONPATH=../core-qrexec:test-packages
./run-tests
```

To run only the tests related to e.g. `lvm`, you may use:

`./run-tests -v $(python3 -m qubes.tests.run -l | grep lvm)`

You can later re-use the created virtual environment including all of the via `pip3` installed packages with `source ~/python35/bin/activate`.

We recommend to run the unit tests with the Python version that the code is meant to be run with in dom0 (3.5 was just an example above). For instance, the `release4.0` (Qubes 4.0) branch is intended
to be run with Python 3.5 whereas the Qubes 4.1 branch (`master` as of 2020-07) is intended to be run with Python 3.7 or higher. You can always check your dom0 installation for the Python version of
the current stable branch.

### Tests configuration

Test runs can be altered using environment variables:

- `DEFAULT_LVM_POOL` - LVM thin pool to use for tests, in `VolumeGroup/ThinPool` format
- `QUBES_TEST_PCIDEV` - PCI device to be used in PCI passthrough tests (for example sound card)
- `QUBES_TEST_TEMPLATES` - space separated list of templates to run tests on; if not set, all installed templates are tested
- `QUBES_TEST_LOAD_ALL` - load all tests (including tests for all templates) when relevant test modules are imported; this needs to be set for test runners not supporting [load_tests protocol](https://docs.python.org/3/library/unittest.html#load-tests-protocol)

### Adding a new test to core-admin

After adding a new unit test to [core-admin/qubes/tests](https://github.com/QubesOS/qubes-core-admin/tree/master/qubes/tests) you'll have to include it in [core-admin/qubes/tests/\_\_init\_\_.py](https://github.com/QubesOS/qubes-core-admin/tree/master/qubes/tests/__init__.py)

#### Editing `__init__.py`

You'll also need to add your test at the bottom of the `__init__.py` file, in the method `def load_tests`, in the for loop with `modname`.
Again, given the hypothetical `example.py` test:

~~~python
    for modname in (
            'qubes.tests.basic',
            'qubes.tests.dom0_update',
            'qubes.tests.network',
            'qubes.tests.vm_qrexec_gui',
            'qubes.tests.backup',
            'qubes.tests.backupcompatibility',
            'qubes.tests.regressions',
            'qubes.tests.example', # This is our newly added test
            ):
~~~

### Testing PyQt applications

When testing (Py)QT applications, it's useful to create a separate QApplication object for each test.
But QT framework does not allow multiple QApplication objects in the same process at the same time.
This means it's critical to reliably cleanup the previous instance before creating a new one.
This turns out to be a non-trivial task, especially if _any_ test uses the event loop.
Failure to perform proper cleanup in many cases results in SEGV.
Below you can find steps for the proper cleanup:

~~~python
import asyncio
import quamash
import unittest
import gc

class SomeTestCase(unittest.TestCase):
    def setUp(self):
        [...]

        # force "cleanlooks" style, the default one on Xfce (GtkStyle) use
        # static variable internally and caches pointers to later destroyed
        # objects (result: SEGV)
        self.qtapp = QtGui.QApplication(["test", "-style", "cleanlooks"])

        # construct event loop even if this particular test doesn't use it,
        # otherwise events with qtapp references will be queued there anyway and the
        # first test that actually use event loop will try to dereference (already
        # destroyed) objects, resulting in SEGV
        self.loop = quamash.QEventLoop(self.qtapp)

    def tearDown(self):
        [...]
        # process any pending events before destroying the object
        self.qtapp.processEvents()

        # queue destroying the QApplication object, do that for any other QT
        # related objects here too
        self.qtapp.deleteLater()

        # process any pending events (other than just queued destroy), just in case
        self.qtapp.processEvents()

        # execute main loop, which will process all events, _including just queued destroy_
        self.loop.run_until_complete(asyncio.sleep(0))

        # at this point it QT objects are destroyed, cleanup all remaining references;
        # del other QT object here too
        self.loop.close()
        del self.qtapp
        del self.loop
        gc.collect()
~~~

## Installation Tests with openQA

**URL:** <https://openqa.qubes-os.org/>

**Tests:** <https://github.com/marmarek/openqa-tests-qubesos>

Manually testing the installation of Qubes OS is a time-consuming process.
We use [openQA] to automate this process.
It works by installing Qubes in KVM and interacting with it as a user would, including simulating mouse clicks and keyboard presses.
Then, it checks the output to see whether various tests were passed, e.g. by comparing the virtual screen output to screenshots of a successful installation.

Using openQA to automatically test the Qubes installation process works as of Qubes 4.0-rc4 on 2018-01-26, provided that the versions of KVM and QEMU are new enough and the hardware has VT-x and EPT.
KVM also supports nested virtualization, so HVM should theoretically work.
In practice, however, either Xen or QEMU crashes when this is attempted.
Nonetheless, PV works well, which is sufficient for automated installation testing.

Thanks to an anonymous donor, our openQA system is hosted in a datacenter on hardware that meets these requirements.

[unittest]: https://docs.python.org/3/library/unittest.html
[OpenQA]: http://open.qa/
