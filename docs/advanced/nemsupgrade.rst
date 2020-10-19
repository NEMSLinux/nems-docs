Upgrade NEMS Linux to Newer Version
===================================

Definition of Version Terms
---------------------------

When we designate a version with an 'x', such as NEMS Linux 1.2.x, we
mean anything within the 1.2 rolling release cycle. This means 1.2
(which can also be considered 1.2.0 if desired), 1.2.1, 1.2.2, and
so-on.

Legacy Distro Support
---------------------

`Upgrade NagiosPi or NEMS 1.0 to the Latest Version of
NEMS <https://docs.nemslinux.com/usage/nagiospi-to-nems>`__

Rolling Release Upgrade Instructions
------------------------------------

**Important Exception:** Due to the sudden and unexpected release of the
Raspberry Pi 4 Model B 8 , NEMS Linux 1.5.2, while a point release, is
in fact a major upgrade. Therefore, you will need to follow the Major
Release Upgrade Instructions if you choose to deploy NEMS Linux 1.5.2.
This is because the bootloader on the new board has changed from
previous versions, so a rolling upgrade is not possible.

A rolling release is a second decimal point release, and rolling
upgrades are available within each major release as made available.
Rolling releases are usually pushed out in order to fix bugs or improve
features. An example of a rolling release would be going from NEMS Linux
1.2 to 1.2.1, or 1.2.1 to 1.2.3. Once a new NEMS Linux major release is
available, it is recommended to perform a major release upgrade to
ensure you have the latest and greatest NEMS Linux has to offer.

1. Login to NEMS Linux via SSH as the *pi* user.
2. Type: ``sudo nems-upgrade``
3. Reboot.

**Please Note:** If you receive a notice
that `nems-upgrade <https://docs.nemslinux.com/commands/nems-upgrade>`__ is
an unknown program, did you initialize NEMS Linux? Please re-read
the `Installation
Instructions <https://docs.nemslinux.com/installation>`__ if that is the
case.

Major Release Upgrade Instructions
----------------------------------

These steps may be followed to upgrade from one major point release to
the next major point release. For example, this process will take you
from NEMS Linux 1.1 to NEMS Linux 1.2, or NEMS Linux 1.2.x to NEMS Linux
1.3, or ultimately, NEMS Linux 1.3 to 2.0, and so-on.

1. Connect to your existing NEMS Linux dashboard from your computer and
   press Migrator→Backup. That will give you your backup.nems file.
2. Deploy the latest version of NEMS Linux on a **new** card (please use
   a new card so you can always revert back to your existing NEMS Linux
   if you have a problem).
3. Boot your Pi with the new NEMS Linux card and initialize it as normal
   (instructions are provided via your web browser when you connect)
4. Once you get to the dashboard simply click Migrator→Restore to open
   the documentation which walks you through restoring your settings
   from your backup.nems file.

Upgrade from NEMS Linux 1.0 or nagiospi
---------------------------------------

See legacy upgrade documentation
here: http://www.baldnerd.com/nems-migrator-legacy-upgrade/
