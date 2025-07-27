==========================
How to set up a test bench
==========================


This guide shows how to set up simple test bench that automatically test your code you’re about to push. It is written especially for ``core3`` branch of ``core-admin.git`` repo, but some ideas are universal.

We will set up a spare machine (bare metal, not a virtual) that will be hosting our experimental Dom0. We will communicate with it via Ethernet and SSH. This tutorial assumes you are familiar with :doc:`QubesBuilder </developer/building/qubes-builder>` and you have it set up and running flawlessly.

   **Notice:** This setup intentionally weakens some security properties in the testing system. So make sure you understand the risks and use exclusively for testing.

Setting up the Machine
----------------------


Install ISO
^^^^^^^^^^^


First, do a clean install from the ``.iso`` :doc:`you built </developer/building/qubes-iso-building>` or grabbed elsewhere (for example :topic:`here <qubesos-4-1-alpha-signed-weekly-builds/3601>`).

Enabling Network Access in Dom0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Internet access is intentionally disabled by default in dom0. But to ease the deployment process we will give it access. The following steps should be done in ``dom0``.

   **Note:** the following assume you have only one network card. If you have two, pick one and leave the other attached to ``sys-net``.

1. Remove the network card (PCI device) from ``sys-net``

2. Restart your computer (for the removal to take effect)

3. Install ``dhcp-client`` and ``openssh-server`` on your testbench’s dom0.

4. Save the following script in ``/home/user/bin/dom0_network.sh`` and make it executable. It should enable your network card in dom0. *Be sure to adjust the script’s variables to suit your needs.*

   .. code:: bash

         #!/bin/sh
         
         # adjust this for your NIC (run lspci)
         BDF=0000:02:00.0
         
         # adjust this for your network driver
         DRIVER=e1000e
         
         prog=$(basename $0)
         
         pciunbind() {
             local path
             path=/sys/bus/pci/devices/${1}/driver/unbind
             if ! [ -w ${path} ]; then
                 echo "${prog}: Device ${1} not bound"
                 return 1
             fi
             echo -n ${1} >${path}
         }
         
         pcibind() {
             local path
             path=/sys/bus/pci/drivers/${2}/bind
             if ! [ -w ${path} ]; then
                 echo "${prog}: Driver ${2} not found"
                 return 1
             fi
             echo ${1} >${path}
         }
         
         pciunbind ${BDF}
         pcibind ${BDF} ${DRIVER}
         
         sleep 1
         dhclient


5. Configure your DHCP server so your testbench gets static IP and connect your machine to your local network. You should ensure that your testbench can reach the Internet.

6. You’ll need to run the above script on every startup. To automate this save the following systemd service ``/etc/systemd/system/dom0-network-direct.service``

   .. code:: bash

         [Unit]
         Description=Connect network to dom0
         
         [Service]
         Type=oneshot
         ExecStart=/home/user/bin/dom0_network.sh
         
         [Install]
         WantedBy=multi-user.target



7. Then, enable and start the SSH Server and the script on boot:

   .. code:: bash

         sudo systemctl enable sshd
         sudo systemctl start sshd
         
         sudo systemctl enable dom0-network-direct
         sudo systemctl start dom0-network-direct




   **Note:** If you want to install additional software in dom0 and your only network card was assigned to dom0, then *instead* of the usual ``sudo qubes-dom0-update <PACKAGE>`` now you run ``sudo dnf --setopt=reposdir=/etc/yum.repos.d install <PACKAGE>``.

Install Tests and Their Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


A regular Qubes installation isn’t ready to run the full suite of tests. For example, in order to run the `Split GPG tests <https://github.com/QubesOS/qubes-app-linux-split-gpg/blob/4bc201bb70c011119eed19df25dc5b46120d04ed/tests/splitgpg/tests.py>`__ you need to have the ``qubes-gpg-split-tests`` package installed in your app qubes.

Because of the above reason, some additional configurations need to be done to your testing environment. This can be done in an automated manner with the help of the :doc:`Salt </user/advanced-topics/salt>` configuration that provisions the :doc:`automated testing environment </developer/debugging/automated-tests>`.

The following commands should work for you, but do keep in mind that the provisioning scripts are designed for the `openQA environment <https://openqa.qubes-os.org/>`__ and not your specific local testing system. Run the following in ``dom0``:

