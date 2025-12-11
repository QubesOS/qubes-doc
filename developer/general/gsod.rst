============================
Google Season of Docs (GSoD)
============================


Thank you for your interest in participating in the `2024 Google Season of Docs <https://developers.google.com/season-of-docs/>`__ program with the `Qubes OS team <https://www.qubes-os.org/team/>`__. This page details our 2024 project idea as well as completed past projects. You can read more about the Google Season of Docs in the official `guides <https://developers.google.com/season-of-docs/docs/>`__ and `FAQ <https://developers.google.com/season-of-docs/docs/faq>`__.

Update and Expand How-To Guides – Qubes OS
------------------------------------------


About the Qubes OS Project
^^^^^^^^^^^^^^^^^^^^^^^^^^


Qubes OS is a security-focused operating system that allows you to organize your digital life into compartments called “qubes.” If one qube is compromised, the others remain safe, so a single cyberattack can no longer take down your entire digital life in one fell swoop. You can think of using Qubes OS as having many different computers on your desk for different activities but with the convenience of a single physical machine, a single unified desktop environment, and a set of tools for using qubes together securely as parts of a unified system.

Qubes OS was launched in 2011 and has `received praise from security experts and organizations <https://www.qubes-os.org/endorsements/>`__ like Edward Snowden, the Freedom of the Press Foundation, Micah Lee, and Let’s Encrypt. Qubes has :doc:`over 40,000 active users </introduction/statistics>`. From network-level to software-level protections, as well as protections against firmware and hardware attacks, Qubes OS is trying to protect the user from the most significant attacks they encounter so that they can get their work done safely.

The project's problem
^^^^^^^^^^^^^^^^^^^^^


- Some of the existing content is stale. It refers to previous Qubes releases and has not yet been updated to the cover the latest stable release.

- There are important topic areas that the current guides do not completely cover, such as “understanding Qubes OS,” “using Qubes OS in practice,” “Qubes OS workflow for coding,” “printing,” and “audio.”

- The guides do not consistently address users of all skill and experience levels (beginner, intermediate, and expert).

- Some of the guides lack relevant illustrations and screenshots.

- When the developers update a software tool, they should update all the guides that mentions this tool. However, there is currently no way for the developers to know which guides mention which tools.



The project's scope
^^^^^^^^^^^^^^^^^^^


The project is estimated to need around six months to complete (see the timeline below). Qubes team members, including Michael Carbone, Andrew Wong, Marta Marczykowska-Górecka, and Marek Marczykowski-Górecki, will supervise and support the writer.

Measuring the project's success
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We will consider the project successful if:

- Existing guides are updated to describe currently supported Qubes OS version

- Missing common guides are identified

- 2-3 new guides are written



Timeline
^^^^^^^^


.. list-table::
   :widths: 15 15
   :align: center
   :header-rows: 1

   * - Dates
     - Action items
   * - May
     - Orientation
   * - June - November
     - Update & extend how-to guides
   * - December
     - Final project evaluation and case study


Project budget
^^^^^^^^^^^^^^


.. list-table::
   :widths: 32 32
   :align: center
   :header-rows: 1

   * - Expense
     - Amount
   * - writer (10 hours/week, 6 months)
     - $12,000
   * - TOTAL
     - $12,000


Additional information
^^^^^^^^^^^^^^^^^^^^^^


Qubes OS regularly participates in Google Summer of Code and Google Season of Docs. This is our third time participating in Google Season of Docs. Our mentorships for GSoD 2019, 2020, and 2023 were successes, and the projects were completed within the times allotted. The past Google Season of Docs projects have given us experience in working with technical writers and have helped us to understand the benefits that technical writers can bring to our project.

Past Projects
-------------


You can view the project we had in 2019 in the `2019 GSoD archive <https://developers.google.com/season-of-docs/docs/2019/participants/project-qubes>`__ and the `2019 writer’s report <https://web.archive.org/web/20200928002746/https://refre.ch/report-qubesos/>`__.

You can view the project we had in 2020 in the `2020 GSoD archive <https://developers.google.com/season-of-docs/docs/2020/participants/project-qubesos-c1e0>`__ and the `2020 writer’s report <https://web.archive.org/web/20210723170547/https://gist.github.com/PROTechThor/bfe9b8b28295d88c438b6f6c754ae733>`__.

You can view the results of the project we had in 2023 `here <https://www.youtube.com/playlist?list=PLjwSYc73nX6aHcpqub-6lzJbL0vhLleTB>`__.

Here are some successful projects which have been implemented in the past by Google Season of Docs participants.

Instructional video series
^^^^^^^^^^^^^^^^^^^^^^^^^^


Instructional video series: The project's problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




There is user demand for high-quality, up-to-date video guides that take users from zero Linux knowledge to using Qubes as a daily driver and performing specific tasks inside of Qubes, but almost no such videos exist. Although most of the required knowledge is documented, many users report that they would prefer to watch videos rather than read text or that they would find videos easier to understand and follow along with.


Instructional video series: The project's scope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




This project consists of creating a series of instructional videos that satisfy the following criteria:

- Prospective users who are not yet familiar with Linux or Qubes OS can easily understand and follow the videos.

- The videos make a good effort to catch and keep the attention of their target audience.

- Users can follow the videos step-by-step to install Qubes OS and accomplish various tasks.

