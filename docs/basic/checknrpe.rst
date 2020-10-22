Check Commands: check_nrpe
==========================

Configuration
-------------

Firewall Ports
~~~~~~~~~~~~~~

If you have a firewall between your NEMS Server and your host, you must
open incoming TCP connections on ports *5666* and *12489* on your host
side.

Since check_nrpe can pose a security risk, please **do not** open these
ports to the world. Rather, ensure your NEMS Server is the only outside
IP allowed to connect to these ports.

Host-Side Service
~~~~~~~~~~~~~~~~~

The NRPE service must be installed before check_nrpe can be used to
monitor the host.

See:

-  `NRPE For Linux <https://docs.nemslinux.com/usage/nrpe_on_linux>`__
-  `NRPE For Windows
   Clients <https://docs.nemslinux.com/usage/nrpe_on_windows>`__

Important Note for Users of NEMS 1.5 and Under
----------------------------------------------

In NEMS Linux 1.5 and lower, an older version of NRPE was used. This can
be upgraded by running *sudo nems-upgrade* however you must also make a
few minor changes in NEMS NConf as follows:

-  Edit *check_nrpe* in *checkcommands*, changing the command line
   to: *$USER1$/check_nrpe -H $HOSTADDRESS$ -c $ARG1$* (essentially,
   just removing the quotation marks).
-  Edit */ Disk Space* and */var Disk Space* in *Advanced Services*,
   changing the ARGS to: *check_disk -a '-w 80 -c 90 -p / -u
   GB'* and *check_disk -a '-w 80 -c 90 -p /var -u GB'* respectively.

Sample Args for check_nrpe
--------------------------

In order to use these commands, NRPE must be installed on the client
system using the NEMS Linux installation procedure found here: `NRPE For
Linux <https://docs.nemslinux.com/usage/nrpe_on_linux>`__

I suggest you always put NRPE in the service titles you create in order
to prevent accidentally assigning a local service to a host who uses
NRPE. So instead of calling the advanced service “Check Disk Space /”
I'd call it “Check Disk Space / via NRPE”.

Check CPU Temperature of Remote System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description:** Detect temperature of remote system CPU.
-  **Client Requirements:** Must have *lm-sensors* installed and
   working.
-  **$ARG1$ Syntax:** check_cpu_temp -a “WARN CRIT”

**$ARG1$ Examples:**

Warn if CPU is hotter than 40°C and Critical if over 50°C:

*check_cpu_temp -a "40 50"*

Warn if CPU is hotter than 35°C and Critical if over 47°C:

*check_cpu_temp -a "35 47"*

Check Disk Usage of Remote System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description:** Determine disk usage by percentage.
-  **Client Requirements:** None.
-  **$ARG1$ Syntax:** check_disk -a “-w WARN -c CRIT -p PATH”

**$ARG1$ Examples:**

Warn if the disk at / is 80% full and Critical if over 90% full and
report in gigabytes:

*check_disk -a '-w 80 -c 90 -p / -u GB'*

Warn if the disk mounted on /var is 80% full and Critical if over 90%
full and report in gigabytes:

*check_disk -a '-w 80 -c 90 -p /var -u GB'*

Warn if the disk mounted on /mnt/backup is 50% full and Critical if over
70% full and report in gigabytes:

*check_disk -a '-w 50 -c 70 -p /mnt/backup -u GB'*