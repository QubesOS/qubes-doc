=========================
Disposable implementation
=========================

.. warning::

      This page is intended for advanced users.

Disposable behavior
-------------------


A :term:`disposable template <disposable template>` is not a disposable qube in itself, but a qube that can be used to create different disposable types: normal :term:`disposables <disposable>` and :term:`named disposables <named disposable>`. This intermediary template serves different functions: first, it allows customization of the private volume of a disposable, and second, it provides a degree of inheritance that would not be possible with normal templates. It has the :py:attr:`~core-admin:qubes.vm.mix.dvmtemplate.DVMTemplateMixin.template_for_dispvms` property enabled, being a :py:class:`~core-admin:qubes.vm.mix.dvmtemplate.DVMTemplateMixin`.

A :term:`disposable` is a qube with the :py:class:`~core-admin:qubes.vm.dispvm.DispVM` class and is based on a disposable template. Every disposable type has all of its volumes configured to disable :py:attr:`~core-admin:qubes.storage.Volume.save_on_stop`, therefore no changes are saved on shutdown. Normal disposables enable the property :py:attr:`~core-admin:qubes.vm.dispvm.DispVM.auto_cleanup` by default, thus Qubes OS automatically removes the qube upon shutdown. Named disposables don't enable :py:attr:`~core-admin:qubes.vm.dispvm.DispVM.auto_cleanup` by default, thus the qube skeleton is not removed upon shutdown, thus allowing to keep qube settings.

Named disposables are useful for service qubes, as referencing static names is easier when the qube name is mentioned on qrexec policies (:file:`qubes.UpdatesProxy` target) or as a property of another qube, such as a disposable :term:`net qube` which is referenced by downstream clients in the ``netvm`` property.

Disposables are generally named according to the :samp:`disp{1234}` scheme, where :samp:`{1234}` is derived from the :py:attr:`~core-admin:qubes.vm.dispvm.DispVM.dispid` property, a random integer ranging from 0 to 9999 with a fail-safe mechanism to avoid reusing the same value in a short period. Named disposables have a user-set permanent name.


Creating disposables through qrexec
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every qube has the :py:attr:`~core-admin:qubes.vm.dispvm.DispVM.default_dispvm` property, which defines which disposable template will be used to spawn disposables for this qube by default (when using actions such as "open in disposable").
It can have one of three values:

- a disposable template
- empty value
- default system value (this will use the system-wide :py:attr:`~core-admin:qubes.vm.dispvm.DispVM.default_dispvm` property)

In case of disposables, this property is by default set to their own disposable template, to avoid data leaks through, for example, using unintended network access paths.

This value is also used in case of qrexec policy: when policy rules use the :doc:`@dispvm <core-qrexec:qrexec-policy>` tag, it translates to "a disposable based on the source qube's :py:attr:`~core-admin:qubes.vm.dispvm.DispVM.default_dispvm`. It is most commonly used to open files and URLs, (:file:`qubes.OpenInVM` and :file:`qubes.OpenURL`, respectively).

If you want to allow creating disposables based on different disposable templates, you can use the disposable template name or tag as destination. In particular:

- :samp:`@dispvm:{DISPOSABLE_TEMPLATE}`, where :samp:`{DISPOSABLE_TEMPLATE}` is the desired template;
- :samp:`@dispvm:@tag:{CUSTOM_TAG}`, where :samp:`{CUSTOM_TAG}` is the tag of your choice.
