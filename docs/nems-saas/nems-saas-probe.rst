NEMS SaaS Probe
===============

Introduction
^^^^^^^^^^^^

The NEMS SaaS Probe is a small daemon which runs on your endpoints, collecting performance data about the endpoint. This data is then sent to NEMS SaaS, where it is aggregated and provided to your account for reporting and alerting.

The NEMS SaaS Probe is a benign application which gathers non-identifying information such as CPU load, disk space usage, and so-on.

The NEMS SaaS Probe is designed to be easy to deploy, with no firewall rules to create and no check commands to configure.

Its source code is available for your review at https://github.com/NEMSLinux/nems-saas-probe/blob/main/src/nems-saas-probe

Security
^^^^^^^^

NEMS SaaS Probe sends your data packet to the NEMS SaaS servers via an encrypted connection, which is authenticated to your account with your NEMS SaaS Key.

The NEMS SaaS built-in JSON web server provides JSON responses only when the correct NEMS SaaS Key is provided as POST data. This server is intended for LAN or VPN use. If (and only if) absolutely necessary, please consider opening port ``6367`` only to the IP addresses you will be running your application on. While unlikely, it should be noted that a MITM attack could steal your NEMS SaaS Key if you connect to port 6367 successfully from an Internet location (as opposed to LAN or VPN). Do not open port 6367 to the world.

Built-In Web Server
^^^^^^^^^^^^^^^^^^^

As of version 1.0.050, the NEMS SaaS Probe is able to serve JSON responses containing the data packet. The server is running by default on port ``6367``.

This is provided as a helpful feature to developers and power users, but is a requirement of using NEMS SaaS. You do not need to configure your firewall to use this server if you are not a developer tapping into the JSON data, and an in-house NEMS Server (on the same LAN) can use this data to monitor your endpoints in-house.

You may optionally parse this data in your own app, or create a NEMS Linux check command to query this data.

In addition to the standard data packet, there are two other defined keys:

**packet**

Packet will be ``0`` or ``1``. 0 means the packet has not succeeded in sending to NEMS SaaS. 1 means the packet was successfully sent to NEMS SaaS. For more details on why a packet has not been sent, check your nems-saas.log on the system running the NEMS SaaS Probe.

**timer**

Timer is the value, in seconds, of how long the NEMS SaaS Probe is waiting before it sends the next packet to the NEMS SaaS servers. This number is dynamic and changes with each packet. It can be used to set a sleep timer on your own queries to the probe. There is no point in quering the probe again sooner since the probe will not have any new information to report (the packet will be the same).

Disable
-------

Turn off the built-in web server with the ``--noserver`` command line argument.

Query Example
-------------

Your query must contain a POST containing only your account's NEMS SaaS Key (found in your user settings when logged into NEMS SaaS).

``curl --http0.9 -d "00000000-0000-0000-0000-00000000" -X POST http://192.168.0.5:6367``

Replace ``00000000-0000-0000-0000-00000000`` with your actual NEMS SaaS Key.

Replace ``192.168.0.5`` with the actual IP of the system running the probe.
