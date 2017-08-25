---
layout: doc
title: qvm-file-trust
permalink: /doc/vm-tools/qvm-file-trust/
redirect_from:
- /en/doc/vm-tools/qvm-file-trust/
- /doc/VmTools/QvmFileTrust/
- /wiki/VmTools/QvmFileTrust/
---

qvm-file-trust
==============

NAME
----

qvm-file-trust - manage and view file or folder trust levels

Date
2017-08-24

SYNOPSIS
--------
**qvm-file-trust** [option] path [path ..]

DESCRIPTION
-----------
**qvm-file-trust** can check and modify the **trust level** of files and
folders. A folder is considered untrusted if its path lies in either the global
untrusted folders list (/etc/qubes/always-open-in-dispvm.list) or the local
list (~/.config/qubes/always-open-in-dispvm.list).

A file is considered trusted unless:

1. It sits under an untrusted folder's path

2. It has a 'user.qubes.untrusted' extended file attribute

3. It sits in a file path that has the phrase 'untrusted' in it. This phrase
   can be configured in /etc/qubes/always-open-in-dispvm.phrase

A '-' character can be placed in front of a path in the local list to override
a path listed in the local list.

OPTIONS
-------
-h, --help
Display the help text.
-c, --check
Display the trust level of the file or folder. This is the default action.
-C, --check-multiple
Returns 1 if at least one path is untrusted.
-C, --check-multiple-all-untrusted
Check trust for multiple paths. Returns 1 if and only if ALL paths are
untrusted.
-u, --untrusted
Mark the file or folder as untrusted.
-t, --trusted
Mark the file or folder as trusted.
-q, --quiet
Execute the command silently. Useful for scripts.
-p, --printfolders
Print all folders on the system that are considered untrusted.

EXAMPLES
--------
Check the trust level of a file:
    qvm-file-trust [--check] ./leaked-document.pdf

Mark a file as untrusted:
    qvm-file-trust --untrusted ./leaked-document.pdf

Mark multiple items as trusted at once:
    qvm-file-trust --trusted ~/files/ ./recipes.txt

ERRORS
------
0   No errors. File or folder is **trusted**

1   No errors. File or folder is **untrusted**

64  Improper arguments provided

65  Issue reading/setting extended file attributes

72  Unable to read from/write to a file, such as global or local rule lists

77  Unable to unlock/chmod file, or no permissions

AUTHORS
------
Andrew Morgan \<andrew at amorgan xyz\>
