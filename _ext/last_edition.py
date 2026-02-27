#!/usr/bin/env python3
"""Add last_edition_datetime to the html context"""

import datetime
import os
import subprocess

MIGRATION_DATETIME = datetime.datetime.fromisoformat("2025-08-06 02:20:01+02:00")

_DEFAULT_TIMEOUT = 1
_GIT_TIMEOUT = int(os.environ.get("QUBES_DOC_LAST_EDITION_TIMEOUT", _DEFAULT_TIMEOUT))


def html_page_context(app, pagename, templatename, context, doctree):
    """Edit the html context to add last_edition_datetime

    Default value of last_edition_datetime: None

    If possible, try to get the last commit iso date from git log.
    If any error occurs while trying to run `git log` it will silently fail.
    If the last commit is related to the migration to reStructuredText, do not
    provide a last_edition_datetime
    """
    context["last_edition_datetime"] = None

    if "sourcename" not in context or "page_source_suffix" not in context:
        return

    git_dir = app.env.srcdir / ".git"

    try:
        last_datetime_raw = subprocess.check_output(
            (
                "git",
                "--git-dir",
                git_dir,
                "log",
                "-1",
                "--pretty=format:%ci",
                "--",
                f"{pagename}{context['page_source_suffix']}",
            ),
            timeout=_GIT_TIMEOUT,
        ).decode()
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
        PermissionError,
        OSError,
    ):
        return

    try:
        last_datetime = datetime.datetime.fromisoformat(last_datetime_raw)
    except ValueError:
        return

    if last_datetime > MIGRATION_DATETIME:
        context["last_edition_datetime"] = last_datetime


def setup(app):
    app.connect("html-page-context", html_page_context)
