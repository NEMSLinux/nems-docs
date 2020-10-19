NEMS Administrator User
=======================

Default Username and Password
-----------------------------

The default username for initial setup is *nemsadmin*. This is used to
sign-in to your NEMS server (over SSH or keyboard connected to your NEMS
server) only until you
run `nems-init <https://docs.nemslinux.com/commands/nems-init>`__.

**Username:** *nemsadmin*

**Password:** *nemsadmin*

Once your ``nems-init`` process is complete, you will need to instead
sign-in as your newly created account (which you specify
during *nems-init*).

When you initialize NEMS, you will provide a password for the NEMS web
interfaces. This username/password will be what you use to access NEMS
features (eg., nCONF, Nagios Core, NagVis, Check_MK, Samba, Webmin, SSH,
etc.).

.. Warning:: **Do not** use the traditional *passwd* command to change your NEMS
             administrator's password. Doing so will leave your system in a broken
             state (which can be fixed by running the correct command). Instead,
             use ``sudo nems-passwd``