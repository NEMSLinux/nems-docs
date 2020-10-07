Frequently Asked Questions
==========================

My browser warns, "Your connection is not secure". Why?
-------------------------------------------------------

NEMS Linux uses SSL (aka https) connections to secure your connection
and the data you transmit and receive to and from your NEMS server. This
is accomplished using what is called a *self-signed certificate*. By
nature, self-signed certificates are considered “untrusted” by your
browser because, simply put, anyone can make them. It does not mean your
connection is not encrypted or secure, but rather it means your browser
cannot determine who created the certificate, and therefore they cannot
verify your security. If you visited a web site, say *google.com* and
received a warning that your connection is not secure, you should
immediately stop what you're doing and not proceed. However, in the case
of NEMS Linux, which is a local server on your network (not a “dot com”
on the web), you can safely trust the self-signed certificates and add
an exception to your browser.

How do I configure WiFi?
------------------------

-  See the Wireless Network Interfaces section of the `Networking
   documentation <https://docs.nemslinux.com/networking#wireless_network_interface>`__.

How do I set a static IP address?
---------------------------------

-  See the IP Address/ Settings section of the `Networking
   documentation <https://docs.nemslinux.com/networking#ip_addressdns_settings>`__.

Why does Cockpit have greyed-out features? I can't change anything!
-------------------------------------------------------------------

-  As per `the Cockpit
   docs <https://docs2.nemslinux.com/en/latest/apps/cockpit.html>`__: make sure you
   also check the box “use my password for privileged tasks” while
   logging in. Otherwise your level of access will match the
   non-elevated user and all features which require root access will be
   greyed out.

Why does NEMS Linux "call home" so much?
----------------------------------------

If you're running a custom  server or monitoring  lookups, you'll see a
lot of requests for nemslinux.com. If you've enabled NEMS Check-In, NEMS
will do a  lookup for nemslinux.com every 5 minutes. That's 288 requests
per day. Then, there is the *nems-info online* command, which pings
nemslinux.com to simply determine if you have an Internet connection.
This is required every time NEMS Linux runs a command that requires
Internet connectivity. It checks for that connection first, and if
successful, it resumes. Else, it does not go through with the command
since no Internet connection is detected. This is probably where you're
seeing the most lookups. Then, there's  requests, such as when it checks
to see if you are authenticated with the NEMS Cloud Services server,
which will occur at various times depending on what checks are occurring
and what you are doing (eg., if you open NEMS SST, it will immediately
check). Another one is that you may or may not have a sample check
command which pings nemslinux.com to see if it is up or down. You can
remove that check if it exists using NEMS NConf.

Why is NEMS using so much bandwidth?
------------------------------------

NEMS Linux includes a small handful of sample check commands, and one of
those is an Internet Speedtest which uses Ookla's Speedtest service to
monitor and report your Internet speed. For more information, please
read `Check Command:
check_internet_speed <https://docs.nemslinux.com/check_commands/check_internet_speed>`__.
