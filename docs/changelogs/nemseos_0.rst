NEMSeOS 0 Changelogs
====================

**December 1, 2020** - NEMSeOS 0.1 alpha Build 1.

Features:

  - If no configuration found, auto-detect running NEMS Server
    | on same subnet when network connection is extablished.
  - Ability to extend all GPIO pins hi/low value from running
    | NEMS Server.
  - At release time, NEMS Warning Light GPIO pins, plus Omzlo
    | Warning Light pHAT are supported.
  - Accessing IP address of NEMSeOS in browser will show state,
    | including an interval provided by the NEMS Server which
    | counts up with each iteration. This makes it easy to see
    | if your NEMS GPIO Extender has stopped transmitting or
    | receiving (as the counter would stop).
  - Basic error handling included to show in browser if a
    | connection cannot be established.
  - Manually editing the ``nems-tools.conf`` file from any
    | Linux machine is possible by mounting the SD card's
    | *boot* partition.
  - Editing your config file manually allows you to connect
    | to a NEMS Server on a different network, even WAN (Internet).
  - NEMSeOS 0.1 alpha contains Cockpit running on port 9090 and
    | accessible from within your browser. Username/Password are
    | pi/raspberry. This is only included during alpha/beta testing
    | and will later be removed once the system is stable and can be
    | run fully as an appliance. Cockpit can be used for now to
    | login to the device's terminal, or safely shut down the NEMSeOS
    | device.

Changelogs since Build 1

-  Add i2c support to enable access to Omzlo Warning Light pHAT.
