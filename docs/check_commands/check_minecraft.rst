Check Command: check_minecraft
==============================

Check Minecraft server status, including whether up, down or full.
Also reports the server response time in milliseconds.

`check_minecraft` provides the current state of the Minecraft server (Online,
Down or Full), and also provides the following performance data:

- `Online Players` provides the current count of online players, plus the
  server maximum. A warning threshold is automatically set when the server
  reaches 75% of its set limits, and a critical threshold is met when 90%
  of the allowed players are connected.
- `Minecraft Version` informs you of the version of the running Minecraft
  server.
- `Response Time` tells you, in milliseconds, how long the Minecraft server
  is taking to respond.

.. figure:: ../img/ss_check_minecraft_perfdata.png
  :width: 600
  :alt: check_minecraft Service in NEMS Adagios


Need a Minecraft server? Create one for free and host it on a Raspberry Pi!
Download `Pinecraft Installer <https://github.com/Cat5TV/pinecraft/>`__ today!

Command Line
------------

`./check_minecraft -H [host_address] -P [game_port]`
