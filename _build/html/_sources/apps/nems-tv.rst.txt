NEMS TV Dashboard
=================

Introduction
------------

NEMS TV Dashboard provides a tactical display specifically designed for
single-screen TV display where a keyboard/mouse are not used. Ideal
as a status monitor in your server room, NEMS
TV Dashboard will report all unacknowledged host and service alerts as
they occur.

Screenshot
~~~~~~~~~~

.. figure:: ../img/tv_dashboard_1.4.1.png
  :width: 600
  :align: center
  :alt: Nems Dashboard Screenshot circa NEMS Linux 1.4.1

Usage
-----

To use NEMS TV Dashboard, simply connect a computer (E.G., Raspberry Pi
Zero) to your TV display and open ``https://nems.local/tv`` in the
browser.

Fullscreen Mode
---------------

Ideally, make NEMS TV Dashboard fullscreen by pressing F11. Press it
again to restore the window.

Security
--------

For convenience and usability, NEMS TV Dashboard does not prompt for
your NEMS username and password by default. If you prefer to keep the
Dashboard private, please open `NEMS
SST <./nems-sst.html#tv-dashboard>`__ and turn off “Allow
TV Dashboard Without Password” - but make sure you have a keyboard
connected to the computer connected to your TV (or something like VNC
access) to login.

Under The Hood
--------------

NEMS TV Dashboard uses the Check_MK Livestatus socket in the back-end,
making it fast, efficient, and lightweight.

Requirements
------------

-  NEMS Linux 1.4.1+
-  A display of some sort, connected to a computer/SBC with Web Browser
   and network connection with access to NEMS server.
-  NEMS TV Dashboard requires a modern web browser to operate. If you
   experience issues, please test in a different browser.
-  NEMS Linux 1.6+ to include Internet speedtest at all times.

Source Code
-----------

`nems-tv on Github <https://github.com/cat5tv/nems-tv>`__ is based on
*merlin-dashboard* by fnordpojk. Licensed under
`GPL v3 <https://www.gnu.org/licenses/gpl-3.0.en.html>`__.
