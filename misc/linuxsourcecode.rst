NEMS Linux Source Code
======================

Are you a coder or want to explore some of the things NEMS does under
the hood?

NEMS itself is a Linux distro built from pre-compiling several tools
onto a customized Debian base. The day-to-day operation of NEMS is
provided by a combination of those tools (Eg., Nagios, Monitorix,
Webmin, Check_MK) but a fair bit of the magic happens thanks to custom
bash and PHP scripts I've developed (or modified in some cases) to make
NEMS do the things I wanted it to do, and the things users have
requested.

You can explore these custom scripts `on my Github
page <https://github.com/Cat5TV?utf8=✓&tab=repositories&q=nems&type=&language=>`__.

Files Of Interest
-----------------

nems-scripts
~~~~~~~~~~~~

-  `fixes.sh <https://github.com/Cat5TV/nems-scripts/blob/master/fixes.sh>`__ -
   This script allows me to fix bugs and issues in existing NEMS
   deployments. It also allows me to add minor features not worthy of a
   point release. This runs automatically every day and at reboot.