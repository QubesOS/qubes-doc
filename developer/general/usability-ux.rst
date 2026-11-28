=========================
Usability & UX Guidelines
=========================

Unnecessary complexity and bad UI often scare users away from good software. To avoid this terrible fate, please always take usability and good user experience into account when contributing to Qubes OS.

If you plan to contribute to GUI tools, please read these guidelines. Additional information can also be found in our `visual style guide <https://www.qubes-os.org/doc/visual-style-guide/>`__.

Ease of Use
-----------

In open source software, a good user interface should not only enable users to achieve their goals, but also allow them to remain in control of the process. The UI should neither overwhelm the users with the amount of information presented nor hide important context from them. In the words falsely attributed to Albert Einstein: our goal is to make things as simple as possible, but not simpler. Make things simple, but removing important elements in the name of simplicity or getting rid of valuable functionality for simplicity's sake is making them too simple.

Make sure that the UI you design adheres to the following principles.

Do not waste the user's time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- the program should not *require* extensive configuration
    **example**: you don't need to set the policy directory used by the :program:`Qubes Policy Editor` - the program lists available policy files for you
- the most typical and most recommended workflows should require the least user time and attention
    **example**: :guilabel:`Create New Qube` opens at the typical use-case (a new app qube) with options such as "template" and "networking" set to system defaults; the user only has to enter qube name and click ``Create``
- the defaults should be sensible - they should work for most use cases and not require changes in most situations, if at all possible
    **example**: default settings for newly created qubes
- minimize repetitiveness: if possible, avoid multiple clicks or multiple steps for operations that can be implemented with less clicks/steps
    **example**: in the ``Devices widget``, if a device is already attached to a qube, you have an option to ``Detach`` the device, but also to ``Detach and Attach`` to another qube - the user doesn't have to do two actions, but only one

Make the UI resilient to errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- users should not be able to break the program (or the entire system) or enter an unrecoverable state
- users should not be able to compromise the integrity and security of their system accidentally
- as far as possible, there should be a possibility to undo actions
- if some actions cannot be undone (for example deleting a qube), they should be impossible to perform accidentally (in case of Qubes OS, you have to type the qube name to delete it, even using GUI tools)
- the defaults should be reasonably secure
- avoid leaving users stranded - if there is an error message, there should also be guidance on how to recover or (preferably) an actionable solution

Reduce cognitive load
^^^^^^^^^^^^^^^^^^^^^

- show only the relevant information
    **example**: domains widget does not show qubes that are not running and not consuming resources
- use simple and understandable language
    when in doubt, like the author of this document, always use the simpler word and don't write like it's a master's thesis in English literature
- make it easy to discover and understand features and available options
    **example**: :guilabel:`Qubes Global Config` aims to show and describe multiple configuration settings that otherwise were only available via CLI and knowing about them
- do not expect the user to remember: remind them of past actions and choices
    **example**: during the update process, show which qubes are being updated right now, which are still queued for updated and which are done updating
- the defaults should make sense for most use cases and not require the user to verify them thoroughly
    **example**: a new qube will use the default template and default networking settings


Language
--------

There will always be the need to communicate things to users. In these cases, an interface should aim to make this information easy to understand. The following are simple hints to help achieve this - as with any writing advice, those are guidelines, not laws.

Avoid acronyms
^^^^^^^^^^^^^^

Acronyms are compact and make good names for command line tools, but until the user learns an acronym’s meaning, it is gibberish. Avoid introducing new acronyms, unless necessary, and provide explanations if the acronym is uncommon. Some acronyms are more familiar than the full name - it is strongly recommended to use USB instead of Universal Serial Bus, for example.

Use simple words
^^^^^^^^^^^^^^^^

Use the minimum amount of words needed to be informative. Go with common words that are as widely understood. "Unneeded" is better than "superfluous", "correct" is better than "rectify" and "pointless" is better than "nugatory".

