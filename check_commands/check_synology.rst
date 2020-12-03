Check Commands: check_synology
==============================

This feature is coming to NEMS Linux 1.6 (Q1 2021) and the documentation will be improved at that time.

Use SNMP to check Synology NAS.

Assign Synology NAS host to Synology Host Group adds the following sample Advanced Services:

- Synology Disks
- Synology Fans
- Synology Power
- Synology RAID
- Synology System
- Synology UPS
- Synology Version

By default, the *admins* contact group will be notified.

The sample Advanced Services provided in NEMS Linux assume the community name to use is `public`.

``check_synology`` uses `check_snmp_synology <https://github.com/corben2/check_snmp_synology>`__.
