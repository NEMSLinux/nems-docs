Check Command: check_mikrotik
=============================

**check_mikrotik_voltage**
Warning Voltage
Critical Voltage

**check_mikrotik_cpu**
Warning CPU %
Critical CPU %

**check_mikrotik_temp**
Warning Temperature
Critical Temperature

**check_mikrotik_port_sum**
- *ARG1: Test Name*
  - Available Options:
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

**check_mikrotik_port_info**
Same as check_mikrotik_port_sum but output info without any thresholds.

Source: https://github.com/bemworld/check_mikrotik_switch
