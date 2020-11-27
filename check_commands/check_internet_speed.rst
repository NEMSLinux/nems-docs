Check Command: check_internet_speed
===================================

Tests the speed of your Internet connection.

Demo Data
---------

Out of the box, NEMS Linux 1.5+ will check the Internet connectivity speed
using an automatically selected nearby test server. Warning
notifications will be generated if your upload or download speed falls
below 10 Mb/s and Critical warnings if either falls below 7 Mb/s. These
are just sample thresholds which can (and should) be modified to suit
your connection speed by modifying the service in NEMS NConf.

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

Dynamic Server Detection
-------------------------

NEMS Linux automatically chooses the best speedtest server for your test
(generally, the one nearest to you geographically). This may change now
and again as servers become unresponsive or otherwise go offline. Since
it is dynamic, the server selection is done behind the scenes by your
NEMS Server, so you never have to think about it.

Logging
--------

A cache log is saved at /var/log/nems/speedtest.log whenever the script
is run. In NEMS Linux 1.6+, this cache is used by NEMS TV Dashboard to
display current Internet speed.
