Install NEMS Linux on an Indiedroid Nova
========================================

What You Need
-------------

* Indiedroid Nova SBC
* 16 GB or higher fast MicroSD card
* A reliable, high-quality power supply for your Nova, preferably connected to a UPS
* An Ethernet cable

Video Demonstration
-------------------

While this video was created for the Raspberry Pi version, it is exactly the same process for Indiedroid Nova (just use the correct download for the Indiedroid Nova).

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/k9n9j6-GxTg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Instructions
------------

Install NEMS Linux to MicroSD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Download the latest version of NEMS Linux from https://nemslinux.com/
* Install the Raspberry Pi Imager from https://www.raspberrypi.com/software/
* Click "Choose OS"
* Click "Choose Custom" at the bottom of the list
* Browse to your downloaded copy of NEMS Linux
* Click "Choose Storage"
* Insert your MicroSD card or USB Flash Drive
* Carefully select your MicroSD card or USB Flash Drive
* Click "Write"

First Boot
~~~~~~~~~~

* Connect the MicroSD card or USB Flash Drive containing NEMS Linux to your Indiedroid Nova
* Connect the gigabit Ethernet port of the Indiedroid Nova to your network using an Ethernet cable
* Power on the Indiedroid Nova to boot your NEMS Server
* Wait approximately 5 minutes to perform first-boot operations

During the first-boot operation, the filesystem will be automatically resized to the capacity of your storage and the NEMS Server will reboot.

After the first-boot operations have completed, visit https://nems.local/ in your web browser. If name resolution doesn’t work, try the IP address of your NEMS device instead, which you can find in your router's DHCP leases table, or on a TV connected to your NEMS Server's HDMI port.

.. figure:: ../img/NEMS-details-displayed-on-a-connected-TV.png
  :width: 600
  :align: center
  :alt: NEMS Server details

  NEMS Server details as shown on a connected TV circa September 2018.
  
  Install to eMMC
  ~~~~~~~~~~~~~~~
  
  Now that you are booted into your NEMS Server via the MicroSD card, you may choose to utilize the Indiedroid Nova's built-in eMMC storage (more reliable, faster).
  
  * Open the browser-based terminal in Cockpit or SSH to your NEMS Server.
  * Type `sudo nems-install` and follow the prompts.
