=======================================
Help, support, mailing lists, and forum
=======================================


The Qubes community is here to help! Since Qubes is a security-oriented operating system, we want to make sure you `stay safe <#staying-safe>`__ as you get the support you need, and we want to make sure our community remains a friendly and productive place by ensuring we all follow the :doc:`Code of Conduct </introduction/code-of-conduct>` and `discussion guidelines <#discussion-guidelines>`__.

How to get help and support
---------------------------


First, let’s see what kind of help you need.

I have a problem or a question.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


No worries! Here’s how we recommend proceeding:

1. Check the :doc:`documentation </index>`. There may already be a page about it. Specifically, check out the :ref:`How-To Guides <how-to-guides>` and :ref:`Troubleshooting <troubleshooting>` sections.

2. Search the :doc:`FAQ </introduction/faq>`. Your question might already be answered.

3. Try :ref:`searching the issue tracker <introduction/issue-tracking:search tips>`. There may already be an open **or closed** issue about your problem. The issue tracker is constantly being updated with known bugs and may contain workarounds for problems you’re experiencing. If there are any pinned issues at the top, make sure to check them first!

4. Try `searching the Qubes Forum <https://forum.qubes-os.org/>`__. There may already be a matching topic.

5. Try `searching the qubes-users archives <https://www.mail-archive.com/qubes-users@googlegroups.com/>`__. There may have already been a relevant thread.



I didn't find a solution or an answer!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Sorry to hear that! In that case, we recommend asking for help on the `Qubes Forum <https://forum.qubes-os.org/>`__ or on the `qubes-users mailing list <#qubes-users>`__. Choose the venue you prefer, but please don’t ask on both at the same time! Before you ask, please review our `discussion guidelines <#discussion-guidelines>`__ and StackOverflow’s advice on `how to ask good questions <https://stackoverflow.com/help/how-to-ask>`__. Don’t forget to `stay safe <#staying-safe>`__!

I don't need support, but I think I found a bug.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We’d be grateful if you reported it (but please make sure no one else has already reported it first)! Please see :doc:`Issue Tracking </introduction/issue-tracking>` for details.

I don't need support, but I'd like to request a feature.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


No promises, but we’d be happy to consider it! Please see :doc:`Issue Tracking </introduction/issue-tracking>` for details.

Where's the best place to discuss Qubes?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


That would be the `Qubes Forum <https://forum.qubes-os.org/>`__ and the `qubes-users mailing list <#qubes-users>`__. Please have a look at our `discussion guidelines <#discussion-guidelines>`__ before diving in. Enjoy!

How can I get involved and contribute?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Thank you for asking! Please see :doc:`How to Contribute </introduction/contributing>` for all the ways you can do so.

I would like to report a security vulnerability.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


That sounds more like you helping us! Thanks! Please see :ref:`Reporting Security Issues in Qubes OS <project-security/security:reporting security issues in qubes os>`.

Staying safe
------------


The Qubes mailing lists and forum are open to the public. The contents are crawled by search engines and archived by third-party services outside of our control. Please do not send or post anything that you are not comfortable seeing discussed in public. If confidentiality is a concern, please use PGP encryption in an off-list email.

The Qubes community includes people from all walks of life and from around the world. Individuals differ in areas of experience and technical expertise. You will come into contact with others whose views and agendas differ from your own. Everyone is free to write what they please, as long as it doesn’t violate our :doc:`Code of Conduct </introduction/code-of-conduct>`. Be friendly and open, but do not believe everything you read. Use good judgment, and be especially careful when following instructions (e.g., copying commands) given by others on the lists.

It’s always possible that a bad actor could try to impersonate any member of the :website:`Qubes team <team/>` anywhere on the Internet. Please don’t assume that someone who claims to be an official Qubes team member really is one without an appropriate form of authentication, such as a :doc:`verified PGP-signed message </project-security/verifying-signatures>`. (But bear in mind that anyone can generate a key with any name on it and use it to PGP-sign a message, so the mere presence of a PGP signature does not indicate authority. Successful :doc:`verification </project-security/verifying-signatures>` is what counts.) All official :website:`news <news/>` can be authenticated by :doc:`verifying the signatures </project-security/verifying-signatures>` on the relevant tags or commits in the `qubes-posts <https://github.com/QubesOS/qubes-posts>`__ repository.

