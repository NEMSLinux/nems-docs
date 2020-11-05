Cockpit
=======

NEMS Linux includes `Cockpit from Red Hat <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/getting_started_with_cockpit/index>`__. In its NEMS implementation, Cockpit provides browser-based SSH access, some realtime performance graphs, and basic system administration tools such as the ability to reboot or safely shutdown your NEMS server.

.. figure:: ../../img/Cockpit-terminal.png
  :width: 600
  :align: center
  :alt: Cockpit Terminal

  Cockpit allows terminal access and other system-level tools within a browser session.
  
Login to Cockpit
----------------

You'll find Cockpit in the System menu on NEMS Dashboard. To login, enter your NEMS Linux username and password.

.. tip:: **Seeing Disabled Features in Cockpit?** If you wish to be able to perform elevated system actions (such as rebooting your NEMS Server or modifying your NEMS Server's network connection), make sure you also check the box “use my password for privileged tasks” while logging in. Otherwise your level of access will match the non-elevated user and all features which require root access will be greyed out.
