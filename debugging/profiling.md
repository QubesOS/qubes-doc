---
layout: doc
title: Profiling
permalink: /doc/profiling/
redirect_from:
- /en/doc/profiling/
- /doc/Profiling/
- /wiki/Profiling/
---

Profiling
=========

This is python profiling primer.

For the purpose of this document, `qubes-dev` is name of the domain used for postprocessing profiling stats.

Requirements
------------

~~~
yum install gprof2dot graphviz
git clone http://git.woju.eu/qubes/profiling.git
~~~

If you profile something on dom0, move `Upload.sh` from repository to dom0:

~~~
mkdir -p ~/profiling
qvm-run -p qubes-dev 'cat ~/profiling/Upload.sh' > ~/profiling/Upload.sh
~~~

-   WARNING: this will obviously be running third-party code which is not signed by ITL nor Fedora. You have been warned.

Workflow
--------

### Identify function responsible for some slow action

You have to select area in which you suspect less than optimal performance. If you do not narrow the area, graphs may be unreadable.

### Replace suspect function with probe

Replace

    def foo(self, bar):
        # function content

with

    def foo(self, *args, **kwargs):
        profile.runctx('self.real_foo(*args, **kwargs)', globals(), locals(),
            time.strftime('/home/user/profiling/foo-%Y%m%d-%H%M%S.pstats'))

    def real_foo(self, bar):
        # function content

### Run application

Beware that some functions may be called often. For example `qubesmanager/main.py:update_table` gets run once per second. This will produce one pstat file per second.

Remember to revert your changes to application afterwards.

### Upload statistics

If you are in dom0:

~~~
cd ~/profiling
./Upload.sh
~~~

### Analyse

~~~
make
~~~

For every `${basename}.pstats` this will produce `${basename}.txt` and `${basename}.svg`. SVG contains call graph. Text file contains list of all functions sorted by cumulative execution time. You may also try `make all-png`.

~~~
make index.html
~~~

This creates `index.html` with all SVG graphics linked to TXT files. Ready for upload.

~~~
make REMOTE=example.com:public_html/qubes/profiling/ upload
~~~

Example
-------

This example is from `qubes-manager` (`qubesmanager/main.py`).

!["update\_table-20140424-170010.svg"](//attachment/wiki/Profiling/update_table-20140424-170010.svg)

It is apparent than problem is around `get_disk_usage` which calls something via `subprocess.call`. It does it 15 times, probably once per VM.