Follow current Qubes OS terminology
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- use **disposable [qube]** instead of ``DVM`` or ``Disposable Virtual Machine``
- use **networking** or **net qube** instead of ``NetVM``
- use **qube** instead of ``virtual machine``, ``container``, ``domain`` or ``domU``
- use terminology consistent with other user-facing tools, not necessarily with internal programming details

Avoid technical words
^^^^^^^^^^^^^^^^^^^^^

Technical words are usually more accurate, but they often *only* make sense to technical users and are confusing and unhelpful to non-technical users. Strive for accuracy and usefulness above strict technical correctness. If at any point you wish to add to a label a "well, actually", resist the temptation.

Prefer a common, understandable concept to detailed technical explanations of a particular implementation
    - Use ``disk space`` instead of ``root.img``, since while not quite accurate, it makes contextual sense
    - Use ``saving`` instead of ``savefile`` as the former is the action trying to be completed
    - Use ``Qubes`` instead of ``qrexec-daemon`` as it gives better context on what is happening

Avoid redundancy
^^^^^^^^^^^^^^^^

- do not over-use words like ``qube`` or ``domain`` in long lists
- it is preferable to create common categories/headers than to repeat a single category multiple times

.. image:: /attachment/doc/ux-badmenu.png
   :alt: Qubes 3.2 system menu with redundant 'domain' prefix to every qube name

System menu in Qubes 3.2 used to make both of those mistakes: redundant 'domain' prefix and no category headers.

Usability and Accessibility
---------------------------

Usability and accessibility are always tied together. When designing interfaces for Qubes OS, follow general good UI practices, striving for understandability, clarity of interactions, avoid surprising the user, avoid - as far as possible - actions that cannot be undone and strive to make it easy to do the correct/secure action and difficult to do the insecure action.

Use the checklist below to verify fundamental accessibility and usability principles:

- **visual readability**
    - there is sufficient contrast between text and background (use `WCAG level AA guidelines <https://www.w3.org/TR/WCAG21/>`__ as minimum when in doubt)
    - UI remains readable in dark mode and in light mode
- **color independence**
    - important information is never communicated solely through color: labels, text, shapes etc. accompany all color-coded information
- **text scaling support**
    - the program works for large font sizes (including what you might consider absurdly large)
- **keyboard/mouse accessibility**
    - all actions can be reached and performed when using only the keyboard and only the mouse without exorbitant leaps of logic or reading the documentation
    - tab-order for controls is logical
- **focus visibility**
    - it is always visible which element has focus, when using keyboard navigation
    - focus is not irrevocably lost on some operations
- **clarity and communication**
    - language used in the GUI is clear, understandable and simple; avoid complex sentences and overly complex vocabulary
    - error messages are specific and visible; if possible, errors are accompanied by information about how to recover from them (ideally, this would be done automatically, but of course this is not always possible)
    - validation is always clearly communicated: the user can easily understand why certain inputs are incorrect
    - error and validation feedback does not rely on timing

Consistency and UI Elements
---------------------------

Concepts, names, icons, interaction patters and styling should be consistent across different tools. When in doubt, pattern the behavior of your application on other Qubes OS tools.

Particular GUI patterns used in Qubes OS are:

Qube names
^^^^^^^^^^

Qube name should be whenever possible accompanied by the appropriate qube icon in the correct color.


Examples:

.. figure:: /attachment/doc/ui_design_qubename_1.png
   :alt: part of Qubes OS Global Config: two dropdowns used to configure Clock qube and Default net qube. In both dropdowns, the qube names are accompanied by the qube icon to their left

   Dropdowns in :guilabel:`Qubes OS Global Config` contain icons. Always use existing dropdown widgets if possible: they generally already provide the icon display.


.. figure:: /attachment/doc/ui_design_qubename_2.png
   :alt: part of Create New Qube Dialog showing selected net qube with its icon to the left of the qube name

   In :guilabel:`Create New Qube` Dialog, selected network qube is displayed with its icon and also with the qube color used to color the qube name, to reinforce the qube-label association.

