=========
 CHANGES
=========

4.0.1 (unreleased)
==================

- Host documentation at https://zopeappapidoc.readthedocs.io/


4.0.0 (2017-05-25)
==================

- Add support for Python 3.4, 3.5, 3.6 and PyPy.

- The long-deprecated layer configuration was removed. It was only
  ever available if the ``deprecatedlayers`` ZCML feature was installed.

- Modernize some of the templates. ``zope.app.apidoc`` can now be used
  with Chameleon 3.2 via z3c.pt and z3c.ptcompat.

- Declared install dependency on ``zope.app.exception``.

- Docstrings are treated as UTF-8 on Python 2.

- Handle keyword only arguments and annotations in function signatures
  on Python 3.

- Change the default documentation format to ``restructuredtext`` for
  modules that do not specify a ``__docformat__``. Previously it was
  ``structuredtext`` (STX).

3.7.5 (2010-09-12)
==================

- Define ``__file__`` in doctests to make them pass under Python 2.4.

3.7.4 (2010-09-01)
==================

- Prefer the standard library's doctest module to the one from zope.testing.

- Remove unneeded dependencies zope.app.component and zope.app.container

3.7.3 (2010-07-14)
==================

- Apply refactoring from #153309.
- Fix LP bug 605057: ZCML links were no longer working (Guilherme Salgado)

3.7.2 (2010-03-07)
==================

- Adapted tests for Python2.4


3.7.1 (2010-01-05)
==================

- Updated tests to work with zope.publisher 3.12 (using ``zope.login``).

3.7.0 (2009-12-22)
==================

- Updated tests to work with latest ``zope.testing`` and use ``zope.browserpage`` in
  favor of ``zope.app.pagetemplate``.

3.6.8 (2009-11-18)
==================

- Updated the tests after moving ``IPossibleSite`` and ``ISite`` to
  ``zope.component``.

3.6.7 (2009-09-29)
==================

- Updated the tests after moving ``ITraverser`` back to ``zope.traversing``.

3.6.6 (2009-09-15)
==================

- Made the tests work again with the most recent Zope Toolkit KGS.

3.6.5 (2009-07-24)
==================

- Update documentation file in ``zope.site`` from ``README.txt`` to
  ``site.txt``.

3.6.4 (2009-07-23)
==================

- The ``IContained`` interface moved to ``zope.location.interfaces``. Make a
  test pass.

3.6.3 (2009-05-16)
==================

- Explicitly defined default views.

- Replace relative url links with absolute ones.

- Added ``z3c`` packages to the code browser.

- Made ``bin/static-apidoc`` principally working (publisher and
  webserver mode). There are still some files which are not correctly
  fetched.

3.6.2 (2009-03-17)
==================

- Adapt principal registry book chapter to a new place, as it was moved
  from zope.app.security to zope.principalregistry.

- Remove zcml slugs and old zpkg-related files.

3.6.1 (2009-02-04)
==================

- When a module provides an interface or has an __all__ attribute,
  use one of those for the module documentation.  Fixes LP #323375.

- Undid broken link to ``savepoint.txt`` caused in 3.6.0.  The latest
  version of the transaction package puts savepoint.txt in the ``tests``
  subpackage.

- Expanded the presentation of module documentation.

- Class documentation now includes constructor information.

3.6.0 (2009-01-31)
==================

- Use zope.container instead of zope.app.container.

- Use zope.site instead of zope.app.component and zope.app.folder (in
  at least a few places).

- ``savepoint.txt`` moved from ZODB's test directory a level up -- we
  follow.

- Make compatible with new zope.traversing and zope.location.

3.5.0 (2009-01-17)
==================

- Adapted transaction book chapters for new transaction egg. The
  README.txt was removed and savepoint.txt was moved. Also add chapter
  about dooming transactions (doom.txt).

- Changed mailing list address to zope-dev at zope.org, because zope3-dev
  is retired now.

- Cleaned up dependencies.

3.4.3 (2007-11-10)
==================

- Fix https://bugs.launchpad.net/zope3/+bug/161737: Misleading text in
  the interface viewer.

- Fix https://bugs.launchpad.net/zope3/+bug/161190: The zope3-dev
  mailinglist has been retired, point to zope-dev.


3.4.2 (2007-10-30)
==================

- Avoid deprecation warnings for ``ZopeMessageFactory``.

3.4.1 (2007-10-23)
==================

- Avoid deprecation warnings.

3.4.0 (2007-10-10)
==================

- Improved package meta-data.

- Fixed the code to at least gracefully ignore unzipped eggs. Eventually we
  want to handle eggs well.

3.4.0a1 (2007-04-22)
====================

- Initial release independent of the main Zope tree.