.. code:: bash

      # For future reference the following commands are an adaptation of
      # https://github.com/marmarek/openqa-tests-qubesos/blob/master/tests/update.pm
      
      # Install git
      sudo qubes-dom0-update git || sudo dnf --setopt=reposdir=/etc/yum.repos.d install git
      
      # Download the openQA automated testing environment Salt configuration
      git clone https://github.com/marmarek/openqa-tests-qubesos/
      cd openqa-tests-qubesos/extra-files
      sudo cp -a system-tests/ /srv/salt/
      sudo qubesctl top.enable system-tests
      
      # Install the same configuration as the one in openQA
      QUBES_VERSION=4.1
      PILLAR_DIR=/srv/pillar/base/update
      sudo mkdir -p $PILLAR_DIR
      printf 'update:\n  qubes_ver: '$QUBES_VERSION'\n' | sudo tee $PILLAR_DIR/init.sls
      printf "base:\n  '*':\n    - update\n" | sudo tee $PILLAR_DIR/init.top
      sudo qubesctl top.enable update pillar=True
      
      # Apply states to dom0 and VMs
      # NOTE: These commands can take several minutes (if not more) without showing output
      sudo qubesctl --show-output state.highstate
      sudo qubesctl --max-concurrency=2 --skip-dom0 --templates --show-output state.highstate


Development VM
--------------


SSH
^^^


Arrange firewall so you can reach the testbench from your ``qubes-dev`` VM. Generate SSH key in ``qubes-dev``:

.. code:: bash

      ssh-keygen -t ecdsa -b 521



Add the following section in ``.ssh/config`` in ``qubes-dev``:

.. code:: bash

      Host testbench
          # substitute username in testbench
          User user
          # substitute address of your testbench
          HostName 192.168.123.45



Passwordless SSH Login
^^^^^^^^^^^^^^^^^^^^^^


To log to your testbench without entering password every time, copy your newly generated public key (``id_ecdsa.pub``) to ``~/.ssh/authorized_keys`` on your testbench. You can do this easily by running this command on ``qubes-dev``: ``ssh-copy-id -i ~/.ssh/id_ecdsa.pub user@192.168.123.45`` (substituting with the actual username address of your testbench).

Scripting
^^^^^^^^^


This step is optional, but very helpful. Put these scripts somewhere in your ``${PATH}``, like ``/usr/local/bin``.

``qtb-runtests``:

.. code:: bash

      #!/bin/sh
      
      ssh testbench python -m qubes.tests.run


``qtb-install``:

.. code:: bash

      #!/bin/sh
      
      TMPDIR=/tmp/qtb-rpms
      
      if [ $# -eq 0 ]; then
              echo "usage: $(basename $0) <rpmfile> ..."
              exit 2
      fi
      
      set -e
      
      ssh testbench mkdir -p "${TMPDIR}"
      scp "${@}" testbench:"${TMPDIR}" || echo "check if you have 'scp' installed on your testbench"
      
      while [ $# -gt 0 ]; do
              ssh testbench sudo rpm -i --replacepkgs --replacefiles "${TMPDIR}/$(basename ${1})"
              shift
      done


``qtb-iterate``:

.. code:: bash

      #!/bin/sh
      
      set -e
      
      # substitute path to your builder installation
      pushd ${HOME}/builder >/dev/null
      
      # the following are needed only if you have sources outside builder
      #rm -rf qubes-src/core-admin
      #qb -c core-admin package fetch
      
      qb -c core-admin -d host-fc41 prep build
      # update your dom0 fedora distribution as appropriate
      qtb-install qubes-src/core-admin/rpm/x86_64/qubes-core-dom0-*.rpm
      qtb-runtests


Hooking git
^^^^^^^^^^^


I (woju) have those two git hooks. They ensure tests are passing (or are marked as expected failure) when committing and pushing. For committing it is only possible to run tests that may be executed from git repo (even if the rest were available, I probably wouldn’t want to do that). For pushing, I also install RPM and run tests on testbench.

``core-admin/.git/hooks/pre-commit``: (you may retain also the default hook, here omitted for readability)

.. code:: bash

      #!/bin/sh
      
      set -e
      
      python -c "import sys, qubes.tests.run; sys.exit(not qubes.tests.run.main())"


``core-admin/.git/hooks/pre-push``:

.. code:: bash

      #!/bin/sh
      
      exec qtb-iterate

