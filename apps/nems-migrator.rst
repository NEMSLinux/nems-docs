NEMS Migrator Local Backup
==========================

Introduction
------------

SD cards are prone to failure, and NEMS Linux has protections in place
to ensure the longevity of your storage media. However, what happens if
your card does fail?

NEMS Migrator provides a constant backup of your NEMS Server's
configuration, which can be backed up locally or
`in NEMS Cloud Services <../nems-cloud-services/nems-migrator.html>`__
(or both). Restoring your NEMS Migrator backup gets your configuration
back online within minutes.

Combined with `NEMS
CheckIn <../nems-cloud-services/checkin.html>`__ to notify you
in event of failure, NEMS Migrator is an excellent way to ensure your
NEMS Server is protected against failure.

Local Backups
-------------

Backup
~~~~~~

Your NEMS Linux server automatically generates a backup of your
configuration ready for you to download at any time.

Your NEMS Migrator backup (filename: *backup.nems*) contains your NEMS
server configuration, allowing you to quickly re-deply on a new NEMS
server or re-flashed device without having to re-create your Nagios
configuration manually.

A NEMS Migrator backup is proprietary to NEMS. It is not intended for
user consumption, but rather can be used to restore NEMS Linux to a
previous configuration, or quickly rebuild after an SD card failure (for
example).

NEMS Migrator will check your backup status every few minutes. If the
backup is older than 30 minutes, it will replace your backup.nems file
with a current snapshot. Therefore you know that if you make a copy of
your backup.nems file, it is no older than 30 minutes. If however you
make changes to your configuration, those changes may not appear in your
backup for up to 30 minutes.

To use NEMS Migrator to upgrade from an earlier version of NEMS Linux
(or even NagiosPi), please read `Upgrade NEMS Linux to Newer
Version <../advanced/nemsupgrade.html>`__.

To automate your NEMS Migrator backup, please see `Backup Your NEMS
Configuration
Automatically <../basic/backupnems.html>`__ for
helpful resources and tips.

Restore
~~~~~~~

Please
see `nems-restore <../commands/nems-restore.html>`__.