- The videos show the actual software being used (i.e., Qubes OS and any relevant software running inside of it).

- The videos are technically accurate, include security warnings where appropriate, and use terminology in a way that is consistent with the rest of the documentation (also see the :doc:`glossary </user/reference/glossary>`).

- The video series is comprehensive enough that users do not need to consult the documentation or ask questions (e.g., on the forum) in order to accomplish the most popular tasks and activities.

- The videos include voice narration. (Showing the speaker is optional.)

- The quality of the videos is consistent with current standards regarding things like editing, transitions, animations, lighting, and audio quality.

- The videos are in high definition (minimum 1080p, preferably 4k).

- The videos are separated into a series, where each video is an appropriate length and is appropriately connected to the other videos in the series.

- The videos are suitable for upload and sharing on popular video-sharing and social-media platforms, such as YouTube and Twitter. (The account or channel under which the videos are uploaded is open to discussion on platforms where the Qubes OS Project does not already have a significant established presence, such as YouTube.)

- The videos are suitable for embedding in appropriate places in the Qubes documentation. (E.g., a video on how to update Qubes OS should be appropriate for appearing on the :doc:`how to update </user/how-to-guides/how-to-update>` page.)

- Where possible, the videos should strive to be version-independent. (For example, a video explaining the template system should still be relevant many releases from now if the template system has not changed.)



Below is an example of the content (which is already :doc:`documented </index>`) that the video series is likely to cover. The precise scope of content is to be determined in consultation with the video creator.

- Introduction to Qubes

- Selecting appropriate hardware

- How to install Qubes OS

- First steps after installing

- How to organize your qubes

- How to update

- How to back up, restore, and migrate

- How to copy and paste text (including dom0)

- How to copy and move files (including dom0)

- How to install software

- How to use and customize disposables

- How to enter fullscreen mode

- How to use devices (including block storage, USB, PCI, and optical)

- Templates: understanding, installing, uninstalling, reinstalling, etc.

- Common troubleshooting (preferably included in previous videos at appropriate points)

- The Qubes firewall

- Passwordless root

- Anti Evil Maid

- Split GPG

- CTAP proxy

- YubiKey

- Whonix

- How to install and use a VPN in Qubes

- How to install and use Windows in Qubes

- Other popular topics, as time permits



The project is estimated to need around six months to complete (see the timeline below). Qubes team members, including Michael Carbone, Andrew Wong, and Marek Marczykowski-Górecki, will supervise and support the creator.



Instructional video series: Measuring the project's success
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




We will consider the project successful if, after publication of the video series:

- Actual prospective users with no prior familiarity with Linux or Qubes OS are able to successfully install and use Qubes OS as intended by following along with the videos.

- The reception to the videos is generally positive and complaints about quality and accuracy are minimal.

- Appropriate analytics (e.g., YouTube metrics) are average or better for videos of this type (to be determined in consultation with the creator).



Consolidate troubleshooting guides
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Consolidate troubleshooting guides

**Brief explanation**: Troubleshooting guides are scattered across many pages and sometimes incomplete, leading to repeatedly posting the same instruction over and over when helping users to diagnose problems. This could be helped by writing a consolidated guide with a clear list of symptom-action layout.

**Expected results**:

- Review existing :ref:`troubleshooting guides <troubleshooting>`

- Review `issues <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen%20is%3Aissue%20label%3A%22C%3A%20doc%22>`__ containing common troubleshooting steps (checking specific logs etc)

- Propose updated, consolidated troubleshooting documentation, including its layout



**Knowledge prerequisite**:

- `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__



**Mentor**: `Marek Marczykowski-Górecki <https://www.qubes-os.org/team/>`__

Improve Getting Started page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Improve Getting Started page

**Brief explanation**: The :doc:`Getting Started page </introduction/getting-started>` is the place a new user would go to understand better how to use Qubes. It is currently has old screenshots not using the default desktop environment and could have much better flow. In addition, this improved page content may end up being served more directly to the user via the `offline documentation <https://github.com/QubesOS/qubes-issues/issues/1019>`__ or the firstboot guide.

**Expected results**:

- Review the existing page and website, similar pages for other OSes

- Provide visual mock-ups and proposed text



**Knowledge prerequisite**:

- basic Qubes OS knowledge

- `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__



**Mentor**: `Michael Carbone <https://www.qubes-os.org/team/>`__

Rewrite qrexec documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Rewrite qrexec documentation

**Brief explanation**: Current qrexec (qubes remote exec) documentation is hard to follow, important information is hidden within a wall of text. Some parts are split into multiple sections, for example version specific to avoid duplication, but it doesn’t help reading it. Additionally, protocol documentation describes only few specific use cases, instead of being clear and precise protocol specification. Fixing this last point may require very close cooperation with developers, as the current documentation doesn’t multiple corner cases (that’s one of the issue with its current shape).

**Expected results**:

- Review existing :doc:`qrexec documentation </developer/services/qrexec>` and an `issue about it <https://github.com/QubesOS/qubes-issues/issues/1392>`__

- Propose updated, consolidated admin documentation (policy writing, adding services)

- Propose consolidated protocol specification, based on the current documentation, and cooperation with developers



**Knowledge prerequisite**:

- `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__



**Mentor**: `Marek Marczykowski-Górecki <https://www.qubes-os.org/team/>`__
