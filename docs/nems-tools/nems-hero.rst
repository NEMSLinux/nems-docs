nems-tools: NEMS Hero
---------------------

In the event of a catastrophic issue, such as a corrupt NEMS user or
forgotten password, NEMS Linux technical support may use NEMS Hero to
recover your NEMS Server, or to provide technical assistance.

NEMS Hero grants temporary root access to a NEMS Server which has been
freshly rebooted, and only if the NEMS Server is accessible (via a LAN
or WAN connection).

NEMS Hero Security
~~~~~~~~~~~~~~~~~~

NEMS Hero uses an RSA key pair to establish an SSH trust relationship
between a NEMS Server and the NEMS Linux technical support team. This
trust relationship self destructs once a NEMS Server has been running
for more than 15 minutes.

In order for a connection to be established, the following conditions
must be met:

#. port forwarding must be setup on the network of the NEMS Server to
   allow a support technician remote SSH access to port 22 on the NEMS
   Server,
#. the NEMS Server must have been rebooted within the past 15 minutes,
#. the NEMS Server must not have a ``/boot/no-hero`` file in place,
#. the NEMS Linux technical support representative must have our
   private RSA key,
#. the NEMS Linux technical support representative must know our
   strong password to access the private RSA key.

.. Tip:: If desired, this functionality can be disabled on a
         self-hosted NEMS Server by creating a file ``/boot/no-hero``
         on your NEMS Server. Because the ``/boot`` partition can be
         viewed and modified by plugging your NEMS Server's storage into
         a Windows, macOS or Linux computer, you can easily delete that
         file later and reboot your NEMS Server to re-enable NEMS Hero.

System Requirements
~~~~~~~~~~~~~~~~~~~

NEMS Hero requires NEMS Linux 1.6 or higher.
