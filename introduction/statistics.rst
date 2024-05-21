==========
Statistics
==========




.. figure:: https://tools.qubes-os.org/counter/stats.png
   :alt: Estimated Qubes OS userbase graph

FAQ
---


How often is this graph updated?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Daily.

Why is the bar for the current month so low?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Since the graph is updated daily, the bar for the current month will be
very low at the start of the month and rise gradually until the end of
the month.

How is the userbase estimated?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We simply count the number of unique IPv4 addresses that connect to the
Qubes update servers each month (except for Tor connections; see
`below <#how-are-tor-users-counted>`__). (Note: Users who have manually
configured their systems to bypass the metalink and connect directly to
a mirror are not counted.)

How are Tor users counted?
^^^^^^^^^^^^^^^^^^^^^^^^^^


We estimate the number of Tor users as a proportion of the total number
of *requests* from Tor exit nodes on the assumption that the proportion
of users to requests is roughly the same for both clearnet and Tor
users. To be precise, the formula is:

.. code:: bash

      tor_users = tor_requests * (plain_users / plain_requests)



Where:

- ``tor_users`` is the estimated number of Qubes users who download
  updates via Tor each month.

- ``tor_requests`` is the total number of requests the Qubes update
  servers receive from Tor exit nodes each month.

- ``plain_users`` is the number of unique clearnet IPv4 addresses that
  connect to the Qubes update servers each month.

- ``plain_requests`` is the total number of requests the Qubes update
  servers receive from clearnet IPv4 addresses each month.



We cross-reference the list of connecting IP addresses with `TorDNSEL’s exit lists <https://metrics.torproject.org/collector.html#type-tordnsel>`__
in order to distinguish Tor and clearnet IPs and requests. For this
purpose, we count an IP address as belonging to a Tor exit node if there
was a Tor exit node active for that address within the 24-hour periods
before or after it connected to the Qubes update servers.

What kinds of data do you collect about Qubes users?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Please see our :doc:`Privacy Policy </introduction/privacy>`.

Where can I find the raw data and source code?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The raw data is available
`here <https://tools.qubes-os.org/counter/stats.json>`__. (This does not
include any personally-identifying user data.) Please note that the
format of this data is not documented and may change any time if the
developers feel the need to include something else. The source code is
available `here <https://github.com/woju/qubes-stats>`__.
