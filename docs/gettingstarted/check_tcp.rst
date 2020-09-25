Monitor A Non-Standard Port with check_tcp
==========================================

Exercise Introduction
---------------------

In this exercise you will learn to monitor the uptime of any TCP/UDP port. 
Monitor the state of any TCP/UDP port on a network connected device, and notify you if it stops responding: tell if your local blockchain node has stopped responding on port 8333, Apache2 has stopped responding on port 443, or monitor the state of openssh running on your server on port 22. These are just examples. The options are limitless.

NEMS Linux includes a dummy port listener running on port 9590. The port listener is cleverly called 9590, and does nothing other than reply that it is up. This can be used to simulate a port on another device. Let's setup a service monitor on the NEMS host to warn us if port 9590 ever goes offline.