.. figure:: /attachment/doc/ui_design_qubename_3.png
   :alt: list of running qubes from the domains widget; each qube name has the qube icon to the left of it

   In the domains widgets, every qube is always accompanied by its icon.

Action buttons
^^^^^^^^^^^^^^

If possible, any button should have a brief and understandable description of the action it will cause if pressed written on the button itself. Avoid generic "OK" buttons. Usually only one button should be marked visually as the main "confirmation" button. If there are multiple buttons who could serve this role, individual discernment must be used.


Use flat buttons.

Use the following CSS classes (with appropriate text size and padding) for confirm and cancel buttons:

.. code-block:: css

    .confirm-button {
        background: @blue-500;
        border-radius: 2px;
        color: white;
        font-weight: 600;
    }

    .cancel-button {
        background: @gray-100;
        border-radius: 2px;
        border: 1px solid @gray-200;
        font-weight: 600;
    }

For color definitions, see :ref:`below <developer/general/usability-ux:Colors>`.

Examples:

.. figure:: /attachment/doc/ui_design_buttons_1.png
   :alt: part of Qubes OS Global Config: three buttons at the bottom of the screen. Blue button with text "Apply Changes and Close", and two flat normal buttons with text "Apply Changes" and "Cancel"

   The visually marked button is "Apply Changes and Close", because this is assumed to be the typical interaction with the tool.

.. figure:: /attachment/doc/ui_design_buttons_2.png
   :alt: part of Policy Editor: three buttons at the bottom of the screen. Flat button with text "Quit" and two blue buttons with "Save changes" and "Save and exit"

   Button text should be brief and clear. Two actions seemed to be typical for the interaction with the tool (saving and exiting and saving without exiting), so both are emphasised.


Icons
-----

Core of Qubes OS Icon Set is the set of qube-related icons that can be found in the `qubes-artwork <https://github.com/QubesOS/qubes-artwork/tree/main/icons/scalable/apps>`__ repository.

Those icons represent possible qube classes and colors. For mapping of qube icon to qube type, see the :doc:`/user/reference/glossary`.

Most symbolic icons in Qubes GUI are taken from `lucide.dev <https://lucide.dev>`__ (MIT-licensed open source icon set).

The following stroke width is generally recommended for the following icon sizes (adjusted when needed for clarity and cohesion):

- 16px = 1.5px stroke
- 24px = 2px stroke
- 32px = 3px stroke
- 48px = 4px stroke
- 64px = 6px stroke

If any further icons are needed, base them on `lucide.dev <https://lucide.dev>`__ icon set.


Colors
------

For GUI elements, use the following subset of Tailwind color system (from `Tailwind CSS system <https://www.tailwindcss.com>`__).

