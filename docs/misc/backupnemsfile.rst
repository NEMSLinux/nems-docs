Why support may ask for your backup.nems file
=============================================

... and why you should never share it with others
-------------------------------------------------

During support sessions I often request either SSH access or a copy of
the user’s *backup.nems* file. SSH access, it should be obvious, should
not be shared with just anyone. Also, you should never, ever, ever, open
SSH to the world on your NEMS server if you have not yet initialized it.
This is because there are botnets that look for omputers which use the
default passwords, and then compromize them.

SSH aside, as it is pretty obvious why it is sometimes the best way for
me to provide support, I wanted to document why I may ask for
your *backup.nems* file, what this file tells me, and why you should not
just send it to anyone offering to help.

Your *backup.nems* file contains your complete NEMS configuration
including those for your Nagios hosts, services, and your plain text
resource.cfg file. This file contains your SMTP credentials which can be
used by me to help diagnose email notification problems, but could also
be used by a malicious user to compromize the mail account. This file
also contains the administrator login information for your Windows
machines, as entered by you. This too can be used by me to help diagnose
an issue with hosts not responding, but can also be used by a malicious
user to compromize your systems should this information get into the
wrong hands.

All this to say, store your *backup.nems* file as you would any other
unencrypted backup set. It contains private information which is very
helpful in diagnosing and helping resolve issues, but should be treated
as a very confidential file.

UPDATE: As of February 2, 2018, NEMS Migrator encrypts sensitive
configuration files before compiling backup.nems if you enter an
encryption/decryption password in NEMS SST. While the backup itself is
unencrypted, this prevents access to sensitive data such as your
passwords.

Please *do not* share your *backup.nems* file with third parties unless
you are certain you can trust them. If you have any questions related to
this document, please comment in the Community Forum.