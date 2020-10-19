####################
Available Platforms
####################

*************************************
NEMS Linux on Single Board Computers
*************************************

When choosing your hardware, general SBC comparisons are not necessarily
relevant since you will be deploying a NEMS Linux server specifically.
As an example, an ODROID-C2 vs Raspberry Pi 3 comparison will say
Raspberry Pi 3 has better support for video drivers. Well, that won't
matter to you; you're using NEMS Linux and we've pre-built the distro
for you. So because of this, it is helpful to review `the NEMS Linux
Stats page <https://nemslinux.com/stats/>`__, and `join our Discord
Server <https://discord.gg/e9xT9mh>`__ to make an educated decision.

Here are some general guidelines.

1. eMMC storage is better than an SD Card. This is a universal truth. SD
   Cards have a high failure rate whereas eMMC tends to operate with
   perceptively similar reliability to a traditional SSD. NEMS performs
   a lot of read/write operations, as you can imagine, so the more
   reliable your storage medium, the more reliable your NEMS Server.
2. More RAM means better performance. The minimum recommended RAM is 1 ,
   though 2  or higher will greatly improve performance and reliability
   of your NEMS Server.

Visit `the NEMS Linux web site <https://nemslinux.com/>`__ for a
complete list of supported platforms.

Raspberry Pi
------------

|image1|

`BUY NOW <https://cat5.tv/pi/>`__

Pine64
------

|image2|

Hardkernel ODROID XU4
---------------------

|image3|

FriendlyElec
------------

|image4|

Orange Pi
---------

|image5|

ASUS Tinker Board / S
---------------------

|image6|

ASUS Tinker Board S must be switched to Maskrom boot mode in order to
boot from SD card. The built-in eMMC is not big enough to run NEMS Linux
from.

Khadas VIM3
-----------

|image7|

You can boot from SD or USB, then install NEMS Linux to the integrated
eMMC storage by typing *sudo nems-install*

NEMS Linux Appliance
--------------------

|image8|

*****************************
NEMS Linux Virtual Appliance
*****************************

The NEMS Linux Virtual Appliance is only available
to `Patrons <https://patreon.com/nems>`__.

The NEMS Linux virtual appliance has 3 available releases:

-  **NEMS OVA** (Open Virtual Appliance) can be easily deployed on
   virtualization hypervisors such as VMware ESXi, vSphere, Player or
   Workstation or Oracle VirtualBox. The OVA package contains the entire
   virtual appliance and is ready to import and boot.
-  **NEMS VHD** (Virtual Hard Disk) can be used to deploy NEMS Linux on
   Microsoft Hyper-V.
-  **NEMS QCOW2** (QEMU Copy-On-Write) can be used to deploy NEMS Linux
   on QEMU, KVM, Proxmox VE, and other hypervisors that support the
   QCOW2 format.

The underlying software in each release is identical. The individual
releases are created in order to ease deployment across a variety of the
most popular virtualization hypervisors.

Host Requirements
-----------------

*All Hypervisors*

-  VT-x/AMD-V capable CPU with feature enabled in BIOS/UEFI
-  Minimum 6  free RAM
-  100  hard disk space

*VMware ESXi Only*

-  Version 5.5 or higher. NEMS Linux uses Virtual Hardware Version 10.

Guest Specifications
--------------------

-  64-Bit
-  80  Virtual Hard Disk (Dynamic / Thin Provisioning)
-  4  RAM

Deployment Notes
----------------

-  Before booting, you must configure your virtual Network Interface to
   use your actual  in Bridged mode.
-  While configuring your virtual Network Interface, you must generate a
   new MAC address for the virtual NIC. If your hypervisor does not
   offer a feature to automatically generate a MAC address you can
   visit `nemslinux.com/api/mac <https://nemslinux.com/api/mac>`__ to
   generate one. Do not simply enter random numbers. **Record your
   virtual MAC address somewhere safe.** Do not change your MAC address
   after initializing NEMS. Doing so would result in your HWID changing,
   which will disassociate your Virtual Appliance with NEMS Cloud
   Services.
-  x86 Virtualization must be available and enabled on your physical CPU
   in order to boot the Virtual Appliance. This is found in your host
   machine's BIOS/UEFI settings and will be called VT-x (Intel) or AMD-V
   (AMD), or something similar such as “Virtualization Extensions”.
