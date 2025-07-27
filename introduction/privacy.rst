==============
Privacy policy
==============


The short version is that we try to respect your privacy as much as possible. We absolutely do not sell any user data. In fact, we go out of our way to help you keep your data private from everyone, including us. For example, from the moment you :doc:`install Qubes OS </user/downloading-installing-upgrading/installation-guide>`, we offer to set up `Whonix <https://www.whonix.org/>`__ so that all of your updates are routed through `Tor <https://www.torproject.org/>`__.

Website
-------


For the legally-required boilerplate, see :website:`Website Privacy Policy <website-privacy-policy/>`.

This is just a static website generated with Jekyll and hosted from GitHub Pages. We try to use as little JavaScript as possible. We host all resources locally (no third-party CDNs) so that you only have to connect to one domain. This site should be easy to browse using Tor Browser and with scripts blocked. We also have an `onion service <http://qubesosfasa4zl44o4tws22di6kepyzfeqv3tg4e3ztknltfxqrymdad.onion/>`__ (access is not logged). We even go out of our way to make it easy to download `this website’s git repo <https://github.com/QubesOS/qubesos.github.io>`__, including all the website source code, so that you can host this entire site from your own local machine offline. Better yet, we’ve specifically written all of the :doc:`documentation </index>` in Markdown so that the plain text can be enjoyed from the comfort of your terminal. Here’s the `repo <https://github.com/QubesOS/qubes-doc>`__. (By the way, Git tags on our repos are PGP-signed so you can :doc:`verify </project-security/verifying-signatures>` the authenticity of the content.) Obviously, we don’t use any ads or trackers, but this is still a public website, so man-in-the-middle attacks and such are always a possibility. Please be careful. See :ref:`FAQ: Should I trust this website? <introduction/faq:should i trust this website?>`

Update Servers and Repositories
-------------------------------


We provide repositories at https://yum.qubes-os.org and https://deb.qubes-os.org.

We collect and store standard server access and error logs, which include IP addresses. We use this data for generating :doc:`Qubes userbase statistics </introduction/statistics>` and for incident response.

The data is retained for up to three months so that we can re-calculate the previous two months’ statistics in case anything goes wrong. After that, the data is deleted. We never sell the data to anyone or share it with any third party.

If you would like to hide your IP address from us, we strongly encourage it and are happy to help you do so! Simply choose the Whonix option to route all of your updates over Tor when :doc:`installing Qubes OS </user/downloading-installing-upgrading/installation-guide>`.

Onion Services
--------------


We provide an `onion service <http://www.qubesosfasa4zl44o4tws22di6kepyzfeqv3tg4e3ztknltfxqrymdad.onion>`__ for the website and onion service mirrors of the repositories. Access to these servers is not logged.

Mirrors
-------


There are also other third-party mirrors hosted by volunteers. These are used both for :website:`ISO downloads <downloads/#mirrors>` and `updates <#update-servers-and-repositories>`__. We have no control over what data these mirrors collect or with whom they share it. Please see the privacy policy of each respective mirror operator.

Qubes OS
--------


We have specifically designed Qubes OS so that it is not possible to collect any data directly from Qubes OS installations. In other words, Qubes OS does not have the ability to “phone home” and is intentionally architected to forbid that from happening. This is mainly because we have ensured that dom0 has no network access.

We don’t want the ability to collect any data directly from Qubes OS installations, because if anyone has that power, then the system is not secure. We use Qubes OS ourselves as a daily driver for our work and personal lives, so our interests are aligned with yours. We want privacy too! Thankfully, Qubes OS is free and open-source software, so you don’t have to take our word for it.

Of course, third-party software (including other operating systems) running inside of Qubes OS may not be as privacy-respecting, so please be mindful of what you install. We have no control over such third-party software.

For more information, please see :ref:`FAQ: How does Qubes OS provide privacy? <introduction/faq:how does qubes os provide privacy?>`
