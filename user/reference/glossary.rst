========
Glossary
========

.. glossary::

   Qubes OS
      A security-oriented operating system (OS). The main principle of Qubes OS is security by compartmentalization (isolation), in which activities are compartmentalized (isolated) in separate :term:`qubes <qube>`.

      - **Important:** The official name is "Qubes OS" (note the capitalization and the space between "Qubes" and "OS"). In casual conversation, this is often shortened to "Qubes". Only in technical contexts where spaces are not permitted (e.g., in usernames) may the space be omitted, as in ``@QubesOS``.


.. glossary::

   qube
      A secure compartment in Qubes OS. Currently, qubes are implemented as Xen :term:`domains <domain>`, but Qubes OS is independent of its underlying compartmentalization technology. :term:`VMs <VM>` could be replaced with a different technology, and qubes would still be called "qubes". Therefore, always opt for the term ``qube`` over the other terms unless explicitly guided otherwise.

      - **Important:** The term "qube" is a common noun and should follow the capitalization rules of common nouns. For example, "I have three qubes" is correct, while "I have three Qubes" is incorrect. Note that starting a sentence with the plural of "qube" (i.e., "Qubes ...") can be ambiguous, since it may not be clear whether the referent is a plurality of qubes or :term:`Qubes OS`.

      - Example usage: Bank in your ``banking`` qube and web surf in your ``untrusted`` qube. That way, if your ``untrusted`` qube is compromised, your banking activities remains secure.

      - Historical note: The term "qube" was originally invented as an alternative to "VM" intended to make it easier for less technical users to understand Qubes OS and learn how to use it.

   domain
      In Xen, a synonym for a virtual machine. See `"domain" on the Xen Wiki <https://wiki.xenproject.org/wiki/Domain>`__. This term has no official meaning in Qubes OS, but is often used colloquially.

   VM
      An abbreviation for "virtual machine". A software implementation of a computer that provides the functionality of a physical machine.

Qube types
----------


.. glossary::

   admin qube
      .. image:: https://raw.githubusercontent.com/QubesOS/qubes-artwork/refs/heads/main/icons/scalable/apps/adminvm-black.svg
         :width: 24px
         :align: left
         :alt: admin qube icon

      A type of :term:`qube` used for administering Qubes OS. Currently, the only admin qube is :term:`dom0`.

   app qube
      .. image:: https://raw.githubusercontent.com/QubesOS/qubes-artwork/refs/heads/main/icons/scalable/apps/appvm-red.svg
         :width: 24px
         :align: left
         :alt: app qube icon

      A :term:`qube` that is based on a template. Normally, *app qubes* are used to run user applications and store user files.

      An *app qube* does not have a root filesystem of its own. The qube borrows its root filesystem from its  :term:`template`, and only owns its own home directory and user files (in Linux-based qubes, they are the /home and /user/local directories).

      - Previously known as: ``AppVM``, ``TemplateBasedVM``.


   disposable
      .. image:: https://raw.githubusercontent.com/QubesOS/qubes-artwork/refs/heads/main/icons/scalable/apps/dispvm-red.svg
         :width: 24px
         :align: left
         :alt: disposable qube icon

      A :term:`disposable` qube is a stateless :term:`qube` - it does not save any data between reboots. Every time it is started, it has the same fresh filesystem.  These qubes can be used for a variety of situations, from experimentation to creating a more secure network connection. See :doc:`/user/how-to-guides/how-to-use-disposables`.

      - Previously known as: ``DisposableVM``, ``DispVM``.

   standalone
      Any :term:`qube` that has its own root filesystem and does not share it with another qube. Distinct from both :term:`template` and :term:`app qube`.

      See :doc:`/user/advanced-topics/standalones-and-hvms`.

      - Previously known as: ``StandaloneVM``.

   template
      Any :term:`qube` that shares its root filesystem with another qube. A qube that is borrowing a template's root filesystem is known as an :term:`app qube` and is said to be "based on" the template. Templates are intended for installing and updating software applications, but not for running them.

      See :doc:`/user/templates/templates`.

      - No template is an :term:`app qube`.

      - A template cannot be based on another template.

      - Regular templates cannot function as :term:`disposable template`. (Disposable templates must be app qubes).

      - Previously known as: ``TemplateVM``.


Qube's types variations
-----------------------


