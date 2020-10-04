Omzlo PiWatcher Smart Watchdog for Raspberry Pi
===============================================

The `Omzlo PiWatcher <https://cat5.tv/piwatcher>`__ is a very
small hat for Raspberry Pi that allows programmable power events to take
place.

NEMS Linux includes built-in support for the PiWatcher board. There is
no configuration needed: Simply plug it in and boot up your NEMS Linux
server. If your Raspberry Pi should become unresponsive or otherwise
freeze up, your NEMS server will automatically power cycle after 2
minutes.

To confirm your PiWatcher devices is detected and active, visit NEMS
Server Overview on your NEMS Dashboard.

To test if your piWatcher is working, stop the heartbeat and wait 2
minutes:

.. code-block:: console

    sudo kill -9 $(cat /var/run/nems-piwatcher.pid)

This should not be done on a production server (it is akin to pulling
the power on a live system).

.. figure:: ../../img/piwatcher.png
  :width: 300
  :align: center
  :alt: PiWatcher

Omzlo PiWatcher
