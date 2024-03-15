Check NetScaler ADC (check_netscaler)
#####################################

NEMS Linux monitors Citrix NetScaler Application Delivery Controllers.
  
.. note:: *check_netscaler* requires NEMS Linux 1.7 or higher.


NEMS NConf Parameters
---------------------

- `Check Name` - See the table below for the available commands.
- `Object Name` - The object name to check.
- `Username` - The username to use to connect. This should be a limited account.
- `Password` - The password of that limited user.
- `Warning %` - The percentage to trigger a WARNING state.
- `Critical %` - The percentage to trigger a CRITICAL state.


Commands
--------

- `state` - check the current service state of vservers (e.g. lb, vpn, gslb), services, and service groups and servers
- `matches`, `matches_not` - check if a string matches the API response or not
- `above`, `below` - check if a value is above/below a threshold (e.g. traffic limits, concurrent connections)
- `sslcert` - check the lifetime for installed SSL certificates
- `nsconfig` - check for configuration changes which are not saved to disk
- `license` - check the expiry date of a locally installed license file
- `hastatus` - check the high availability status of an appliance
- `staserver` - check if configured STA (secure ticket authority) servers are available
- `servicegroup` - check the state of a service group and its members
- `hwinfo` - just print information about the Netscaler itself
- `interfaces` - check the state of all interfaces and add performance data for each interface
- `perfdata` - gather performance data from all sorts of API endpoints
- `ntp` - check the NTP synchronization status
- `debug` - debug command, print all data for an endpoint


Source
------

From https://github.com/slauger/check_netscaler
