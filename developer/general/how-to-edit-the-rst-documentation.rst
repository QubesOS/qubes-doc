=============================
How to edit the documentation
=============================

The Qubes OS documentation is stored as `reStructuredText (rST) <https://docutils.sourceforge.io/rst.html>`__ files in the `qubes-doc <https://github.com/QubesOS/qubes-doc>`__ repository.

We use `Sphinx <https://www.sphinx-doc.org/>`__ for building and `Read The Docs (RTD) <https://readthedocs.com/>`__ for hosting. RTD is a `continuous‑documentation deployment platform <https://docs.readthedocs.com/platform/stable/continuous-deployment.html>`__ that can automatically detect changes in a GitHub repository and build the latest version of a documentation.

.. figure:: /attachment/doc/rst-rtd-workflow.png
    :alt: Qubes OS Documentation Workflow - once new documentation is written or changed, it is built and verified with Sphinx, pushed on GitHub/GitLab and hosted on RTD
    :scale: 15 %
    :align: center

By cloning and regularly pulling from `qubes-doc <https://github.com/QubesOS/qubes-doc>`__ repository, users can maintain their own up-to-date offline copy of the Qubes documentation rather than relying solely on the web and either serve it locally or read the rST files directly. EPUB or PDF versions of Qubes OS documentation can also be downloaded from `doc.qubes-os.org <https://doc.qubes-os.org/en/latest/>`__:

.. figure:: /attachment/doc/rst-rtd-epub-pdf.png
   :alt: Highlights from where one can download a ePUB or PDF of hte Qubes OS documentation deployed on RTD
   :scale: 20 %
   :align: center

The documentation is a volunteer community effort. People like you are constantly working to make it better. If you notice something that can be fixed or improved, please follow the steps below to open a pull request!

How to submit a pull request
============================

We keep all the rST documentation in `qubes-doc <https://github.com/QubesOS/qubes-doc>`__, a dedicated Git repository hosted on `GitHub <https://github.com/>`__. Thanks to GitHub’s easy web interface, you can edit the documentation even if you’re not familiar with Git or the command line! All you need is a free GitHub account.

A few notes before we get started:

-  Since Qubes is a security-oriented project, every documentation change will be :ref:`reviewed <developer/general/how-to-edit-the-rst-documentation:security>` before it’s accepted. This allows us to maintain quality control and protect our users.

-  To give your contribution a better chance of being accepted, please follow our :doc:`/developer/general/rst-documentation-style-guide`.

-  We don’t want you to spend time and effort on a contribution that we can’t accept. If your contribution would take a lot of time, please :doc:`file an issue </introduction/issue-tracking>` for it first so that we can make sure we’re on the same page before significant works begins.

-  Alternatively, you may already have written content that doesn’t conform to these guidelines, but you’d be willing to modify it so that it does. In this case, you can still submit it by following the instructions below. Just make a note in your pull request (PR) that you’re aware of the changes that need to be made and that you’re just asking for the content to be reviewed before you spend time making those changes.

-  Finally, if you’ve written something that doesn’t belong in qubes-doc but that would be beneficial to the Qubes community, please consider adding it to the :ref:`external documentation <developer/general/rst-documentation-style-guide:core vs. external documentation>`.

(**Advanced users:** If you’re already familiar with GitHub or wish to
work from the command line, you can skip the rest of this section. All you need to do to contribute is to `fork and clone <https://guides.github.com/activities/forking/>`__ the `qubes-doc <https://github.com/QubesOS/qubes-doc>`__ repo, make your changes, then `submit a pull request <https://help.github.com/articles/using-pull-requests/>`__. You can continue reading :ref:`viewing_pr`.)

Ok, let’s begin. Every documentation page has a :guilabel:`Edit on GitHub` link.

|page-source-button|

When you click on it, you’ll be taken to the source file — a reStructuredText (``.rst``) file — on GitHub.

On this page, there will be a button to edit the file (if you are already logged in).

|github-edit|

If you are not logged in you can click on :guilabel:`Sign In` and you’ll be prompted to sign in with your GitHub username and password. You can also create a free account from here.

|github-sign-in|

If this is your first contribution to the documentation, you need to fork the repository (make your own copy).

|fork1|

It’s easy — just click the green :guilabel:`Create fork` button on the next page. This step is only needed the first time you make a contribution.

|fork2|

Now you can make your modifications.

|fork3|

