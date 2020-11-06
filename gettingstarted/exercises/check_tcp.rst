Monitor A Non-Standard Port with check_tcp
==========================================

Exercise Introduction
---------------------

In this exercise you will learn to monitor the state of any TCP/UDP port on a network connected device, and notify yourself if it stops responding. Some quick examples are to tell if your local blockchain node has stopped responding on port 8333, Apache2 has stopped responding on port 443, or even monitor the state of openssh-server running on port 22. The options are limitless.

NEMS Linux includes a dummy port listener running on port 9590. The port listener is cleverly called 9590, and does nothing other than reply that it is up. This can be used to simulate a port on another device. While you can create a check for any port on any host, let's start with using this dummy port just to become familiar with how NEMS Linux works. Our goal: To setup a service monitor on the NEMS host which warns us if port 9590 ever goes offline.

Steps
-----

#. On the left menu of NConf, you'll see “Services”. Click “Add”.
#. Set the Service Name to: `9590`
#. Leave Service Enabled set to: Yes
#. Set the Check Command to: check_tcp
#. Set Assigned to Host to: NEMS (this host comes pre-installed)
#. Leave Check Period set to: 24×7
#. Set Notification Period to: 24x7
#. Leave Service Templates as is, none selected.
#. Under Contact Groups highlight the 'admins' group and press the arrow pointed right to move it to Selected Items.
#. Leave Notes, Notes URL and Action URL blank.
#. Set Max Check Attempts to: 30
#. Set Check Interval to: 1
#. Set Retry Interval to: 1
#. Set First Notification Delay to: 5
#. Set Notification Interval to: 15
#. Set Notification Options to: w,u,c,r,f,s
#. Leave Active Checking, Passive Checking, Notification Enabled, Check Freshness and Freshness Threshold blank.
#. Leave Assign Service to servicegroup as is, none selected.
#. Set Params for check command to the port number: 9590
#. Press Submit
#. Press Generate Nagios Config, followed by pressing the Generate button on the next screen to deploy and activate your new configuration.

Conclusion
----------

Once the new config is running, try failing the service by opening Monit Service Manager under System on the NEMS Dashboard. Click on the Process named 9590, and then click “Stop service”. You'll notice in around 1 minute the status of 9590 will show as a problem in all status views (E.G., NEMS TV Dashboard, NEMS Adagios, Nagios Core), and after roughly 5 minutes you will receive a notification (assuming your notifications settings are configured).

Once you have received a notification, visit NEMS Adagios to Acknowledge the outage. Then, return to Monit, open the 9590 Process, and click “Enable Monitoring”. This will re-load 9590 and you'll soon see it change to a Recovered state.

Once complete, try setting up a new service to monitor a real host on your network. Simply change the name of the service to something appropriate, the host in step 5 (you already know how to add new hosts if you don’t already have it configured), and the port number in step 19.
