Resolving DNS Hostnames on LAN
==============================

Introduction
------------

NEMS Linux uses two main Linux components to resolve `*`.local
hostnames:

1. **avahi-daemon** - This allows other computers to see the `nems.local` host on the LAN.
2. **libnss-mdns** - This allows NEMS Linux to see other `*`.local computers on the LAN.

Enabling Multicast Name Resolution
----------------------------------

In order for NEMS Linux to be able to resolve a DNS hostname to its IP address, multicast must be enabled on the client system.

Most modern systems will already provide multicast in one shape or another, so you only need to take action if a host is not replying to its hostname.

- **Microsoft Windows Target** - Multicast is provided by the *Link-Local Multicast Name Resolution (LLMNR)* service which can be enabled or disabled using the computer's group policy (Local Computer Policy -> Computer Configuration -> Administrative Templates -> Network -> DNS Client). Otherwise, it is also included with a local installation of iTunes, or alternatively you can install `Apple's Bonjour service <https://support.apple.com/kb/DL999?locale=en_US>`__.
- **Linux Target** - Simply install *avahi-daemon*. It will automatically enable itself during installation. avahi-daemon is in your distro's official repositories, so can be installed via any package manager.
- **macOS Target** - No need to install anything; it's already included.

.. note::

   If the target computer has a firewall enabled, you'll also need to allow UDP traffic through ports 5353 and 53791.