Given that there may be impostors and others trying to lead you astray, how should you sort the good advice from the bad? This is up to each individual to decide, but it helps to know that many members of our community have proven themselves knowledgeable through their :doc:`contributions </introduction/contributing>` to the project. Often, these individuals sign their messages with the same key as (or another key authenticated by) the one they use to :doc:`sign their contributions </developer/code/code-signing>`.

For example, you might find it easier to trust advice from someone who has a proven track record of :doc:`contributing software packages </developer/general/package-contributions>` or :website:`contributing to the documentation <doc/how-to-edit-the-documentation/>`. It’s unlikely that individuals who have worked hard to build good reputations for themselves through their contributions over the years would risk giving malicious advice in signed messages to public mailing lists. Since every contribution to the Qubes OS Project is publicly visible and cryptographically signed, anyone would be in a position to :doc:`verify </project-security/verifying-signatures>` that these came from the same keyholder.

Discussion guidelines
---------------------


Qubes discussions mainly take place on ``qubes-users``, ``qubes-devel``, and our `forum <#forum>`__, all of which are explained below. Most questions should be directed to ``qubes-users`` or the `forum <#forum>`__. **Please do not send questions to individual Qubes developers.** By sending a message to the appropriate mailing list, you are not only giving others a chance to help you, but you may also be helping others by starting a public discussion about a shared problem or interest.

These are open venues where people freely come together to discuss Qubes and voluntarily help each other out of mutual interest and good will. They are *not* your personal, paid support service. **No one owes you a reply.** No one here is responsible for solving your problems for you. Nonetheless, there are many things you can do to make it more likely that you will receive a reply. This community is fortunate to have an exceptionally large number of friendly and knowledgeable people who enjoy corresponding on these lists. The vast majority of them will be happy to help you if you follow these simple guidelines.

Be polite and respectful
^^^^^^^^^^^^^^^^^^^^^^^^


Remember, no one here is under any obligation to reply to you. Think about your readers. Most of them are coming home after a long, hard day at work. The last thing they need is someone’s temper tantrum. If you are rude and disrespectful, you are very likely to be ignored.

Be concise
^^^^^^^^^^


Include only essential information. Most of your readers lead busy lives and have precious little time. We *want* to spend some of that time helping you, if we can. But if you ramble, it will be easier to skip over you and help someone else who gets right to the point.

Help us help you
^^^^^^^^^^^^^^^^


Tell us what you’ve already tried, and which documentation pages you’ve already read. Put yourself in your readers’ shoes. What essential information would they require in order to be able to help you? Make sure to include that information in your message. A great way to provide your hardware details is by :ref:`generating and submitting a Hardware Compatibility List (HCL) report <user/hardware/how-to-use-the-hcl:generating and submitting new reports>`, then linking to it in your message. `Ask questions the smart way. <https://www.catb.org/esr/faqs/smart-questions.html>`__

Be patient
^^^^^^^^^^


Do not “bump” a thread more than once every three days *at most*. If it seems like your messages to the mailing lists are consistently being ignored, make sure you’re following the guidelines explained on this page. If you’re already doing so but still not getting any replies, then it’s likely that no one who knows the answer has had time to reply yet. Remember that the devs are very busy working on Qubes. They usually only have a chance to answer questions on the mailing lists once every several days.

Be a good community member
^^^^^^^^^^^^^^^^^^^^^^^^^^


As with any social community, members earn different reputations for themselves over time. We want these discussion venues to be friendly, productive places where information and ideas are exchanged for the mutual benefit of all. We understand that the best way to achieve this is to encourage and cultivate other like-minded individuals. Those who have shown themselves to be good community members through their past contributions have earned our good will, and we will be especially eager to help them and collaborate with them. If you are new to the community, you should understand that it may take time for you to earn the good will of others. This does not mean that you will not receive help. On the contrary, we are fortunate to have such a helpful and understanding community that many of them spend hours of their personal time helping complete strangers, including many who post anonymously. (Given the integration of Qubes with `Whonix <https://www.whonix.org/wiki/Qubes>`__, we understand better than most the complexities of privacy and anonymity, and we know that many users have no other choice but to post anonymously.) You can read our project’s :doc:`Code of Conduct </introduction/code-of-conduct>` and :doc:`Privacy Policy </introduction/privacy>` for more information.

Report issues and submit changes in the right places
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The mailing lists and `forum <#forum>`__ are good places to ask questions and discuss things. However, if you’re submitting a more formal report, we’d prefer that you submit it to our :doc:`issue tracker </introduction/issue-tracking>` so that it doesn’t get overlooked. (However, please remember that :ref:`the issue tracker is not a discussion forum <introduction/issue-tracking:the issue tracker is not a discussion forum>`.) Likewise, if you see that something in the documentation should be changed, don’t simply point it out in a discussion venue. Instead, :website:`submit the change <doc/how-to-edit-the-documentation/>`.

