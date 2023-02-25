Check Commands: check_synology
==============================

Requires NEMS Linux 1.6.

Description
-----------

Use SNMP to check Synology NAS.

Assigning your Synology NAS host to the ``Synology`` Host Group in NEMS Configurator adds the following sample Advanced Services:

- Synology Disks
- Synology Fans
- Synology Power
- Synology RAID
- Synology System
- Synology UPS
- Synology Version

By default, the *admins* contact group will be notified.

The sample Advanced Services provided in NEMS Linux assume the community name to use is `public`.

Compatibility
-------------

Tested with the following versions of Synology DiskStation Manager:

- DSM 6.2.2-24922 Update 4
- DSM 7.0-41890
- DSM 7.1.1-42962 Update 4

This isn't to say you must run one of these versions. Rather, these are simply the versions we have tested with successfully. It can be assumed that the Synology checks built-in to NEMS Linux will also work with other point releases of DSM.

Source
------

``check_synology`` uses `check_snmp_synology <https://github.com/corben2/check_snmp_synology>`__.
