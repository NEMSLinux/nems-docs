Check Command:  check_ilo2_health
=================================

Check hardware health of HP Proliant Servers by querying the HPE
Integrated Lights-Out (iLO) 2/3/4/5 Management Controller.

No need for snmp or installation of software.

Checks if all sensors are ok, returns warning on high temperatures
and fan failures and critical on overall health failure.

**Note:** The plugin shows only temperature sensors by default.
Faulty hardware components are only listed if iLO returns an error state.

The plugin makes use of the HP Lights-Out XML scripting interface.

Arguments [Optional]
--------------------

- `-e`: plugin ignores "syntax error" messages in the XML output. This may help for older firmwares.
- `-n`: output without temperature listing.
- `-d`: add PerfParse compatible temperature output.
- `-v`: print out the full XML output from the BMC.
- `-3`: support for iLO3|4
- `-a`: check fan redundancy (only some models)
- `-c`: check drive bays (only some models)
- `-o`: check power redundancy (only some models)
- `-b`: temperature output with location
- `-l`: parse iLO eventlog
- `-b`: show temperature with location
- `-x`: ignore battery missing
- `-i`: ignore NIC Link Down status (iLO4).
- `-g`: display additional infos like firmware version and servername (may need increased timeout!)
- `-f`: read input from file instead from iLO, possible to feed -v output to it
- `--sslopts`: Defaults to 'SSL_verify_mode => SSL_VERIFY_NONE'. Use 'SSL_verify_mode => SSL_VERIFY_NONE, SSL_version => "TLSv1"' to avoid TLS Downgrade bug.

Source
------

- https://exchange.nagios.org/directory/Plugins/Hardware/Server-Hardware/HP-%28Compaq%29/check_ilo2_health/details
