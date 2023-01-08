NEMS Linux Source Code
======================

Are you a coder or want to explore some of the things NEMS does under
the hood? Perhaps you'd like to add some features or fix a bug. Or
maybe you just found an issue that you'd like to report. This is all
done through our GitHub repositories and the associated Issue trackers.

NEMS Linux itself is a Linux distro built by pre-compiling several tools
into a customized Debian server base. The features of NEMS is
fascilitated by combining these tools (Eg., Nagios, Monitorix,
Webmin, Check_MK) plus integration of a wide variety of custom applications
to make NEMS a complete, well-rounded enterprise-ready distribution.

You can explore these custom scripts `on GitHub
<https://github.com/NEMSLinux?tab=repositories>`__.

Debpack
-------

Debpack is a custom front-end developed by NEMS Linux's develoeprs and used
by NEMS Linux's provision infrastructure, which compiles Debian packages
for distribution via the NEMS Linux Debian repositories located at
https://repos.nemslinux.com/

When browsing our source code, you will often see a folder called `debpack`
in the root folder of the repository. Entering this folder will provide you
with the root tree of the application. E.g., `/debpack/usr/local/bin/nems-info`
will place a file on the NEMS Server at `/usr/local/bin/nems-info`

Official Repositories
---------------------

NEMS Admin
~~~~~~~~~~

`nems-admin` is where the scripts live that build the NEMS Linux distributable
image. Generally users will never need this repository since it's only used by
our development team to create new images, but if you are having a problem
specifically with one of our distros (E.g., not booting on a new model Raspberry
Pi) this would be the appropriate repository to post your issue. Think: if it
has to do with the image itself (not the software contained therein), this is
the place.

- Issue Tracker: https://github.com/NEMSLinux/nems-admin/issues/
- Source Code: https://github.com/NEMSLinux/nems-admin/

NEMS Migrator
~~~~~~~~~~~~~

`nems-migrator` is the suite of tools that provides an automated backup
(both onsite and offsite) to NEMS Servers, and also provides the utilities
to restore a backup to a new NEMS Server. If restoring your `backup.nems`
file shows issues, this is where to report it.

- Issue Tracker: https://github.com/NEMSLinux/nems-migrator/issues/
- Source Code: https://github.com/NEMSLinux/nems-migrator/

NEMS Migrator Data
~~~~~~~~~~~~~~~~~~

`nems-migrator-data` is where the sample data resides for NEMS Migrator.
Generally this is not a place for end users. We separated the data from
the main `nems-migrator` application to reduce the time to perform a
`nems-update` when `nems-migrator` is updated (as the sample data is
unlikely to change). NEMS Migrator uses the sample data not only for
restoration of backups, but this data is also tapped into by tools such
as `nems-init`, which is included in the `nems-scripts` repository. If you
are having issues with NEMS Migrator, this is not the correct repository:
You'd be looking for `nems-migrator` above.

- Issue Tracker: https://github.com/NEMSLinux/nems-migrator-data/issues/
- Source Code: https://github.com/NEMSLinux/nems-migrator-data/

NEMS Scripts
~~~~~~~~~~~~

`nems-scripts` contains custom scripts to perform a variety of NEMS Linux
tasks. Examples would be the `nems-init` command and `nems-quickfix`.
NEMS Scripts also contains the underlying code to provision the operation of
checks such as `temper` and `speedtest`. If you are having an issue with a
check command, it's more likely you're looking for `nems-plugins` below.
NEMS Scripts is generally not user-serviceable and simply fascilitates
features our developers tap into in order to provide functionality to other
tools within NEMS Linux.

- Issue Tracker: https://github.com/NEMSLinux/nems-scripts/issues/
- Source Code: https://github.com/NEMSLinux/nems-scripts/

NEMS Plugins
~~~~~~~~~~~~

`nems-plugins` are the check commands included in NEMS NConf. If you're
having an issue with a particular check command, this is most likely the
place to post an issue.

- Issue Tracker: https://github.com/NEMSLinux/nems-plugins/issues/
- Source Code: https://github.com/NEMSLinux/nems-plugins/

NEMS Tools
~~~~~~~~~~

`nems-tools` provides some "behind the scenes" functionality to NEMS Linux,
such as NEMS GPIO Extender and NEMS Warning Light.

- Issue Tracker: https://github.com/NEMSLinux/nems-tools/issues/
- Source Code: https://github.com/NEMSLinux/nems-tools/

nems-www
~~~~~~~~

`nems-www` provides the web site interface and navigation of NEMS Dashboard.

- Issue Tracker: https://github.com/NEMSLinux/nems-www/issues/
- Source Code: https://github.com/NEMSLinux/nems-www/

NEMS TV Dashboard
~~~~~~~~~~~~~~~~~

`nems-tv` provides NEMS TV Dashboard.

- Issue Tracker: https://github.com/NEMSLinux/nems-tv/issues/
- Source Code: https://github.com/NEMSLinux/nems-tv/

NEMS NConf
~~~~~~~~~~

`nconf` provides the PHP side of NEMS NConf. This system utilizes a MySQL
database which exists within `nems-migrator-data`.

- Issue Tracker: https://github.com/NEMSLinux/nconf/issues/
- Source Code: https://github.com/NEMSLinux/nconf/

WMIC
~~~~

`wmic` provides Microsoft Windows' WMI compatibility for NEMS Linux
(Windows Management Instrumentation).

- Issue Tracker: https://github.com/NEMSLinux/wmic/issues/
- Source Code: https://github.com/NEMSLinux/wmic/

Hardware Detection
~~~~~~~~~~~~~~~~~~

`hw-detect` allows NEMS Linux to detect and update the running NEMS
Server's hardware profile.

- Issue Tracker: https://github.com/NEMSLinux/hw-detect/issues/
- Source Code: https://github.com/NEMSLinux/hw-detect/

9590
~~~~

`9590` provides a simple tool to respond on port 9590 for testing TCP
port up/down status. Part of the `NEMS Linux Getting Started Guide <https://docs.nemslinux.com/>`__.

- Issue Tracker: https://github.com/NEMSLinux/9590/issues/
- Source Code: https://github.com/NEMSLinux/9590/

NEMS Documentation
~~~~~~~~~~~~~~~~~~

`nems-docs` is the Restructured Text source code for the NEMS Linux
documentation found at https://docs.nemslinux.com/ - if you contribute
via a PR, please ensure you add your name to the credits.

- Issue Tracker: https://github.com/NEMSLinux/nems-docs/issues/
- Source Code: https://github.com/NEMSLinux/nems-docs/
