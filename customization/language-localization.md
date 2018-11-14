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

The pinyin input method will be installed in a TemplateVM to make it available after restarts and across multiple AppVMs.

1. In a TemplateVM, install `ibus-pinyin` via the package manager or terminal.
   If the template is Fedora-based, run `sudo dnf install ibus-pinyin`.
   If the template is Debian-based, run `sudo apt install ibus-pinyin`

2. Shut down the TemplateVM.

3. Start or restart an AppVM based on the template in which you installed `ibus-pinyin` and open a terminal.

4. Run `ibus-setup`.

5. You will likely get an error message telling you to paste the following into your bashrc:

        export GTK_IM_MODULE=ibus
        export XMODIFIERS=@im=ibus
        export QT_IM_MODULE=ibus

   Copy the text into your `~/.bashrc` file with your favorite text editor.
   You will need to do this for any AppVM in which you wish to use pinyin input.

6. Set up ibus input as you like using the graphical menu (add pinyin or intelligent pinyin to selections).
   You can bring the menu back by issuing `ibus-setup` from a terminal.

7. Set up your shortcut for switching between inputs.
   By default it is super-space.

If `ibus-pinyin` is not enabled when you restart one of these AppVMs, open a terminal and run `ibus-setup` to activate ibus again.

For further discussion, see [this qubes-users thread](https://groups.google.com/forum/#!searchin/qubes-users/languge/qubes-users/VcNPlhdgVQM/iF9PqSzayacJ).
