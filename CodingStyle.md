---
layout: doc
title: CodingStyle
permalink: /doc/CodingStyle/
redirect_from: /wiki/CodingStyle/
---

Coding Guidelines for Qubes Developers
======================================

Rationale
---------

Maintaining proper coding style is very important for any larger software project, such as Qubes. Here's why:

-   It eases maintenance, such as adding new functionality or generalization later,
-   It allows others (as well as the original author after some time!) to easily understand fragments of code, what they were supposed to do, and so makes it easier to later extend them with newer functionality or bug fixes,
-   It allows others to easily review the code and catch various bugs,
-   It provides for an aesthetically pleasing experience when one reads the code...

Often, developers, usually smart developers, neglect the value of proper coding style, thinking that it's most important how their code works, and expecting that if it solves some problem using a nice and neat trick, then it's all that is really required. Such thinking shows, however, immaturity and is a signal that the developer, however bright and smart, might not be a good fit for any larger project. Writing a clever exploit, that is to be used at one Black Hat show is one thing, while writing a useful software that is to be used and maintained for years, is quite a different story. If you want to show off how smart programmer you are, then you should become a researcher and write exploits. If, on the other hand, you want to be part of a team that makes real, useful software, you should ensure your coding style is impeccable. We often, at Qubes project, often took shortcuts, and often wrote nasty code, and this always back fired at us, sometime months, sometime years later, the net result being we had to spend time fixing code, rather than implementing new functionality.

And here's a [link to the real case](https://groups.google.com/forum/#!msg/qubes-devel/XgTo6L8-5XA/JLOadvBqnqMJ) (one Qubes Security Bulletin) demonstrating how the above described problem lead to a real security bug. Never assume you're smart enough that you can disregard clean and rigorous coding!

General typographic conventions
-------------------------------

-   **Use space-expanded tabs that equal 4 spaces.** Yes, we know, there are many arguments for using "real" tabs, instead of space-expanded tabs, but we need to pick one convention to make the project consistent. One argument for using space-expanded tabs is that this way the programmer is in control of how the code will look like, despite how other users have configured their editors to visualize the tabs (of course, we assume any sane person uses a fixed-width font for viewing the source code). Anyway, if this makes you feel better, assume this is just an arbitrary choice.

-   **Maintain max. line length of 80 characters**. Even though today's monitors often are very wide and it's often not a problem to have 120 characters displayed in an editor, still maintaining shorter line lengths improves readability. It also allows to have two parallel windows open, side by side, each with different parts of the source code.

-   Class, functions, variables, and arguments naming convention for any OS other than Windows:
    -   `ClassName`
    -   `some_variable`, `some_function`, `some_argument`

-   Class, functions, variables, and arguments naming convention for **Windows OS** -- exceptionally to preserve Windows conventions please use the following:
    -   `ClassName`, `FunctionName`
    -   `pszArgumentOne`, `hPipe` -- use hungerian notation for argument and variables

-   Horizontal spacing -- maintain at least decent amount of horizontal spacing, such as e.g. add obligatory space after `if` or before `{` in C, and similar in other languages. Whether to also use spaces within expressions, such as (x\*2+5) vs. (x \* 2 + 5) is left to the developer's judgment. Do not put spaces immediately after and before the brackets in expressions, so avoid constructs like this: `if ( condition )` and use `if (condition)` instead.

-   **Use single new lines** ('\\n' aka LF) in any non-Windows source code. On Windows, exceptionally, use the CRLF line endings -- this will allow the source code to be easily view-able in various Windows-based programs.

-   **Use descriptive names for variables and functions**! Really, these days, when most editors have auto-completion feature, there is no excuse for using short variable names.

-   Comments should be indent together with the code, e.g. like this:

    {% highlight trac-wiki %}
    for (...) {
        // The following code finds PGP private key matching the given public key in O(1)
        while (key_found) {
            (...)
        }
    }
    {% endhighlight %}

File naming conventions
-----------------------

-   All file names written with small letters, use dash to separate words, rather than underscores, e.g. `qubes-dom0-update`. Never use spaces!

**File naming in Linux/Unix-like systems:**

-   User commands that operate on particular VMs (also those accessible in VMs): `/usr/bin/qvm-*`
-   User commands that apply to the whole system (Dom0 only): `/usr/bin/qubes-*`
-   Auxilary executables and scripts in `/usr/libexec/qubes/` (Note: previously we used `/usr/lib/qubes` but decided to change that)
-   Helper, non-exeutable files in `/usr/share/qubes/`
-   Various config files in `/etc/qubes`
-   Qubes RPC services in `/etc/qubes-rpc`. Qubes RPC Policy definitions (only in Dom0) in `/etc/qubes-rpc/policy/`
-   All VM-related configs, images, and other files in `/var/lib/qubes/`
-   System-wide temporary files the reflect the current state of system in `/var/run/qubes`
-   Logs: either log to the system-wide messages, or to `/var/log/qubes/`

**File naming in Windows systems:**

