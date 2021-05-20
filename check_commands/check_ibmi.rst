Check Command: check_ibmi*
==========================

Check Commands
~~~~~~~~~~~~~~

.. list-table:: IBM i Check Commands in NEMS Linux
   :widths: 25 75
   :header-rows: 1

   * - Command Name in NEMS NConf
     - Description
   * - check_ibmi_cpu
     - Check the CPU utilization of the entire IBM i host.
   * - check_ibmi_job_cpu
     - Check the CPU usage of a specific job.
   * - check_ibmi_overload_jobs
     - Retrieve the number of jobs that exceeds the expected CPU usage.
   * - check_ibmi_temp_jobs
     - Retrieve top jobs that have the most temp storage usage. Number of jobs is user configurable.
   * - check_ibmi_jobs
     - Check the number of active jobs.
   * - check_ibmi_disk_config
     - Report the disk configuration of the host.
   * - check_ibmi_disk_usage
     - Disk usage.
   * - check_ibmi_asp_usage
     - Retrieve the ASP usage percentage of the entire system.
   * - check_ibmi_disk
     - Disk utilization.
   * - check_ibmi_messages
     - Check IBM i messages. **I do not know what the 'ty' argument represents. If you know, please message me or create a PR.**
   * - check_ibmi_message
     - Check if a specific message (by Message ID) exists in a specific message queue. May be a comma-separated list of Message IDs.
   * - check_ibmi_page_faults
     - Check for page faults.
   * - check_ibmi_subjobs
     - Number of subsystem jobs.
   * - check_ibmi_sql
     - Retrieve the longest running SQL.
   * - check_ibmi_sql_custom
     - The user could leverage SQL services to create self-defined matrix. That's what the manual says. Someone, please clarify.
   * - check_ibmi_users
     - Report the number of users currently logged in (no thresholds or notifications).
   * - check_ibmi_info
     - Report basic info about the IBM i host.
   * - check_ibmi_integration
     - Check if the IBM i NEMS Linux integration daemon is running. If not, make sure you enabled it in NEMS SST (it is disabled by default).

Configuration
~~~~~~~~~~~~~

NEMS Linux includes the command `add_ibmi` to allow you to easily configure the credentials for
your IBM i Host or SST. To run it, access your NEMS Linux terminal and type `sudo add_ibmi`

Once you have added the credentials, you may proceed to add the host to NEMS NConf as usual. Be
sure to add the IBM_i host template to your host configuration in NEMS NConf.

Environment
-----------

GROUP PTF
- V7R1: SF99701 LEVEL 38
- V7R2: SF99702 LEVEL 16
- V7R3: SF99703 LEVEL 4

USER PROFILE
- check-ibmi-long-run-sql needs *ALLOBJ
- check-ibmi-disk-config  needs *ALLOBJ,*SERVICE,*IOSYSCFG

PORT
- as-central	8470
- as-database	8471
- as-dtaq		8472
- as-file		8473
- as-netprt	8474
- as-rmtcmd	8475
- as-signon	8476
- as-svrmap	449

Requirements
~~~~~~~~~~~~

Requires NEMS Linux 1.6+.

Source
~~~~~~
From https://www.ibm.com/support/pages/setting-nagios-plug-ibm-i
