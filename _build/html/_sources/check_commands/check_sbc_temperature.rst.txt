Check Command: check_sbc_temperature
====================================

**Requires:** NEMS 1.5+

`check_rpi_temperature <https://exchange.nagios.org/directory/Plugins/Hardware/Others/check_rpi_temperature/details>`__ has
been renamed *check_sbc_temperature* because it is not at all Raspberry
Pi specific: Any system that has sysfs logged to
/sys/class/thermal/thermal_zone0/temp will work.

Also tested on the NEMS Linux ODROID XU4 build.

This check command requires two arguments: Warning Temperature °C and
Critical Temperature °C.

Default Thresholds
------------------

NEMS Linux comes with check_sbc_temperature pre-configured on the NEMS
localhost. Here are the default thresholds:

-  **ODROID XU4** 76°C Warn / 82°C Crit