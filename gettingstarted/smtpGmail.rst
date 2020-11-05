Using Gmail SMTP For Nagios Notification Sending
================================================

When using Gmail for SMTP, a few extra steps are required.

First, if you are a G Suite user (that is to say, you're using Gmail but
have an @yourdomain.com email address on their service as opposed to an
@gmail.com address), visit `this
page <https://admin.google.com/AdminHome?pli=1&fral=1#ServiceSettings/emailsettingkey=NewSettingGroupIdPrefix-1574942781&service=email&subtab=filters>`__ and
configure the SMTP Relay Service like this:

.. figure:: ../../img/admin-ajax.png
  :width: 500
  :align: center
  :alt: Gmail Setup

Of course, if you happen to have a static public IP address on your NEMS
server, go ahead and enable IP filtering for even more security.

Then, visit `this
page <https://admin.google.com/AdminHome#ServiceSettings/notab=1&service=securitysetting&subtab=lesssecureappsaccess>`__ and
enable *“Allow users to manage their access to less secure apps”*.

Now that you've done that, **or if you are not a G Suite user**, you'll
need to enable the setting for *“less secure
apps”* here: https://myaccount.google.com/lesssecureapps