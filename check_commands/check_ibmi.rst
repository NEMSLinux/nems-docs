Check Command: check_ibmi*
==========================

Check Commands
~~~~~~~~~~~~~~

-  `check_ibmi_cpu` - Check the CPU utilization of the IBM i host.
-  `check_ibmi_jobs` - Check the number of active jobs.
-  `check_ibmi_disk_config` - Report the disk configuration of the host.
-  `check_ibmi_disk_usage` - Disk usage.
-  `check_ibmi_asp_usage` - ASP disk usage.
-  `check_ibmi_disk` - Disk utilization.
-  `check_ibmi_messages` - Check IBM i messages. **I do not know what the 'ty' argument represents. If you know, please message me or create a PR.**
-  `check_ibmi_message` - Check for a specific message by Message ID. May be a comma-separated list of Message IDs.
-  `check_ibmi_page_faults` - Check for page faults.
-  `check_ibmi_subjobs` - Number of subsystem jobs.
-  `check_ibmi_temp_jobs` - Report a designated number of temporary storage jobs.
-  `check_ibmi_sql` - Long run SQL check.
-  `check_ibmi_sql_custom` - Custom SQL check.
-  `check_ibmi_users` - Report the number of users currently logged in (no thresholds or notifications).
-  `check_ibmi_job_cpu` - Check the CPU usage of a specific job.
-  `check_ibmi_overload_jobs` - Report the CPU overload number of jobs.
-  `check_ibmi_info` - Report basic info about the IBM i host.
-  `check_ibmi_integration` - Check if the IBM i NEMS Linux integration daemon is running. If not, make sure you enabled it in NEMS SST (it is disabled by default).

Configuration
~~~~~~~~~~~~~

NEMS Linux includes the command `add_ibmi` to allow you to easily configure the credentials for
your IBM i Host or SST. To run it, access your NEMS Linux terminal and type `sudo add_ibmi`

Once you have added the credentials, you may proceed to add the host to NEMS NConf as usual. Be
sure to add the IBM_i host template to your host configuration in NEMS NConf.

Environment
-----------

GROUP PTF
V7R1: SF99701 LEVEL 38
V7R2: SF99702 LEVEL 16
V7R3: SF99703 LEVEL 4

USER PROFILE
check-ibmi-long-run-sql needs *ALLOBJ
check-ibmi-disk-config  needs *ALLOBJ,*SERVICE,*IOSYSCFG

PORT
as-central	8470
as-database	8471
as-dtaq		8472
as-file		8473
as-netprt	8474
as-rmtcmd	8475
as-signon	8476
as-svrmap	449

Requirements
~~~~~~~~~~~~

Requires NEMS Linux 1.6+.

Source
~~~~~~
From https://www.ibm.com/support/pages/setting-nagios-plug-ibm-i
