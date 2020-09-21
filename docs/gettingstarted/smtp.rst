Setting Up Email Notifications
==============================

The first thing you’ll want to do on your new NEMS Linux server is configure your SMTP settings. This will allow your NEMS server to email you if a problem is detected.

Access the NEMS System Settings Tool (SST) from the Configuration menu of your NEMS dashboard. This tool does away with the need to use the traditional Nagios resource.cfg file to configure your email settings. One of the nice things about NEMS Linux is that I really don’t have to go into detail about how to do this. It’s so intuitive that it does not require explanation. So I’ll just provide a screenshot in Figure 5.

.. figure:: ../../img/smtp_nems-sst.png
  :width: 600
  :align: center
  :alt: Adding SMTP Credentials in NEMS System Settings Tool

  Configuring your SMTP server in NEMS is as simple as configuring a mail client.

.. Tip:: If you’re using Gmail as your SMTP provider, be sure to review the NEMS Documentation found at https://docs.nemslinux.com/usage/nagios-gmail-smtp for the additional steps required.

Once you are confident your SMTP settings are correctly entered, click Save All Settings and then re-connect over SSH to test your email settings with the following command (replacing youremail@yourdomain.com with your actual recipient email address):

.. code-block:: console

  sudo nems-mailtest youremail@yourdomain.com
  
This command simply verifies your mail settings by sending a test notification. If there are any problems, it will show you on screen what the issue is, and you can make the necessary changes to your account settings in NEMS SST.

Note: NEMS currently requires your SMTP server support TLS authentication. Against my best judgement but in line with user requests, an option will be added to a future release to allow insecure authentication if required, as might be the case with an internal relay.
