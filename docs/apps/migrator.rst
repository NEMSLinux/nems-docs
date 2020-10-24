##############
NEMS Migrator
##############

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/oREK_PUhkAE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Introduction
------------

SD cards are prone to failure, and NEMS Linux has protections in place
to ensure the longevity of your storage media. However, what happens if
your card does fail?

NEMS Migrator provides a constant backup of your NEMS Server's
configuration, which can be backed up locally or in NEMS Cloud Services
(or both). Restoring your NEMS Migrator backup gets your configuration
back online within minutes.

Combined with `NEMS
CheckIn <https://docs2.nemslinux.com/en/latest/nems-cloud-services/checkin.html?highlight=checkin>`__ to notify you
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
Version <https://docs2.nemslinux.com/en/latest/advanced/nemsupgrade.html>`__.

To automate your NEMS Migrator backup, please see `Backup Your NEMS
Configuration
Automatically <https://docs2.nemslinux.com/en/latest/basic/backupnems.html>`__ for
helpful resources and tips.

Restore
~~~~~~~

Please
see `nems-restore <https://docs2.nemslinux.com/en/latest/commands/nems-restore.html?highlight=restore>`__.

NEMS Cloud Backup
-----------------

.. _backup-1:

Backup
------

NEMS Migrator Off-Site Backup (OSB) is a feature of NEMS Cloud Services.
It encrypts your NEMS Migrator backup on your local NEMS server and then
transmits it to our cloud server over a secure connection where it is
retained securely for 90 days.

Your NEMS Migrator Off-Site Backup is encrypted using a password you
create locally in NEMS SST. Because of this, only you can restore from
this file. Your private password is never sent to our server. Your
account is authenticated based on your NEMS HWID and your NEMS Cloud
Services Key which is provided to you when you register.

Sign up
on `Patreon <https://www.patreon.com/bePatron?c=1348071&rid=2163022>`__ (observe
the reward options) and then add your NEMS Cloud Services Key to
NEMS-SST to activate the service.

Once activated, NEMS will automatically backup your configuration
off-site every day at 4am.

Logging
~~~~~~~

The backup results are stored in /var/log/nems/nems-osb.log

Log Format
^^^^^^^^^^

The log file is a single line of data sent by the server. Each variable
is separated by two colons (::) and begin with variable 0.

-  **0** - Plain text date/time of your NEMS server's when the backup
   began
-  **1** - Response code after file sent
-  **2** - Plain-text interpretation of 1 (ie., Success or Failed)
-  **3** - Plain-text interpretation of 1 (ie., Reason for 2)

If (and only if) the backup was successful with a response code of 1,
the following data will also be logged:

-  **4** - The remote server's unix timestamp at time of off-site backup
   authentication
-  **5** - The size of this backup
-  **6** - Your total usage on the remote storage server, including this
   backup
-  **7** - How many daily backups are currently retained for your
   account