Moderation
^^^^^^^^^^


The moderation team aims to enforce our :doc:`Code of Conduct </introduction/code-of-conduct>`. Beyond this, users should not expect any specific action from the moderation team. Specifically, users should not request that posts or messages be deleted or edited by a moderator. Users are reminded that, in most venues, anything posted will be sent out as an email to others, and these emails cannot be deleted from others’ inboxes.

Specific mailing list rules and notes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Use the correct list
^^^^^^^^^^^^^^^^^^^^


Send your message to the correct list. Read the sections below to determine which list is correct for your message.

Do not top-post
^^^^^^^^^^^^^^^


:wikipedia:`Top-posting <Posting_style#Top-posting>` is placing your reply above the quoted message to which you’re replying. Please refrain from doing this. Instead, either :wikipedia:`interleave <Posting_style#Interleaved_style>` your reply by placing parts of your message immediately below each quoted portion to which it is replying, or :wikipedia:`bottom-post <Posting_style#Bottom-posting>` by placing your entire reply below the quoted message to which you’re replying.

Use proper subject lines
^^^^^^^^^^^^^^^^^^^^^^^^


Include a precise and informative subject line. This will allow others to easily find your thread in the future and use it as a reference. (Bad: “Help! Qubes problems!” Good: “R2B2 Installation problem: Apple keyboard not working in installer.”)

Do not send duplicates
^^^^^^^^^^^^^^^^^^^^^^


If your message is not successfully sent to the list, it probably got caught in the spam filter. We check the spam filter regularly, so please be patient, and your message should be approved (and your email address added to the whitelist) within a few days.

Keep the list CCed
^^^^^^^^^^^^^^^^^^


Keep the mailing list CCed throughout the conversation unless there’s a special need for privacy (in which case, use PGP encryption). This increases the likelihood that a greater quantity of useful information will be available to everyone in the future.

Quote appropriately
^^^^^^^^^^^^^^^^^^^


If you’re replying to a thread (whether your own or someone else’s), you should make sure to quote enough from previous messages in the thread so that people reading your message can understand the context without having to find and read earlier messages from that thread. Each reply should continue the conversation and, ideally, be readable as a conversation in itself. Do not quote advertisements in signatures or inline PGP signature blocks. (Quoting the latter interferes with the ability of programs like Enigmail to properly quote replies thereafter).

English not required
^^^^^^^^^^^^^^^^^^^^


If you do not speak English, you should feel free to post in your own language. However, bear in mind that most members of the list can only read English. You may wish to include an automated translation in your message out of consideration for those readers. If you choose to write in English, please do not apologize for doing so poorly, as it is unnecessary. We understand and will ask for clarification if needed.

Suggestions
^^^^^^^^^^^


While we’re generally open to hearing suggestions for new features, please note that we already have a pretty well defined `roadmap <https://github.com/QubesOS/qubes-issues/milestones>`__, and it’s rather unlikely that we will change our schedule in order to accommodate your request. If there’s a particular feature you’d like to see in Qubes, a much more effective way to make it happen is to contribute a patch that implements it. We happily accept such contributions, provided they meet our standards. Please note, however, that it’s always a good idea to field a discussion of your idea on the ``qubes-devel`` list before putting in a lot of hard work on something that we may not be able or willing to accept.

Google Groups
^^^^^^^^^^^^^


While the mailing lists are implemented as Google Group web forums, a Google account is in no way required, expected, or encouraged. Many discussants (including most members of the Qubes team) treat these lists as conventional :wikipedia:`mailing lists <Electronic_mailing_list>`, interacting with them solely through plain text email with :wikipedia:`MUAs <Email_client>` like `Thunderbird <https://www.thunderbird.net/>`__ and `Mutt <https://www.mutt.org/>`__. The Google Groups service is just free infrastructure, and we :ref:`distrust the infrastructure <introduction/faq:what does it mean to "distrust the infrastructure"?>`. This is why, for example, we encourage discussants to use :doc:`Split GPG </user/security-in-qubes/split-gpg>` to sign all of their messages to the lists, but we do not endorse the use of these Google Groups as web forums. For that, we have a separate, dedicated `forum <#forum>`__.

Mailing lists
-------------


