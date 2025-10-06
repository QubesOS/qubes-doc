=========================
Disposable implementation
=========================

.. warning::

      This page is intended for advanced users.

Disposable behavior
-------------------


A :term:`disposable template` is not a disposable in itself, but a special template that can create different :term:`disposable` types, :term:`named disposable <named disposable>` and :term:`unnamed disposables <unnamed disposable>`. This intermediary template serves different functions, first to permit customization of the private volume of a disposable as well as well as a degree of inheritance that would not be possible with normal templates. It has the :py:attr:`template_for_dispvms <core-admin:qubes.vm.mix.dvmtemplate.DVMTemplateMixin.template_for_dispvms>` property enabled, being a :py:class:`DVMTemplateMixin <core-admin:qubes.vm.mix.dvmtemplate.DVMTemplateMixin>`.

A :term:`disposable` is a qube with the :py:class:`DispVM <core-admin:qubes.vm.dispvm.DispVM>` class and is based on a disposable template. Every disposable type has all of its volumes configured to disable :py:attr:`save_on_stop <core-admin:qubes.storage.Volume.save_on_stop>`, therefore no changes are saved on shutdown. Unnamed disposables enables the property :py:attr:`auto_cleanup <core-admin:qubes.vm.dispvm.DispVM.auto_cleanup>` by default, thus automatically removes the qube upon shutdown. Named disposables don't enable :py:attr:`auto_cleanup <core-admin:qubes.vm.dispvm.DispVM.auto_cleanup>` by default, thus the qube skeleton is not removed upon shutdown, thus allowing to keep qube settings.

Named disposables are useful for service qubes, as referencing static names is easier when the qube name is mentioned on Qrexec policies (:file:`qubes.UpdatesProxy` target) or as a property of another qube, such as a disposable :term:`net qube` which is referenced by downstream clients in the ``netvm`` property.

Unnamed disposables have their names in the format :samp:`disp{1234}`, where :samp:`{1234}` is derived from the :py:attr:`dispid <core-admin:qubes.vm.dispvm.DispVM.dispid>` property, a random integer ranging from 0 to 9999 with a fail-safe mechanism to avoid reusing the same value in a short period.


Disposable's creation with Qrexec
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The system and every qube can have the :py:attr:`default_dispvm <core-admin:qubes.vm.dispvm.DispVM.default_dispvm>` property. This property can only have disposable template as value or an empty value. If the qube property is set to the default value, it will use the system's property. An exception to the rule is the property of disposables, which always default to their disposables templates to avoid data leaks such as using unintended network paths.

There are some Qrexec policy rules that have some services with allow resolution in case the target is the :doc:`@dispvm <core-qrexec:qrexec-policy>` tag, which translates to creation of disposables out of the :py:attr:`default_dispvm <core-admin:qubes.vm.dispvm.DispVM.default_dispvm>` property. It is most commonly used to open files and URLs, (:file:`qubes.OpenInVM` and :file:`qubes.OpenURL`, respectively).

It is also possible to write rules that would allow creating disposables out of different disposables templates by using as destination the disposable template name or a tag it has. The destination would be:

- :samp:`@dispvm:{DISPOSABLE_TEMPLATE}`, where :samp:`{DISPOSABLE_TEMPLATE}` is the desired template;
- :samp:`@dispvm:@tag:{CUSTOM_TAG}`, where :samp:`{CUSTOM_TAG}` is the tag of your choice.

Preloaded disposables
---------------------


The user desires to circumvent any slow process, the creation of disposables fits into this category. Preloaded disposables enables fast retrieval of fresh disposables, so users don't have to get away from the computer or switch tasks when requesting disposables (or not requesting one at all because it was slow).

Preloaded disposables are :term:`unnamed disposables <unnamed disposable>`, it aims to solve the issue of disposable's long startup time by keeping running (powered on and paused) disposable qubes queued. In order to accomplish this, they are started in the background without user interaction, hidden from most graphical applications by being an :term:`internal <internal qube>`. They are unpaused (transparently) when a disposable qube is requested by the user, therefore the user must not worry about the managing the creation or deletion of them, just how many they'd like to have at maximum.

Preloaded disposable's stages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are several stages a disposable goes through while preloading and being used. In short:

1. **Preload**: The qube is created and marked as preloaded. Qube is not visible in GUI applications.

  #. **Startup**: Begins qube startup, start basic services in it and attempt to pause.

  #. **Request**: The qube is removed from the preload list. If startup has not yet reached pause, the latter is skipped.

2. **Used**: The qube is marked as used and may be unpaused/resumed (if applicable). Only in this phase, GUI applications treat the qube as any other unnamed disposable and the qube object is returned to the caller if requested.

