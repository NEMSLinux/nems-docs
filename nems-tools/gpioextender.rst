nems-tools: GPIO Extender
-------------------------

If your NEMS Linux server is not powered by a Raspberry Pi, or if it is
not located where you'd like your NEMS Warning Light, plugging a NEMS
Warning Light device into the GPIO isn't possible. That's where the NEMS
Tools GPIO Extender comes in.

To use the NEMS Tools GPIO Extender, you'll need any Raspberry Pi to act
as the receiver, but your NEMS Linux server can be any supported
platform, including Virtual Appliance. A Pi Zero WH would do very nicely
for the task. Since the GPIO Extender receiver is separate from your
NEMS Linux server, you can add Raspberry Pi's GPIO to your ODROID-N2
NEMS Server, for example. Or install your NEMS Warning Light on a
ceiling-mounted unit closer to the area where your technicians work,
connected to the GPIO Extender server (your NEMS Linux server) over
wifi. Or install your NEMS Warning Light on the other side of the world:
Since the NEMS Tools GPIO Extender is IP-based, it can be anywhere as
long as it has network access to your NEMS Linux server (TCP port 9595).

To top it off, you can use an *unlimited* number of NEMS
Tools GPIO Extender receivers with a single NEMS Linux Server.

NEMS Linux 1.5+ has the NEMS Tools GPIO Extender server running on
port 9595.

To connect to the NEMS Linux GPIO Extender, simply boot up a separate
device running `NEMS Extender OS <extender_os.html>`__.
