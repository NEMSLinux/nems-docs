Command: nems-cert
==================

.. figure:: ../../img/screenshot_from_2017-11-09_22-40-23.png
  :width: 600
  :align: center
  :alt: nems-cert

When you
run `nems-init <https://docs.nemslinux.com/commands/nems-init>`__ NEMS
generates your SSL certificates. However, if you ever want to update
your certs, you definitely don't want to run *nems-init* again - that'd
wipe out your configuration.

So *nems-cert* has you covered.

**sudo** nems-cert

This will take you through the certificate creation process once again,
generate your certificates and certificate authority, install them, and
restart the services which use them.

If you generate a new certificate for NEMS you may need to delete the
old one from your browser and restart, and then create a new exception
for the `self-signed
certificate <https://docs.nemslinux.com/self-signed-certs>`__.

nems-cert temporarily uses Debian Snakeoil certificates - so all the
information covered in this doc (other than how to run the program) is
irrelevant at present. For now, when you run nems-cert, it will just do
its thing with no user input. This is to resolve an issue with Windows
10 users unable to connect to their NEMS 1.3 server. A fix will be
issued in future bringing back the nems-cert interface.

Modes Of Operation
------------------

Generic Settings
~~~~~~~~~~~~~~~~

Do you want to create a certificate quickly? The Generic Settings option
allows you to create and deploy a certificate very quickly with
absolutely no user input needed.

Custom Settings
~~~~~~~~~~~~~~~

Custom Settings allows you to manually specify some of the information
for your certificate. This is not generally public information, but will
be seen when you view the certificate in your browser (for example).

-  **Country Code** - This is your 2-digit country code. US for United
   States of America, or CA for Canada, for example. By default, the
   country code from your keyboard locale settings will be used.
-  **Province/State** - The textual representation of your
   province/state. For me, this is: Ontario
-  **Your City** - The textual name of your city. For me, this is:
   Barrie
-  **Company Name or Your Name** - Like all other fields for your cert,
   you have to fill this in. So if you don't have a company, just use
   your name, or make something up.
-  **Your email address** - Your complete email address. This will not
   be shared, but is required to generate a self-signed certificate.

Specifications
--------------

*nems-cert* generates SHA256 encrypted certificates with RSA 2048 keys.

Viewing Your Certificate Information
------------------------------------

Once you have generated your SSL Certificate, you can view it with the
following command:

**sudo** nems-info sslcert

Use of nems-cert Outside of NEMS Linux
--------------------------------------

Of course, the work I do on NEMS is freely available. Just don't forget
to throw something in the `Tip Jar <https://donate.category5.tv/>`__ if
you like what I do.

`Source
Code <https://raw.githubusercontent.com/Cat5TV/nems-scripts/master/gen-cert.sh>`__

If using nems-cert (or, gen-cert.sh in this case) outside NEMS, you'll
simply need to install a few components:

**sudo** apt update && **sudo** apt **install** openssl **dialog**

You'll also want to change where the certs are saved to within the
source code since the NEMS locations won't be relevant.