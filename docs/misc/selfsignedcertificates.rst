NEMS SSL and Self-Signed Certificates
=====================================

My browser warns, "Your connection is not secure". Why?
-------------------------------------------------------

NEMS Linux uses SSL (aka https) connections to secure your connection
and the data you transmit and receive to and from your NEMS server.

This is accomplished using what is called a *self-signed certificate*.
By nature, self-signed certificates are considered “untrusted” by your
browser because, simply put, anyone can make them. It does not mean your
connection is not encrypted or secure, but rather it means your browser
cannot determine who created the certificate, and therefore cannot
verify your security.

If you visit a web site, say *google.com* and received a warning that
your connection is not secure, you should immediately stop what you're
doing and not proceed. However, in the case of NEMS Linux, which is a
local server on *your* network (not a “dot com” somewhere out on the
web), you can safely trust the self-signed certificates and add an
exception to your browser.

Where do the NEMS Self-Signed Certificates come from?
-----------------------------------------------------

When you first deploy NEMS, a “default” certificate is included to help
you get up and running. However, since this certificate is publicly
available in the NEMS source code and img download, it is only used for
your initial connection.

It can be a bit of a pain for novice users to setup SSL certificates, so
like many other things with NEMS, I set out to make it easier.

When
running `nems-init <https://docs.nemslinux.com/commands/nems-init>`__,
your unique SSL certificate is generated, added to your NEMS
configuration and from then on all services will use your newly-created
self-signed certificate.

What type of certificate is created?
------------------------------------

NEMS generates self-signed certificates
using `ssl-cert <https://packages.debian.org/sid/ssl-cert>`__. These
self-signed certificates are called *snakeoil* because they do not use a
certificate authority to authenticate validity. This means they provide
a secure, encrypted connection between your client and NEMS server.
However, they only provide trust to you and those who trust you (as you
must accept the certificate / create an exception). This type of
certificate is free and does not require you have your NEMS server
publicly visible to the Internet.

Now that I have self-signed certs, how do I connect to NEMS?
------------------------------------------------------------

Your browser will warn you that the site is untrusted the first time you
connect. It will also provide an “Advanced” option where you can “Add
Exception”.

I added a permanent exception, then reinstalled, re-initialized or upgraded NEMS, and now I can't connect.
----------------------------------------------------------------------------------------------------------

You need to remove the old certificates from your browser, restart the
browser, and try again.

Why not use Let's Encrypt?
--------------------------

Let's Encrypt (and other certificate authorities) require the server be
web-accessible so they can respond to challenges that prove the identity
of the server. In order to utilize a service such as Let's Encrypt, your
NEMS Linux server would have to be hosted on an FQDN and be
web-accessible. I recommend against this since it's an attack vector
that is completely unnecessary. The only advantage a CA gives you is
trust, but you already trust your NEMS server as you are accessing it on
a local IP.

It's still not working.
-----------------------

Date and Time
~~~~~~~~~~~~~

Check (and fix) the date and time on both your NEMS server and your
computer. If either are incorrect, your system will be unable to
connect.

NEMS has NTP installed, so as long as you set your locale correctly
during `nems-init <https://docs.nemslinux.com/commands/nems-init>`__,
the time and date should be correct. However, if your date is far
inaccurate, NTP will reject the update. Therefore you must ensure your
date and time are correct for NTP to work. See `this helpful
tool <https://www.baldnerd.com/nerdgasms/linuxdate/>`__ I have created
to help you set the date and time quickly and accurately.

Most single board computers also require that you have an optional RTC
battery installed as well. This maintains the date and time in event of
power loss.

Security Software
~~~~~~~~~~~~~~~~~

Modern security software may by default block the use of self-signed
certificates. This is a good security feature due to the inability to
confirm trust of self-signed SSL connections that you do not have
control over. You know you can trust your own NEMS server, but how do
you know you can trust some obscure web site using a self-signed
certificate? You can't.

I recommend against disabling this protection, as it is a good feature
of anti-malware software. Instead, setup an exception for nems.local.
Another idea is to setup an exception for your , or create your  as a
trusted zone.