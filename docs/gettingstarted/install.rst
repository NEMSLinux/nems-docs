Install NEMS Linux
==================

All that is required in order to deploy NEMS Linux is a compatible device and media, such as a microSD card or eMMC, depending on the platform. Please check the NEMS website to see which boards are supported.

Download the latest version of NEMS Linux from https://nemslinux.com and “burn” it using your favorite tool. I’ve really come to prefer `BalenaEtcher <https://balena.io/etcher/>`_ but you can use whatever tool you like best. If you're using a microSD card, please use a UHS-I or better card. I recommend 16GB or more, but you could get away with 8GB if that’s all you have handy. You can always use NEMS Migrator to move to a bigger card down the road.

Upon booting your NEMS Linux server, your filesystem will be automatically resized to the capacity of your storage. You can confirm NEMS is up and running by visiting https://nems.local/ in your web browser. If name resolution doesn’t work, try the IP address of your NEMS device instead, which you can find in your router’s DHCP leases table, or on a TV connected to your NEMS Server's HDMI port.


.. figure:: ../../img/NEMS-details-displayed-on-a-connected-TV.png
  :width: 600
  :align: center
  :alt: NEMS Server details

  NEMS Server details as shown on a connected TV circa September 2018.