-   All base qubes-related files in `C:\Program Files\Invisible Things Lab\Qubes\` (Exceptionally spaces are allowed here to adhere to Windows naming conventions)
-   Other, 3rd party files, not Qubes-specific, such as e.g. Xen PV drivers might be in different vendor subdirs, e.g. `C:\Program Files\Xen PV Drivers`

General programming style guidelines
------------------------------------

-   Do not try to impress wit your coding kung-fu, do not use tricks to save 2 lines of code, always prefer readability over trickiness!
-   Make sure your code compiles and builds without warnings.
-   Always first first about interfaces (e.g. function arguments, or class methods) and data structures before you start writing the actual code.
-   Use comments to explain non-trivial code fragments, or expected behavior of more complex functions, if it is not clear from their name.
-   Do **not** use comments for code fragments where it is immediately clear what the code does. E.g. avoid constructs like this:

    {% highlight trac-wiki %}
    // Return window id
    int get_window_id (...) {
        (...)
        return id;
    }
    {% endhighlight %}

-   Do **not** use comments to disable code fragments. In a production code there should really be no commented or disabled code fragments. If you really, really have a good reason to retain some fragment of unused code, use \#if or \#ifdef to disable it, e.g.:

    {% highlight trac-wiki %}
    #if 0
        (...)   // Some unused code here
    #endif
    {% endhighlight %}

    ... and preferably use some descriptive macro instead of just `0`, e.g.:

    {% highlight trac-wiki %}
    #if USE_OLD_WINDOW_TRAVERSING
        (...)   // Some unused code here
    #endif
    {% endhighlight %}

    Not sure how to do similar thing in Python... Anyone?

> But generally, there is little excuse to keep old, unused code fragments in the code. One should really use the functionality provided by the source code management system, such as git, instead. E.g. create a special branch for storing the old, unused code -- this way you will always be able to merge this code into upstream in the future.

-   Do not hardcode values in the code! The only three numbers that are an exception here and for which it is acceptable to hardcode them are: `0`, `1` and `-1`, and frankly the last two are still controversial...

Source Code management (Git) guidelines
---------------------------------------

-   Use git to maintain all code for Qubes project.

-   Before you start using git, make sure you understand that git is a decentralized Source Code Management system, and that it doesn't behave like traditional, centralized source code management systems, such as SVN. Here's a good [introductory book on git](http://git-scm.com/book). Read it.

-   Qubes code is divided into many git repositories. There are several reasons for that:
    -   This creates natural boundaries between different code blocks, enforcing proper interfaces, and easing independent development to be conducted on various code parts at the same time, without the fear of running into conflicts.
    -   By maintaining relatively small git repositories, it is easy for new developers to understand the code and contribute new patches, without the need to understand all the other code.
    -   Code repositories represent also licensing boundaries. So, e.g. because `core-agent-linux` and `core-agent-windows` are maintained in two different repositories, it is possible to have the latter under a proprietary, non-GPL license, while keeping the former fully open source.
    -   We have drastically changes the layout and naming of the code repositories shortly after Qubes OS R2 Beta 2 release. For details on the current code layout, please read [this article](http://theinvisiblethings.blogspot.com/2013/03/introducing-qubes-odyssey-framework.html).

Security coding guidelines
--------------------------

-   As a general rule: **untrusted input** is our \#1 enemy!
-   Any input that comes from untrusted, or less trusted, or just differently-trusted, entity should always be considered as malicious and should always be sanitized and verified. So, if your software runs in Dom0 and processes some input from any of the VMs, this input should be considered to be malicious. Even if your software runs in a VM, and processes input from some other VM, you should also assume that the input is malicious and verify it.
-   Use `untrusted_` prefix for all variables that hold values read from untrusted party and which have not yet been verified to be decent, e.g.:

    {% highlight trac-wiki %}
       read_struct(untrusted_conf);
       /* sanitize start */
       if (untrusted_conf.width > MAX_WINDOW_WIDTH)
           untrusted_conf.width = MAX_WINDOW_WIDTH;
       if (untrusted_conf.height > MAX_WINDOW_HEIGHT)
           untrusted_conf.height = MAX_WINDOW_HEIGHT;
       width = untrusted_conf.width;
       height = untrusted_conf.height;
    {% endhighlight %}

-   Use another variables, without the `untrusted_` prefix to hold the sanitized values, as seen above.

Python-specific guidelines
--------------------------

-   Please follow the guidlines [here](http://www.python.org/dev/peps/pep-0008/), unless they were in conflict with what is written on this page.

C and C++ specific guidelines
-----------------------------

-   Do not place code in `*.h` files.
-   Use `const` whenever possible, e.g. in function arguments passed via pointers.
-   Do not mix procedural and objective code together -- if you write in C++, use classes and objects.
-   Think about classes hierarchy, before start implementing specific methods.

Bash-specific guidelines
------------------------

-   Avoid writing scripts in bash whenever possible. Use python instead. Bash-scripts are Unix-specific and will not work under Windows VMs, or in Windows admin domain, or Windows gui domain.

