nems-tools: Warning Light
-------------------------

.. figure:: ../img/warninglight.jpg
   :align: right
   :width: 400px

*Warning Light* is a lightweight daemon running on NEMS Linux
(1.4.1+). It is a different type of notification system exclusive to NEMS
Linux.

NEMS Warning Light: DIY Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the state of your monitored hosts should change, *Warning Light*
could be used to trigger a visual response by way of a tower signal lamp
via GPIO, for example.

#. OK: Solid green light
#. WARNING: Solid orange light
#. UNKNOWN: Flashing orange light
#. CRITICAL: Short siren every 15 minutes, solid red light.

*Warning Light* uses `nems-api`_ to monitor the status of your NEMS
Linux server.

*Warning Light* can be connected directly to a supported NEMS Linux
server, or to a supplemental device
running the `NEMS Extender OS`_ with network access, even through the
Internet.

NEMS Warning Light: Pre-Built Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Omzlo (the makers of the PiVoyager and PiWatcher pHATs) have created
an i2c pHAT that integrates with NEMS Warning Light. Learn more on
`the Omzlo NEMS Warning Light page <../accessories/omzlo-warninglight-phat.html>`__.

System Requirements
~~~~~~~~~~~~~~~~~~~

*Warning Light* can be connected directly to the GPIO of your Raspberry
Pi-based NEMS Linux server. If your NEMS server is a different platform
or GPIO to the server is not convenient, you can connect your *Warning
Light* to a supported device (such as a Raspberry Pi Zero) and install
NEMS Extender OS, which will allow you to add an
unlimited number of GPIO receivers to your NEMS server, regardless of
platform.

Technical Info for Makers
~~~~~~~~~~~~~~~~~~~~~~~~~

GPIO Pin Assignments
''''''''''''''''''''

On any Raspberry Pi NEMS Linux server or NEMS Tools GPIO Extender
receiver, the pinout is as follows:

-  OK state -> Pin 24
-  UNKNOWN or WARN state -> Pin 23
-  CRIT state -> Pin 18

See also, `NEMS Linux: Raspberry Pi GPIO Pinout <../accessories/rpi_pinout.html>`__.

**Please Note:** When the final version is released, it will most likely
use the I2C protocol (unless I decide to create a USB version instead of
GPIO-based). However, these GPIO pins will remain functional in order to
provide an alternate means of connecting for tinkerers.

Pins are LOW (0) by default, and will turn HIGH (1) appropriately in
event of a state change. For example, if your NEMS Linux server is in OK
state, Pin 24 will be HIGH while pins 23 and 18 will be LOW.

The pinout should remain the same, though I may expand it to support a
siren signal or passive alarm buzzer. I'd suggest using these pins to
trip a 5V relay, powering a higher-voltage indicator such as a signal
lamp.

Please share what you create. I'd love to see your designs to make NEMS
Warning Light work in your environment.

.. _nems-api: ../advanced/nems-api.html
.. _NEMS Extender OS: ../nems-tools/extender_os.html

NEMS Tools GPIO Extender
~~~~~~~~~~~~~~~~~~~~~~~~

If your NEMS Linux server is not powered by a Raspberry Pi, or if it is
not located where you'd like your NEMS Warning Light, plugging a NEMS
Warning Light device into the GPIO isn't possible. That's where the NEMS
Tools GPIO Extender comes in.

To use the NEMS Tools GPIO Extender, you'll need any Raspberry Pi to act
as the receiver, but your NEMS Linux server can be any supported
platform, including Virtual Appliance. A Pi Zero WH would do very nicely
for the task. Since the GPIO Extender receiver is separate from your
NEMS Linux server, you can add Raspberry Pi's GPIO to your ODROID-N2
NEMS Server, for example. Or install your NEMS Warning Light on a
ceiling-mounted unit closer to the area where your technicians work,
connected to the GPIO Extender server (your NEMS Linux server) over
wifi. Or install your NEMS Warning Light on the other side of the world:
Since the NEMS Tools GPIO Extender is IP-based, it can be anywhere as
long as it has network access to your NEMS Linux server (TCP port 9595).

To top it off, you can use an *unlimited* number of NEMS Tools GPIO
Extender receivers with a single NEMS Linux Server.

Your NEMS Linux server (1.5+) is already running the NEMS Tools GPIO
Extender server on port 9595.

NEMS Tools GPIO Extender Receiver OS allows you to convert any Raspberry
Pi device into a NEMS Tools GPIO Extender.


NEMS Warning Light: Webhook
~~~~~~~~~~~~~~~~~~~~~~~~~~~

NEMS Warning Light also provides the ability to notify by webhook. See `notify-by-webhook <../notifications/webhook.html>`__ for details.


NEMS Warning Light: Log Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can monitor what is happening with *Warning Light* by tailing the
log file.

::

   tail -f /var/log/nems/nems-tools/warninglight

You can view the current state of NEMS Warning Light:

::

   cat /var/log/nems/nems-tools/currentstate

