Check Command: check_qnap
=========================

-  ``status`` checks if QNAP is online
-  ``diskused`` disk usage in percentage
-  ``cpu`` system CPU load in percent
-  ``cputemp`` system CPU temperature in C
-  ``freeram`` free RAM
-  ``temp`` system temperature in C
-  ``hdtemp`` Harddrive temperature in C (all hard drives)
-  ``hdNtemp`` Nth harddrive temperature in C (ex. hd1temp)
-  ``volstatus`` Status of all volumes
-  ``volNstatus`` Nth volume status
-  ``powerstatus`` Power status
-  ``fans`` Fans speed (RPM)
-  ``systemuptime`` System uptime
-  ``sysinfo`` System info display (model, number of hard drives, volumes, name and firmware)

Source: `check_qnap3.sh` file (https://github.com/cloudcentral/nagios-plugins-check_qnap/blob/master/check_qnap3.sh)
