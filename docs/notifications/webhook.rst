Receiving Notifications via Webhook
===================================

.. figure:: ../img/discord-nems-webhook.png
  :width: 300
  :align: right
  :alt: Webhook Notification

Webhooks provide a means of publishing notifications to applications in real-time.

NEMS Linux can use webhooks to send alerts about server downtime or performance issues
directly to a designated Microsoft Teams or Slack channel, or Discord server. This allows
you and your team to stay informed in real-time without having to continuously monitor
your NEMS Server or email.

Webhook functionality was first introduced in NEMS Linux 1.5, but that
version was deprecated in favor of notify-by-webhook. Therefore, webhook
notifications require NEMS Linux 1.7+. NEMS only sends
webhooks. It does not receive them.

How To Use
----------

To have your NEMS Server notify you via webhook, simply add your
webhook URL to `NEMS SST <../apps/nems-sst.html>`__ (under *Notifications*)
and then add ``notify-by-webhook`` to both the Host and Service notifications
for your contact in NEMS Configurator.

Supported Webhooks
------------------

-  Microsoft Teams
-  Discord
-  Slack

If you would like support added for another application, please post a
feature request in the
`nems-plugins Issue Tracker <https://github.com/NEMSLinux/nems-plugins/issues>`__.

Test Your Webhook
-----------------
.. code-block:: console

    sudo nems-webhooktest

Webhook Icon
------------

You may wish to include an icon when setting up your webhook. You can create your own, or `download one we have created for you from the NEMS Branding page <../../misc/nemsbranding.html#nems-generic-icons>`__.
