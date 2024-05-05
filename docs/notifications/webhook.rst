Receiving Notifications via Webhook
===================================

.. figure:: ../img/discord-nems-webhook.png
  :width: 300
  :align: right
  :alt: Webhook Notification

Send notifications directly to your webhook. For example, have
your NEMS Linux server post alerts directly to your company Discord
channel.

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

Currently Supported Webhooks
----------------------------

-  Discord
-  Slack
-  Microsoft Teams

If you would like support added for another webhook, please simply put
it in as a feature request in the Community Forum.

Test Your Webhook
-----------------
.. code-block:: console

    sudo nems-webhooktest

Webhook Icon
------------

You may wish to include an icon when setting up your webhook. You can create your own, or `download one we have created for you from the NEMS Branding page <../../misc/nemsbranding.html#nems-generic-icons>`__.
