This directory contains changelog *fragments* — small .rst (reStructuredText) files describing individual pull requests or fixes. These are compiled into ``CHANGES.rst`` by `towncrier <https://towncrier.readthedocs.io/en/latest/>`_.

The resulting changelog is meant for **users**. Focus your entry on what changed from a user's point of view, rather than internal implementation details.

Use full sentences, in the past tense, with proper punctuation. For example::

    Added framework supporting evaluation of usecase-specific grader prompt.

File Naming
===========

Each file should be named using the format:

    <ISSUE_OR_PR_NUMBER>.<TYPE>.rst

Where ``<TYPE>`` is one of:

- ``feature`` — New user-facing functionality
- ``bugfix`` — Fixes a defect or broken behavior
- ``doc`` — Documentation-only change
- ``removal`` — Deprecation or removal of a feature
- ``misc`` — Internal or minor change not visible to users

Examples:

    1234.bugfix.rst

    2345.feature.rst

If your change fixes an issue, use the issue number in the filename. Otherwise, use the pull request number.
Place the file in the `changelog/` directory.


When Not to Add a Fragment
==========================
If your change doesn't merit a changelog entry (e.g., minor refactor, test-only update), apply the skip changelog label to your pull request.
