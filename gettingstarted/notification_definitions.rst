Understanding Notification Definitions
======================================

Before you setup your first check commands, you'll need to understand what the single-character notification options mean. Failure to correctly set notification settings could result in no notifications being generated.

Refer back to this list as needed, as you'll need to understand what commands such as `w,u,c,r,f` mean.

Host Notification Settings
--------------------------

When you see `d,u,r,f,s,n`, these are the definitions:

* **d** Notify if host is down,
* **u** Notify if host is unreachable (eg. Internet down),
* **r** Notify upon recovery,
* **f** Notify if the host is flapping (up/down/up/down),
* **s** Notify if a scheduled service downtime begins or ends,
* **n** Never notify.

.. admonition:: Exercise
  :class: note
  
  The NEMS Server sample host uses the *linux-server* Host Template. So rather than having to set the notification options within the host itself, we set these within the template. Can you determine from the above list what the default notification settings are for *linux-server* devices by looking at the host template? You'll find the *linux-server* Host Template in Configuration -> NEMS Configurator. Press the *Show* button next to *Host templates* on the menu, followed by the edit pencil next to *linux-server*.

Service Notification Settings
-----------------------------

When you see `w,u,c,r,f,n`, these are the definitions:

* **w** Notify if in warning state,
* **u** Notify if in unknown state,
* **c** Notify if in critical state,
* **r** Notify if recovered from a previously bad state,
* **f** Notify if the service is flapping (up/down/up/down),
* **n** Never notify.