.. list-table:: Colors
   :class: tw-color-table
   :header-rows: 1
   :stub-columns: 1
   :widths: 15 10 10 10 10 10 10 10 10 10 10 10

   * - Color
     - 50
     - 100
     - 200
     - 300
     - 400
     - 500
     - 600
     - 700
     - 800
     - 900
     - 950
   * - Gray
     - .. image:: /attachment/doc/colors/f9fafb.png
          :width: 18px
          :height: 12px
          :alt: gray-50

       | gray-50
       | #f9fafb

     - .. image:: /attachment/doc/colors/f3f4f6.png
          :width: 18px
          :height: 12px
          :alt: gray-100

       | gray-100
       | #f3f4f6

     - .. image:: /attachment/doc/colors/e5e7eb.png
          :width: 18px
          :height: 12px
          :alt: gray-200

       | gray-200
       | #e5e7eb

     - .. image:: /attachment/doc/colors/d1d5db.png
          :width: 18px
          :height: 12px
          :alt: gray-300

       | gray-300
       | #d1d5db

     - .. image:: /attachment/doc/colors/9ca3af.png
          :width: 18px
          :height: 12px
          :alt: gray-400

       | gray-400
       | #9ca3af

     - .. image:: /attachment/doc/colors/6b7280.png
          :width: 18px
          :height: 12px
          :alt: gray-500

       | gray-500
       | #6b7280

     - .. image:: /attachment/doc/colors/4b5563.png
          :width: 18px
          :height: 12px
          :alt: gray-600

       | gray-600
       | #4b5563

     - .. image:: /attachment/doc/colors/374151.png
          :width: 18px
          :height: 12px
          :alt: gray-700

       | gray-700
       | #374151

     - .. image:: /attachment/doc/colors/1f2937.png
          :width: 18px
          :height: 12px
          :alt: gray-800

       | gray-800
       | #1f2937

     - .. image:: /attachment/doc/colors/111827.png
          :width: 18px
          :height: 12px
          :alt: gray-900

       | gray-900
       | #111827

     - .. image:: /attachment/doc/colors/030712.png
          :width: 18px
          :height: 12px
          :alt: gray-950

       | gray-950
       | #030712

   * - Neutral
     - .. image:: /attachment/doc/colors/fafafa.png
          :width: 18px
          :height: 12px
          :alt: neutral-50

       | neutral-50
       | #fafafa

     - .. image:: /attachment/doc/colors/f5f5f5.png
          :width: 18px
          :height: 12px
          :alt: neutral-100

       | neutral-100
       | #f5f5f5

     - .. image:: /attachment/doc/colors/e5e5e5.png
          :width: 18px
          :height: 12px
          :alt: neutral-200

       | neutral-200
       | #e5e5e5

     - .. image:: /attachment/doc/colors/d4d4d4.png
          :width: 18px
          :height: 12px
          :alt: neutral-300

       | neutral-300
       | #d4d4d4

     - .. image:: /attachment/doc/colors/a3a3a3.png
          :width: 18px
          :height: 12px
          :alt: neutral-400

       | neutral-400
       | #a3a3a3

     - .. image:: /attachment/doc/colors/737373.png
          :width: 18px
          :height: 12px
          :alt: neutral-500

       | neutral-500
       | #737373

     - .. image:: /attachment/doc/colors/525252.png
          :width: 18px
          :height: 12px
          :alt: neutral-600

       | neutral-600
       | #525252

     - .. image:: /attachment/doc/colors/404040.png
          :width: 18px
          :height: 12px
          :alt: neutral-700

       | neutral-700
       | #404040

     - .. image:: /attachment/doc/colors/262626.png
          :width: 18px
          :height: 12px
          :alt: neutral-800

       | neutral-800
       | #262626

     - .. image:: /attachment/doc/colors/171717.png
          :width: 18px
          :height: 12px
          :alt: neutral-900

       | neutral-900
       | #171717

     - .. image:: /attachment/doc/colors/0a0a0a.png
          :width: 18px
          :height: 12px
          :alt: neutral-950

       | neutral-950
       | #0a0a0a

   * - Red
     - .. image:: /attachment/doc/colors/fef2f2.png
          :width: 18px
          :height: 12px
          :alt: red-50

       | red-50
       | #fef2f2

     - .. image:: /attachment/doc/colors/fee2e2.png
          :width: 18px
          :height: 12px
          :alt: red-100

       | red-100
       | #fee2e2

     - .. image:: /attachment/doc/colors/fecaca.png
          :width: 18px
          :height: 12px
          :alt: red-200

       | red-200
       | #fecaca

     - .. image:: /attachment/doc/colors/fca5a5.png
          :width: 18px
          :height: 12px
          :alt: red-300

       | red-300
       | #fca5a5

     - .. image:: /attachment/doc/colors/f87171.png
          :width: 18px
          :height: 12px
          :alt: red-400

       | red-400
       | #f87171

     - .. image:: /attachment/doc/colors/ef4444.png
          :width: 18px
          :height: 12px
          :alt: red-500

       | red-500
       | #ef4444

     - .. image:: /attachment/doc/colors/dc2626.png
          :width: 18px
          :height: 12px
          :alt: red-600

       | red-600
       | #dc2626

     - .. image:: /attachment/doc/colors/b91c1c.png
          :width: 18px
          :height: 12px
          :alt: red-700

       | red-700
       | #b91c1c

     - .. image:: /attachment/doc/colors/991b1b.png
          :width: 18px
          :height: 12px
          :alt: red-800

       | red-800
       | #991b1b

     - .. image:: /attachment/doc/colors/7f1d1d.png
          :width: 18px
          :height: 12px
          :alt: red-900

       | red-900
       | #7f1d1d

     - .. image:: /attachment/doc/colors/450a0a.png
          :width: 18px
          :height: 12px
          :alt: red-950

       | red-950
       | #450a0a

   * - Orange
     - .. image:: /attachment/doc/colors/fff7ed.png
          :width: 18px
          :height: 12px
          :alt: orange-50

       | orange-50
       | #fff7ed

     - .. image:: /attachment/doc/colors/ffedd5.png
          :width: 18px
          :height: 12px
          :alt: orange-100

       | orange-100
       | #ffedd5

     - .. image:: /attachment/doc/colors/fed7aa.png
          :width: 18px
          :height: 12px
          :alt: orange-200

       | orange-200
       | #fed7aa

     - .. image:: /attachment/doc/colors/fdba74.png
          :width: 18px
          :height: 12px
          :alt: orange-300

       | orange-300
       | #fdba74

     - .. image:: /attachment/doc/colors/fb923c.png
          :width: 18px
          :height: 12px
          :alt: orange-400

       | orange-400
       | #fb923c

     - .. image:: /attachment/doc/colors/f97316.png
          :width: 18px
          :height: 12px
          :alt: orange-500

       | orange-500
       | #f97316

     - .. image:: /attachment/doc/colors/ea580c.png
          :width: 18px
          :height: 12px
          :alt: orange-600

       | orange-600
       | #ea580c

     - .. image:: /attachment/doc/colors/c2410c.png
          :width: 18px
          :height: 12px
          :alt: orange-700

       | orange-700
       | #c2410c

     - .. image:: /attachment/doc/colors/9a3412.png
          :width: 18px
          :height: 12px
          :alt: orange-800

       | orange-800
       | #9a3412

     - .. image:: /attachment/doc/colors/7c2d12.png
          :width: 18px
          :height: 12px
          :alt: orange-900

       | orange-900
       | #7c2d12

     - .. image:: /attachment/doc/colors/431407.png
          :width: 18px
          :height: 12px
          :alt: orange-950

       | orange-950
       | #431407

   * - Yellow
     - .. image:: /attachment/doc/colors/fefce8.png
          :width: 18px
          :height: 12px
          :alt: yellow-50

       | yellow-50
       | #fefce8

     - .. image:: /attachment/doc/colors/fef9c3.png
          :width: 18px
          :height: 12px
          :alt: yellow-100

       | yellow-100
       | #fef9c3

     - .. image:: /attachment/doc/colors/fef08a.png
          :width: 18px
          :height: 12px
          :alt: yellow-200

       | yellow-200
       | #fef08a

     - .. image:: /attachment/doc/colors/fde047.png
          :width: 18px
          :height: 12px
          :alt: yellow-300

       | yellow-300
       | #fde047

     - .. image:: /attachment/doc/colors/facc15.png
          :width: 18px
          :height: 12px
          :alt: yellow-400

       | yellow-400
       | #facc15

     - .. image:: /attachment/doc/colors/eab308.png
          :width: 18px
          :height: 12px
          :alt: yellow-500

       | yellow-500
       | #eab308

     - .. image:: /attachment/doc/colors/ca8a04.png
          :width: 18px
          :height: 12px
          :alt: yellow-600

       | yellow-600
       | #ca8a04

     - .. image:: /attachment/doc/colors/a16207.png
          :width: 18px
          :height: 12px
          :alt: yellow-700

       | yellow-700
       | #a16207

     - .. image:: /attachment/doc/colors/854d0e.png
          :width: 18px
          :height: 12px
          :alt: yellow-800

       | yellow-800
       | #854d0e

     - .. image:: /attachment/doc/colors/713f12.png
          :width: 18px
          :height: 12px
          :alt: yellow-900

       | yellow-900
       | #713f12

     - .. image:: /attachment/doc/colors/422006.png
          :width: 18px
          :height: 12px
          :alt: yellow-950

       | yellow-950
       | #422006

   * - Green
     - .. image:: /attachment/doc/colors/f0fdf4.png
          :width: 18px
          :height: 12px
          :alt: green-50

       | green-50
       | #f0fdf4

     - .. image:: /attachment/doc/colors/dcfce7.png
          :width: 18px
          :height: 12px
          :alt: green-100

       | green-100
       | #dcfce7

     - .. image:: /attachment/doc/colors/bbf7d0.png
          :width: 18px
          :height: 12px
          :alt: green-200

       | green-200
       | #bbf7d0

     - .. image:: /attachment/doc/colors/86efac.png
          :width: 18px
          :height: 12px
          :alt: green-300

       | green-300
       | #86efac

     - .. image:: /attachment/doc/colors/4ade80.png
          :width: 18px
          :height: 12px
          :alt: green-400

       | green-400
       | #4ade80

     - .. image:: /attachment/doc/colors/22c55e.png
          :width: 18px
          :height: 12px
          :alt: green-500

       | green-500
       | #22c55e

     - .. image:: /attachment/doc/colors/16a34a.png
          :width: 18px
          :height: 12px
          :alt: green-600

       | green-600
       | #16a34a

     - .. image:: /attachment/doc/colors/15803d.png
          :width: 18px
          :height: 12px
          :alt: green-700

       | green-700
       | #15803d

     - .. image:: /attachment/doc/colors/166534.png
          :width: 18px
          :height: 12px
          :alt: green-800

       | green-800
       | #166534

     - .. image:: /attachment/doc/colors/14532d.png
          :width: 18px
          :height: 12px
          :alt: green-900

       | green-900
       | #14532d

     - .. image:: /attachment/doc/colors/052e16.png
          :width: 18px
          :height: 12px
          :alt: green-950

       | green-950
       | #052e16

   * - Blue
     - .. image:: /attachment/doc/colors/eff6ff.png
          :width: 18px
          :height: 12px
          :alt: blue-50

       | blue-50
       | #eff6ff

     - .. image:: /attachment/doc/colors/dbeafe.png
          :width: 18px
          :height: 12px
          :alt: blue-100

       | blue-100
       | #dbeafe

     - .. image:: /attachment/doc/colors/bfdbfe.png
          :width: 18px
          :height: 12px
          :alt: blue-200

       | blue-200
       | #bfdbfe

     - .. image:: /attachment/doc/colors/93c5fd.png
          :width: 18px
          :height: 12px
          :alt: blue-300

       | blue-300
       | #93c5fd

     - .. image:: /attachment/doc/colors/60a5fa.png
          :width: 18px
          :height: 12px
          :alt: blue-400

       | blue-400
       | #60a5fa

     - .. image:: /attachment/doc/colors/3b82f6.png
          :width: 18px
          :height: 12px
          :alt: blue-500

       | blue-500
       | #3b82f6

     - .. image:: /attachment/doc/colors/2563eb.png
          :width: 18px
          :height: 12px
          :alt: blue-600

       | blue-600
       | #2563eb

     - .. image:: /attachment/doc/colors/1d4ed8.png
          :width: 18px
          :height: 12px
          :alt: blue-700

       | blue-700
       | #1d4ed8

     - .. image:: /attachment/doc/colors/1e40af.png
          :width: 18px
          :height: 12px
          :alt: blue-800

       | blue-800
       | #1e40af

     - .. image:: /attachment/doc/colors/1e3a8a.png
          :width: 18px
          :height: 12px
          :alt: blue-900

       | blue-900
       | #1e3a8a

     - .. image:: /attachment/doc/colors/172554.png
          :width: 18px
          :height: 12px
          :alt: blue-950

       | blue-950
       | #172554

   * - Purple
     - .. image:: /attachment/doc/colors/faf5ff.png
          :width: 18px
          :height: 12px
          :alt: purple-50

       | purple-50
       | #faf5ff

     - .. image:: /attachment/doc/colors/f3e8ff.png
          :width: 18px
          :height: 12px
          :alt: purple-100

       | purple-100
       | #f3e8ff

     - .. image:: /attachment/doc/colors/e9d5ff.png
          :width: 18px
          :height: 12px
          :alt: purple-200

       | purple-200
       | #e9d5ff

     - .. image:: /attachment/doc/colors/d8b4fe.png
          :width: 18px
          :height: 12px
          :alt: purple-300

       | purple-300
       | #d8b4fe

     - .. image:: /attachment/doc/colors/c084fc.png
          :width: 18px
          :height: 12px
          :alt: purple-400

       | purple-400
       | #c084fc

     - .. image:: /attachment/doc/colors/a855f7.png
          :width: 18px
          :height: 12px
          :alt: purple-500

       | purple-500
       | #a855f7

     - .. image:: /attachment/doc/colors/9333ea.png
          :width: 18px
          :height: 12px
          :alt: purple-600

       | purple-600
       | #9333ea

     - .. image:: /attachment/doc/colors/7e22ce.png
          :width: 18px
          :height: 12px
          :alt: purple-700

       | purple-700
       | #7e22ce

     - .. image:: /attachment/doc/colors/6b21a8.png
          :width: 18px
          :height: 12px
          :alt: purple-800

       | purple-800
       | #6b21a8

     - .. image:: /attachment/doc/colors/581c87.png
          :width: 18px
          :height: 12px
          :alt: purple-900

       | purple-900
       | #581c87

     - .. image:: /attachment/doc/colors/3b0764.png
          :width: 18px
          :height: 12px
          :alt: purple-950

       | purple-950
       | #3b0764

