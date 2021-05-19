Check Command: check_tasmota
============================

Check IoT sensor states for sensors running the Tasmota Firmware, such as SONOFF IoT devices.

Included Check Commands
~~~~~~~~~~~~~~~~~~~~~~~

**Note:** I do not have one of these devices for testing in NEMS Linux, so have done my best to
understand the command parameters. If you test your device, please report back to me (Robbie) with
your feedback as to the accuracy of this documentation, or any changes that are required. If you
encounter an issue you cannot resolve, please let me know.

NEMS Linux includes the two sample check commands provided by the plugin author:

- `check_tasmota_power` - Check the power state of a compatible IoT device. Warn/Crit should be a
binary threshold: `0` or `1`.
- `check_tasmota_sensor` - Check the state of any compatible sensor. Must specify the device (E.G.,
ENERGY or AM2301) and the sensor (E.G., Humidity, Temperature, Voltage, Current, Total, Today, Yesterday).

Requirements
~~~~~~~~~~~~

Requires NEMS Linux 1.6+.

Source
~~~~~~
From https://github.com/dirkheitzmann/nagios-plugin-check_tasmota
