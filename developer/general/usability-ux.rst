=========================
Usability & UX Guidelines
=========================

Unnecesary complexity and cumbersome UI often causes good software to remain unused. To avoid this grisly fate, please always take usability and good user experience into account when contributing to Qubes OS.

Especially if you plan to contribute to GUI tools, please read those guidelines. Additional information can also be found in our `visual style guide <https://www.qubes-os.org/doc/visual-style-guide/>`__.

Ease of Use
-----------

In open source software, a good user interface should not only enable users to achieve their goals, but also allow them to remain in control of the process. The UI should neither overwhelm the users with the amount of information presented nor hide important context from them. In the words falsely attributed to Albert Einstein: our goal is to make things as simple as possible, but not simpler.

Make sure that the UI you design adheres to the following principles:

- **do not waste user's time**
    - the program should not *require* extensive configuration
    - the most typical and most recommended workflows should require the least user time and attention
    - the defaults should be sensible
    - minimize repetitiveness: if possible, avoid multiple clicks or multiple steps for operations that can be implemented with less clicks/steps

- **resilience to errors**
    - users should not be able to break the program (or the entire system) or enter an unrecoverable state
    - users should not be able to compromise the integrity and security of their system accidentally
    - as far as possible, there should be a possibility to undo actions
    - the defaults should be secure
    - avoid leaving users stranded - if there is an error message, there should also be guidance on how to recover or (preferably) an actionable solution

- **reduce cognitive load**
    - show only the relevant information
    - use simple and understandable language
    - make it easy to discover and understand features and available options
    - do not expect the user to remember: remind them of past actions and choices
    - the defaults should make sense for most use cases


Language
--------

There will always be the need to communicate things to users. In these cases, an interface should aim to make this information easy to understand. The following are simple hints to help achieve this - as with any writing advice, those are guidelines, not laws.

- **avoid acronyms**
    - acronyms are compact and make good names for command line tools, but until the user learns an acronym’s meaning, it is gibberish. Avoid introducing new acronyms, unless necessary, and provide explanations if the acronym is uncommon. Some acronyms are more familiar than the full name - it is strongly recommended to use USB instead of Universal Serial Bus, for example.
- **use simple words**
    - use the minimum amount of words needed to be informative. Go with common words that are as widely understood. "Unneeded" is better than "superfluous", "correct" is better than "rectify" and "pointless" is better than "nugatory".
- **follow current Qubes OS terminology**
    - use **disposable [qube]** instead of ``DVM`` or ``Disposable Virtual Machine``
    - use **networking** or **net qube** instead of ``NetVM``
    - use **qube** instead of ``virtual machine`` or ``container``
    - use terminology consistent with other user-facing tools, not necessarily with internal programming details
- **avoid technical words**
    - technical words are usually more accurate, but they often *only* make sense to technical users and are confusing and unhelpful to non-technical users. Strive for accuracy and usefulness above strict technical correctness. If at any point you wish to add to a label a "well, actually", resist the temptation.
- **use simple concepts**
    - prefer a common, understandable concept to detailed technical explanations of a particular implementation
        - Use ``disk space`` instead of ``root.img``, since while not quite accurate, it makes contextual sense
        - Use ``saving`` instead of ``savefile`` as the former is the action trying to be completed
        - Use ``Qubes`` instead of ``qrexec-daemon`` as it gives better context on what is happening
- **avoid redundancy**
    - do not over-use words like ``qube`` or ``domain`` in long lists
    - it is preferable to create common categories/headers than to repeat a single category multiple times

Usability and Accessibility
---------------------------

Usability and accessibility are always tied together. When designing interfaces for Qubes OS, follow general good UI practices, striving for understandability, clarity of interactions, avoid surprising the user, avoid - as far as possible - actions that cannot be undone and strive to make it easy to do the correct/secure action and difficult to do the insecure action.

Certain security considerations make it difficult to make Qubes OS fully accessible to tools such as screen readers (as a screen reader by design violates many security boundaries Qubes OS establishes). However, let the perfect not be the enemy of the good and let us strive for accessibility to a degree that is possible.

Use the checklist below to verify fundamental accessibility and usability principles:

- **visual readability**
    - there is sufficient contrast between text and background
    - UI remains readable in dark mode and in light mode
- **color independence**
    - important information is never communicated solely through color: labels, text, shapes etc. accompany all color-coded information
- **text scaling support**
    - the program works for large font sizes (including what you might consider absurdly large)
