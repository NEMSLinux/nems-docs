Initialization
==============

Generally speaking, the only time you’ll really have to touch the Linux terminal on a NEMS server is during the initialization procedure. This task works magic in automatically configuring your entire server in just a few seconds. It generates self-signed certificates so every NEMS Linux user has a unique certificate, allows you to configure your timezone, creates your Nagios admin user, your Linux account, and so on. To initialize your NEMS Linux server, connect to your server over SSH on the default Port 22 using the following credentials:

.. code-block:: console

    Username: nemsadmin
    Password: nemsadmin
    
Once connected, type:

.. code-block:: console

    sudo nems-init

You’ll be asked to enter the password again. Follow the prompts. All the complicated stuff is made easy.

.. figure:: ../../img/NEMS-Initialization.png
  :width: 600
  :align: center
  :alt: NEMS Initialization screen

  NEMS Initilization screen.
  
Congratulations! Your NEMS Linux server is now online and ready to monitor your network assets.
