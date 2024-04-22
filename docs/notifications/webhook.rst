Receiving Notifications via Webhook
===================================

.. figure:: ../img/discord-nems-webhook.png
  :width: 300
  :align: right
  :alt: Webhook Notification

Send notifications directly to your webhook. For example, have
your NEMS Linux server post alerts directly to your company Discord
channel.

To have your NEMS Server notify you via webhook, simply add your
webhook to `NEMS SST <../apps/nems-sst.html>`__ and then add
notify-by-webhook to both the Host and Service notifications for your
contact in NEMS Configurator.

Webhook functionality was first introduced in NEMS Linux 1.5, but that
version was deprecated in favor of notify-by-webhook. Therefore, webhook
notifications require NEMS Linux 1.7+. NEMS only sends
webhooks. It does not receive them.

Currently Supported Webhooks:
-----------------------------

-  Discord
-  Slack
-  Microsoft Teams

If you would like support added for another webhook, please simply put
it in as a feature request in the Community Forum.

Test Your Webhook
-----------------
.. code-block:: console

    sudo nems-webhooktest
