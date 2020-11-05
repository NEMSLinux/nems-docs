Monitoring Your Assets
======================

Now that we’ve configured our first host, let’s see how to check its status. There are several ways to keep tabs on your assets with NEMS Linux. For the Nagios purists, Nagios Core is included on the Reporting menu. We’ll instead look at Adagios, found on the same menu. Adagios offers the same overall functionality of Nagios Core’s front-end but replaces it with a modern, responsive web interface.

.. figure:: ../../img/Adagios-interface-on-NEMS-Linux-1.4.1.png
  :width: 600
  :align: center
  :alt: Monitor assets in Adagios

  Adagios interface on NEMS Linux 1.4.1.

To check the status of our hosts, simply click “Hosts” on the navigation to the left.

.. figure:: ../../img/Adagios-hosts-view.png
  :width: 600
  :align: center
  :alt: Adagios hosts view
  
  Adagios hosts view.

You’ll see the host we added--server1 in my example--is showing with the status of UP. This means the ping replied. There is no Service Status, since we did not add any extra service monitors. To see an example of what is possible, expand the NEMS host (which is included on your NEMS Linux server) by clicking the triangle next to its name.

.. figure:: ../../img/Expanded-view-of-Host-reveals-configured-service-checks.png
  :width: 600
  :align: center
  :alt: Expanded Adagios host view
  
  Expanded view of Host reveals configured service checks.

I would also like to encourage you to test both NEMS Mobile UI and NEMS TV Dashboard, both of which are also found on the Reporting menu of the NEMS Dashboard. The first is meant to offer you a complete mobile interface for monitoring your assets, and the latter allows you to set up a TV display in your server room that shows a real-time tactical overview of your NEMS host and service checks.

.. figure:: ../../img/NEMS-TV-Dashboard-on-NEMS-Linux-1.4.1.png
  :width: 600
  :align: center
  :alt: Expanded Adagios host view
  
  NEMS TV Dashboard on NEMS Linux 1.4.1.