- **keyboard/mouse accessibility**
    - all actions can be reached and performed when using only the keyboard and only the mouse without exorbitant leaps of logic or reading the documentation
    - Tab-order for controls is logical
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

   Dropdowns in Qubes OS Global Config contain icons. Always use existing dropdown widgets if possible: they generally already provide the icon display.


.. figure:: /attachment/doc/ui_design_qubename_2.png
   :alt: part of Create New Qube Dialog showing selected net qube with its icon to the left of the qube name

   In Create New Qube Dialog, selected network qube is displayed with its icon and also with the qube color used to color the qube name, to reinforce the qube-label association.

.. figure:: /attachment/doc/ui_design_qubename_3.png
   :alt: list of running qubes from the domains widget; each qube name has the qube icon to the left of it

   In the domains widgets, every qube is always accompanied by its icon.

Action buttons
^^^^^^^^^^^^^^

If possible, any button should have a brief and understandable description of the action it will cause if pressed written on the button itself. Avoid generic "OK" buttons.

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

For color definitions, see below.

Examples:

.. figure:: /attachment/doc/ui_design_buttons_1.png
   :alt: part of Qubes OS Global Config: three buttons at the bottom of the screen. Blue button with text "Apply Changes and Close", and two flat normal buttons with text "Apply Changes" and "Cancel"

   Usually only one button should be marked visually as the main "confirmation" button. If there are multiple buttons who could serve this role, individual discernment must be used.

.. figure:: /attachment/doc/ui_design_buttons_2.png
   :alt: part of Policy Editor: three buttons at the bottom of the screen. Flat button with text "Quit" and two blue buttons with "Save changes" and "Save and exit"

   Button text should be brief and clear.


Icons
-----