.. glossary::

   disposable template
      Any :term:`app qube` on which :term:`disposable` are based. A disposable template shares its user directories (and, indirectly, the root filesystem of the regular :term:`template` on which it is based) with all :term:`disposable` based on it.

      - Not to be confused with the concept of a regular :term:`template` that is itself disposable, which does not exist in Qubes OS.

      - Disposable templates must be app qubes. They cannot be regular :term:`template`.

      - Every :term:`disposable` is based on a disposable template, which is in turn based on a regular :term:`template`.

      - Unlike :term:`disposable`, disposable templates have the persistence properties of normal :term:`app qube`.

      - Previously known as: ``DisposableVM Template``, ``DVM Template``, ``DVM``. It is advised against the use of the ``DVM`` terms as it can be interpreted by some users as an abbreviation of ``DispVM``, which a ``DVM`` is not.

   named disposable
      A type of :term:`disposable` given a permanent name that continues to exist even after it is shut down and can be restarted again.

      - Only one instance of a named disposable can run at a time.

      - Technical note: Named disposables are useful for certain :term:`service qube`\ s, where the combination of persistent device assignment and ephemeral qube state is desirable.

   unnamed disposable
      A type of :term:`disposable` with a temporary name that ceases to exist after the qube is shut down. Closing the first application that was opened in the disposable will trigger the qube to shut down. Thus, if there is not initial application, such is the case with Qubes Devices widget, the qube has to be manually turned off.

      - Multiple instances of a unnamed disposable can run at a time.

      - Technical note: Unnamed disposables are useful for certain converting, viewing and editing untrusted files, where the combination of opening multiple files in disposable qubes that you don't need to remember their name for long is desirable.

   management qube
      A :term:`qube` used for automated management of a Qubes OS installation via :doc:`/user/advanced-topics/salt`.

   net qube
      Internally known as :term:`qube` that specifies from which qube, if any, it receives network access. Despite the name, "net qube" (or :term:`app qube` to be the :term:`service qube` ``sys-firewall``, which in turn uses ``sys-net`` as its net qube.

      - If a qube does not have a net qube (i.e., its ``netvm`` is set to ``None``), then that qube is offline. It is disconnected from all networking.

      - The name :term:`service qube` called a "NetVM". The name of the ``netvm`` property is a holdover from that era.

   service qube
      Any :term:`app qube` with the primary purpose of which is to provide services to other qubes. ``sys-net`` and ``sys-firewall`` are examples of service qubes.

   internal qube
      A qube which has the ``internal`` feature set. Used for the :term:`management qube` and preloaded disposables. These qubes are hidden from most Qubes OS graphical applications, as they are not intended to be used directly.

   GUI domain
      The GUI domain handles all the display-related tasks and some system management. There can be multiple GUI domains present on the system. Every GUI domain can have its own set of privileges, permissions, managed qubes etc. By default, :term:`dom0` is the only GUI domain.

Miscellaneous
-------------


.. glossary::

   dom0
      :term:`domain` zero. A type of :term:`admin qube`. Also known as the **host** domain, dom0 is the initial qube started by the Xen hypervisor on boot. Dom0 runs the Xen management toolstack and has special privileges relative to other domains, such as direct access to most hardware.

      - The term "dom0" is a common noun and should follow the capitalization rules of common nouns.

   domU
      Unprivileged :term:`domain`. Also known as **guest** domains, domUs are the counterparts to dom0. In Xen, all VMs except dom0 are domUs. By default, most domUs lack direct hardware access.

      - The term "domU" is a common noun and should follow the capitalization rules of common nouns.

      - Sometimes the term :term:`vm` is used as a synonym for domU. This is technically inaccurate, as :term:`dom0` is also a VM in Xen.

   HVM
      Hardware-assisted Virtual Machine. Any fully virtualized, or hardware-assisted, :term:`vm` utilizing the virtualization extensions of the host CPU. Although HVMs are typically slower than paravirtualized qubes due to the required emulation, HVMs allow the user to create domains based on any operating system.

      See :doc:`/user/advanced-topics/standalones-and-hvms`.

   firmware
      Software that runs outside the control of the operating system. Some firmware executes on the same CPU cores as Qubes OS does, but all computers have many additional processors that the operating system does not run on, and these computers also run firmware.

   policies
      In Qubes OS, "policies" govern interactions between qubes, powered by :doc:`Qubes' qrexec system </developer/services/qrexec>`. A single policy is a rule applied to a qube or set of qubes, that governs how and when information or assets may be shared with other qubes.
      An example is the rules governing how files can be copied between qubes.
      Policy rules are grouped together in files under ``/etc/qubes/policy.d``
      Policies are an important part of what makes Qubes OS special.

   Qubes Windows Tools (QWT)
      A set of programs and drivers that provide integration of Windows qubes with the rest of the Qubes OS system.

      See :doc:`/user/templates/windows/qubes-windows-tools` and :doc:`/user/templates/windows/qubes-windows`.
