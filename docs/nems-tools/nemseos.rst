nems-tools: NEMS Extender OS
----------------------------

The NEMS Extender OS (NEMSeOS) turns any Raspberry Pi device into a NEMS
GPIO Extender receiver, complete with NEMS Warning Light connectivity.

.. figure:: ../img/nems-extender-os.png
  :width: 600
  :align: center
  :alt: NEMS Extender OS

  Browser view of NEMS Extender OS

With NEMS Extender OS, your NEMS Server is the transmitter, and
the Raspberry Pi running NEMS Extender OS is the receiver. In this
way, you can run your NEMS Server on a different platform, such as
virtual appliance, ODROID-XU4 or PINE64 RockPro64, but then connect
a NEMS Warning Light (or other compatible GPIO devices) to a separate
Raspberry Pi device.

A single NEMS Server can provide data to an unlimited number of NEMS
GPIO Extender receivers. This means, for example, you can place a
NEMS Warning Light in your server room, and one in your office.
You can even place one at home if you're really that committed to
uptime.

NEMS Extender OS will be released at the same time as NEMS Linux 1.6.

Following first boot, a file `nems-tools.conf` will be created in the
/boot partition. If you need to change the configuration, simply shutdown
NEMS Extender OS and plug the card into a computer to edit the file.
