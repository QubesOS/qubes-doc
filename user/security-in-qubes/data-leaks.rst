==========
Data leaks
==========


The Role of the Firewall
------------------------


:doc:`Firewalling in Qubes </user/security-in-qubes/firewall>` **is not intended to be a leak-prevention mechanism.**

There are several reasons for this, which will be explained below. However, the main reason is that Qubes cannot prevent an attacker who has compromised one app qube with restrictive firewall rules from leaking data via cooperative covert channels through another compromised app qube with nonrestrictive firewall rules.

For example, suppose you have an ``email`` app qube. You have set the firewall rules for ``email`` such that it can communicate only with your email server. Now suppose that an attacker sends you a GPG-encrypted message which exploits a hypothetical bug in the GnuPG process. There are now multiple ways the attacker could proceed to leak data (such as confidential email messages) from ``email``. The most obvious way is by simply emailing the data to himself. Another possibility is that the attacker has also compromised another one of your app qubes, such as your ``netvm``, which is normally assumed to be untrusted and has unrestricted access to the network. In this case, the attacker might move data from ``email`` to the ``netvm`` via a covert channel, such as the CPU cache. Such covert channels have been described and even implemented in some “lab environments” and might allow for bandwidths of even a few tens of bits/sec. It is unclear whether such channels could be implemented in a real world system, where multiple VMs are running at the same time, each handling tens or hundreds of processes, all using the same cache memory, but it is worth keeping in mind. Of course, this would require special malware written specifically to attack Qubes OS, and perhaps even a specific Qubes OS version and/or configuration. Nevertheless, it might be possible.

Note that physically air-gapped machines are not necessarily immune to this problem. Covert channels can potentially take many forms (e.g., sneakernet thumb drive, bluetooth, or even microphone and speakers).

For a further discussion of covert channels, see `this thread <https://groups.google.com/d/topic/qubes-users/AqZV65yZLuU/discussion>`__ and :issue:`#817 <817>`.

Types of Data Leaks
-------------------


In order to understand and attempt to prevent data leaks in Qubes, we must distinguish among three different types of relevant data leaks:

1. **Intentional leaks.** Malicious software which actively tries to leak data out of an app qube, perhaps via cooperative covert channels established with other malicious software in another app qube or on some server via networking, if networking, even limited, is allowed for the app qube.

2. **Intentional sniffing.** Malicious software trying to use side channels to, e.g., actively guess some key material used in another VM by some non-malicious software there (e.g., non-leak-proof GPG accidentally leaking out bits of the private key by generating some timing patterns when using this key for some crypto operation). Such attacks have been described in the academic literature, but it is doubtful that they would succeed in practice in a moderately busy general purpose system like Qubes OS where the attacker normally has no way to trigger the target crypto operation explicitly and it is normally required that the attacker trigger many such operations.

3. **Unintentional leaks.** Non-malicious software which is either buggy or doesn’t maintain the privacy of user data, whether by design or accident. For example, software which automatically sends error reports to a remote server, where these reports contain details about the system which the user did not want to share.



Both Qubes firewall and an empty NetVM (i.e., setting the NetVM of an app qube to “none”) can fully protect against leaks of type 3. However, neither Qubes firewall nor an empty NetVM are guaranteed to protect against leaks of types 1 and 2. There are few effective, practical policy measures available to end-users today to stop the leaks of type 1. It is likely that the only way to fully protect against leaks of type 2 is to either pause or shut down all other VMs while performing sensitive operations in the target VM(s) (such as key generation).

For further discussion, see `this thread <https://groups.google.com/d/topic/qubes-users/t0cmNfuVduw/discussion>`__.