-  Ensure RAM is not assigned as “dynamic” RAM. ESXi, for example, may
   remove all RAM from the appliance if set to dynamic, which will
   result in NEMS Linux not functioning correctly. RAM should be static.

**************************************
NEMS Linux Amazon Machine Image (AMI)
**************************************

The NEMS Linux Amazon Machine Image is available in the Amazon EC2
Community AMIs marketplace. Simply search for *NEMS Linux* when
launching your instance.

Important Note
--------------

Your being here means you are an early adopter of NEMS Linux on Amazon
Web Services. During this early testing phase, it is available through
the community marketplace. However, once NEMS has been tried-and-true,
it will be moving into the Amazon Marketplace. This means it will
inevitably fall under Amazon's fee structure. For now, it's as free as
Amazon allows me to make it.

AMI IDs
-------

The NEMS Linux AMI is found under *Community AMIs* on us-east-1 (N.
Virginia). If you wish to deploy on a different AWS Service Endpoint and
are a current Patron supporting the project on Patreon, please let me
know and I will copy the AMI to your preferred region. Since this costs
me extra money to do, I only do it by request, and only for those who
contribute to the project.

-  NEMS 1.5 AMI Build 1 - ami-03480e018178d1c75

Introduction
------------

NEMS Linux AMI leverages Amazon's T2 instance types, dramatically
reducing the cost of running a NEMS Server in the Cloud by bursting to
full core performance only when required. T2 instances are also
available to use in the AWS Free Tier, which includes 750 hours of
t2.micro instances each month for one year for new AWS customers.

The NEMS Linux AMI is an amd64 build.

AWS Requirements
----------------

The NEMS Linux AMI requires the following:

-  If monitoring 1-20 hosts: t2.micro or higher EC2 instance
-  If monitoring more than 20 hosts: t2.medium or higher EC2 instance
-  an elastic IP address
-  volume is 16GB by default and may need to be increased in time

Deployment Notes
----------------

-  **Important:** Before booting, you must configure an elastic IP
   address for your NEMS Linux instance. Failure to do this will break
   several features, including NEMS Cloud Services, NEMS CheckIn, and
   your daily backup.

-  To access NEMS Linux remotely, you will need to configure your
   Security Group for the NEMS Linux instance to allow incoming
   connections on the NEMS Linux ports
   (See `Networking <https://docs.nemslinux.com/networking>`__ for more
   info). It is recommended to make these accessible only from your
   trusted IP addresses.

-  NEMS Linux allows you to use either username/password combinations or
   username/key pair combinations to login via SSH. As this could pose a
   security issue, please ensure only your own IP address has access to
   NEMS Linux ports (in your EC2 Security Group configuration for the
   instance).

   -  Default username: **nemsadmin**
   -  Default password: **nemsadmin**

Known Issues
------------

-  If you run a *nems-init* on a NEMS Server that has already been
   initialized, your public key will need to be manually imported. This
   will be improved in future, but wasn't a high priority as it should
   not affect many people (if anyone).


****************************
NEMS Linux Docker Container
****************************

The NEMS Linux Docker Container is coming soon. It is currently
in *heavy testing*. If you decide to try it, please do not do so in a
production environment, and be sure to report any issues on our Discord
server.


Install NEMS Linux for Docker
-----------------------------

Basic Installation
~~~~~~~~~~~~~~~~~~

This command will launch a new Docker container called *nemslinux* using
default settings:

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

docker run --network=multi-host-network --hostname nems --mount
type=tmpfs,destination=/tmp,tmpfs-mode=1777 --mount
type=tmpfs,destination=/var/www/html/backup/snapshot,tmpfs-mode=1770
--restart=unless-stopped --stop-timeout 120 --name nemslinux -d
baldnerd/nemslinux:1.6_build1

Using Static IP
^^^^^^^^^^^^^^^

Change the sample 10.0.0.105 IP address to suit your needs.

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
as `temper <https://docs.nemslinux.com/hardware/temper>`__ to your
Docker-based NEMS Server, first determine its /dev assignment on your
host, and then run NEMS as follows, replacing ttyUSB0 with your actual
USB device:

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

docker exec -it nemslinux nems-init

Access NEMS Linux CLI
---------------------

Should you have need to access the NEMS Linux CLI, you may do so by
launching *bash* in your container.

docker exec -it nemslinux bash