Desktop Environments
--------------------

The desktop GUIs that QubesOS supports out of the box are `KDE <https://kde.org>`__ and `Xfce <https://xfce.org>`__. All GUI tools should function well under both of those desktop environments. There is also a significant minority of users who use tiling desktop environments. Ideally, GUI tools should also function in those desktop environments.

Both of those desktop environments have their own `human interface guidelines <https://en.wikipedia.org/wiki/Human_interface_guidelines>`__, and we suggest you familiarize yourself with the platform you developing for.

- `KDE HIG <https://hig.kde.org/>`__

- `Xfce UI Guidlines <https://wiki.xfce.org/dev/hig/general>`__

Further Learning & Inspiration
------------------------------

Learning to make well designing intuitive interfaces and software is specialized skillset that can take years to cultivate, but if you are interested in furthering your understanding, we suggest the following resources:

- `Learn Design Principles <https://web.archive.org/web/20180101172357/http://learndesignprinciples.com/>`__ by Melissa Mandelbaum

- `Usability in Free Software <https://jancborchardt.net/usability-in-free-software>`__ by Jan C. Borchardt

- `Superheroes & Villains in Design <https://vimeo.com/70030549>`__ by Aral Balkan

- `First Rule of Usability? Don’t Listen to Users <https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/>`__ by Jakob Nielsen

- `10 Usability Heuristics for User Interface Design <https://www.nngroup.com/articles/ten-usability-heuristics/>`__ by Jakob Nielsen

- `Hack Design <https://hackdesign.org/>`__ - online learning program
