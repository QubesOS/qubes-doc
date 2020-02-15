---
layout: doc
title: GUI Troubleshooting
  permalink: /doc/gui-troubleshooting/
redirect_from:
- /en/doc/gui-troubleshooting/
- /doc/GuiTroubleshooting/
- /wiki/GuiTroubleshooting/
---

# GUI Troubleshooting

If you can start your VM, but can't launch any applications, then you need to fix the issues from the `VM console`, accessible from xen through:

~~~
qvm-start <VMname> # Make sure the VM is started
sudo xl console <VMname>
~~~

## Tips

### Disable auditd messages

To disable auditd messages, you need to edit your VM kernel parameters:

~~~
previous_kernel_parameters=$(qvm-prefs --get <VMname> kernelopts) # Get current kernel parameters
qvm-prefs --set <VMname> kernelopts "<previous_kernel_parameters> audit=0"
~~~

Then, restart your VM.

Once your troubleshooting is done, don't forget to remove this kernel parameters, it makes troubleshooting VMs not starting easier.
