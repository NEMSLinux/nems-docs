Check Command: check_ibmi*
==========================

Check Commands
~~~~~~~~~~~~~~

`check_ibmi_cpu` - Check the CPU utilization of the IBM i host.
`check_ibmi_jobs` - Check the number of active jobs.
`check_ibmi_disk_config` - Report the disk configuration of the host.


Configuration
~~~~~~~~~~~~~

NEMS Linux includes the command `add_ibmi` to allow you to easily configure the credentials for
your IBM i Host or SST. To run it, access your NEMS Linux terminal and type `sudo add_ibmi`

Once you have added the credentials, you may proceed to add the host to NEMS NConf as usual. Be
sure to add the IBM_i host template to your host configuration in NEMS NConf.

Requirements
~~~~~~~~~~~~

Requires NEMS Linux 1.6+.

Source
~~~~~~
From https://www.ibm.com/support/pages/setting-nagios-plug-ibm-i
