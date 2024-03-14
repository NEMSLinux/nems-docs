Check Proxmox Virtual Environment (check_pve)
=============================================

Monitor your Proxmox VE nodes with individual service checks for hypervisor CPU load, root
filesystem usage on the PVE node, Proxmox VE version, memory usage and swap usage).

.. figure:: ../img/check_pve-version.png
  :width: 600
  :alt: check_pve version Service in NEMS Adagios

Usage
-----

Check Command
~~~~~~~~~~~~~

*check_pve* is part of NEMS Linux 1.7+.

Usage
~~~~~
  
./check_pve variable=value

Check Command Arguments
~~~~~~~~~~~~~~~~~~~~~~~

- ``ip``: IP address of the Proxmox server [Required]
- ``port``: Port number Proxmox is accessible on (default: 8006)
- ``node``: The name of the node you wish to check [Required]
- ``username``: Username of user with PVEAuditor permission set [Required]
- ``password``: Password for that user [Required]
- ``realm``: Authentication realm (Eg., pve or pam) [Required]
- ``check``: Specify the check to perform (load, rootfs, version, memory, swap) [Required]
- ``warn``: Warning threshold [int] percentage (default: 80)
- ``crit``: Critical threshold [int] percentage (default: 95)

CLI Example
~~~~~~~~~~~

.. code-block:: console

  ./check_pve ip=10.0.0.5 port=8006 node=myserver username=auditor password=Str0ngP4ssw0rd realm=pve check=load warn=80 crit=95
