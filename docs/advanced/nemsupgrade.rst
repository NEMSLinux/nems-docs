Upgrade NEMS Linux to Newer Version
===================================

Definition of Version Terms
---------------------------

Major Release
^^^^^^^^^^^^^

The whole number and first decimal place of any NEMS Linux version
represents the major release. 1.7 is a major release. A major release
requires reinstallation of NEMS Linux. The steps to migrate all your
settings is found below.

Point Release
^^^^^^^^^^^^^

When we designate a version with an 'x', such as NEMS Linux 1.2.x, we
mean anything within the 1.2 rolling release cycle. This means 1.2
(which can also be considered 1.2.0 if desired), 1.2.1, 1.2.2, and
so-on. Point releases within the currently-running major release can be
obtained with the ``sudo nems-upgrade`` command.

Summary
^^^^^^^

1.7 is a major release. 1.2.1 is the first point release of NEMS Linux 1.2.

Major Release Upgrade Instructions
----------------------------------

These steps may be followed to upgrade from one major point release to
the next major point release. For example, this process will take you
from NEMS Linux 1.1 to NEMS Linux 1.2, or NEMS Linux 1.2.x to NEMS Linux
1.3, or even NEMS Linux 1.3 to 1.7, and so-on.

1. Connect to your existing NEMS Linux dashboard from your computer and
   press Migrator→Backup. That will give you your `backup.nems` file.
2. Deploy the latest version of NEMS Linux on a **new** card (please use
   a new card so you can always revert back to your existing NEMS Linux
   if you have a problem).
3. Boot your NEMS Server with the new NEMS Linux card and initialize it as normal
   (instructions are provided via your web browser when you connect).
4. Once you get to the dashboard simply go through the NEMS Migrator
   `nems-restore <https://docs.nemslinux.com/en/latest/commands/nems-restore.html#how-to-restore-a-nems-migrator-backup>`__
   process to restore your settings from your backup.nems file.

.. Tip:: To save your backup.nems file to the new installation, you can browse to your home folder using samba (or \\nems.local\home in Windows).

Rolling Release Upgrade Instructions
------------------------------------

A rolling release is a second decimal point release, and rolling
upgrades are available within each major release as made available.
Rolling releases are usually pushed out in order to fix bugs or improve
features. An example of a rolling release would be going from NEMS Linux
1.2 to 1.2.1, or 1.2.1 to 1.2.3. Once a new NEMS Linux major release is
available, it is recommended to perform a major release upgrade to
ensure you have the latest and greatest NEMS Linux has to offer.

1. Login to NEMS Linux via SSH.
2. Type: ``sudo nems-upgrade``
3. Reboot.

**Please Note:** If you receive a notice
that `nems-upgrade <../commands/nems-upgrade.html>`__ is
an unknown program, did you initialize NEMS Linux? Please re-read
the `Initialization
Instructions <../gettingstarted/initialization.html>`__ if that is the
case.

Legacy Distro Support
---------------------

`Upgrade NagiosPi or NEMS 1.0 to the Latest Version of
NEMS <advanced/legacyupgrade.html>`__
