Resolving DNS Hostnames on LAN
==============================

NEMS Linux uses two main Linux components to resolve \*.local hostnames:

1. **avahi-daemon** - This allows other computers to see NEMS
   Linux.local on the 
2. **libnss-mdns** - This allows NEMS Linux to see other \*.local
   computers on the 

In order for NEMS Linux to be able to resolve a  hostname rather than IP
address, multicast must be enabled on the client system.

-  **Microsoft Windows Target** - If you already have iTunes installed,
   you do not need to do anything else (since it's included). Otherwise,
   you can install `Apple's Bonjour
   service <https://support.apple.com/kb/DL999?locale=en_US>`__ or you
   can enable Microsoft's own Link-Local Multicast Name Resolution
   (LLMNR) service.
-  **Linux Target** - Install *avahi-daemon*. It will automatically
   enable itself during installation. It's in your favorite package
   manager already.
-  **macOS Target** - No need to install anything; it's already
   included.

**Important Note About Firewall** - If the target computer has a
firewall enabled, you'll also need to allow UDP traffic through ports
5353 and 53791.