NEMS Cloud Services
===================

Quick points

-  *nems-info cloudauth* will show if your NEMS Cloud Services account
   is active or not.
-  When active, NEMS Cloud Services will receive the updated status of
   all your NEMS servers every 60 seconds.

Requirements
============

In order to use NEMS Cloud Services, you must be running NEMS Linux 1.5
or higher. You must also be a Patron of `NEMS Linux on
Patreon <https://patreon.com/nems/>`__ at a tier that includes NEMS
Cloud Services.

Included Services
=================

NEMS Migrator Off Site Backup
-----------------------------

NEMS Migrator Off Site Backup ensures your NEMS server configuration is
backed up off site every day, and you can revert to any day's snapshot.

See `NEMS
Migrator <https://docs.nemslinux.com/features/nems-migrator>`__

`checkin <https://docs.nemslinux.com/_media/features/checkin>`__

NEMS Cloud Services Dashboard
-----------------------------

Features
~~~~~~~~

-  View your NEMS Linux state information from anywhere.
-  Open NEMS TV Dashboard for any of your NEMS Servers from anywhere.
-  Connect multiple NEMS Servers to a single dashboard to be able to see
   the state of multiple distributed NEMS Servers on one screen.
-  Extend NEMS Warning Light and NEMS GPIO Extender to support multiple
   NEMS Servers and be geographically located anywhere in the world.

Security Points
~~~~~~~~~~~~~~~

-  Cloud Dashboard password is set in NEMS SST
-  Password is salted with a 256-byte key before the data from nems is
   encrypted
-  data includes state information only (same info that appears on nems
   tv dashboard)
-  multiple NEMS servers may be linked together to a single cloud
   dashboard
-  since nobody knows your custom password, only you can see your data
   (it cannot be decrypted without your password)
-  leaving dashboard open continually extends cookie, so it is suitable
   for server room (don't need to continually login)

Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Why do I have to enter my NEMS HWID, NEMS Cloud Services Key and
Decryption Password to login? Can't you make it so I can create a
username and password and login that way?**

Your NEMS HWID and NEMS Cloud Services Key authenticates your session.
Your Decryption Password on the other hand allows NEMS Cloud Services to
decrypt your NEMS State information. For your safety, your decryption
password is never stored on the server, and only you know it. I will not
create a mechanism for your private decryption password to be associated
with your account. You must enter it every time you login, since it is
never stored within NEMS Cloud Services.

**Since I have to enter my decryption password only once per session,
how can you say it is not stored?**

When you enter your encryption password, it is transmitted over your
browser's SSL connection to the NEMS Cloud Services server. There, it is
not stored in the session. Rather, your password is salted and hashed,
and this hash is what is stored in the session. Once your session has
expired, your hash is discarded.
