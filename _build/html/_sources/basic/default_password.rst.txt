NEMS Administrator User
=======================

Default Username and Password
-----------------------------

The default username on a fresh installation of NEMS Linux is *nemsadmin*.
This is used to sign-in to your NEMS Server (over SSH or keyboard connected
to your NEMS Server) only until you
run `nems-init <../commands/nems-init.html>`__.

**Username:** *nemsadmin*

**Password:** *nemsadmin*

Post-Initialization
-------------------

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

Multiple User Environments
--------------------------

At present, NEMS Linux is single-tenant. This means that if you wish to give
one of your staff access to your NEMS Server, you would need to give them
your NEMS Administrator credentials. This will change as NEMS Linux evolves.
Please consider supporting the project `on Patreon <https://patreon.com/nems>`__
to help fund the development of NEMS Linux.
