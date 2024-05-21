=================================
Passwordless root access in qubes
=================================


The rationale behind passwordless root in qubes is set out
:doc:`here </user/security-in-qubes/vm-sudo>`. Implementation is by the
qubes-core-agent-passwordless-root package.

This page sets out the configuration changes made, with (not necessary
complete) list of mechanisms depending on each of them:

1. sudo (``/etc/sudoers.d/qubes``):

   .. code:: bash

         Defaults !requiretty
         %qubes ALL=(ALL) ROLE=unconfined_r TYPE=unconfined_t NOPASSWD: ALL
         
         (...)



   - Easy user -> root access (main option for the user).

   - ``qvm-usb`` (not really working, as of R2).



2. PolicyKit (``/etc/polkit-1/rules.d/00-qubes-allow-all.rules``):

   .. code:: bash

         //allow any action, detailed reasoning in sudoers.d/qubes
         polkit.addRule(function(action,subject) { if (subject.isInGroup("qubes")) return polkit.Result.YES; });


   PAM (``/etc/pam.d/su.qubes`` or ``/usr/share/pam-configs/su.qubes``)
   ``auth        sufficient  pam_succeed_if.so use_uid user ingroup qubes``

   - NetworkManager configuration from normal user (``nm-applet``).

   - Updates installation (``gpk-update-viewer``).

   - User can use pkexec just like sudo Note: above is needed mostly
     because Qubes user GUI session isn’t treated by PolicyKit/logind
     as “local” session because of the way in which X server and
     session is started. Perhaps we will address this issue in the
     future, but this is really low priority. Patches welcomed anyway.



3. Empty root password:

   - Used for access to ‘root’ account from text console
     (``qvm-console-dispvm``) - the only way to access the VM when GUI
     isn’t working.

   - Can be used for easy ‘su -’ from user to root.