.. You can also preview the changes by clicking the :guilabel:`Preview changes` tab.

|edit|

If you want to add images, read :ref:`how_to_add_images` and refer to :ref:`build_locally` if you want to locally verify that everything looks correct before submitting any changes.

Once you’re finished, describe your changes at the bottom and click :guilabel:`Commit changes`.

|commit|

After that, you’ll see exactly what modifications you’ve made. At this stage, those changes are still in your own copy (fork) of the documentation. If everything looks good, send those changes to us by pressing the :guilabel:`Create pull request` button.

You will be able to adjust the pull request message and title there. In most cases, the defaults are ok, so you can just confirm by pressing the :guilabel:`Create pull request` button again. However, if you’re not ready for your PR to be reviewed or merged yet, please `make a draft PR instead <https://github.blog/news-insights/product-news/introducing-draft-pull-requests/>`__.

|pull-request-confirm|

If any of your changes should be reflected in the :doc:`documentation index (a.k.a. table of contents) </index>` — for example, if you’re adding a new page, changing the title of an existing page, or removing a page — please see :ref:`edit_doc_index`.

That’s all! We will review your changes. If everything looks good, we’ll pull them into the official documentation. Otherwise, we may have some questions for you, which we’ll post in a comment on your pull request. (GitHub will automatically notify you if we do.) If, for some reason, we can’t accept your pull request, we’ll post a comment explaining why we can’t.

.. _viewing_pr:

Viewing your pull request on RTD
--------------------------------

Every time you push a commit to your pull request, a build on RTD will be triggered. To view your PR you can go to Qubes OS builds on `RTD <https://app.readthedocs.org/projects/qubes-doc/builds/>`__, find the last build of your PR and click on it:

|pull-request-builds|

There you can view the rendered docs or inspect the logs for errors:

|pull-request-build|

You can also just head straight to the following url: ``https://qubes-doc--<PR-NUMBER>.org.readthedocs.build/en/<PR-NUMBER>/``.

Tips & Tricks
-------------

- Pull upstream changes into your fork regularly. Diverging too far from main can be cumbersome to update at a later stage.
- To pull in upstream changes:

  .. code:: console

   $ git remote add upstream https://github.com/QubesOS/qubes-doc.git
   $ git fetch upstream

- Check the log and the current changes, before merging:

  .. code:: console

   $ git log upstream/main

- Then merge the changes that you fetched:

  .. code:: console

   $ git merge upstream/main

Keep your pull requests limited to a single issue, pull requests should be as atomic as possible.

.. _edit_doc_index:

TL;DR: How to edit the documentation index
==========================================

For a more comprehensive guide to the rST syntax and pitfalls please refer to the :doc:`/developer/general/rst-documentation-style-guide`.

The source file for the :doc:`documentation index (a.k.a. table of contents) </index>` is `index.rst <https://github.com/QubesOS/qubes-doc/blob/main/index.rst>`__.

:file:`index.rst` contains information about the hierarchy between the files in the documentation and/or
the connection between them. `toctree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`__ is the rST directive which defines the table of contents.

If you want to add a newly created documentation file, do so as follows:

.. code-block:: rst

   .. toctree:
      /path/to/old_doc_file_name
      /path/to/new_doc_file_name

Editing this file will change what appears on the documentation index.

Please always be mindful that rST syntax is sensitive to indentation (3 spaces)!

.. _how_to_add_images:

TL;DR: How to add images
========================

For a more comprehensive guide to the rST syntax and pitfalls please refer to the :doc:`/developer/general/rst-documentation-style-guide`.

Images reside inside the `qubes-doc repository <https://github.com/QubesOS/qubes-doc/>`__ in the directory `attachment/doc <https://github.com/QubesOS/qubes-doc/tree/main/attachment/doc>`__.

To add an image to a page, use the following syntax:

.. code-block:: rst

   .. figure:: /attachment/doc/r4.0-snapshot12.png
     :alt: Qubes desktop screenshot depicting <description>

If you want to add a caption to the image, you may do so using the optional ``caption`` of the `figure directive <https://docutils.sourceforge.io/docs/ref/rst/directives.html#figure>`__. Another way without a caption is to use the `image directive <https://docutils.sourceforge.io/docs/ref/rst/directives.html#image>`__.

Then, add your image(s) in a the :file:`attachment/doc` folder in the `qubes-doc <https://github.com/QubesOS/qubes-doc>`__ repository using the same path and filename. This is the only permitted way to include images. Do not link to images on other websites.

