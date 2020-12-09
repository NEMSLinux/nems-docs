Check Command: check_nems_osb
=============================

Monitor the status of your NEMS Migrator Off-Site Backup.
If your backup fails, this check will notify you.

.. figure:: ../img/check_nems_osb.png
  :width: 600
  :align: center
  :alt: check_nems_osb output in NEMS Adagios

  check_nems_osb output in NEMS Adagios (circa NEMS Linux 1.6)
  
If you do not have a NEMS Cloud Services account, ``check_nems_osb``
will return an *UNKNOWN* state.

Additionally, even if the last backup was successful, ``check_nems_osb``
will go into a *WARNING* state if the backup has not run for a couple days.

The included sample will not notify you if it is in this state (only
*WARNING*, *CRITICAL* and *RECOVERED* will notify, unless you change
the notification options of the included sample service).

``check_nems_osb`` does not have any arguments. By adding it to your
NEMS host, it will check and notify based on the state of your backups.
There are no thresholds required since a failed backup is *CRITICAL*, and
a successful backup is *OK*.
