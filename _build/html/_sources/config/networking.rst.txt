.. include:: ../global.rst

Network Configuration
=====================

NEMS Linux requires an Internet connection to obtain updates and
patches,
to tap into `NEMS Cloud Services <../nems-cloud-services/index.html>`__ features such as `NEMS CheckIn <../nems-cloud-services/checkin.html>`__, `NEMS
Migrator Off-Site Backup <../nems-cloud-services/nems-migrator.html>`__, and `NEMS Anonymous Stats <../misc/anonymousstats.html>`__, and to `send
notifications <../notifications/index.html>`__.

**You cannot use NEMS Linux without an Internet connection.**

.. admonition:: Security Notice
  :class: warning

  NEMS Linux is intended to be accessible only to your trusted admin
  team. :underline:`Never` open ports to the world. Rather, specifically allow
  your admin IP address(es) access to the needed resources, or use
  a VPN.

Firewall Ports
--------------

To allow you/others to access your NEMS Server from outside your LAN,
you will require the following ports be opened to your NEMS Server:

-  **SSH Access:** `22 TCP In`
-  **NEMS Dashboard Web Interface / nems-api:**
   `80, 443 TCP In`
-  **NEMS Tools GPIO Extender:** `9595 TCP In`
-  **Monit Service Monitor Web Access:** `2812 TCP In`
-  **Cockpit Admin Interface:** `9090 TCP In`
-  **AVAHI / mDNS Name Resolution:** `548, 5353, 5354 TCP In/Out`

Most standard network configurations allow servers to
communicate with the outside world without any additional setup.
However, if you have a very restrictive firewall configuration, you may
need to open additional ports for your NEMS Server to be able to
communicate with systems it is monitoring, as well as the NEMS Update
servers.

-  **NEMS Update:** 80, 443, 9418 TCP Out
-  **NRPE Check Commands:** 5666, 12489 TCP Out
-  **WMI Check Commands:** 135, 445, 1024-1034 Out

You must also ensure your NEMS Server is allowed to communicate with the
following TLDs:

-  \*.nemslinux.com
-  \*.github.com

How to Configure Networking on NEMS Linux
-----------------------------------------

NEMS Linux includes the `Cockpit <../apps/cockpit.html>`__ administrative
front-end. With some exceptions (listed below)
you will only use this interface to configure your networking on a
NEMS Linux server.

Setting up your networking by any other means (E.G., a general Linux
networking tutorial, modifying system files, or using third-party tools)
may result in your NEMS Server's network stack being broken, and so
is strongly discouraged. Should you ignore this warning and break your
NEMS Server, re-flash NEMS Linux and import your
`NEMS Migrator Backup <../apps/nems-migrator.html>`__ to recover.

Docker / Amazon Web Services
----------------------------

Network setup for NEMS Linux on Docker and Amazon Web Services is
administered from the host, not the appliance. In these environments,
Cockpit is not used to configure the network, and you must familiarize
yourself with the host platform's configuration options.

-  **Docker:** You must assign the IP upon launching the container.
   See `Docker documentation <https://docs.docker.com/engine/reference/run/#network-settings>`__.
