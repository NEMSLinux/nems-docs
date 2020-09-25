NEMS CheckIn
============

NEMS CheckIn is a feature of NEMS Linux designed to address concerns that if a NEMS Server was to go offline, the admin would stop receiving notifications and may not realize this for some time. In early versions of NEMS Linux, this led to some users setting up multiple NEMS Servers--NEMS Servers to monitor NEMS Servers.

NEMS CheckIn is the answer to this. If enabled, NEMS CheckIn will simply send a ping to the NEMS Cloud Services server every 15 minutes.

NEMS CheckIn can be enabled within NEMS System Settings Tool under NEMS Cloud Services. It is disabled by default.

.. figure:: ../../img/NEMS-SST-CheckIn.png
  :width: 600
  :align: center
  :alt: NEMS CheckIn Settings in NEMS SST

  Configuring NEMS CheckIn in NEMS SST is a breeze

Should the server not hear from your NEMS Linux server within a set time frame, an email will be sent to the email address you've specified in NEMS System Settings Tool, alerting you that your NEMS Server has failed to check in. It is a simple but highly effective solution.

.. figure:: ../../img/Sample-NEMS-CheckIn-notification.png
  :width: 600
  :align: center
  :alt: NEMS CheckIn Notification

  A sample NEMS CheckIn notification

To enable and configure NEMS CheckIn, visit the NEMS Cloud Services tab in NEMS System Settings Tool (SST).

NEMS CheckIn requires an active NEMS Cloud Services account.
