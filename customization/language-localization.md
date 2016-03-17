---
layout: doc
title: Language Localization
permalink: /doc/language-localization/
redirect_from:
- /en/doc/language-localization/
- /doc/LanguageLocalization/
- /wiki/LanguageLocalization/
---

Language Localization
=====================

How to set up pinyin input in Qubes
-----------------------------------

1. Don't try to install anything in Dom0. 

2. Choose a TemplateVM in which you will be using pinyin input on AppVM
   instances thereof and open a terminal there.

3. Issue `sudo yum install ibus-pinyin` (or, for a Debian template,
   `sudo apt-get install ibus-pinyin`). 

4. Close and shut down the TemplateVM. 

5. Restart an AppVM which inherits from the template and open a terminal.
 
6. Issue `ibus-setup`.

7. You will likely get the error message telling you to paste

        export GTK_IM_MODULE=ibus
        export XMODIFIERS=@im=ibus
        export QT_IM_MODULE=ibus

   into your bashrc. 

   Copy the text, and then issue: `sudo nano ~/.bashrc`
   Paste the text into the bottom of the file and press ctrl-x to save and
   close. 
   You will need to do this on any AppVM in which you wish to use pinyin input.

8. Setup ibus input as you like using the graphical menu (add pinyin or
   intelligent pinyin to selections). You can bring the menu back by issuing
   `ibus-setup` from a terminal. 

9. Use super-space as you are used to using to switch between pinyin-unicode and
   Latin character input.

10. Whenever you restart one of these AppVMs, you will need to open a terminal
    and issue `imsettings-switch ibus` to activate ibus. 

For further discussion, see [this thread](https://groups.google.com/forum/#!searchin/qubes-users/languge/qubes-users/VcNPlhdgVQM/iF9PqSzayacJ).

