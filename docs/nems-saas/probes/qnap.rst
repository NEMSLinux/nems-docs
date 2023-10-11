NEMS SaaS Probe Installation on QNAP NAS
========================================

Introduction
^^^^^^^^^^^^

QNAP NAS devices run a Linux distribution called `QTS <https://www.qnap.com/qts/>`__. As such, the NEMS SaaS probe is able to monitor your QNAP NAS device as if it was any other Linux server.

Ensure Your QNAP Is Prepared
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step 1. Enable SSH Access.
--------------------------

In order to access the Linux terminal on your QNAP device, you must enable SSH access.

Open ``Control Panel -> Network & File Services -> Telnet / SSH`` and place a checkbox next to ``Allow SSH Connections``.

.. figure:: ../../img/qnap_controlPanelSSH.png
  :width: 800
  :align: center
  :alt: Enable SSH in QNAP Control Panel

If you use a different account than ``admin`` as your administrator account (which you should!) click ``Edit Access Permissions`` and add your user.

Once you're finished, you can later return to this screen to disable SSH access.

Step 2. Connect to your QNAP SSH Terminal.
------------------------------------------

Step 3. Install nems-saas-config
--------------------------------

Step 4. Install nems-saas-probe
-------------------------------

``sudo wget -O /usr/local/bin/nems-saas-probe https://github.com/NEMSLinux/nems-saas-probe/raw/main/linux/amd64/nems-saas-probe && sudo chmod +x /usr/local/bin/nems-saas-probe``

Step 5. Enable auto-load at boot.
---------------------------------
