==================
Contribution guide
==================

This is contribution guide for pykakasi project.
You are welcome to send a Pull-Request, reporting bugs and ask questions.

Resources
=========

- Project owner: Hiroshi Miura
- Slack chat: `Join`_ to  https://pykakasi.slack.com/
- Bug Tracker:  Github issue `Tracker`_
- Status: alpha
- Activity: low

.. _`Join`: https://join.slack.com/t/pykakasi/shared_invite/enQtNTU0MjAyNzY2MTE5LTk2YWU5ZGIwZjAxMTZlMzhmMmM2NjQ5YTZlM2QyMDg1MTdjMGVkZTU1N2ZjYWE5N2QzMTNkM2FlZGI2YzRiMTY
.. _`Tracker`: https://github.com/miurahr/pykakasi/issues

Bug triage
==========

Every report to github issue tracker should be triaged
whether it is bug, question or invalid.


Send patch
==========

Here is small amount rule when you want to send patch the project;

1. every proposal for modification should send as 'Pull Request'

1. each pull request can consist of multiple commits.

1. you are encourage to split modifications to individual commits that are logical subpart.

CI tests
=========

Pykakasi project configured to use AppVeyor, Travis-CI and CoverAlls for regression test.
You can see test results on badge and see details in a web page linked from badge.
The results are also notified in gitter channel.

Local test
==========

To run test, you can do it as ordinary::

    python setup.py test

or::

    pytest

You can also run test using pyenv/tox with versions::

    pyenv install 2.7.13
    pyenv install 3.5.5
    pyenv install 3.6.4
    pyenv local 2.7.13, 3.5.5, 3.6.4
    tox
