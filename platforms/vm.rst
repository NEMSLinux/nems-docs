.. include:: ../global.rst

NEMS Linux Virtual Appliance
============================

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
-  Minimum 6 GB free RAM
-  100 GB hard disk space

*VMware ESXi Only*

-  Version 5.5 or higher. NEMS Linux uses Virtual Hardware Version 10.

Guest Specifications
--------------------

-  64-Bit
-  80 GB Virtual Hard Disk (Dynamic / Thin Provisioning where supported)
-  4 GB RAM

Deployment Notes
----------------

-  **Network Bridge** - Before booting, you must configure your virtual
   Network Interface to use your actual LAN in Bridged mode.
-  **Unique MAC Address** - While configuring your virtual Network
   Interface, you must generate a
   new MAC address for the virtual NIC. If your hypervisor does not
   offer a feature to automatically generate a MAC address you can
   visit `nemslinux.com/api/mac <https://nemslinux.com/api/mac>`__ to
   generate one. Do not simply enter random numbers. **Record your
   virtual MAC address somewhere safe.** Do not change your MAC address
   after initializing NEMS. Doing so would result in your HWID changing,
   which will disassociate your Virtual Appliance with NEMS Cloud
   Services.
-  **CPU Virtualization Features** - x86 Virtualization must be available
   and enabled on your physical CPU
   in order to boot the Virtual Appliance. This is found in your host
   machine's BIOS/UEFI settings and will be called VT-x (Intel) or AMD-V
   (AMD), or something similar such as “Virtualization Extensions”.
-  **Static RAM Mode** - Ensure RAM is :underline:`not` assigned as
   “dynamic” RAM. ESXi, for example, may
   remove all RAM from the appliance if set to dynamic, which will
   result in NEMS Linux not functioning correctly. RAM should be static.