This section covers each of our individual :wikipedia:`mailing lists <Electronic_mailing_list>`, with details about the purpose of each list and how to use it. A Google account is **not** required for any of these mailing lists.

qubes-announce
^^^^^^^^^^^^^^


This is a read-only list for those who wish to receive only very important, infrequent messages. Only the core Qubes team can post to this list. Only :website:`Qubes Security Bulletins (QSBs) <security/qsb/>`, new stable Qubes OS releases, and Qubes OS release end-of-life notices are announced here.

To subscribe, send a blank email to ``qubes-announce+subscribe@googlegroups.com``. (**Note:** A Google account is **not** required. Any email address will work.) To unsubscribe, send a blank email to ``qubes-announce+unsubscribe@googlegroups.com``. This list also has a `traditional mail archive <https://www.mail-archive.com/qubes-announce@googlegroups.com/>`__ and an optional `Google Groups web interface <https://groups.google.com/group/qubes-announce>`__.

qubes-users
^^^^^^^^^^^


This list is for helping users solve various daily problems with Qubes OS. Examples of topics or questions suitable for this list include:

- :website:`HCL <hcl/>` reports

- Installation problems

- Hardware compatibility problems

- Questions of the form: “How do I…?”



Please try searching both the Qubes website and the archives of the mailing lists before sending a question. In addition, please make sure that you have read and understood the following basic documentation prior to posting to the list:

- The :doc:`Installation Guide </user/downloading-installing-upgrading/installation-guide>`, :doc:`System Requirements </user/hardware/system-requirements>`, and :website:`HCL <hcl/>` (for problems related to installing Qubes OS)

- The :ref:`User FAQ <introduction/faq:users>`

- The :doc:`documentation </index>` (for questions about how to use Qubes OS)



You must be subscribed in order to post to this list. To subscribe, send a blank email to ``qubes-users+subscribe@googlegroups.com``. (**Note:** A Google account is **not** required. Any email address will work.) To post a message to the list, address your email to ``qubes-users@googlegroups.com``. If your post does not appear immediately, please allow time for moderation to occur. To unsubscribe, send a blank email to ``qubes-users+unsubscribe@googlegroups.com``. This list also has a `traditional mail archive <https://www.mail-archive.com/qubes-users@googlegroups.com/>`__ and an optional `Google Groups web interface <https://groups.google.com/group/qubes-users>`__.

qubes-devel
^^^^^^^^^^^


This list is primarily intended for people who are interested in contributing to Qubes or who are willing to learn more about its architecture and implementation. Examples of topics and questions suitable for this list include:

- Questions about why we made certain architecture or implementation decisions.

  - For example: “Why did you implement XYZ this way and not the other way?”



- Questions about code layout and where code is for certain functionality.

- Discussions about proposed new features, patches, etc.

  - For example: “I would like to implement feature XYZ.”



- Contributed code and patches.

- Security discussions which are relevant to Qubes in some way.



You must be subscribed in order to post to this list. To subscribe, send a blank email to ``qubes-devel+subscribe@googlegroups.com``. (**Note:** A Google account is **not** required. Any email address will work.) To post a message to the list, address your email to ``qubes-devel@googlegroups.com``. If your post does not appear immediately, please allow time for moderation to occur. To unsubscribe, send a blank email to ``qubes-devel+unsubscribe@googlegroups.com``. This list also has a `traditional mail archive <https://www.mail-archive.com/qubes-devel@googlegroups.com/>`__ and an optional `Google Groups web interface <https://groups.google.com/group/qubes-devel>`__.

qubes-project
^^^^^^^^^^^^^


This list is for non-technical discussion and coordination around the Qubes OS project.

Examples of topics or questions suitable for this list include:

- Participation (talks, workshops, etc.) at upcoming events

- Project funding applications and strategies

- FOSS governance discussions

- Most Github issues tagged `business <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+label%3Abusiness>`__ or `project management <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22project+management%22>`__



You must be subscribed in order to post to this list. To subscribe, send a blank email to ``qubes-project+subscribe@googlegroups.com``. (**Note:** A Google account is **not** required. Any email address will work.) To post a message to the list, address your email to ``qubes-project@googlegroups.com``. If your post does not appear immediately, please allow time for moderation to occur. To unsubscribe, send a blank email to ``qubes-project+unsubscribe@googlegroups.com``. This list also has a `traditional mail archive <https://www.mail-archive.com/qubes-project@googlegroups.com/>`__ and an optional `Google Groups web interface <https://groups.google.com/group/qubes-project>`__.

