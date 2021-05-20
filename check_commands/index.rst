Included Check Commands
=======================

While not a comprehensive list of the available check commands in NEMS Linux,
here are some of the available check commands:

-  `check_apc <check_apc.html>`__ -
   Check APC UPS.
-  `check_dhtxx <../accessories/dhtsensors.html>`__ -
   Use a DHTxx (DHT11 / DHT22 / AM2302) Arduino sensor to report on the
   room temperature and humidity.
-  `check_esxi_hardware <check_esxi_hardware.html>`__ -
   Monitor the hardware of ESX and ESXi servers.
-  `check_http <check_http.html>`__ -
   Check the status of an HTTP/HTTPS server on a remote host.
-  `check_internet_speed <check_internet_speed.html>`__ -
   Check the speed of your internet connection.
-  `check_mikrotik_switch <check_mikrotik.html>`__ -
   Monitor stats for some MikroTik routers, including thermal sensors,
   packet loss, uptime, and so-on.
-  `check_ncpa <check_ncpa.html>`__ - Monitor Windows, Mac and Linux
   hosts. NCPA is written in Python and is able to run on almost any
   Operating System. 
-  `check_nems_osb <check_nems_osb.html>`__
   Determine whether NEMS Migrator Offsite Backup was successful.
-  `check_nems_php_agent <check_nems_php_agent.html>`__
   Monitor a Linux web server that has PHP using your custom NEMS PHP Agent.
-  `check_nrpe <check_nrpe.html>`__ -
   Monitor your hosts at a deeper level. Things like CPU usage, free
   disk space, free RAM, and so-on.
-  `check_ping <check_ping.html>`__ -
   Ping by hostname or IP address with warn/crit thresholds for response
   time and packet loss.
-  `check_qnap <check_qnap.html>`__ - Monitor various sensors on a QNAP NAS.
-  `check_synology <check_synology.html>`__ - Monitor various sensors on a Synology NAS.
-  `check_temper <../accessories/temper.html>`__ - Use a
   TEMPer USB temperature sensor to detect and report the room
   temperature.
-  `check_sbc_temperature <check_sbc_temperature.html>`__ -
   Check your NEMS SBC temperature with perfdata and warn/crit
   thresholds.
-  `check_tcp <check_tcp.html>`__ -
   Check response of a specific TCP connection.
-  `check_win_users <check_win_users.html>`__ - Check the count of users on a Windows server based on a query.
-  check_wmi_plus
   (See `this <https://github.com/speartail/checkwmiplus/blob/master/check_wmi_plus.README.txt>`__ and `that <https://github.com/shinken-monitoring/pack-windows/blob/master/libexec/check_wmi_plus.d/check_wmi_plus.ini>`__)
-  `custom_check_mem <custom_check_mem.html>`__ -
   Monitor the percentage of RAM free on either the local NEMS server or
   a remote system via NRPE.
-  `check_1wire_temp <check_1wire_temp.html>`__ - Monitor temperature using a 1-wire device such as the DS18S20.
-  `check_tasmota <check_tasmota.html>`__ - SONOFF / Tasmota IoT device monitoring.
-  `check_ibmi* <check_ibmi.html>`__ - IBM i monitoring using Nagios i.

.. toctree::
    :maxdepth: 1
    :caption: Check Command List

    check_apc
    ../accessories/dhtsensors
    check_esxi_hardware
    check_http
    check_internet_speed
    check_mikrotik
    check_ncpa
    check_nems_osb
    check_nems_php_agent
    check_nrpe
    check_ping
    check_qnap
    check_synology
    ../accessories/temper
    check_sbc_temperature
    check_tcp
    check_win_users
    custom_check_mem
    check_1wire_temp
    check_tasmota
    check_ibmi
