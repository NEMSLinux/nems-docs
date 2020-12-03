.. include:: ../global.rst

NEMS Linux Docker Container
===========================

.. note:: The NEMS Linux Docker Container is not yet publicly available. It is coming soon.

NEMS Linux for Docker **IS NOT YET AVAILBLE**.

Install NEMS Linux for Docker
-----------------------------

Basic Installation
~~~~~~~~~~~~~~~~~~

This command will launch a new Docker container called *nemslinux* using
default settings:

.. code-block:: console

  docker run --hostname nems --mount
  type=tmpfs,destination=/tmp,tmpfs-mode=1777 --mount
  type=tmpfs,destination=/var/www/html/backup/snapshot,tmpfs-mode=1770
  --restart=unless-stopped --stop-timeout 120 --name nemslinux -d
  baldnerd/nemslinux:1.6_build1

Install NEMS Linux Docker Container on a Physical Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker is unlike a standard deployment since by default (with a basic
install) only the host computer will have access to it. That of course
is not ideal for a NEMS Linux server if you wish to be able to
administer it from multiple systems, view dashboards, or use a NEMS
Warning Light.

While NEMS Linux will function fine on a Docker network (eg.,
172.17.0.2), if you wish to have full access to your NEMS Server just as
you would with a physical appliance, you will need to connect it to your
physical network.

The two most common options for specifying a network is to use either
DHCP or a Static IP Address:

Using DHCP
^^^^^^^^^^

.. code-block:: console

  docker run --network=multi-host-network --hostname nems --mount
  type=tmpfs,destination=/tmp,tmpfs-mode=1777 --mount
  type=tmpfs,destination=/var/www/html/backup/snapshot,tmpfs-mode=1770
  --restart=unless-stopped --stop-timeout 120 --name nemslinux -d
  baldnerd/nemslinux:1.6_build1

Using Static IP
^^^^^^^^^^^^^^^

Change the sample 10.0.0.105 IP address to suit your needs.

.. code-block:: console

  docker network connect --ip 10.0.0.105 multi-host-network run --hostname
  nems --mount type=tmpfs,destination=/tmp,tmpfs-mode=1777 --mount
  type=tmpfs,destination=/var/www/html/backup/snapshot,tmpfs-mode=1770
  --restart=unless-stopped --stop-timeout 120 --name nemslinux -d
  baldnerd/nemslinux:1.6_build1

Please see `Docker's Network Connections
documentation <https://docs.docker.com/engine/reference/commandline/network_connect/>`__ for
more help.

With USB Support
~~~~~~~~~~~~~~~~

To connect a USB device such
as `temper <../accessories/temper.html>`__ to your
Docker-based NEMS Server, first determine its /dev assignment on your
host, and then run NEMS as follows, replacing ttyUSB0 with your actual
USB device:

.. code-block:: console

  docker run --device=/dev/ttyUSB0 --hostname nems --mount
  type=tmpfs,destination=/tmp,tmpfs-mode=1777 --mount
  type=tmpfs,destination=/var/www/html/backup/snapshot,tmpfs-mode=1770
  --restart=unless-stopped --stop-timeout 120 --name nemslinux -d
  baldnerd/nemslinux:1.6_build1

Initialize Your Docker-Based NEMS Server
----------------------------------------

Initializing a NEMS Server within a Docker Container is different than
all other platforms.

On the Docker host, simply run:

.. code-block:: console

   docker exec -it nemslinux nems-init

Access NEMS Linux CLI
---------------------

Should you have need to access the NEMS Linux CLI, you may do so by
launching *bash* in your container.

.. code-block:: console

   docker exec -it nemslinux bash
