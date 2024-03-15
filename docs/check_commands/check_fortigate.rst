Check Fortinet FortiGate Appliances (check_fortigate)
#####################################################

Checks Fortinet appliances via SNMP v1/v2c/v3, with perf data.

*check_fortigate* requires NEMS Linux 1.7 or higher.

.. admonition:: Veriage Disclaimer

   Please note that Fortinet's use of the terms "master" and "slave" to distinguish between primary and secondary devices is an industry-standard terminology in the context of networking hardware. While NEMS Linux respects the terminology used by Fortinet for its products, it's essential to recognize that these terms can carry historical connotations and may not reflect the values of equity and inclusivity that we strive for in modern society. NEMS Linux is committed to supporting equity, diversity, and inclusion in all aspects of its development and operation.


Available checkcommands
***********************

Check Fortigate Cluster
=======================

Check the status of a Fortigate cluster, providing information about the active/passive state and any warnings or critical alerts.

**Check Command:** `check_fortigate_cluster`

**Parameters**

- Community Name (default: public)


Check Fortigate CPU
===================

**Check Command:** `check_fortigate_cpu`

Monitor the CPU usage of a Fortigate device, ensuring that it remains within acceptable thresholds to maintain optimal network performance.

**Parameters:**

- Community Name (default: public)


Check Fortigate RAM (check_fortigate_mem)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Monitor the RAM usage of a Fortigate device, ensuring that it remains within acceptable thresholds to prevent network performance degradation.

Available Parameters
^^^^^^^^^^^^^^^^^^^^

- Community Name (default: public)

Check Fortigate Network (check_fortigate_net)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Monitor the network traffic on a Fortigate device, ensuring that it remains within acceptable thresholds to prevent congestion and bottlenecks.

Available Parameters
^^^^^^^^^^^^^^^^^^^^

- Community Name (default: public)
- Warning Bytes (default: 500000)
- Critical Bytes (default: 1000000)

Check Fortigate Sessions (check_fortigate_ses)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Monitor the session count on a Fortigate device, ensuring that it remains within acceptable thresholds to prevent resource exhaustion.

Available Parameters
^^^^^^^^^^^^^^^^^^^^

- Community Name (default: public)
- Warning Sessions (default: 4500)
- Critical Sessions (default: 6000)

Check Fortigate Slave CPU (check_fortigate_slave_cpu)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Monitors the CPU usage of a slave unit in a Fortigate cluster, ensuring that it remains within acceptable thresholds for optimal performance.

Available Parameters
^^^^^^^^^^^^^^^^^^^^

- Community Name (default: public)

Check Fortigate Slave RAM (check_fortigate_slave_mem)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Monitor the RAM usage of a slave unit in a Fortigate cluster, ensuring that it remains within acceptable thresholds to prevent performance degradation.

Available Parameters
^^^^^^^^^^^^^^^^^^^^

- Community Name (default: public)

Check Fortigate Slave Network (check_fortigate_slave_net)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Monitor the network traffic on a slave unit in a Fortigate cluster, ensuring that it remains within acceptable thresholds to prevent congestion and bottlenecks.

Available Parameters
^^^^^^^^^^^^^^^^^^^^

- Community Name (default: public)
- Warning Bytes (default: 500000)
- Critical Bytes (default: 1000000)

Check Fortigate Slave Sessions (check_fortigate_slave_ses)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This command monitors the session count on a slave unit in a Fortigate cluster, ensuring that it remains within acceptable levels to prevent resource exhaustion.

Available Parameters
^^^^^^^^^^^^^^^^^^^^^

- Community Name (default: public)
- Warning Sessions (default: 4500)
- Critical Sessions (default: 6000)

Check Fortigate VPN (check_fortigate_vpn)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Monitor the status of VPN connections on a Fortigate device, ensuring that they are operational and secure. This check supports both IPSec and SSL/OpenVPN connections.

Available Parameters
^^^^^^^^^^^^^^^^^^^^

- Community Name (default: public)
- VPN Mode: ipsec, ssl, both (default: both)

Check Fortigate Access Points (check_fortigate_wtp)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the status of FortiAPs (WTPs) on a Fortigate device, ensuring that they are operational and properly configured.

Available Parameters
^^^^^^^^^^^^^^^^^^^^

- Community Name (default: public)




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

Source
------

From https://github.com/riskersen/Monitoring/tree/master/fortigate
