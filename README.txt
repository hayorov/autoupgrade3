autoupgrade3
===========

Python 3 friendly automatic upgrade of Python modules and packages

quick start
-----------

::

    :::python
    from autoupgrade3 import AutoUpgrade
    AutoUpgrade("pip").upgrade_if_needed()

The above will upgrade "pip" if there is a new version of pip out there.
The upgrade will be unattended and the python script will be restarted

installation
------------

::

    pip install autoupgrade3

or install latest from repo:

::

    pip install https://bitbucket.org/jorkar/autoupgrade3/get/master.tar.gz

api
---

classes
~~~~~~~

::

    :::python
    class AutoUpgrade(__builtin__.object)

AutoUpgrade class, holds one package

Methods
^^^^^^^

::

    :::python
    __init__(self, pkg, index=None, verbose=False)

Args: pkg (str): name of package index (str): alternative index, if not
given default from *pip* will be used. Include full index url, e.g.
https://example.com/simple

::

    :::python
    check(self)

Check if pkg has a later version Returns true if later version exists.

::

    :::python
    restart(self)

Restart application with same args as it was started. Does **not**
return

::

    :::python
    upgrade(self, dependencies=False)

Upgrade the package unconditionaly Args: dependencies, update
dependencies if True (see pip--no-deps)

::

    :::python
    upgrade_if_needed(self, restart=True, dependencies=False)

Upgrade the package if there is a later version available. Args:
restart, restart app if True dependencies, update dependencies if True
(see pip --no-deps)

Supported platforms
-------------------

Currently tested on Linux with Python 2.7/3.5. Should be usable on Windows and \*nix.

Release notes
-------------

0.2.1
~~~~~

Forked from autoupgrade
Python 3.5 support

0.2.0
~~~~~

Corrections: - Issue #2, Index did not work when specified - Issue #3,
Autoupgrade should not print to console (added verbose flag to keep
backward compatibility - Issue #4, Support for pip > 0.6

0.1.5
~~~~~

Corrections: - Issue #1, Extra index did not work for all servers.

0.1.4
~~~~~

-  Fixed bug when version contains characters.

0.1.3
~~~~~

-  Fixed vital fault in 0.1.2

0.1.2
~~~~~

-  Setup file fixes
-  Removed verbose output as default
-  Return value fixed of upgrade()

0.1.1
~~~~~

-  Dependencies updated

0.1.0
~~~~~

Initial release

Info
====

-  Homepage: https://github.com/hayorov/autoupgrade3

