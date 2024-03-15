Check Fortinet FortiGate Appliances (check_fortigate)
=====================================================

Checks Fortinet appliances via SNMP v1/v2c/v3, with perf data.

Usage
-----

.. code-block:: bash

    check_fortigate.pl -H -C -T [-w|-c|-S|-s|-R|-M|-V|-?]

Options
-------

.. option:: -H, --host STRING or IPADDRESS

    Check interface on the indicated host.

.. option:: -P, --port INTEGER

    Port of indicated host, defaults to 161.

.. option:: -v, --version STRING

    SNMP Version, defaults to SNMP v2, v1-v3 supported.

.. option:: -T, --type STRING

    CPU, MEM, Ses, VPN, Cluster, Firmware, HW, etc.

.. option:: -S, --serial STRING

    Primary serial number.

.. option:: -s, --slave

    Get values of slave.

.. option:: -w, --warning INTEGER

    Warning threshold, applies to cpu, mem, session, firmware.

.. option:: -c, --critical INTEGER

    Critical threshold, applies to cpu, mem, session, firmware.

.. option:: -R, --reset

    Resets ip file (cluster only).

.. option:: -M, --mode STRING

    Output-Mode: 0 => just print, 1 => print and show failed tunnel, 2 => critical.

.. option:: -V, --vpnmode STRING

    VPN-Mode: both => IPSec & SSL/OpenVPN, ipsec => IPSec only, ssl => SSL/OpenVPN only.

SNMP v1/v2c only:

.. option:: -C, --community STRING

    Community-String for SNMP, only at SNMP v1/v2c, defaults to public.

SNMP v3 only:

.. option:: -U, --username STRING

    Username.

.. option:: -A, --authpassword STRING

    Auth password.

.. option:: -a, --authprotocol STRING

    Auth algorithm, defaults to sha.

.. option:: -X, --privpassword STRING

    Private password.

.. option:: -x, --privprotocol STRING

    Private algorithm, defaults to aes.

.. option:: -?, --help

    Returns full help text.

Requires
--------

- Net::SNMP
- List::Compare
- Getopt::Long
- Pod::Usage
- Switch

Description
-----------

This plugin checks Fortinet FortiGate devices via SNMP.

From Web:

1. Select Network -> Interface -> Local interface
2. Administrative Access: Enable SNMP
3. Select Config -> SNMP
4. Enable SNMP, fill your details
5. SNMP v1/v2c: Create new
6. Configure for your needs, Traps are not required for this plugin!

From CLI:

.. code-block:: bash

    config system interface
    edit "internal"
    set allowaccess ping https ssh snmp fgfm
    next
    end

    config system snmp sysinfo
    set description "DMZ1 FortiGate 300C"
    set location "Room 404"
    set conctact-info "BOFH"
    set status enable
    end

    config system snmp community
    edit 1
    set events cpu-high mem-low fm-if-change
    config hosts
    edit 1
    set interface "internal"
    set ip %SNMP Client IP%
    next
    end
    set name "public"
    set trap-v1-status disable
    set trap-v2c-status disable
    next
    end

Thats it!

Samples
-------

To use SNMPv3 just replace ``-C public`` with ``-v 3 -U username -A this_is_auth_string -a sha -x aes128 -X this_is_priv_string``.

Cluster:

.. code-block:: bash

    $ check_fortigate.pl -H 192.168.123.100 -C public -T cluster

    OK: Fortinet 300C (Master: FGSERIALMASTER, Slave: FGSERIALSLAVE): HA (Active/Passive) is active
    - Warning if unknown node appears
    - Critical if single node
    - Optional: Critical, if preferred master (-S Serial) is not master

CPU:

.. code-block:: bash

    $ check_fortigate.pl -H 192.168.123.100 -C public -T cpu

    OK: Fortinet 300C (Master: FGSERIALMASTER) CPU is okay: 1%|'cpu'=1%;80;90

CPU-Slave:

.. code-block:: bash

    $ check_fortigate.pl -H 192.168.123.100 -C public -T cpu -s

    OK: Fortinet 300C (Master: FGSERIALMASTER) slave_CPU is okay: 5%|'slave_cpu'=5%;80;90
    - Defaults: 80%/90%

Memory:

.. code-block:: bash

    $ check_fortigate.pl -H 192.168.123.100 -C public -T mem

    OK: Fortinet 300C (Master: FGSERIALMASTER) Memory is okay: 29%|'memory'=29%;80;90

Memory-Slave:

.. code-block:: bash

    $ check_fortigate.pl -H 192.168.123.100 -C public -T mem

    OK: Fortinet 300C (Master: FGSERIALMASTER) slave_M
