Check Command: check_internet_speed
===================================

Tests the speed of your Internet connection.

Demo Data
---------

Out of the box, NEMS Linux 1.5+ will check the Internet connectivity speed
using `Cloudflare's Speed Test <https://speed.cloudflare.com/>`__ service.
By default, warning notifications will be generated if your upload or
download speed falls below 10 Mb/s and Critical warnings if either falls
below 7 Mb/s. These are just sample thresholds which can (and should) be
modified to suit your connection speed by modifying the service in NEMS NConf.

Data Usage Warning
------------------

**Every time the speedtest runs, anywhere from 100-400 MB of data is
transferred** (depending on your connection speed). Since the sample
service is set to check every 30 minutes while in a good state, that
could be nearly 5GB of data per day. If your Internet is slow, the sample
service will check (retry) every 5 minutes, increasing the bandwidth
usage significantly.

While in most cases this is fine, you *must* modify your thresholds to
suit your connection, and modify your service schedule if you have
limited or pay-per-use bandwidth.

Logging
--------

A cache log is saved at /var/log/nems/speedtest.log whenever the script
is run. In NEMS Linux 1.6+, this cache is used by NEMS TV Dashboard to
display current Internet speed.

The format of this multi-line cache file is as follows:

  | State of service
  | Ping time
  | Ping measurement
  | Download speed
  | Download speed measurement
  | Upload speed
  | Upload speed measurement

Troubleshooting
---------------

**Service check timed out after [number] seconds**

If you are receiving a service check timeout and are certain you do indeed have
Internet connectivity, the most likely culprit is that your NEMS Server is unable
to process the speedtest within 120 seconds. A Raspberry Pi 4 with a reasonably
fast MicroSD card should be able to perform a speedtest in under 40 seconds. Please
upgrade your NEMS Server to an officially-supported platform. Power users may increase
the value of `service_check_timeout` in `/usr/local/nagios/etc/nagios.cfg` however
this may result in cascading checks, which will bring a low-powered SBC to its knees.
You are much safer to upgrade to a board that meets your requirements.
