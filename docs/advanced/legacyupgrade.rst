NEMS Migrator: Upgrade NEMS 1.0 or nagiospi to latest NEMS
==========================================================

Thanks for being an early-adopter! Whether you're coming from NEMS 1.0
or its predecessor, nagiospi, I want to make it as easy as possible for
you to get the latest and greatest, without having to reconfigure
everything. It's been exciting to see the NEMS project really catching
on, and I endeavor to make it the best it can be. Your suggestions along
the way have helped me focus on some great features for as NEMS
continues to evolve.

NEMS 1.1+ has a nifty backup and export tool called NEMS Migrator. While
it comes pre-packaged in 1.1+, I designed it specifically to run on
legacy builds as well (NEMS 1.0 or nagiospi), giving you the opportunity
to export your old configuration, deploy the latest version of NEMS, and
then restore the configuration to NEMS. Easy peasy!

Here's what you need to do:

.. note:: These instructions are for NEMS 1.0 or nagiospi only. **Do not** do this on NEMS 1.1+ as the tool is already built-in.

1. SSH into your legacy NEMS/nagiospi server.

2. Become root:

.. code-block:: console

   sudo su

3. Update repository data.

.. code-block:: console

   apt-get update

4. Install Git.

.. code-block:: console

   apt-get install git

5. Install NEMS-Migrator in /tmp.

.. code-block:: console

   cd /tmp && git clone https://github.com/Cat5TV/nems-migrator

6. Create the backup config on your NEMS/nagiospi system. 

If on NEMS 1.0:

.. code-block:: console

    cd /tmp/nems-migrator && ./backup.sh

If on nagiospi: 

.. code-block:: console

    cd /tmp/nems-migrator && ./nagiospi2nems.sh

7. Download the backup to your computer by opening it in your web
   browser. In your favorite web browser, simply add /backup/ to the end
   of your NEMS/nagiospi server address. Eg., *http://10.0.0.5/backup/*

8. Now that you have your backup.nems file, follow `the instructions to
   restore your configuration to a new version of
   NEMS <https://docs2.nemslinux.com/en/latest/commands/nems-restore.html>`__.