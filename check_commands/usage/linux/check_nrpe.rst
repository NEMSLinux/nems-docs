Monitor Linux Hosts with NRPE
=============================

.. Warning:: These instructions are for your Linux *client*. **NEVER**
  run these commands on your NEMS Server.

The Nagios Remote Plugin Executor (NRPE) allows your Nagios Enterprise
Monitoring Server to communicate with the Linux machines on your server
to determine things like free disk space, CPU load, and detect possible
issues that a simple ping can't determine.

There are countless instructions online to download tar.gz files and
install manually, or use a PPA to install via apt-get, but NEMS includes
a helpful installer that will configure everything for you.

.. Warning:: Do not install the NRPE plugin via software repositories as
  these are abandoned and lack some important functionality.

To install the needed NRPE client on Debian / Ubuntu / other
Debian-based Linux operating systems (as root):

.. code:: bash

   wget -O - https://raw.githubusercontent.com/Cat5TV/nems-admin/master/build/047-nrpe | bash

**Please note:** Rudimentary support for RPM-based distros is included,
but may not work. Please consider RPM support as experimental, and
report your findings (especially your solutions or pull requests) so I
can improve it.

Next, we just have to tell NRPE that it's allowed to communicate with
our Nagios server. On the client system, open the file
*/usr/local/nagios/etc/nrpe.cfg*

Find the line that reads: ``allowed_hosts=127.0.0.1,::1``

Now there are a few ways we can allow our server. First (and most
obvious) is to add its IP address like this:

::

   allowed_hosts=127.0.0.1,::1,192.168.0.5

Where 192.168.0.5 is our Nagios/NEMS server.

Alternatively we can tell NRPE that it's allowed to communicate with any
local system:

::

   allowed_hosts=127.0.0.1,::1,192.168.0.0/24

Now, save the file and restart NRPE as follows:

.. code:: bash

   systemctl restart nrpe

.. Tip:: If you have a software firewall running on
  your Linux machine, setup an exception for your NEMS server IP to gain
  access through TCP ports 5666 and 12489.

And there we have it! Your NEMS Server can now check your Linux machine
at a deeper level using `check_nrpe <../../check_nrpe.html>`__.
