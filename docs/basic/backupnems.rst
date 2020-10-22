NEMS Linux Tips: Backup Your NEMS Configuration Automatically
=============================================================

Introduction
------------

One of the worst things that can happen to your NEMS Linux deployment is
having your SD card fail. So keeping a current backup of your NEMS
configuration is a smart idea.

Backup Location
---------------

Your NEMS Migrator snapshots are always accessible at
https://NEMSIP/backup/backup.nems *or* via Samba at
\\\nems.local\backup\backup.nems - accessing either will automatically
generate and send a *backup.nems* file, which contains all the NEMS
configuration settings, logs, data, etc. to allow an easy recovery by
restoring to a new NEMS deployment.

Both locations are protected by your NEMS username and password, as
created
during `nems-init <https://docs.nemslinux.com/commands/nems-init>`__.

The *backup.nems* file can also be used to migrate your NEMS Linux
deployment from one architecture to another. For example, if your
infrastructure outgrows a Raspberry Pi 3-based NEMS server, you can
deploy on an ODROID XU4 and migrate your entire NEMS setup to the new
deployment.

Knowing the location of your *backup.nems* file makes it easy to add a
NEMS backup to your daily backup script for automated inclusion in your
regular backup.

Backup Your backup.nems File Automatically
------------------------------------------

From another Linux server (eg., where your backups run) simply add this
to your backup task:

Download Via wget Using Secure SSL (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using SSL not only protects the content of your backup, but also
protects your username and password from prying eyes

**wget** -O "/backup/backup.nems" https://NEMSIP/backup/ --user=YOURUSER
--password=YOURPASSWORD --no-check-certificate

I included --no-check-certificate since NEMS is using a self-signed
certificate. This will allow the communication to be encrypted, but not
fail on the “invalid” self-signed cert.

Note the -O “/backup/backup.nems” is just an example of the OUTPUT
folder. You'll want to change this to suit your local system. Eg., -O
“/home/robbie/backups/backup.nems” - the -O is telling it where to save
the local copy.

Download Via wget Without Encryption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is only recommended for legacy NEMS versions that don't support SSL

**wget** -O "/backup/backup.nems" http://nems.local/backup/
--user=YOURUSER --password=YOURPASSWORD

In both of the above examples, replace */backup/backup.nems* with where
you want nems-migrator to output the download,
and *YOURUSER* and *YOURPASSWORD* to those you set
during `nems-init <https://docs.nemslinux.com/commands/nems-init>`__.

Once you have a backup.nems file being backed up to a different system,
I recommend you have your backup script run an *rdiff-backup* of
your */backup* folder (in this example) to allow for versioning.

Windows-Based Backup
~~~~~~~~~~~~~~~~~~~~

If you are on a Windows network and would like to include your
backup.nems file in your nightly backup set, you may access it at
\\\nems.local\backup\backup.nems using your NEMS username and password
as set in `nems-init <https://docs.nemslinux.com/commands/nems-init>`__.
