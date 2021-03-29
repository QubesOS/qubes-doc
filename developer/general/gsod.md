---
lang: en
layout: sidebar
permalink: /gsod/
ref: 242
title: Google Season of Docs
---

# 2021 Google Season of Docs

Thank you for your interest in participating in the [2021 Google Season of Docs][gsod] program with the [Qubes OS team][team]. You can read more about the Google Season of Docs in the official [guides][gsod-doc] and [FAQ][gsod-faq].

## 2021 Project Idea 

### Qubes OS on Virtual Machines and Disposable VMs documentation - Qubes OS

#### About your organization

Qubes OS is a free and open source operating system uniquely designed to protect the security and privacy of the user. Its architecture is built to enable a user to define different security environments ("qubes") on their computer and visually manage their interaction with each other and the world.

Qubes OS was launched in 2011 and has [received praise from security experts](https://www.qubes-os.org/experts/) like Edward Snowden, Bill Buddington (EFF), Isis Lovecruft (Tor Project), and Kenn White (Open Crypto Audit), and has over [30,000 active users](https://www.qubes-os.org/statistics/).

From network-level to software-level protections, as well as protections against firmware and hardware attacks, Qubes OS is trying to protect the user from the most significant attacks they encounter so that they can get their work done, safely.

#### The Project

The goal of the project is to improve the documentation related to Disposable VMs and installing Qubes OS on Virtual Machines.

The current Disposable VMs documentation is scarce, inconsistent in places and is scattered across multiple pages, sometimes hard to find. This project involves consolidating it into one or few easy to find pages, covering all related subjects. It should be written in way easy to follow and understand, clearly separating basic use cases, advanced ones and internal details. The terminology should also be used consistently.

Additionally, Qubes OS is missing an installation guide for virtual machines. Users are installing an outdated and unsupported version of Qubes OS (3.2) instead of the supported version. There is unofficial existing installation guide for Qubes OS on a virtual box but it is misleading and lacks documentation. Usually, users face some errors and bugs while installing Qubes OS on a virtual machine. This project also involves writing an installation guide that details how to install Qubes on virtual machines, and how to troubleshoot any issues that may arise. 

#### Project’s scope

The technical writer will:

* Review existing Disposable VM documentation

* Propose new documentation layout, including split between pages

* Propose updated and clarified content

* Provide a new option of installation guide for users working on virtual machines. 

* Review existing problems and provide solutions to them. 

* Giving a warning for using outdated versions of Qubes.

Knowledge prerequisites:

* Basic Qubes OS knowledge - intro, getting started.

* Markdown.

* Experience in virtual boxes and machines.

* Basic knowledge about Fedora Linux architecture.

The project is estimated to need around 6 months, with a part-time (20hr/week) workload. Qubes OS team members focused on documentation (Michael Carbone, Andrew David Wong, Marek Marczykowski-Górecki) have committed to supporting the project.

#### Measuring the project’s success

We will consider the project successful if, after publication of the new documentation:

* The Disposable VM documentation is consilidated into a few pages and easier to find.

* Disposable VM terminology is consistent across all pages

* There is a new installation guide detailing how to install Qubes on virtual machines (VirtualBox), complete with screenshots and troubleshooting steps where necessary. 

* There is a decrease (by ~20%) in the number of issues and questions raised for topics covered in the documentation, whether in the official Github issues tracker, the Qubes mailing list, or the Qubes community forum.

#### Budget

| Budget item | Amount | Running total | Note / Justification |
|-|-|-|-|
| Technical writer audit, update, and write new documentation | $12000 | $12000 | based on a 20hr/week for 6 months at 25$/hr |
| TOTAL |  | $12000 |  |

#### Additional information 
Qubes OS regularly participates in the Google Summer of Code and Google Season of Docs. This is our third time in a row participating in Google Season of Docs. Our mentorships for GSoD 2019 and 2020 were successes and both projects were completed 
within the times allotted. The past Google Season of Docs projects have given us experience in working with technical writers, and has helped us to understand the benefits of technical writers can to our project

## Past Projects

You can view the project we had in 2019 in the [2019 GSoD archive][2019-qubes-gsod] and the [2019 writer's report][2019-qubes-report].

You can also view the project we had in 2020 in the [2020 GSoD archive][2020-qubes-gsod] and the [2020 writer's report][2020-qubes-report].

Here are some successful projects which have been implemented in the past by Google Season of Docs participants. 

### Consolidate troubleshooting guides

**Project**: Consolidate troubleshooting guides

**Brief explanation**: Troubleshooting guides are scattered across many pages and sometimes incomplete, leading to repeatedly posting the same instruction over and over when helping users to diagnose problems.
This could be helped by writing consolidated guide with with a clear list of symptom-action layout.

**Expected results**:

- Review existing [troubleshooting guides](/doc/#troubleshooting)
- Review [issues][doc-issues] containing common troubleshooting steps (checking specific logs etc)
- Propose updated, consolidated troubleshooting documentation, including its layout

**Knowledge prerequisite**:

- [Markdown][markdown]

**Mentor**: [Marek Marczykowski-Górecki][team]

### Improve Getting Started page

**Project**: Improve Getting Started page

**Brief explanation**: The [Getting Started page](https://www.qubes-os.org/getting-started/) is the place a new user would go to understand better how to use Qubes. It is currently has old screenshots not using the default desktop environment and could have much better flow. In addition, this improved page content may end up being served more directly to the user via the [offline documentation](https://github.com/QubesOS/qubes-issues/issues/1019) or the firstboot guide. 

**Expected results**: 

 - Review the existing page and website, similar pages for other OSes
 - Provide visual mock-ups and proposed text 

**Knowledge prerequisite**: 

- basic Qubes OS knowledge
- [Markdown][markdown]

**Mentor**: [Michael Carbone][team]

### Rewrite qrexec documentation

**Project**: Rewrite qrexec documentation

**Brief explanation**: Current qrexec (qubes remote exec) documentation is hard to follow, important informations are hidden within a wall of text.
Some parts are split into multiple sections, for example version specific to avoid duplication, but it doesn't help reading it.
Additionally, protocol documentation describes only few specific use cases, instead of being clear and precise protocol specification.
Fixing this last point may require very close cooperation with developers, as the current documentation doesn't multiple corner cases (that's one of the issue with its current shape).

**Expected results**:

- Review existing [qrexec documentation](https://www.qubes-os.org/doc/qrexec3/) and an [issue about it](https://github.com/QubesOS/qubes-issues/issues/1392)
- Propose updated, consolidated admin documentation (policy writing, adding services)
- Propose consolidated protocol specification, based on the current documentation, and cooperation with developers

**Knowledge prerequisite**:

- [Markdown][markdown]

**Mentor**: [Marek Marczykowski-Górecki][team]


[gsod]: https://developers.google.com/season-of-docs/
[team]: /team/
[gsod-doc]: https://developers.google.com/season-of-docs/docs/
[gsod-faq]: https://developers.google.com/season-of-docs/docs/faq
[gsod.md]: https://github.com/QubesOS/qubes-doc/blob/master/developer/general/gsod.md
[gsod-2020-thread]: https://groups.google.com/d/msgid/qubes-project/aac9b148-4081-ebd8-cb9d-9a9191033484%40qubes-os.org
[Documentation Guidelines]: /doc/doc-guidelines/
[Help, Support, and Mailing Lists]: /support/
[intro]: /intro/
[getting started]: /getting-started/
[markdown]: https://daringfireball.net/projects/markdown/
[doc-issues]: https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22C%3A+doc%22
[2019-qubes-gsod]:  https://developers.google.com/season-of-docs/docs/2019/participants/project-qubes
[2019-qubes-report]: https://refre.ch/report-qubesos/
[2020-qubes-gsod]: https://developers.google.com/season-of-docs/docs/2020/participants/project-qubesos-c1e0
[2020-qubes-report]: https://gist.github.com/PROTechThor/bfe9b8b28295d88c438b6f6c754ae733
[existing installation guide]: https://www.youtube.com/watch?v=mATI8Lht0Js
[virtual box issue]: https://www.virtualbox.org/ticket/16771
