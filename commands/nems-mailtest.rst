Commands: nems-mailtest
-----------------------

Test Your Email Notification Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I've written an easy-to-use script which will load your settings from
resource.cfg and send you a test email. It will also show you in the
terminal the results, which may be helpful if you believe there is an
error (since you'll be able to see the output of sendemail).

To run the test script: ``nems-mailtest youremail@yourdomain.com`` where
*youremail@yourdomain.com* is your actual recipient email address (must
be different than the one you set in *resource.cfg*).

If you'd prefer JSON output, add a 1 to the command:
``nems-mailtest youremail@yourdomain.com 1`` JSON output requires NEMS
Linux 1.6+.
