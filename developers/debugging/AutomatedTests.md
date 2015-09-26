---
layout: doc
title: Automated tests
permalink: /doc/AutomatedTests/
---

Automatic tests
===============

Starting with Qubes R3 we use [python unittest](TODO) to perform automatic
tests of Qubes OS. Regardless of the name, we use it for both [unit
tests](https://en.wikipedia.org/wiki/Unit_tests) and [integration
tests](https://en.wikipedia.org/wiki/Integration_tests). The main purpose is of
course to deliver much more stable releases.

Integration tests are written with assumption to be called on dedicated
hardware. **Do not run those test on machine where you have important data, you
can loose it**. Especially all the VMs with name starting with `test-` are
removed. All the tests are started from dom0, even when testing some VM
component. Those tests will create new VM(s), run the test, then remove the VM(s).

Most of the tests are stored in [core-admin
repository](https://github.com/QubesOS/qubes-core-admin/tree/master/tests) in
`tests` directory. To start them you can use standard python unittest runner:
    python -m unittest -v qubes.tests
Or our custom one:
    python -m qubes.tests.run -v

Our test runner can be used mostly the same as the standard one, with some nice
additional features like no need to prefix all the tests with "qubes.tests", or
color output. It is also the only way to run only selected template tests.

You can use `python -m qubes.tests.run -h` to get usage information:

    [user@dom0 ~]$ python -m qubes.tests.run -h
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
      --do-not-clean, --dnc, -D
                            do not execute tearDown on failed tests. Implies
                            --failfast.
      --do-clean, -C        do execute tearDown even on failed tests.
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

    When running only specific tests, write their names like in log, in format:
    MODULE+"/"+CLASS+"/"+FUNCTION. MODULE should omit initial "qubes.tests.".
    Example: basic/TC_00_Basic/test_000_create

For example to run only tests for fedora-21 template, you can use `-l` option, then filter the list:

    [user@dom0 ~]$ python -m qubes.tests.run -l | grep fedora-21
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
    [user@dom0 ~]$ python -m qubes.tests.run -v `python -m qubes.tests.run -l | grep fedora-21`


## Adding a new test to core-admin
After you added a new unit test to [core-admin/tests](https://github.com/QubesOS/qubes-core-admin/tree/master/tests) 
you have to make sure of two things:

1. The test will be added to the RPM file created by [QubesBuilder](/doc/QubesBuilder/) 
For this you need to edit [core-admin/tests/Makefile](https://github.com/QubesOS/qubes-core-admin/tree/master/tests/Makefile)
2. The test will be loaded by [core-admin/tests/\_\_init\_\_.py](https://github.com/QubesOS/qubes-core-admin/tree/master/tests/__init__.py)

### Editing the  Makefile
Add at the bottom of the file the two lines which will copy your test and its
compiled version to the right directory in the RPM file. I.e. adding `example.py`

    cp example.py $(DESTDIR)$(PYTHON_TESTSPATH)
    cp example.py[co] $(DESTDIR)$(PYTHON_TESTSPATH)


### Editing \_\_init\_\_.py
Add at the bottom of the file in the method `def load_tests` to the variable
`modname` your test. I.e adding `example.py`.
```python
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
```
