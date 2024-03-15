Check NetScaler ADC (check_netscaler)
#####################################

NEMS Linux monitors NetScaler Application Delivery Controllers.
  
*check_netscaler* requires NEMS Linux 1.7 or higher.


**Parameters:**

- `Check Name` - See the table below for the available commands.
- `Object Name` - The object name to check.
- `Username` - The username to use to connect. This should be a limited account.
- `Password` - The password of that limited user.
- `Warning %` - The percentage to trigger a WARNING state.
- `Critical %` - The percentage to trigger a CRITICAL state.


Commands
--------

+-------------------+-----------------------------------------------------------------+
| command           | description                                                     |
+-------------------+-----------------------------------------------------------------+
| **state**         | check the current service state of vservers (e.g. lb, vpn,     |
|                   | gslb), services and service groups and servers                  |
+-------------------+-----------------------------------------------------------------+
| **matches,       | check if a string matches the the api response or not           |
| matches_not**     |                                                                 |
+-------------------+-----------------------------------------------------------------+
| **above, below**  | check if a value is above/below a threshold (e.g. traffic      |
|                   | limits, concurrent connections)                                 |
+-------------------+-----------------------------------------------------------------+
| **sslcert**       | check the lifetime for installed ssl certificates               |
+-------------------+-----------------------------------------------------------------+
| **nsconfig**      | check for configuration changes which are not saved to disk     |
+-------------------+-----------------------------------------------------------------+
| **license**       | check the expiry date of a local installed license file         |
+-------------------+-----------------------------------------------------------------+
| **hastatus**      | check the high availability status of a appliance               |
+-------------------+-----------------------------------------------------------------+
| **staserver**     | check if configured STA (secure ticket authority) servers are   |
|                   | available                                                       |
+-------------------+-----------------------------------------------------------------+
| **servicegroup**  | check the state of a servicegroup and its members               |
+-------------------+-----------------------------------------------------------------+
| **hwinfo**        | just print information about the Netscaler itself               |
+-------------------+-----------------------------------------------------------------+
| **interfaces**    | check state of all interfaces and add performance data for each |
|                   | interface                                                       |
+-------------------+-----------------------------------------------------------------+
| **perfdata**      | gather performancedata from all sorts of API endpoints          |
+-------------------+-----------------------------------------------------------------+
| **ntp**           | check the ntp synchronization status                            |
+-------------------+-----------------------------------------------------------------+
| **debug**         | debug command, print all data for a endpoint                    |
+-------------------+-----------------------------------------------------------------+


Source
------

From https://github.com/slauger/check_netscaler
