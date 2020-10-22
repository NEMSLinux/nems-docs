Check Command: check_apc
========================

APC UPS's use SNMPv1. You can configure SNMP for your UPS from its web
interface or within your UPS's configuration software client.

*check_apc* provides performance data and range monitoring for a wide
series of data and a large number of APC UPS's, including Symmetra and
SmartUPS models.

This check command requires NEMS Linux 1.6+.

check_apc Available Command Arguments
-------------------------------------

id

Return the UPS model name (e.g. 'APC Smart-UPS 600') and interlan info
about Firmware, CPU S/N and manufacturing date

bat_status

Return the status of the UPS batteries

bat_capacity

Return the remaining battery capacity expressed in percent of full
capacity

bat_temp

Return the current internal UPS temperature expressed in Celsius

bat_run_remaining

Return the UPS battery run time remaining before battery exhaustion

\*\* NB: thresholds must be expressed in minutes \*\*

bat_replace

Return whether the UPS batteries need replacing

bat_num_batt

Return the number of external battery packs connected to the UPS

bat_num_bad_batt

Return the number of external battery packs connected to the UPS that
are defective

bat_act_volt

Return the actual battery bus voltage in Volts

\*\* NB: thresholds must be expressed in range as nearest values. ex:
normal=220, warning=215:225, critical=210:230 \*\*

\*\* Additionally, the checks will look for Nominal Voltage (as returned
by the UPS), and exit as CRITICAL if Actual Voltage is LOWER or Equal
\*\*

power_modules

Return the status of the Power Modules

in_phase

Return the current AC input phase

in_volt

Return the current utility line voltage in VAC

\*\* NB: thresholds must be expressed in range as nearest values. ex:
normal=220, warning=215:225, critical=210:230 \*\*

in_freq

Return the current input frequency to the UPS system in Hz

\*\* NB: thresholds must be expressed in range as nearest values. ex:
normal=50, warning=45:55, critical=40:60 \*\*

out_status

Return the current state of the UPS

out_phase

Return the current output phase

out_volt

Return the output voltage of the UPS system in VAC

\*\* NB: thresholds must be expressed in range as nearest values. ex:
normal=220, warning=215:225, critical=210:230 \*\*

out_freq

Return the current output frequency of the UPS system in Hz

\*\* NB: thresholds must be expressed in range as nearest values. ex:
normal=50, warning=45:55, critical=40:60 \*\*

out_load

Return the current UPS load expressed in percent of rated capacity

out_current

Return the current in amperes drawn by the load on the UPS

comm_status

Return the status of agent's communication with UPS.

No command is supplied, the script return OKAY with the UPS model
information.