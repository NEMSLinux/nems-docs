:orphan:

NEMS Command: nems-upgrade
==========================

*nems-upgrade* automatically upgrades NEMS Linux. It is very easy to use,
and is how I am able to offer NEMS as a rolling release during each major
release cycle (called NEMS Branch). This way, you do not have to
re-download and re-flash NEMS every time I release a new feature.

Generally, bugfixes and minor improvements do not require manual
intervention: they are automatically handled by nightly update processes.

By contrast, rolling release upgrades (I.E., point release upgrades)
require you to manually upgrade with the *nems-upgrade* command, which
requires root access.

In order to run nems-upgrade your NEMS Server must first
be `initialized <../gettingstarted/initialization.html>`__.

**Command Line Options**

-  `sudo nems-upgrade` - Upgrade NEMS to the latest rolling release
   within the current branch.
-  `sudo nems-upgrade reset` - Reset NEMS to the top-level
   branch of the currently running version and upgrade from there.
   Helpful when fixing a botched upgrade, should one occur.
