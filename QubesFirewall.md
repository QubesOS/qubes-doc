---
layout: wiki
title: QubesFirewall
permalink: /wiki/QubesFirewall/
---

Understanding Qubes networking and firewall
===========================================

Understanding firewalling in Qubes
----------------------------------

Every AppVM in Qubes is connected to the network via a FirewallVM, which is used to enforce network-level policies. By default there is one default Firewall VM, but the user is free to create more, if needed.

For more information, see the following:

-   [​https://groups.google.com/group/qubes-devel/browse\_thread/thread/9e231b0e14bf9d62](https://groups.google.com/group/qubes-devel/browse_thread/thread/9e231b0e14bf9d62)
-   [​http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html](http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html)

How to edit rules
-----------------

In order to edit rules for a given domain, select this domain in the Qubes Manager and press the "firewall" button:

[![No image "r2b1-manager-firewall.png" attached to QubesFirewall](/chrome/common/attachment.png "No image "r2b1-manager-firewall.png" attached to QubesFirewall")](/attachment/wiki/QubesFirewall/r2b1-manager-firewall.png)

Note that if you specify a rule by DNS name it will be resolved to IP(s) *at the moment of applying the rules*, and not on the fly for each new connection. This means it will not work for serves using load balancing. More on this in the message quoted below.

Alternatively, one can use the `qvm-firewall` command from Dom0 to edit the firewall rules by hand:

Enabling networking between two AppVMs
--------------------------------------

Normally any networking traffic between VMs is prohibited for security reasons. However, in special situations, one might one to selectively allow specific AppVMs to be able to establish networking connectivity between each other. For example, this might come useful in some development work, when one wants to test networking code, or to allow file exchange between HVM domains (which do not have Qubes tools installed) via SMB/scp/NFS protocols.

In order to allow networking between AppVM A and B follow those steps:

-   Make sure both A and B are connected to the same firewall vm (by default all AppVMs use the same firewall VM).
-   Note the Qubes IP addresses assigned to both AppVMs. This can be done using the `qvm-ls -n` command, or via the Qubes Manager preferences pane for each AppVM.
-   Start both AppVMs, and also open a terminal in the firewall VM
-   In the firewall VM's terminal enter the following iptables rule:

    ``` {.wiki}
    sudo iptables -I FORWARD 2 -s <IP address of A> -d <IP address of B> -j ACCEPT
    ```

-   Now you should be able to reach the AppVM B from A -- test it using e.g. ping issues from AppVM A. Note however, that this doesn't allow you to reach A from B -- for this you would need another rule, with A and B addresses swapped.
-   If everything works as expected, then the above iptables rule(s) should be written into firewall VM's `qubes_firewall_user_script` script which is run on every firewall update. This is necessary, because Qubes orders every firewall VM to update all the rules whenever new VM is started in the system. If we didn't enter our rules into this "hook" script, then shortly our custom rules would disappear and inter-VM networking would stop working. Here's an example how to update the script (note that, by default, there is no script file present, so we likely will be creating it, unless we had some other custom rules defines earlier in this firewallvm):

    ``` {.wiki}
    [user@firewallvm ~]$ sudo bash
    [root@firewallvm user]# echo "iptables -I FORWARD 2 -s 10.137.2.25 -d 10.137.2.6 -j ACCEPT" >> /rw/config/qubes_firewall_user_script
    ```

Port forwarding to an AppVM from the outside world
--------------------------------------------------

TODO