-  **Amazon Web Services:** You must assign an Elastic IP to your NEMS Linux
   instance.
   See `Amazon Web Services documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__.

Important Notes
---------------

1. When logging in to Cockpit, make sure you check the box “Reuse my
   password for privileged tasks” otherwise none of these options will
   be available to you. See `here <../apps/cockpit.html>`__.
2. You'll find Cockpit in the System menu of your NEMS Dashboard. For
   more details about Cockpit, `read the
   documentation <../apps/cockpit.html>`__.
3. Network configuration does not persist from board to board: if you
   configure NEMS on one device and then move its storage (E.G., SD card)
   to a different device, the new device will revert to the default
   setting of DHCP.

Network Interfaces
------------------

NEMS Linux will enable any connected Interface it detects on boot.

Ethernet Interface
~~~~~~~~~~~~~~~~~~

Recommended. Simply plug in the cable.

Wireless Network Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

Because of the very nature of NEMS, the possible reliability issues
on WiFi, and the fact that a WiFi connection will likely result in false
notifications, it is :underline:`not recommended` to run your NEMS server
on a WiFi connection. However, this may be the only option in some
environments, and so great effort has gone into ensuring it will work
as well as possible.

Examples where NEMS Linux will be hindered by a WiFi connection:

-  User has Gigabit Internet. WiFi connection is 54 Mb/sec. User wants a
   notification if the Internet ever drops below 200 Mb/sec, but this is
   impossible since the WiFi connection is *always* below 200 Mb/sec.
-  While perhaps untrue for the average home user, an enterprise WiFi
   connection, if configured securely, should never have access to particular
   resources on the network. For example, at the Category5 TV studio,
   WiFi can access the Internet, but not the server. Therefore a NEMS
   Server in this environment would not be able to monitor items such as
   server disk space.
-  User's WiFi occasionally drops connection, which could result in false
   notifications that the Internet is down, or cause
   `NEMS CheckIn <../nems-cloud-services/checkin.html>`__ to lose
   contact with the NEMS Server, resulting in yet more false notifications.

.. Warning:: **Raspberry Pi users:** :underline:`Do not` use `raspi-config` for your WiFi.

**Enable the WiFi Radio in NEMS Linux**

In order to be able to activate/deactivate your WiFi connection in
Cockpit, you must first add the connection information to your NEMS
Linux server using the terminal. If you do not, you'll receive an error
“A 'wireless' setting is required if no AP path was given.” when trying
to activate WiFi.

Determine if your WiFi radio is enabled or disabled:

.. code-block:: console

   sudo nmcli radio wifi

If it is disabled, enable it:

.. code-block:: console

   sudo nmcli radio wifi on

Scan for available wireless networks:

.. code-block:: console

   sudo nmcli device wifi list

Determine which is the one you wish to connect to and enter the
following command:

.. code-block:: console

   nmcli device wifi connect [SSID] password [password]

Eg., if your network SSID is MyWiFi and your WiFi password is MyPass123,
the command would look like this:

.. code-block:: console

   nmcli device wifi connect MyWiFi password MyPass123

Now, you can enable or disable your wireless connection within
Cockpit→Networking.

IP Address/DNS Settings
-----------------------

DHCP Assigned IP Address
~~~~~~~~~~~~~~~~~~~~~~~~

By default, NEMS Linux will obtain its network settings from your DHCP
server. For this reason, a quick and easy way to set a static IP on your
NEMS server would be to add it as a DHCP reservation within your
router/DHCP server. To find out what IP address your NEMS server resides
on, either check your DHCP pool, or connect a TV to your NEMS server.
You can also try accessing it
at ``https://nems.local`` from another computer on the same network and
then open `NEMS Server Overview <../apps/serveroverview.html>`__ to see
your IP.

Static IP Address
~~~~~~~~~~~~~~~~~

If your NEMS server is already initialized, it is recommended that you
copy `your backup.nems <../apps/nems-migrator.html>`__ to a different
system prior to setting a static
IP address. This gives you an easy way to recover should you
accidentally lock yourself out of your NEMS server by breaking the
network configuration.

When setting a static IP address, it is important to make sure it is
outside your DHCP pool. Otherwise, some routers/DHCP servers may assign
the IP to a second device, causing all kinds of unforeseen issues.

**Set a static IP Address in NEMS Linux**

1.  Open `Cockpit <../apps/cockpit.html>`__.
2.  Login. Use the default credentials if you have not initialized NEMS,
    or your created credentials if you have. Check the box “Reuse my
    password for privileged tasks” while signing in.
3.  Click “Networking”.
4.  Click the network interface (E.G., eth0).
5.  Ensure “Connect automatically” is checked.
6.  Click the “Automatic (DHCP)” or IP address currently assigned to
    this NIC next to IPv4.
7.  Ensure “Manual” is selected in the dropdown.
8.  Add your new IP settings.
9.  Make sure you click the + next to DNS settings and assign at least
    one DNS server. 8.8.8.8 (Google) or 1.1.1.1 (Cloudflare) will do.
10. Press “Apply” and wait for it to test the connection.
11. Click “Change the setting” after the test is complete.
12. You should now open your NEMS Dasboard at the new IP address. Within
    a few moments, the old one will stop working.
