Check Command: check_1wire_temp
===============================

1-wire devices are a cheap and simple way to monitor temperature. Each 1-wire device has a unique serial number that allows multiple devices to communicate on one bus.

check_1wire_temp is a Nagios plugin that is used to monitor temperature using a 1-wire device such as the DS18S20.

Usage
~~~~~

check_1wire_temp -v -h -l low_temp_warn -L low_temp_crit -w high_temp_warn -H high_temp_crit

Requirements
~~~~~~~~~~~~

Requires NEMS Linux 1.6+.
