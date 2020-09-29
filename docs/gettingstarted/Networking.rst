Networking
==========

NEMS requires an Internet connection to obtain updates and patches, and
to tap into NEMS Cloud Services features such as NEMS Check In, NEMS
Migrator Off-Site Backup, and NEMS Anonymous Stats.

Firewall Ports
--------------

To allow you/others to access your NEMS Server, you will require the
following ports be opened to your NEMS Server:

-  **SSH Access:** 22 TCP In
-  **NEMS Dashboard Web Interface:** 80, 443 TCP In
-  **Monit Service Monitor Web Access:** 2812 TCP In
-  **Cockpit Admin Interface:** 9090 TCP In
-  **AVAHI / mDNS Name Resolution:** 548, 5353, 5354 TCP In/Out

Most standard network configurations allow running servers to
communicate with the outside world without any additional setup.
However, if you have a very restrictive firewall configuration, you may
need to open additional ports for your NEMS Server to be able to
communicate with systems it is monitoring, as well as the NEMS Update
servers.

-  **NEMS Update:** 80, 443, 9418 TCP Out
-  **NRPE Check Commands:** 5666, 12489 TCP Out
-  **WMI Check Commands:** 135, 445, 1024-1034 Out

Docker / Amazon Web Services
----------------------------

The Networking features in Cockpit have been removed from NEMS Linux for
Docker and Amazon Web Services. This is because on these platforms, you
should administer your networking from the host, not the appliance.

-  Docker: You must assign the IP upon launching the container.
   See https://docs.docker.com/engine/reference/run/#network-settings
-  Amazon Web Services: You must assign an Elastic IP to your NEMS Linux
   instance.
   See https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html

Important Notes
---------------

1. When logging in to Cockpit, make sure you check the box “Reuse my
   password for privileged tasks” otherwise none of these options will
   be available to you.
2. You'll find Cockpit in the System menu of your NEMS Dashboard. For
   more details about Cockpit, read the
   documentation: `Cockpit <https://docs.nemslinux.com/features/cockpit>`__
3. Network configuration does not persist from board to board: if you
   configure NEMS on one device and then move its storage (ie., SD card)
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

Because of the very nature of NEMS and the possible reliability issues
on WiFi, it is not recommended to run your NEMS server on a WiFi
connection. However, this may be the only option in some environments,
and so great effort has gone into ensuring it will work as well as
possible.

**Raspberry Pi users:** *Do not* use raspi-config for your WiFi.

In order to be able to activate/deactivate your WiFi connection in
Cockpit, you must first add the connection information to your NEMS
Linux server using the terminal. If you do not, you'll receive an error
“A 'wireless' setting is required if no AP path was given.” when trying
to activate WiFi.

Determine if your WiFi radio is enabled or disabled:

sudo nmcli radio wifi

If it is disabled, enable it:

sudo nmcli radio wifi on

Scan for available wireless networks:

sudo nmcli device wifi list

Determine which is the one you wish to connect to and enter the
following command:

nmcli device wifi connect [SSID] password [password]

Eg., if your network SSID is MyWiFi and your WiFi password is MyPass123,
the command would look like this:

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
at `https://nems.local <https://nems.local/>`__ from another computer on
the same network.

Static IP Address
~~~~~~~~~~~~~~~~~

If your NEMS server is already initialized, it is recommended that you
copy your *backup.nems* to a different system prior to setting a static
IP address. This simply gives you an easy way to recover should you
accidentally lock yourself out of your NEMS server by breaking the
network configuration.

When setting a static IP address, it is important to make sure it is
outside your DHCP pool. Otherwise, some routers/DHCP servers may assign
the IP to a second device, causing all kinds of unforeseen issues.

**Set a static IP Address in NEMS Linux**

1.  Open Cockpit.
2.  Login. Use the default credentials if you have not initialized NEMS,
    or your created credentials if you have. Check the box “Reuse my
    password for privileged tasks”.
3.  Click “Networking”.
4.  Click the network interface (eg., eth0).
5.  Ensure “Connect automatically” is checked.
6.  Click the “Automatic (DHCP)” or IP address currently assigned to
    this NIC next to IPv4.
7.  Ensure “Manual” is selected in the dropdown.
8.  Add your new IP settings.
9.  Make sure you click the + next to  settings and assign at least
    one  server. 8.8.8.8 will do.
10. Press “Apply” and wait for it to test the connection.
11. Click “Change the setting” after the test is complete.
12. You should now open your NEMS Dasboard at the new IP address. Within
    a few moments, the old one will stop working.