Preloaded disposable's worry-free life-cycle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


There are several events that may trigger the creation, deletion of preloaded disposables. If there is a gap between the current number of preloaded disposables and the maximum number allowed, it will be capped *event*\ ually (refill), if the qube is at an invalid state, it will be deleted or replaced (refresh) as soon as possible.

We cannot prevent all gaps at the moment it occurs and users should not be responsible for filling them, the system must manage to fill gaps when possible.

Preloaded disposable's management
"""""""""""""""""""""""""""""""""


These are common events that trigger changes in preloaded disposables quantity:

- Setting or deleting the ``preload-dispvm-max`` feature will refill or remove;
- (Re)starting :file:`qubes-preload-dispvm.service` will refresh;
- Using a preloaded disposable will refill;
- Requesting a disposable will refill;
- Updating the volumes of a template or disposable template will refresh;
- Changing system's :py:attr:`default_dispvm <core-admin:qubes.vm.dispvm.DispVM.default_dispvm>` while system's feature is set to a different value than the disposable template setting will refill or remove; and
- Qubesd was interrupted mid preload creation, on the next service restart, :py:meth:`domain-load <core-admin:qubes.vm.mix.dvmtemplate.DVMTemplateMixin.on_domain_loaded>` of the disposable template will refresh the incomplete disposables.

Preloaded disposable's temporary gaps
"""""""""""""""""""""""""""""""""""""


Some rarer events that may cause a gap in preloaded disposables temporarily:

- There is not enough memory to preload at the moment, won't create the qube; and
- Service to check if the system is fully operational has failed and will remove the qube. Should not attempt refill as it most likely would lead to the same outcome to infinity.

Preloaded disposable's bootstrap
""""""""""""""""""""""""""""""""


To bootstrap the creation of preloaded disposables after boot, the service :file:`qubes-preload-dispvm.service` is used instead of :py:meth:`domain-load <core-admin:qubes.vm.mix.dvmtemplate.DVMTemplateMixin.on_domain_loaded>` of the disposable template because it relies on systemd to:

- Order this action after the autostart or standard qubes, they must precede in order to have a functional system;
- Skip preloading if kernel command line prevents autostart.

Preloaded disposable's memory management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


At the end of preloading, it attempts to manage memory of the qube right before pause, because it is not possible to negotiate memory with the domain after pause. It attempts to retrieve memory from the qube on :py:meth:`domain-pre-paused <core-admin:qubes.vm.dispvm.DispVM.on_domain_pre_paused>` by setting it to use its preferred memory value. In :doc:`qmemman terms </developer/services/qmemman>`, preferred memory is just enough to have the qube running.

This process can take a bit of time because it depends on how fast the qube can free up memory. In ``qubes.qmemman.systemstate``, there is a timeout (``CHECK_PERIOD``) and a threshold in transfer speed (``CHECK_MB_S``) when attempting to balloon, then, when both of these conditions are met, the memory management seizes and the preloaded disposable is paused.

Although it takes some time, increasing the preload creation stage, we do not worry much about it because it economizes memory on the long run, the biggest problems is that qmemman is synchronous, so only one request can be made at a time, anything that takes too much time on qmemman could prevent ballooning/balancing of other qubes on the system.

Preloaded disposable's pause
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Preloaded disposables are paused for various reasons:

- Detection if the qube was used without being requested with :py:meth:`core-admin:qubes.vm.dispvm.DispVM.from_appvm`. Not every communication with a qube goes through :program:`qubesd`, it may go via Qrexec or GUI daemon;
- CPU scheduling economy, domain is not eligible; and
- Cronjob, timers and other things that don't block the init system and service manager completion won't run, they could possibly alter a clean state.

But this comes at a cost:

- Can only connect to the GUI after the qube is requested (longer run time), else, if `early GUI connection was made before the qube is paused <https://github.com/qubesos/qubes-issues/issues/9940>`__:

  - Events such as screen resize by plugging or removing external monitors can't work;
  - No easy way to hide autostarted applications, depends on qube collaboration;
  - Can only preload after GUI login to be able to establish a connection;
  - Can't survive GUI login and logout as the connection might change;

- Memory management before pause may take some seconds, that is not prejudicial to the time to use the qube but it is prejudicial to the system as :doc:`qmemman </developer/services/qmemman>` can not balloon/balance other qubes in the mean time due to its design.

Preloaded disposable's security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


As preloaded disposables are started before being used, methods to prevent accidental tampering have been put in place as well as guarantees to prevent reuse:

- The qube has the ``internal`` feature enabled, Qubes GUI applications were patched to hide and show :term:`internal qubes<internal qube>` by handling events for ``domain-feature-((pre-)?set|delete):internal``;
- When requesting an unnamed disposable, the qube object is only returned to the user once it has finished preloading;
- The qube is paused as the last stage of preloading, this permits receiving :py:meth:`domain-unpaused <core-admin:qubes.vm.dispvm.DispVM.on_domain_unpaused>` event and be notified that the qube was used, marked as such and removed from the preload list to avoid reuse, even without the qube being requested with :py:meth:`core-admin:qubes.vm.dispvm.DispVM.from_appvm`;
- The GUID only connects to the GUI agent on the qube after the preloaded disposable is marked as used, this prevents that an autostarted application such as a terminal appears on the screen before preloading has finished. Enabling a GUI is is controlled by the :py:attr:`is_preload <core-admin:qubes.vm.dispvm.DispVM.is_preload>` property, that when disabled, allows the GUI connection to initiate. This method delays GUI calls considerably as establishing the connection can take ~2 seconds, research is being done to prevent this delay.

Another point of security is reliability:

- The ``preload-dispvm-threshold`` feature controls how much free memory must be present on the system before attempting to create a new preloaded disposable. Used to ensure preloaded disposables do not consume all available memory, which would prevent starting other qubes.

Alternatives considered
^^^^^^^^^^^^^^^^^^^^^^^


For an alternative to be considered for implementation, it must meet the following requirements:

- No memory or ``vcpus`` restrictions such as limiting to a few number of ``vcpus`` or assigns memory on request (can be slow).
- Performant as much as a normal disposable even on long running sessions;
- Caller transparency, no change necessary for callers, the request must be transparent and the server must find the fastest option. This is to avoid transition burden (API breakage).

From the evaluated options, only :ref:`preload queue <developer/services/disposablevm-implementation:preload queue>` meets all requirements.


Restoration from savefile
"""""""""""""""""""""""""


**Description**: Disposable template booted, its image was dumped (suspend to disk), newly disposables would restore this image to become their own.

**Evaluation**:

- Used in R3.2, worked at that time, when there was only one disposable template available, see next points of why it can't be used anymore.
- Incompatible with multiple ``vcpus``.
- Some memory issues.
- Savefile creation takes a long time. The disposable qube savefile contains references to template rootfs and :abbr:`CoW (Copy-on-Write)` files, if there is a modification on the template or disposable template, it took longer than 2.5 minutes to generate the next disposable.

Xen domain fork
"""""""""""""""


