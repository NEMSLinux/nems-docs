Monitor Windows Machines with Ping
==================================

The simplest type of check in NEMS Linux is to ping a host. The reply is
binary: Host is up when ping replies, host is down when ping does not
reply.

**Using a ping check is an excellent starting point for new NEMS Linux
users to become familiar with an easy-to-administer check command.**

To begin pinging a Windows host, simply add it to the windows-servers
group. The host check alive command will use check_ping to verify it as
online or offline.

Most software firewalls, including the Windows [Defender] Firewall,
block ping (ICMP) requests by default. So NEMS will think your host is
down unless you create a rule to allow ICMP echo requests and replies
through your Windows firewall.

Windows Defender Firewall
-------------------------

To enable ICMP response when using Windows Defender Firewall, simply run
the Command Prompt as Administrator and type the following:

IPv4 Networks:

.. code-block:: console

   netsh advfirewall firewall add rule name="ICMP Allow incoming V4 echo
   request" protocol=icmpv4:8,any **dir**\ =in action=allow

IPv6 Networks:

.. code-block:: console

   netsh advfirewall firewall add rule name="ICMP Allow incoming V6 echo
   request" protocol=icmpv6:8,any **dir**\ =in action=allow

Third Party Firewall
--------------------

If you are using a different firewall (eg., ESET Endpoint Security) you
will need to consult that software's documentation to allow ICMP echo
responses.

Here are some things to look for:

-  Many firewalls can exempt certain IP addresses or ranges from being
   blocked. This is often called a Trusted Zone, or whitelisted IP. You
   could add your NEMS Server as a trusted device. If you do this, make
   absolutely certain your NEMS Server is not accessible from the world
   (ie., do not port forward anything to NEMS Linux), and your NEMS user
   password is a strong one that only you know.
-  Most firewalls allow exemption of certain protocols or services. In
   those cases, you can simply enable/allow ping replies. It may be
   called “ping”, “incoming ping”, “ICMP Echo Reply”, or similar.

.. Warning:: **DO NOT SIMPLY DISABLE YOUR FIREWALL.** Correctly establish a firewall rule within your firewall application.