Core of Qubes OS Icon Set is the set of qube-related icons that can be found in the qubes-artwork repository (https://github.com/QubesOS/qubes-artwork/tree/main/icons/scalable/apps ).

Those icons represent possible qube classes and colors. For mapping of qube icon to qube type, see the :doc:`/user/reference/glossary`.

Most symbolic icons in Qubes GUI are taken from lucide.dev (MIT-licensed open source icon set).

The following stroke width is generally recommended for the following icon sizes (adjusted when needed for clarity and cohesion):

- 16px = 1.5px stroke
- 24px = 2px stroke
- 32px = 3px stroke
- 48px = 4px stroke
- 64px = 6px stroke

If any further icons are needed, base them on lucide.dev icon set.


Colors
------

For GUI elements, use Tailwind color system (from `Tailwind CSS system <https://www.tailwindcss.com>`__). In particular, you can refer to the colors below for a comprehensive set of readable colors.

.. raw:: html

   <style>
     .tw-color-table {
       border-collapse: collapse;
       font-size: 0.8em;
     }
     .tw-color-table th {
       padding: 6px 10px;
       text-align: center;
       border: 1px solid #a3a3a3;
     }
     .tw-color-table td {
       border: 1px solid #a3a3a3;
       padding: 6px 8px;
       text-align: center;
       vertical-align: top;
     }
     .tw-color-table td.color-name {
       text-align: left;
       font-weight: bold;
       vertical-align: middle;
     }
     .color-cell {
       display: flex;
       flex-direction: column;
       align-items: center;
       gap: 4px;
     }
     .color-swatch {
       display: block;
       width: 48px;
       height: 32px;
       border-radius: 4px;
       border: 1px solid rgba(0,0,0,0.1);
     }
     .color-label {
       font-size: 0.8em;
       line-height: 1.3;
     }
     .color-hex {
       font-size: 0.8em;
     }
   </style>

   <table class="tw-color-table">
     <thead>
       <tr>
         <th>Color</th>
         <th>50</th><th>100</th><th>200</th><th>300</th><th>400</th>
         <th>500</th><th>600</th><th>700</th><th>800</th><th>900</th><th>950</th>
       </tr>
     </thead>
     <tbody>

       <tr>
         <td class="color-name">Gray</td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#f9fafb"></span><span class="color-label">gray-50</span><span class="color-hex">#f9fafb</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#f3f4f6"></span><span class="color-label">gray-100</span><span class="color-hex">#f3f4f6</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#e5e7eb"></span><span class="color-label">gray-200</span><span class="color-hex">#e5e7eb</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#d1d5db"></span><span class="color-label">gray-300</span><span class="color-hex">#d1d5db</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#9ca3af"></span><span class="color-label">gray-400</span><span class="color-hex">#9ca3af</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#6b7280"></span><span class="color-label">gray-500</span><span class="color-hex">#6b7280</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#4b5563"></span><span class="color-label">gray-600</span><span class="color-hex">#4b5563</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#374151"></span><span class="color-label">gray-700</span><span class="color-hex">#374151</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#1f2937"></span><span class="color-label">gray-800</span><span class="color-hex">#1f2937</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#111827"></span><span class="color-label">gray-900</span><span class="color-hex">#111827</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#030712"></span><span class="color-label">gray-950</span><span class="color-hex">#030712</span></div></td>
       </tr>

       <tr>
         <td class="color-name">Neutral</td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fafafa"></span><span class="color-label">neutral-50</span><span class="color-hex">#fafafa</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#f5f5f5"></span><span class="color-label">neutral-100</span><span class="color-hex">#f5f5f5</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#e5e5e5"></span><span class="color-label">neutral-200</span><span class="color-hex">#e5e5e5</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#d4d4d4"></span><span class="color-label">neutral-300</span><span class="color-hex">#d4d4d4</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#a3a3a3"></span><span class="color-label">neutral-400</span><span class="color-hex">#a3a3a3</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#737373"></span><span class="color-label">neutral-500</span><span class="color-hex">#737373</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#525252"></span><span class="color-label">neutral-600</span><span class="color-hex">#525252</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#404040"></span><span class="color-label">neutral-700</span><span class="color-hex">#404040</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#262626"></span><span class="color-label">neutral-800</span><span class="color-hex">#262626</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#171717"></span><span class="color-label">neutral-900</span><span class="color-hex">#171717</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#0a0a0a"></span><span class="color-label">neutral-950</span><span class="color-hex">#0a0a0a</span></div></td>
       </tr>

       <tr>
         <td class="color-name">Red</td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fef2f2"></span><span class="color-label">red-50</span><span class="color-hex">#fef2f2</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fee2e2"></span><span class="color-label">red-100</span><span class="color-hex">#fee2e2</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fecaca"></span><span class="color-label">red-200</span><span class="color-hex">#fecaca</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fca5a5"></span><span class="color-label">red-300</span><span class="color-hex">#fca5a5</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#f87171"></span><span class="color-label">red-400</span><span class="color-hex">#f87171</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#ef4444"></span><span class="color-label">red-500</span><span class="color-hex">#ef4444</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#dc2626"></span><span class="color-label">red-600</span><span class="color-hex">#dc2626</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#b91c1c"></span><span class="color-label">red-700</span><span class="color-hex">#b91c1c</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#991b1b"></span><span class="color-label">red-800</span><span class="color-hex">#991b1b</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#7f1d1d"></span><span class="color-label">red-900</span><span class="color-hex">#7f1d1d</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#450a0a"></span><span class="color-label">red-950</span><span class="color-hex">#450a0a</span></div></td>
       </tr>

       <tr>
         <td class="color-name">Orange</td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fff7ed"></span><span class="color-label">orange-50</span><span class="color-hex">#fff7ed</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#ffedd5"></span><span class="color-label">orange-100</span><span class="color-hex">#ffedd5</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fed7aa"></span><span class="color-label">orange-200</span><span class="color-hex">#fed7aa</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fdba74"></span><span class="color-label">orange-300</span><span class="color-hex">#fdba74</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fb923c"></span><span class="color-label">orange-400</span><span class="color-hex">#fb923c</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#f97316"></span><span class="color-label">orange-500</span><span class="color-hex">#f97316</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#ea580c"></span><span class="color-label">orange-600</span><span class="color-hex">#ea580c</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#c2410c"></span><span class="color-label">orange-700</span><span class="color-hex">#c2410c</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#9a3412"></span><span class="color-label">orange-800</span><span class="color-hex">#9a3412</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#7c2d12"></span><span class="color-label">orange-900</span><span class="color-hex">#7c2d12</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#431407"></span><span class="color-label">orange-950</span><span class="color-hex">#431407</span></div></td>
       </tr>

       <tr>
         <td class="color-name">Yellow</td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fefce8"></span><span class="color-label">yellow-50</span><span class="color-hex">#fefce8</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fef9c3"></span><span class="color-label">yellow-100</span><span class="color-hex">#fef9c3</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fef08a"></span><span class="color-label">yellow-200</span><span class="color-hex">#fef08a</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#fde047"></span><span class="color-label">yellow-300</span><span class="color-hex">#fde047</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#facc15"></span><span class="color-label">yellow-400</span><span class="color-hex">#facc15</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#eab308"></span><span class="color-label">yellow-500</span><span class="color-hex">#eab308</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#ca8a04"></span><span class="color-label">yellow-600</span><span class="color-hex">#ca8a04</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#a16207"></span><span class="color-label">yellow-700</span><span class="color-hex">#a16207</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#854d0e"></span><span class="color-label">yellow-800</span><span class="color-hex">#854d0e</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#713f12"></span><span class="color-label">yellow-900</span><span class="color-hex">#713f12</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#422006"></span><span class="color-label">yellow-950</span><span class="color-hex">#422006</span></div></td>
       </tr>

       <tr>
         <td class="color-name">Green</td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#f0fdf4"></span><span class="color-label">green-50</span><span class="color-hex">#f0fdf4</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#dcfce7"></span><span class="color-label">green-100</span><span class="color-hex">#dcfce7</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#bbf7d0"></span><span class="color-label">green-200</span><span class="color-hex">#bbf7d0</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#86efac"></span><span class="color-label">green-300</span><span class="color-hex">#86efac</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#4ade80"></span><span class="color-label">green-400</span><span class="color-hex">#4ade80</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#22c55e"></span><span class="color-label">green-500</span><span class="color-hex">#22c55e</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#16a34a"></span><span class="color-label">green-600</span><span class="color-hex">#16a34a</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#15803d"></span><span class="color-label">green-700</span><span class="color-hex">#15803d</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#166534"></span><span class="color-label">green-800</span><span class="color-hex">#166534</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#14532d"></span><span class="color-label">green-900</span><span class="color-hex">#14532d</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#052e16"></span><span class="color-label">green-950</span><span class="color-hex">#052e16</span></div></td>
       </tr>

       <tr>
         <td class="color-name">Blue</td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#eff6ff"></span><span class="color-label">blue-50</span><span class="color-hex">#eff6ff</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#dbeafe"></span><span class="color-label">blue-100</span><span class="color-hex">#dbeafe</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#bfdbfe"></span><span class="color-label">blue-200</span><span class="color-hex">#bfdbfe</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#93c5fd"></span><span class="color-label">blue-300</span><span class="color-hex">#93c5fd</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#60a5fa"></span><span class="color-label">blue-400</span><span class="color-hex">#60a5fa</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#3b82f6"></span><span class="color-label">blue-500</span><span class="color-hex">#3b82f6</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#2563eb"></span><span class="color-label">blue-600</span><span class="color-hex">#2563eb</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#1d4ed8"></span><span class="color-label">blue-700</span><span class="color-hex">#1d4ed8</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#1e40af"></span><span class="color-label">blue-800</span><span class="color-hex">#1e40af</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#1e3a8a"></span><span class="color-label">blue-900</span><span class="color-hex">#1e3a8a</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#172554"></span><span class="color-label">blue-950</span><span class="color-hex">#172554</span></div></td>
       </tr>

       <tr>
         <td class="color-name">Purple</td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#faf5ff"></span><span class="color-label">purple-50</span><span class="color-hex">#faf5ff</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#f3e8ff"></span><span class="color-label">purple-100</span><span class="color-hex">#f3e8ff</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#e9d5ff"></span><span class="color-label">purple-200</span><span class="color-hex">#e9d5ff</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#d8b4fe"></span><span class="color-label">purple-300</span><span class="color-hex">#d8b4fe</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#c084fc"></span><span class="color-label">purple-400</span><span class="color-hex">#c084fc</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#a855f7"></span><span class="color-label">purple-500</span><span class="color-hex">#a855f7</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#9333ea"></span><span class="color-label">purple-600</span><span class="color-hex">#9333ea</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#7e22ce"></span><span class="color-label">purple-700</span><span class="color-hex">#7e22ce</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#6b21a8"></span><span class="color-label">purple-800</span><span class="color-hex">#6b21a8</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#581c87"></span><span class="color-label">purple-900</span><span class="color-hex">#581c87</span></div></td>
         <td><div class="color-cell"><span class="color-swatch" style="background:#3b0764"></span><span class="color-label">purple-950</span><span class="color-hex">#3b0764</span></div></td>
       </tr>

     </tbody>
   </table>

Desktop Environments
--------------------

The desktop GUIs that QubesOS supports out of the box are `KDE <https://kde.org>`__ and `Xfce <https://xfce.org>`__. All GUI tools should function well under both of those desktop environments. There is also a significant minority of users who use tiling DE, such as i3. Ideally, GUI tools should also function in those desktop environments.

All three of these mentioned desktop environments have their own `human interface guidelines <https://en.wikipedia.org/wiki/Human_interface_guidelines>`__, and we suggest you familiarize yourself with the platform you developing for.

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
