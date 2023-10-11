Check Command: check_mikrotik
=============================

Commands
--------

check_mikrotik_voltage
~~~~~~~~~~~~~~~~~~~~~~

Warning Voltage
Critical Voltage

check_mikrotik_cpu
~~~~~~~~~~~~~~~~~~

Warning CPU %
Critical CPU %

check_mikrotik_temp
~~~~~~~~~~~~~~~~~~~

Warning Temperature
Critical Temperature

check_mikrotik_port_sum
~~~~~~~~~~~~~~~~~~~~~~~

check_mikrotik_port_sum -ARG1 -ARG2

- *ARG1: Test Name*
    - cpu                  
    - activeFan            
    - voltage              
    - temperature          
    - processorTemperature 
    - current              
    - powerConsumption     
    - psu1State            
    - psu2State
    - disk
    - diskTotal            
    - diskUsed
    - mem
    - memTotal             
    - memUsed              
    - portName             
    - portOperState        
    - portAdminState       
    - portMtu              
    - portMacAddress       
    - portRxDiscards       
    - portTxDiscards       
    - portTxErrors         
    - portRxErrors         
    - portRxPackets        
    - portTxPackets        
    - portTxBytes          
    - portRxBytes
- *ARG2: Switch Ports*
   - Can be single, multiple and ranges possible, for example: 1, 5-10, 22-24

check_mikrotik_port_info
~~~~~~~~~~~~~~~~~~~~~~~~

Same as check_mikrotik_port_sum but output info without any thresholds.

Sample Services
---------------

These need to be converted for NEMS NConf.

**Check Voltage**

This will check each host that is listed in the MikroTik Switches group. It will issue a warning if the voltage is below 23V or above 26V and a critical error if it is below 22V or above 27V

.. code-block:: console

    define service {
            use                     generic-service
            hostgroup_name          MikroTik Switches
            service_description     MikroTik Voltage
            check_command           check_mikrotik_voltage!23:26!22:27
    }

**Check TX Errors**

This test adds up all tx-errors on ports 1-25 (all ports on a CRS125-24G-1S).

.. code-block:: console

    define service {
            use                     generic-service
            hostgroup_name          MikroTik Switches
            service_description     MikroTik TX Errors
            check_command           check_mikrotik_port_sum!portTxErrors!1-25!10!50
    }

**Port Names**

This test returns the port names of ports 1, 3, 4, 5 and 25

.. code-block:: console

    define service {
            use                     generic-service
            hostgroup_name          MikroTik Switches
            service_description     MikroTik Port Names
            check_command           check_mikrotik_port_info!portName!1,3-5,25
    }

Source: https://github.com/bemworld/check_mikrotik_switch
