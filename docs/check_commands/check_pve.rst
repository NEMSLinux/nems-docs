Check Proxmox Virtual Environment (check_pve)
=============================================

Monitor your Proxmox VE nodes with individual service checks for hypervisor CPU load, root
filesystem usage on the PVE node, Proxmox VE version, memory usage and swap usage).

.. figure:: ../img/check_pve-version.png
  :width: 600
  :alt: check_pve version Service in NEMS Adagios

Usage
-----

.. note:: *check_pve* requires NEMS Linux 1.7 or higher.

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

Configuration
~~~~~~~~~~~~~

- On Proxmox VE
  - Create a new user for NEMS Linux to use for the API.
  - Assign this new user **PVEAudit** permissions.
- In NEMS NConf:
  - Create a host entry for your Proxmox VE server.
  - Add the `check_pve` service to that host, setting the arguments appropriately for your environment.
  - Generate your NEMS config.

.. Warning:: Never use your Proxmox VE root user or any user with more than **PVEAudit** permissions for monitoring.

CLI Example
~~~~~~~~~~~

.. code-block:: console

  ./check_pve ip=10.0.0.5 port=8006 node=myserver username=auditor password=Str0ngP4ssw0rd realm=pve check=load warn=80 crit=95

Output
------

Performance Data
~~~~~~~~~~~~~~~~

``check_pve`` outputs PerfData for further inspection, historical record or aggregation.

All ``check_pve`` checks log their regular response (E.g., rootfs provides PerfData for the percentage of root filesystem usage).

The following check provide additional Performance Data:

``load``

- Current CPU load in percentage
- The low and high CPU load in percentage over the last 15 minutes
- Number of available threads
- Load average (1m, 5m, 15m)

``version``

- Currently running version of Proxmox
- Latest version of Proxmox available

``swap``

- Swap usage in percentage
- Swap space available
- Swap space usage

Cache
-----

`check_pve` connects to your Proxmox VE server to generate a ticket to access the API with. This ticket is cached on your NEMS Server and
re-used for the lifetime of the ticket. Tickets are automatically invalidated by PVE every 2 hours, so NEMS will automatically refresh
your cached ticket every 90 minutes. Make sure you are careful to input the correct PVEAuditor username and password on every instance of
`check_pve` in your environment, otherwise you may experience odd authentication issues when the cache is recreated by an incorrectly-entered
username/password combination.

We also cache the Proxmox version API JSON response to your NEMS Server for 6 hours, ensuring your server always knows the latest version, but
without overtaxing the API.

Caches are stored in `/tmp/pve_*.cache` which means if a miscreant obtained physical access to your NEMS Server they have up to 2 hours before your
PVE API ticket expires. It is therefore imperative that you never use your `root` user or any user who has more than PVEAudit permissions to monitor
a PVE server.