.. _cross_referencing:

TL;DR: Cross-referencing
========================

For a more comprehensive guide to the rST syntax and pitfalls please refer to the :doc:`/developer/general/rst-documentation-style-guide`.

When referencing to an existing rST file use the ``:doc:`` `role <https://www.sphinx-doc.org/en/master/usage/referencing.html#role-doc>`__ as in

.. code-block:: rst

  how to :doc:`contribute code </introduction/contributing>` do [...]

When referencing to a section in an existing rST file use the ``:ref:`` `role <https://www.sphinx-doc.org/en/master/usage/referencing.html#role-ref>`__ as in

.. code-block:: rst

  See the :ref:`USB Troubleshooting guide <user/troubleshooting/usb-troubleshooting:usb vm does not boot after creating and assigning usb controllers to it>` for [...]

Use the path to the file starting from the root of qubes-doc repository, without any leading slash ``/`` and without the ``.rst`` file ending. The section name is usually taken as is in small caps.

Some special cases are as follows (here the emphasis is on the ``"`` in the sections's title:

.. code-block:: rst

   the :ref:`VM Troubleshooting <user/troubleshooting/vm-troubleshooting:"no match found" when trying to install a template>`.

which will point to :ref:`this section <user/troubleshooting/vm-troubleshooting:"no match found" when trying to install a template>`.

.. code:: rst

   we :ref:`distrust the infrastructure <introduction/faq:what does it mean to "distrust the infrastructure"?>`

which will refer to :ref:`this section <introduction/faq:what does it mean to "distrust the infrastructure"?>`.

For further options and use cases please refer to `Cross-references <https://www.sphinx-doc.org/en/master/usage/referencing.html>`__.

Qubes OS rST configuration
==========================

:file:`qubes-doc` directory contains a build configuration file named :file:`conf.py`, used by Sphinx
to define `input and output behaviour <https://www.sphinx-doc.org/en/master/usage/configuration.html>`__. It contains settings and extensions that define how the documentation will be generated. You can find it `here <https://github.com/QubesOS/qubes-doc/blob/main/conf.py>`__.

You can also find a :file:`readthedocs.yml` `file <https://github.com/QubesOS/qubes-doc/blob/main/.readthedocs.yaml>`__ which tells RTD how to build the documentation. It defines the build environment, Python version, required dependencies, and which Sphinx configuration to run. Thus RTD automatically generates and hosts the docs.

Extensions
----------

We use several Sphinx `extensions <https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`__ as defined in :file:`conf.py`, as well a simple custom one to embed YouTube videos, which can be found `here <https://github.com/QubesOS/qubes-doc/tree/main/_ext>`__.

.. _build_locally:

Building the rST documentation locally
======================================

In order to build the Qubes OS rST documentation locally clone the `qubes-doc <https://github.com/QubesOS/qubes-doc>`__ repository (or your forked one if you want to submit a pull request).

It is recommended to use a virtual environment, f.ex. `venv <https://docs.python.org/3/library/venv.html>`__, `poetry <https://python-poetry.org/>`__ or `uv <https://docs.astral.sh/uv/>`__. In the following section there is a sample setup to prepare local environments for building Qubes OS rST documentation.

Using venv
----------

Creating a Python environment with venv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Install needed packages and clone the repository**

   .. code-block:: console

      $ sudo apt install git python3-dev python3.11-venv
      $ git clone https://github.com/QubesOS/qubes-doc.git
      $ cd qubes-doc

2.  **Create a virtual environment**

   Create and enter the virtual environment.

   .. code-block:: console

      $ python3 -m venv .venv
      $ . .venv/bin/activate
      (.venv) $ echo "$VIRTUAL_ENV"

   .. note::

      You will have to activate the environment every time a new shell is opened.

2.  **Install Sphinx and Required Extensions**

   Install Sphinx and the necessary extensions (:program:`sphinx-autobuild`, :program:`sphinx-lint`).

   .. code-block:: console

      (.venv) $ pip install -r requirements.txt sphinx-lint sphinx-autobuild

Linting the documentation from venv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.  **Run Linting**

   The `sphinx-lint` extension checks for common issues like missing references, invalid directives,
   or formatting errors. Run the linting step using the :program:`sphinx-lint` command.

   .. code-block:: console

      (.venv) $ sphinx-lint -i .venv .

2.  **Run Link Checker**

   The `sphinx-linkcheck` extension verifies the validity of all external and internal links.

   The results will be written to the :file:`_build/linkcheck` directory with a detailed report in :file:`output.txt` or :file:`output.json` files
   of all checked links and their status (e.g., OK, broken, timeout).

   .. code-block:: console

      (.venv) $ sphinx-build -b linkcheck . _build/linkcheck

Building the documentation from venv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **Build Documentation**

   Use `sphinx-build` with the `-v` (verbose) flag to generate detailed output during the build process.
   The build command specifies the source directory (current directory :file:`.`, :file:`qubes-doc` in this case), the output directory (:file:`_build/html`), and the builder (`html`).

   .. code-block:: console

      (.venv) $ sphinx-build -v -b html . _build/html

   The build command specifies the source directory (:file:`qubes-doc`), the output directory (:file:`_build/html`), and the builder (`html`).
   The build command will process all source files in the :file:`qubes-doc` directory, generate HTML output in the :file:`_build/html` directory, and print detailed build information to the console.
   Pay attention to errors and warning in the output!
   Please do not introduce any new warnings and fix all errors.

-  **Use sphinx-autobuild for development**

   For an active development workflow, you can use `sphinx-autobuild` to automatically rebuild the documentation
   and refresh browser whenever a file is saved. `sphinx-autobuild` starts a web server at `http://127.0.0.1:8000`,
   automatically rebuilds the documentation and reloads the browser tab when changes are detected in the :file:`qubes-doc` directory.

   .. code-block:: console

      (.venv) $ sphinx-autobuild . _build/html

Using poetry
------------

You can also use `uv <https://docs.astral.sh/uv/getting-started/>`__ if you wish.

Creating a Python environment with poetry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. `Install poetry <https://python-poetry.org/docs/#installation>`__ and git and clone the repository.

   .. code-block:: console

      $ sudo apt install git
      $ git clone https://github.com/QubesOS/qubes-doc.git
      $ cd qubes-doc

2.  **Install Sphinx and Required Extensions**

   Install Poetry, Sphinx and the necessary extensions (`sphinx-autobuild`, `sphinx-lint`).
   A :file:`pyproject.toml` file is `provided <https://github.com/QubesOS/qubes-doc/blob/main/pyproject.toml>`__.

   .. code-block:: console

      $ curl -sSL https://install.python-poetry.org | python3 -
      $ poetry config virtualenvs.in-project true  # optional
      $ poetry install

   .. hint::

      If you would like to avoid prefixing commands with :program:`poetry run`, you can source the virtual environment with ``eval $(poetry env activate)`` on every new shell session. Note that when enabling ``virtualenvs.in-project``, you will find the virtual environment in the project root directory undre ``.venv``, same place the ``venv`` instructions uses.

Linting the documentation with peotry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.  **Run Linting**

   The `sphinx-lint` extension checks for common issues like missing references, invalid directives,
   or formatting errors. Run the linting step using the :program:`sphinx-lint` command.

   .. code-block:: console

      $ poetry run sphinx-lint -i .venv .

2.  **Run Link Checker**

   The `sphinx-linkcheck` extension verifies the validity of all external and internal links.

   The results will be written to the :file:`_build/linkcheck` directory with a detailed report in :file:`output.txt` or :file:`output.json` files
   of all checked links and their status (e.g., OK, broken, timeout).

   .. code-block:: console

      $ poetry run sphinx-build -b linkcheck . _build/linkcheck

Building the documentation with poetry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **Build Documentation**

   Use `sphinx-build` with the `-v` (verbose) flag to generate detailed output during the build process.
   The build command specifies the source directory (current directory :file:`.`, :file:`qubes-doc` in this case), the output directory (:file:`_build/html`), and the builder (`html`).

   .. code-block:: console

      $ poetry run sphinx-build -v -b html . _build/html

   The build command specifies the source directory (:file:`qubes-doc`), the output directory (:file:`_build/html`), and the builder (`html`).
   The build command will process all source files in the :file:`qubes-doc` directory, generate HTML output in the :file:`_build/html` directory, and print detailed build information to the console.
   Pay attention to errors and warning in the output!
   Please do not introduce any new warnings and fix all errors.

-  **Use sphinx-autobuild for development**

   For an active development workflow, you can use `sphinx-autobuild` to automatically rebuild the documentation
   and refresh browser whenever a file is saved. `sphinx-autobuild` starts a web server at `http://127.0.0.1:8000`,
   automatically rebuilds the documentation and reloads the browser tab when changes are detected in the :file:`qubes-doc` directory.

   .. code-block:: console

      $ poetry run sphinx-autobuild . _build/html

Editor
------

An editor you can use is `ReText <https://github.com/retext-project/retext>`__ but any editor would do.

.. code-block:: console

   $ sudo apt install libxcb-cursor0
   $ python3 -m venv .venv
   $ . .venv/bin/activate
   $ pip3 install ReText

Security
========

Also see: :ref:`FAQ: Why is the documentation hosted on ReadTheDocs as opposed to the website? <introduction/faq:why is the documentation hosted on readthedocs as opposed to the website?>`

All pull requests (PRs) against `qubes-doc <https://github.com/QubesOS/qubes-doc>`__ must pass review prior to be merged, except in the case of :ref:`external documentation <index:external documentation>` (see `#4693 <https://github.com/QubesOS/qubes-issues/issues/4693>`__). This process is designed to ensure that contributed text is accurate and non-malicious. This process is a best effort that should provide a reasonable degree of assurance, but it is not foolproof. For example, all text characters are checked for ANSI escape sequences. However, binaries, such as images, are simply checked to ensure they appear or function the way they should when the website is rendered. They are not further analyzed in an attempt to determine whether they are malicious.

Once a pull request passes review, the reviewer should add a signed comment stating, “Passed review as of ``<LATEST_COMMIT>`` (or similar). The documentation maintainer then verifies that the pull request is mechanically sound (no merge conflicts, broken links, ANSI escapes, etc.). If so, the documentation maintainer then merges the pull request, adds a PGP-signed tag to the latest commit (usually the merge commit), then pushes to the remote. In cases in which another reviewer is not required, the documentation maintainer may review the pull request (in which case no signed comment is necessary, since it would be redundant with the signed tag).

Questions, problems, and improvements
=====================================

If you have a question about something you read in the documentation or about how to edit the documentation, please post it on the `forum <https://forum.qubes-os.org/>`__ or send it to the appropriate :doc:`mailing list </introduction/support>`. If you see that something in the documentation should be fixed or improved, please :ref:`contribute <developer/general/how-to-edit-the-rst-documentation:how to submit a pull request>` the change yourself. To report an issue with the documentation, please follow our standard :doc:`issue reporting guidelines </introduction/issue-tracking>`. (If you report an issue with the documentation, you will likely be asked to submit a pull request for it, unless there is a clear indication in your report that you are not willing or able to do so.)

.. |page-source-button| image:: /attachment/doc/doc-pr_01_page-source-button-rtd.png
   :alt: Highlights the Edit Source Button to GitHub sources on doc.qubes-os.org
.. |github-edit| image:: /attachment/doc/doc-pr_02_github-edit-rst.png
   :alt: Highlights the Sign-In on GitHub
.. |github-sign-in| image:: /attachment/doc/doc-pr_03_sign-in-rst.png
   :alt: GitHub Login
.. |fork1| image:: /attachment/doc/doc-pr_04_fork-rst1.png
   :alt: Highlights the Fork Button on GitHub for the qubes-doc repository
.. |fork2| image:: /attachment/doc/doc-pr_04_fork-rst2.png
   :alt: Highlights the Create Fork Button on GitHub when forking the qubes-doc repository
.. |fork3| image:: /attachment/doc/doc-pr_04_fork-rst3.png
   :alt: Forked qubes-doc repository on GitHub
.. |edit| image:: /attachment/doc/doc-pr_05_edit-rst.png
   :alt: Highlights the edit options for an rst file in the GitHub forked qubes-doc repository
.. |commit| image:: /attachment/doc/doc-pr_06_commit-msg-rst.png
   :alt: Highlights the commit changes button on GitHub
.. |pull-request-confirm| image:: /attachment/doc/doc-pr_09_create-pr-rst.png
   :alt: Highlights the create pull request button on GitHub when creating a pull request
.. |pull-request-builds| image:: /attachment/doc/doc-pr_10_view-pr-rtd.png
   :alt: Highlights the pull request <number> and its build in the build list on RTD
.. |pull-request-build| image:: /attachment/doc/doc-pr_11_view-pr-rtd.png
   :alt: Highlights the View Docs button in a specific build for a pull request <number> on RTD
