NEMS Command: nems-upgrade
==========================

*nems-upgrade* automatically upgrades NEMS. It is very easy to use, and
is how I am able to offer NEMS as a rolling release during each major
release cycle (called NEMS Branch). This way, you do not have to
re-download and re-flash NEMS every time I release a new feature.

Generally, bugfixes and minor improvements do not require manual
intervention: they are automatically handled by NEMS' *fixes.sh*, which
you do not have to run manually (it automatically runs every day).

By contrast, rolling release upgrades (ie., point release upgrades)
require you to manually upgrade with the *nems-upgrade* command, which
requires root access.

In order to run nems-upgrade your NEMS Server must first
be `initialized <https://docs.nemslinux.com/commands/nems-init>`__.

**Commandline Options**

-  *sudo nems-upgrade* - Upgrade NEMS to the latest rolling release
   within the current branch.
-  *sudo nems-upgrade \ *\ **reset** - Reset NEMS to the top-level
   branch of the currently running version and upgrade from there.
   Helpful when fixing a botched upgrade, should one occur.