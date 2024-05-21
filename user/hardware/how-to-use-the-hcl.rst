================================================
How to use the hardware compatibility list (HCL)
================================================


The :doc:`HCL </user/hardware/hcl>` is a compilation of reports generated and submitted
by users across various Qubes versions about their hardware’s
compatibility with Qubes.

**Note:** Except in the case of developer-reported entries, the Qubes
team has not independently verified the accuracy of these reports.
Please first consult the data sheets (CPU, chipset, motherboard) prior
to buying new hardware for Qubes. Make sure it meets the :doc:`System Requirements </user/hardware/system-requirements>` and search in particular for
support of:

- HVM (“AMD virtualization (AMD-V)”, “Intel virtualization (VT-x)”,
  “VIA virtualization (VIA VT)”)

- IOMMU (“AMD I/O Virtualization Technology (AMD-Vi)”, “Intel
  Virtualization Technology for Directed I/O (VT-d)”)

- TPM (“Trusted Platform Module (TPM)” connected to a “20-pin TPM
  header” on motherboards.)



If using the list to make a purchasing decision, we recommend that you
choose hardware with:

- the best achievable Qubes security level (green columns in HVM,
  IOMMU, TPM)

- and general machine compatibility (green columns in Qubes version,
  dom0 kernel, remarks).



Also see :doc:`Certified Hardware </user/hardware/certified-hardware>`.

Generating and Submitting New Reports
-------------------------------------


In order to generate an HCL report in Qubes, simply open a terminal in
dom0 (Applications Menu > Terminal Emulator) and run
``qubes-hcl-report <qube-name>``, where ``<qube-name>`` is the name of
the qube in which the generated HCL files will be saved.

You are encouraged to submit your HCL report for the benefit of further
Qubes development and other users. When submitting reports, test the
hardware yourself, if possible. If you would like to submit your HCL
report, please copy and paste the contents of the **HCL Info** ``.yml``
file into an email to the :ref:`qubes-users mailing list <introduction/support:qubes-users>` with the subject
``HCL - <your machine model name>``, or create a post in the `HCL Reports category <https://forum.qubes-os.org/c/user-support/hcl-reports/23>`__
of the forum. Pasting the contents into the email or post has the
advantage that members of the mailing list and the forum can see the
report without downloading and opening a file. In addition, new forum
members are unable to attach files to posts.

Please include any useful information about any Qubes features you may
have tested (see the legend below), as well as general machine
compatibility (video, networking, sleep, etc.). Please consider sending
the **HCL Support Files** ``.cpio.gz`` file as well. To generate these
add the ``-s`` or ``--support`` command line option.

**Please note:** The **HCL Support Files** may contain numerous hardware
details, including serial numbers. If, for privacy or security reasons,
you do not wish to make this information public, please **do not** post
the ``.cpio.gz`` file on a public mailing list or forum.
