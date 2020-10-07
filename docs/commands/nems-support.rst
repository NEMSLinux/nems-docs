NEMS Command: nems-support
==========================

*nems-support* automatically creates an encrypted backup file
called **support.nems** which contains all information about your
running NEMS server. This information is intended to be used during
support sessions in event that you are experiencing issues and require
assistance from NEMS Linux support.

Currently, NEMS Linux is a community project driven by one
individual: **Robbie Ferguson**. You should be wary of sending your
support.nems file to anyone but Robbie, as it contains confidential
information (eg., your email settings from NEMS SST). The file is
encrypted, but can easily be decrypted using your NEMS Hardware ID if
that information is available.

Robbie accepts support requests via the Community Forum and by Private
Message on Patreon. The email address for you to send your support.nems
file to will always be on either @category5.tv or @nemslinux.com
domains. If anyone ever asks you to send it somewhere else, be cautious.

**To create a support.nems file, run:**

sudo nems-support

You will then be advised where to send your support.nems file, along
with a 6-digit string you must send with the file. This string is simply
the first 6 digits of your HWID, to prevent sending the full key. Robbie
will use this string to look up your full HWID for decryption.

If your support request has to do with a Community Forum thread, please
also include the  to the thread within the body of your email.

Once created, you can access the support.nems file from your computer by
navigating
to `https://NEMS.local/backup/support.nems <https://nems.local/backup/support.nems>`__ -or-
find the file on the SMB share at \\\NEMS.local\backup

Report
------

The command line option *report* forgoes the backup portion
of *nems-support* and only generates a small textual report to assist in
diagnosing problems.

**To generate this report, run:**

sudo nems-support report

The support.nems and support-report.txt files self-destruct after 15
minutes.