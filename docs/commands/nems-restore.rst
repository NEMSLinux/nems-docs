NEMS Linux Command: nems-restore
================================

The NEMS Migrator tool allows you to export/backup your NEMS
configuration (*backup.nems*) as well as import a previous backup
(through the Restore option).

The NEMS Migrator backup and restore options are great for keeping a
safe backup without having to shutdown your NEMS server. Just download
the file once in a while, or `back it up automatically with your daily
backup
script <https://docs.nemslinux.com/tips/backup_nems_automatically>`__.

NEMS Migrator is also helpful when upgrading from previous versions of
NEMS, or when moving from one platform to another, saving you having to
reconfigure your NEMS deployment just to get the latest features or
upgraded hardware.

Important Note
--------------

I am a firm believer in redundancy, and protecting your data. What I'd
like you to do is, export your migration file, then install NEMS on
a *new* MicroSD card. Then boot from that and restore your NEMS Migrator
backup. Once you've confirmed everything worked well, you can deprecate
the old one safely. However, if something went wrong, you can contact me
to fix it for you, and continue running from the old SD card in the
interim.

How to Restore a NEMS Migrator Backup
-------------------------------------

While you can use NEMS Migrator to *backup* any version of NEMS Linux
(and even NagiosPi) the restore feature requires NEMS Linux 1.2+

First Step
~~~~~~~~~~

1. Deploy the version of NEMS you wish to restore the backup to. Please
   heed my Important Note above.
2. Boot the new NEMS Linux deployment and mount the USB flash drive.

Restore a Local Backup
~~~~~~~~~~~~~~~~~~~~~~

1. From any computer on your network, obtain a copy of
   your *backup.nems* file from a running NEMS server, you can download
   it directly in your web browser at *https://nems.local/backup/* or
   click the Migrator menu item on your NEMS Dashboard.

2. Get your *backup.nems* file to your NEMS Server via one of the
   following methods:

   -  Place your *backup.nems* file on a USB flash drive and mount that
      flash drive on your NEMS Server.

   -  Copy your *backup.nems* file to your NEMS Server over Samba
      at *\\\nems.local\home* which will place it in the home folder of
      your NEMS user, which will be accessible on NEMS Linux
      at */home/\ *\ **username**\ *\ /backup.nems*

   -  Copy your *backup.nems* file to your NEMS Server via SCP:

      **scp** <path to backup.nems> <username>@<nemsIP>:/home/<username>

3. Determine the location of *backup.nems* on your NEMS Server. For
   example, if you mounted the USB flash drive on */mnt/flash* you may
   determine the location to be */mnt/flash/backup.nems*, or if you
   copied it to the home folder, your file will be located
   at */home/\ *\ **username**\ *\ /backup.nems*

4. Armed with that information, run the following command (use the *full
   path* to your backup.nems file):

   **sudo** nems-restore /mnt/flash/backup.nems

   or

   **sudo** nems-restore /home/<username>/backup.nems

Restore an Off-Site Backup
==========================

This requires an active NEMS Migrator Off-Site Backup (NEMS-OSB)
account.

1. Run the command and choose the date you'd like to restore to:

   **sudo** nems-restore osb

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="350" src=https://youtu.be/oREK_PUhkAE frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>

Restore Off-Site Backup from Other Device
-----------------------------------------

By default NEMS-OSB will assume you are restoring to the same device
that was used when the Off-Site Backup was created. However this may not
always be the case (ie., perhaps your device failed and you need to
restore to a new device).

1. In NEMS System Settings Tool's “NEMS Cloud Services” tab, enter the
   NEMS Cloud Services Key from your old device. It will fail to
   authenticate since it is for a different HWID, but this is required
   in order to authenticate your account.

2. You will also need to enter your Personal Encryption/Decryption
   Password so NEMS can read the OSB data from your old device.

3. Run the command and choose the date you'd like to restore to:

   **sudo** nems-restore osb OLD_HWID

   (where OLD_HWID is the HWID from your old device)

Every Off-Site Backup is hard-tied to its originating HWID. You must
restore your backup to the new device before closing the old NEMS-OSB
account. Once a NEMS-OSB account is closed or moved to another HWID, the
old backups are no longer recoverable (for security reasons). You do not
need a NEMS-OSB account on your new device to restore, as long as you
know the originating HWID and NEMS Cloud Services key.

Final Step
~~~~~~~~~~

1. Follow the prompts on screen to restore your configuration to the new
   NEMS Linux deployment. If it fails for any reason, you can safely
   shut down and replace the SD card with your original deployment.

If you have any problems (or praise) please post in `the NEMS Linux
community forum <http://forum.category5.tv/forum-8.html>`__.


