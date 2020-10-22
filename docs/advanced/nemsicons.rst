Copying OS icons to NEMS
========================
To add additional or custom OS icons to NEMS, perform the following:

From a file browser window, open the Home share on the NEMS server (i.e. \\nems_ip\Home) and log in with your NEMS credentials.

.. figure:: ../../img/icons_02.PNG
  :width: 600
  :align: center

Create a folder.  In this example, it is "icons"

.. figure:: ../../img/icons_03.PNG
  :width: 600
  :align: center
  
Start an SSH session to the NEMS server and login.  The "icons" folder is displayed when ls is ran.
Copy the icon images into this new folder.

.. figure:: ../../img/icons_05.PNG
  :width: 600
  :align: center

"cd" into the "icons" folder and run ls to verify the icon files are there.
Copy the icon images into this new folder.

.. figure:: ../../img/icons_06.PNG
  :width: 600
  :align: center

The icon file can be copied or moved into the /var/www/nconf/img/logos/base folder.
-To copy "sudo cp *.* /var/www/nconf/img/logos/base"
-To move "sudo mv *.* /var/www/nconf/img/logos/base"

.. figure:: ../../img/icons_07.PNG
  :width: 600
  :align: center

Login the nconf for NEMS.
In this example, the icon for "switch" will be changed.

.. figure:: ../../img/icons_09.PNG
  :width: 600
  :align: center

Click on Show for OS, then click on edit (pencil icon) for the OS to be modified.

.. figure:: ../../img/icons_10.PNG
  :width: 600
  :align: center

Edit the gif name to the new icon name and click submit.

.. figure:: ../../img/icons_11.PNG
  :width: 600
  :align: center

.. figure:: ../../img/icons_12.PNG
  :width: 600
  :align: center

Go back to Hosts and verify the icon has changed.

.. figure:: ../../img/icons_13.PNG
  :width: 600
  :align: center


Nagios icon packs
https://exchange.nagios.org/directory/Graphics-and-Logos/Images-and-Logos