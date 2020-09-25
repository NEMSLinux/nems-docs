Understanding Notification Definitions
======================================

Before you setup your first check commands, you'll need to understand what the single-character notification options mean. Refer back to this list as needed, as you'll need to understand what commands such as `w,u,c,r,f` mean.

Service Notification Settings
-----------------------------

When you see `w,u,c,r,f,n`, these are the definitions:

* **w** Notify if in warning state,
* **u** Notify if in unknown state,
* **c** Notify if in critical state,
* **r** Notify if recovered from a previously bad state,
* **f** Notify if the service is flapping (on and off and on and off)
* **n** Never notify.

Host Notification Settings
--------------------------

When you see `d,u,r,f,s,n`, these are the definitions:

* **d** Notify if host is down,
* **u** Notify if host is unreachable (eg. Internet down),
* **r** Notify upon recovery,
* **f** Notify if the host is flapping,
* **s** Notify if a scheduled service downtime begins or ends,
* **n** Never notify.

Failure to correctly set notification settings will result in no notifications being generated.
