nems-tools: NEMS Hero
---------------------

In the event of a catastrophic issue, such as a corrupt NEMS user or
forgotten password, NEMS Linux technical support may use NEMS Hero to
recover your NEMS Server, or to provide technical support.

NEMS Hero grants temporary root access to a NEMS Server which has been
freshly rebooted, and only if the NEMS Server is accessible (via a LAN
or WAN connection).

NEMS Hero uses an RSA key pair to establish an SSH trust relationship
between a NEMS Server and the NEMS Linux technical support team. This
trust relationship self destructs once a NEMS Server has been running
for more than 15 minutes. In order for a connection to be established,
port forwarding must be setup on the network of the NEMS Server to
allow a support technician remote SSH access to port 22 on the NEMS
Server.

.. Tip:: If desired, this functionality can be disabled on a
         self-hosted NEMS Server by creating a file ``/boot/no-hero``
         on your NEMS Server. Because the ``/boot`` partition can be
         viewed by plugging your NEMS Server's storage into a Windows,
         macOS or Linux computer, you can easily delete that file later
         and reboot your NEMS Server to re-enable NEMS Hero.

NEMS Hero is a feature of NEMS Linux 1.6+.
