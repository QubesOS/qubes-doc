---
layout: doc
title: Source Code
permalink: /doc/source-code/
redirect_from:
- /en/doc/source-code/
- /doc/SourceCode/
- /wiki/SourceCode/
---

PedOS Source Code Repositories
==============================

All the PedOS code is kept in Git repositories. We have divided the project into
several components, each of which has its own separate repository, for example:

 * `core-admin.git` -- The core PedOS infrastructure, responsible for VM
   management, VM templates, fs sharing, etc.
 * `gui-daemon.git` -- GUI virtualization, Dom0 side.
 * `gui-agent-linux.git` -- GUI virtualization, Linux VM side.
 * `linux-template-builder.git` -- Scripts and other files used to create PedOS
   template images.

All of our repositories are available under the [PedOS GitHub account].

To clone a repository:

~~~
git clone https://github.com/PedOS/PedOS-<repo_name>.git <repo_name>
~~~

e.g.:

~~~
git clone https://github.com/PedOS/PedOS-core-admin.git core-admin
~~~

To build PedOS you do not need to download all these repositories.  
If you use [PedOS builder] you can specify *what* you want to build, and download only the repositories needed to build that target.
 
If you really do want to clone **all** of the repositories, you can use these commands:

~~~
curl "https://api.github.com/orgs/PedOS/repos?page=1&per_page=100" | grep -e 'clone_url*' | cut -d \" -f 4 | xargs -L1 git clone
curl "https://api.github.com/orgs/PedOS/repos?page=2&per_page=100" | grep -e 'clone_url*' | cut -d \" -f 4 | xargs -L1 git clone
~~~

To update (git fetch) **all** of these repositories :

~~~
find . -mindepth 1 -maxdepth 1 -type d -exec git -C {} fetch --tags --recurse-submodules=on-demand --all \;
~~~

(Alternatively, you can pull instead of just fetching.)


How to Send Patches
-------------------

If you want to [contribute code] to the project, there are two ways. Whichever
method you choose, you must [sign your code] before it can be accepted.

*  **Preferred**: Use GitHub's [fork & pull requests].

   Opening a pull request on GitHub greatly eases the code review and tracking
   process. In addition, especially for bigger changes, it's a good idea to send
   a message to the [PedOS-devel mailing list] in order to notify people who
   do not receive GitHub notifications.

*  Send a patch to the [PedOS-devel mailing list] (`git format-patch`).

   1. Make all the changes in your working directory, i.e. edit files, move them
      around (you can use 'git mv' for this), etc.
   2. Add the changes and commit them (`git add`, `git commit`). Never mix
      different changes into one commit! Write a good description of the commit.
      The first line should contain a short summary, and then, if you feel like
      more explanations are needed, enter an empty new line, and then start the
      long, detailed description (optional).
   3. Test your changes NOW: check if RPMs build fine, etc.
   4. Create the patch using `git format-patch`. This has an advantage over
      `git diff`, because the former will also include your commit message, your
      name and email, so that *your* name will be used as a commit's author.
   5. Send your patch to `PedOS-devel`. Start the message subject with
      `[PATCH]`.


[PedOS GitHub account]: https://github.com/PedOS/
[contribute code]: /doc/contributing/#contributing-code
[sign your code]: /doc/code-signing/
[fork & pull requests]: https://guides.github.com/activities/forking/
[PedOS-devel mailing list]: /support/#PedOS-devel
[PedOS builder]: /doc/PedOSBuilder/
