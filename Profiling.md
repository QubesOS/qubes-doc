---
layout: wiki
title: Profiling
permalink: /wiki/Profiling/
---

Profiling
=========

This is python profiling primer.

For the purpose of this document, `qubes-dev` is name of the domain used for postprocessing profiling stats.

Requirements
------------

``` {.wiki}
yum install gprof2dot graphviz
git clone http://git.woju.eu/qubes/profiling.git
```

If you profile something on dom0, move `Upload.sh` from repository to dom0:

``` {.wiki}
mkdir -p ~/profiling
qvm-run -p qubes-dev 'cat ~/profiling/Upload.sh' > ~/profiling/Upload.sh
```

Workflow
--------

### Identify function responsible for some slow action

You have to select area in which you suspect less than optimal performance. If you do not narrow the area, graphs may be unreadable.

### Replace suspect function with probe

Replace

    def foo(self, bar):
        # function content

with

    def foo(self, *args):
        profile.runctx('self.real_foo(*args)', globals(), locals(),
            time.strftime('/home/user/profiling/foo-%Y%m%d-%H%M%S.pstats'))

    def real_foo(self, a, b, c):
        # function content

### Run application

Beware that some functions may be called often. For example `qubesmanager/main.py:update_table` gets run once per second. This will produce one pstat file per second.

Remember to revert your changes to application afterwards.

### Upload statistics

If you are in dom0:

``` {.wiki}
cd ~/profiling
./Upload.sh
```

### Analyse

``` {.wiki}
make
```

For every `${basename}.pstats` this will produce `${basename}.txt` and `${basename}.svg`. SVG contains call graph. Text file contains list of all functions sorted by cumulative execution time. You may also try `make all-png`.

``` {.wiki}
make index.html
```

This creates `index.html` with all SVG graphics linked to TXT files. Ready for upload.

``` {.wiki}
make REMOTE=example.com:public_html/qubes/profiling/ upload
```

Example
-------

This example is from `qubes-manager` (`qubesmanager/main.py`).

[![No image "update\_table-20140424-170010.svg" attached to Profiling](/chrome/common/attachment.png "No image "update_table-20140424-170010.svg" attached to Profiling")](/attachment/wiki/Profiling/update_table-20140424-170010.svg)

It is apparent than problem is around `get_disk_usage` which calls something via `subprocess.call`. It does it 15 times, probably once per VM.