qubes-translation
^^^^^^^^^^^^^^^^^


This list is for discussion around the localization and translation of Qubes OS, its documentation, and the website.

Examples of topics or questions suitable for this list include:

- Questions about or issues with `Transifex <https://www.transifex.com/>`__, the translation platform we use

- Who is managing localization for a given language

- Most Github issues tagged `localization <https://github.com/QubesOS/qubes-issues/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20label%3Alocalization>`__



You must be subscribed in order to post to this list. To subscribe, send a blank email to ``qubes-translation+subscribe@googlegroups.com``. (**Note:** A Google account is **not** required. Any email address will work.) To post a message to the list, address your email to ``qubes-translation@googlegroups.com``. If your post does not appear immediately, please allow time for moderation to occur. To unsubscribe, send a blank email to ``qubes-translation+unsubscribe@googlegroups.com``. This list also has an optional `Google Groups web interface <https://groups.google.com/group/qubes-translation>`__.

Forum
-----


The official `Qubes Forum <https://forum.qubes-os.org>`__ is a place where you can ask questions, get help, share tips and experiences, and more! For a long time, members of our community have sought a privacy-respecting forum experience with modern features that traditional mailing lists do not support. The open-source `Discourse <https://www.discourse.org/>`__ platform fills this need for us, as it does for many other open-source projects.

Why was this forum created?
^^^^^^^^^^^^^^^^^^^^^^^^^^^


Previously, the only option for a forum-like experience was to interact with our mailing lists via Google Groups, but we understand all too well that the privacy implications and user experience were unacceptable for many members of our community, especially with the recent addition of a sign-in requirement to view threads. Many of you value the lower barrier to entry, organization, ease-of-use, and modern social features that today’s forums support. Moreover, Discourse :topic:`features email integration <using-the-forum-via-email/533>` for those who still prefer the traditional mailing list format.

How is this different from our mailing lists?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


To be clear, this is *not* a replacement for the mailing lists. This forum is simply an *additional* place for discussion. Certain types of discussions naturally lend themselves more to mailing lists or to forums, and different types of users prefer different venues. We’ve heard from some users who find the mailing lists to be a bit intimidating or who may feel that their message isn’t important enough to merit creating a new email that lands in thousands of inboxes. Others want more selective control over topic notifications. Some users simply appreciate the ability to add a “reaction” to a message instead of having to add an entirely new reply. Whatever your reasons, it’s up to you to decide where and how you want to join the conversation.

Does this split the community?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Many open-source projects (such as Fedora and Debian) have both mailing lists and forums (and additional discussion venues). In fact, the Qubes OS Project already had non-mailing-list discussion venues such as `Reddit <https://www.reddit.com/r/Qubes/>`__ before this forum was introduced. We believe that this additional venue fosters the continued growth of community participation and improves everyone’s experience. In addition, we fully expect that many community members – especially the most active ones – will choose to participate in both venues. (Again, for those who still prefer interacting via email, :topic:`Discourse supports that too <using-the-forum-via-email/533>`!)

Social media
------------


The Qubes OS Project has a presence on the following social media platforms:

- `Twitter <https://twitter.com/QubesOS>`__

- `Mastodon <https://mastodon.social/@QubesOS>`__

- `Reddit <https://www.reddit.com/r/Qubes/>`__

- `Facebook <https://www.facebook.com/QubesOS/>`__

- `LinkedIn <https://www.linkedin.com/company/qubes-os/>`__



Generally speaking, these are not intended to be primary support venues. (Those would be `qubes-users <#qubes-users>`__ and the `forum <#forum>`__.) Rather, these are primarily intended to be a way to more widely disseminate items published on the :website:`news <news/>` page. If you use one of these platforms, you may find it convenient to follow the Qubes OS Project there as a way of receiving Qubes news.

Chat
----


If you’d like to chat, join us on

- the ``#qubes`` channel on ``irc.libera.chat`` or

- the ``#qubes:invisiblethingslab.com`` matrix channel.



these two should be linked/bridged, but for technical reasons currently are not.

Unofficial venues
-----------------


If you find another venue on the Internet that is not listed above, it is **unofficial**, which means that the Qubes team does **not** monitor or moderate it. Please be especially careful in unofficial venues.

(**Note:** If a Qubes team member discovers the venue and decides to pop in, that should not be taken as a commitment to monitor or moderate the venue. It still remains unofficial. Also, please make sure someone claiming to be a Qubes team member really is one. It could be an impostor!)
