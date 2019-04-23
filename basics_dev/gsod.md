---
layout: sidebar
title: Google Season of Docs
permalink: /gsod/
---

# Google Season of Docs

Thank you for your interest in participating in the [Google Season of Docs][gsod] program with the [Qubes OS team][team]. You can read more about the Google Season of Docs in the official [guides][gsod-doc] and [FAQ][gsod-faq].


## Project Ideas List

Everyone is encouraged to add ideas to this list, either by [editing this page directly][gsod.md] (preferred) or by replying to [this thread][gsod-2019-thread] (then we'll add it to this page for you). (See our [Documentation Guidelines] for general information about how to submit changes to the documentation, and see [Help, Support, and Mailing Lists] for information about our mailing lists.)

We currently have [over a hundred open documentation issues][doc-issues] in our issue tracker. Please feel free to use these for project ideas, as appropriate.

Here's a suggested template for adding project ideas:

```
### Adding a Proposal

**Project**: Something that you're totally excited about.

**Brief explanation**: What is the project?

**Expected results**: What is the expected result in the timeframe given?

**Knowledge prerequisite**: Pre-requisites for working on the project. What knowledge or resources are needed? If applicable, links to more information or discussions.

**Mentor**: Name and email address.
```
### Offline documentation

**Project**: Offline documentation

**Brief explanation**: Qubes OS has thorough documentation on the project website, however a user may find it more convenient to view documentation - especially for troubleshooting network issues -- offline on their Qubes machine. This will improve usability for new users and better support users if they need to troubleshoot anything.

**Expected results**: 

 - Review [past discussions on the issue](https://github.com/QubesOS/qubes-issues/issues/1019)
 - Recommend workflow and platform for displaying offline documentation
 - Test workflow and platform to ensure usability and functionality

**Knowledge prerequisite**: 

 - none

**Mentor**: [Marek Marczykowski-Górecki][team]

### Create guide on firstboot for new users

**Project**: Create guide on firstboot for new users

**Brief explanation**: When a user first boots Qubes after installing it, there is an opportunity to introduce the user to some of the unique functionality Qubes has. This could be the same content as the [improved getting started page](#improve-getting-started-page).

**Expected results**: 

 - Review [past discussions on the issue](https://github.com/QubesOS/qubes-issues/issues/1774)
 - Provide visual mock-ups and proposed text 
  
**Knowledge prerequisite**: 

 - some experience with Anaconda would be helpful

**Mentor**: [Marek Marczykowski-Górecki][team]

### Improve Qubes Intro page

**Project**: Improve Qubes Intro page

**Brief explanation**: The [Intro page](https://www.qubes-os.org/intro/) is the first place a prospective user goes for information about Qubes OS. It is currently text-heavy and in Question & Answer format. This project is to re-write and design the Intro page to be more appealing to prospective users.

**Expected results**: 

 - Review the existing page and website, similar pages for other OSes
 - Provide visual mock-ups and proposed text 

**Knowledge prerequisite**: 

 - none

**Mentor**: [Michael Carbone][team]

### Improve Getting Started page

**Project**: Improve Getting Started page

**Brief explanation**: The [Getting Started page](https://www.qubes-os.org/getting-started/) is the place a new user would go to understand better how to use Qubes. It is currently has old screenshots not using the default desktop environment and could have much better flow. In addition, this improved page content may end up being served more directly to the user via the [offline documentation](#offline-documentation) or the [firstboot guide](#create-guide-on-firstboot-for-new-users). 

**Expected results**: 

 - Review the existing page and website, similar pages for other OSes
 - Provide visual mock-ups and proposed text 

**Knowledge prerequisite**: 

 - none

**Mentor**: [Michael Carbone][team]

### Improve Disposable VMs documentation

**Project**: Improve Disposable VMs documentation

**Brief explanation**: Current Disposable VMs documentation is scarce, inconsistent in places and in scattered across multiple pages, sometimes hard to find.
This project is about consolidating it into one or few easy to find pages, covering all related subjects.
And written in way easy to follow and understand, clearly separating basic use cases, advanced ones and internal details.
Additionally, terminology is used inconsistently.

**Expected results**:

- Review existing Disposable VM documentation
- Propose new documentation layout, including split between pages
- Propose updated and clarified content

**Knowledge prerequisite**:

- basic Qubes OS knowledge - [intro], [getting started]
- [Markdown][markdown]

**Mentor**: [Marek Marczykowski-Górecki][team]

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

### Consolidate troubleshooting guides

**Project**: Consolidate troubleshooting guides

**Brief explanation**: Troubleshooting guides are scattered across many pages and sometimes incomplete, leading to repeatedly posting the same instruction over and over when helping users to diagnose problems.
This could be helped by writing consolidated guide with with a clear list of symptom-action layout.

**Expected results**:

- Review existing [troubleshooting guides](https://www.qubes-os.org/doc/#troubleshooting)
- Review [issues][doc-issues] containing common troubleshooting steps (checking specific logs etc)
- Propose updated, consolidated troubleshooting documentation, including its layout

**Knowledge prerequisite**:

- [Markdown][markdown]

**Mentor**: [Marek Marczykowski-Górecki][team]

[gsod]: https://developers.google.com/season-of-docs/
[team]: /team/
[gsod-doc]: https://developers.google.com/season-of-docs/docs/
[gsod-faq]: https://developers.google.com/season-of-docs/docs/faq
[gsod.md]: https://github.com/QubesOS/qubes-doc/blob/master/basics_dev/gsod.md
[gsod-2019-thread]: https://groups.google.com/d/msgid/qubes-project/aac9b148-4081-ebd8-cb9d-9a9191033484%40qubes-os.org
[Documentation Guidelines]: /doc/doc-guidelines/
[Help, Support, and Mailing Lists]: /support/
[intro]: /intro/
[getting started]: /getting-started/
[markdown]: https://daringfireball.net/projects/markdown/
[doc-issues]: https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22C%3A+doc%22

