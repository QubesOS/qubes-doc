---
layout: doc
title: Rxvt
permalink: /doc/rxvt/
redirect_from:
- /en/doc/rxvt/
- /doc/Rxvt/
- /wiki/Rxvt/
---

Rxvt
====

`rxvt-unicode` is an advanced and efficient vt102 emulator. Here is a quick guide to configuration in both dom0 and guest VM.

Installation
------------

`dnf install rxvt-unicode-256color-ml` will bring both base `rxvt-unicode` and extension.
Let me also recommend excellent Terminus font: `dnf install terminus-fonts`.

Xresources
----------

In TemplateVM create file `/etc/X11/Xresources.urxvt` and paste config below.
`!`-lines are comments and may be left out.
`#`-lines are directives to CPP (C preprocessor) and are necessary.
This shouldn't go to `/etc/X11/Xresources`, because that file is not preprocessed by default.

~~~
! CGA colour palette

!*color0:                       #000000
!*color1:                       #AA0000
!*color2:                       #00AA00
!*color3:                       #AA5500
!*color4:                       #0000AA
!*color5:                       #AA00AA
!*color6:                       #00AAAA
!*color7:                       #AAAAAA
!*color8:                       #555555
!*color9:                       #FF5555
!*color10:                      #55FF55
!*color11:                      #FFFF55
!*color12:                      #5555FF
!*color13:                      #FF55FF
!*color14:                      #55FFFF
!*color15:                      #FFFFFF

! Qubes' favourite tango palette (improved with cyan)

#define TANGO_Butter1           #c4a000
#define TANGO_Butter2           #edd400
#define TANGO_Butter3           #fce94f
#define TANGO_Orange1           #ce5c00
#define TANGO_Orange2           #f57900
#define TANGO_Orange3           #fcaf3e
#define TANGO_Chocolate1        #8f5902
#define TANGO_Chocolate2        #c17d11
#define TANGO_Chocolate3        #e9b96e
#define TANGO_Chameleon1        #4e9a06
#define TANGO_Chameleon2        #73d216
#define TANGO_Chameleon3        #8ae234
#define TANGO_SkyBlue1          #204a87
#define TANGO_SkyBlue2          #3465a4
#define TANGO_SkyBlue3          #729fcf
#define TANGO_Plum1             #5c3566
#define TANGO_Plum2             #75507b
#define TANGO_Plum3             #ad7fa8
#define TANGO_ScarletRed1       #a40000
#define TANGO_ScarletRed2       #cc0000
#define TANGO_ScarletRed3       #ef2929
#define TANGO_Aluminium1        #2e3436
#define TANGO_Aluminium2        #555753
#define TANGO_Aluminium3        #888a85
#define TANGO_Aluminium4        #babdb6
#define TANGO_Aluminium5        #d3d7cf
#define TANGO_Aluminium6        #eeeeec

*color0:  TANGO_Aluminium1
*color1:  TANGO_ScarletRed2
*color2:  TANGO_Chameleon1
*color3:  TANGO_Chocolate2
*color4:  TANGO_SkyBlue1
*color5:  TANGO_Plum2
*color6:  #06989a
*color7:  TANGO_Aluminium4

*color8:  TANGO_Aluminium3
*color9:  TANGO_ScarletRed3
*color10: TANGO_Chameleon3
*color11: TANGO_Butter3
*color12: TANGO_SkyBlue3
*color13: TANGO_Plum3
*color14: #34e2e2
*color15: TANGO_Aluminium6

URxvt.foreground:               #E0E0E0
!URxvt.background:              black
!URxvt.cursorColor:             rgb:ffff/0000/0000

URxvt.cursorColor:              TANGO_ScarletRed3

!URxvt.font:                    -*-terminus-*-*-*-*-14-*-*-*-*-*-iso8859-2
!URxvt.boldFont:                -*-terminus-*-*-*-*-14-*-*-*-*-*-iso8859-2
URxvt.font:                     xft:Terminus:pixelsize=14:style=Bold
URxvt.boldFont:                 xft:Terminus:pixelsize=14:style=Bold
URxvt.italicFont:               xft:Terminus:pixelsize=14:style=Regular
URxvt.boldItalicFont:           xft:Terminus:pixelsize=14:style=Regular
URxvt.scrollBar:                False
URxvt.visualBell:               False

! Qubes X11 passthrough does not support those, but in dom0 they are nice.
URxvt.background:               rgba:0000/0000/0000/afff
URxvt.depth:                    32
URxvt.urgentOnBell:             True

! TODO: write qubes-rpc to handle printing
URxvt.print-pipe:               cat > $(TMPDIR=$HOME mktemp urxvt.XXXXXX)

! selection-to-clipboard violates
! http://standards.freedesktop.org/clipboards-spec/clipboards-latest.txt [1],
! but it does for greater good: urxvt has no other means to move PRIMARY to
! CLIPBOARD, so Qubes' clipboard won't work without it. Also the rationale given
! in [1] has little relevance to advanced terminal emulator, specifically there
! is no need for w32-style intuition and virtually no need to "paste over".
URxvt.perl-ext-common:          default,selection-to-clipboard

! Prevent rxvt from entering Keyboard symbols entry mode whenever you press
! ctrl+shift, e.g. to copy or paste something to/from Qubes' clipboard.
URxvt.iso14755_52: false

URxvt.insecure:                 False

! some termcap-aware software sometimes throw '$TERM too long'
!URxvt.termName:                rxvt-256color
~~~

Then create script to automatically merge those to xrdb.
File `/etc/X11/xinit/xinitrc.d/urxvt.sh`:

~~~
#!/bin/sh

[ -r /etc/X11/Xresources.urxvt ] && xrdb -merge /etc/X11/Xresources.urxvt
~~~

Shortcuts
---------

For each AppVM, go to *Qubes Manager \> VM Settings \> Applications*. 
Find `rxvt-unicode` (or `rxvt-unicode (256-color) multi-language`) and add.