**Description**: domain forking is the process of creating a domain with an empty memory space and a parent domain specified from which to populate the memory when necessary. For the new domain to be functional the domain state is copied over as part of the fork operation (HVM params, heap allocation etc). This description was sourced from `[Xen-devel] [RFC PATCH for-next 17/18] xen/mem_sharing: VM forking, Tamas K Lengyel <https://lists.xenproject.org/archives/html/xen-devel/2019-09/msg02497.html>`__.

**Evaluation**:

- Shares too much information from the trunk to the forks. This appears to have improved if not totally fixed on Linux 6.14, as mentioned by Andrew Cooper on Qubes OS Summit 2025;
- Requires changing properties after the fork is done, this includes, but not limited to, ``xid`` of connected qubes, network uplink;
- Not designed for long running sessions, the initial intention was fuzzing. As fast as the creation can be, the usage may be slower as memory is mapped on request. Xen doesn't have a poper :abbr:`CoW (Copy-on-Write)` support for domain memory, so making a full copy of a domain on fork also has some overhead;
- Tamas K Lengyiel `VM Forking & Hypervisor-Based Fuzzing with Xen <https://www.youtube.com/watch?v=3MYo8ctD_aU>`__ presentation during the Open Source Summit Europe in 2022, showed impressive results on CPU i5-8350U, an average of time of 0.745 ms per fork (created 1300 VM/s). These fast results were later explained that was due to not initializing the whole VM memory on the fork unless it was requested, as explained on the point above. Still impressive results but current usage is limited to fuzzing.

Preload queue
"""""""""""""


**Description**: Start disposables and queue them in a disposable template feature, unnamed disposables requested will prefer to retrieve disposables from this list.

**Evaluation**:

- Because the qube is running prior to being requested, multiple components have to be patched to support it to various levels off difficulty. Excluding from backups to allowing removal of disposable templates that only have preloaded disposables to even stranger issues such as deferring net qube change from a preloaded disposable where the old net qube has already been purged from the system.
- The biggest difference between the queue and the other alternatives is that this solution works, is reliable and fulfills all requirements. A proper solution would be patching upstream Xen to implement :abbr:`CoW (Copy-on-Write)`, but that would involve a lot more work than what the Qubes Team can provide with current resources.
