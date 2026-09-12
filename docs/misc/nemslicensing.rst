=====================
NEMS Linux Licensing
=====================

NEMS Linux is deeply committed to open-source software. Because NEMS Linux is a complete operating system distribution, it is composed of custom NEMS code, open-source third-party utilities, and hardware firmware, each governed by its respective license terms.

NEMS Linux Core (AGPLv3)
========================

NEMS Linux core scripts, custom management tools, and web interfaces developed specifically for NEMS Linux are licensed under the **GNU Affero General Public License version 3 (AGPLv3)**.

* **Full License Text:** https://www.gnu.org/licenses/agpl-3.0.en.html

**In simple terms:** You are free to inspect, modify, and distribute the core NEMS source code. If you modify NEMS Linux and make it accessible to users over a network, you must make your modified source code publicly available under the same AGPLv3 terms.

Editions & Commercial Usage
===========================

NEMS Linux is offered in two primary deployment tiers:

* **SOHO / Hobbyist Edition:** Free to download, deploy, and use for personal home labs, hobbyists, and small office networks.
* **Enterprise Edition:** Deploying NEMS Linux to monitor corporate, enterprise, or commercial production environments requires an official **NEMS Linux Enterprise Subscription**. Enterprise subscriptions provide production-ready virtual appliances (OVA, VHD, QCOW2), Cloud Services, off-site encrypted backups, and direct technical SLA support.

For commercial subscription details, visit: https://nemslinux.com/

Third-Party Open Source Components
==================================

NEMS Linux is built on top of Debian GNU/Linux and integrates established third-party open-source projects (such as Nagios Core, various check plugins, and system utilities).

* Third-party software components retain their respective upstream open-source licenses (GPL, MIT, Apache, BSD, etc.).
* Full license and copyright notices for all installed system packages can be inspected locally on any running NEMS system under `/usr/share/doc/*/copyright`.

Third-Party Firmware & Hardware Compatibility
=============================================

To ensure broad hardware compatibility (such as network adapters and specialized hardware controllers) right out of the box, NEMS Linux pre-installs hardware firmware binaries sourced from Debian's `non-free-firmware` repository.

All included proprietary firmware files remain the property of their respective hardware vendors and are distributed under their original manufacturer licenses.

Artwork, Assets, and Branding
=============================

* **Wallpapers:** Included background wallpapers are released under **CC0 (Public Domain)**.
* **Trademarks & Branding:** The "NEMS Linux" name, logos, and official project branding are protected. Distributing a modified version of NEMS Linux code under the AGPLv3 does not grant permission to use NEMS Linux logos or branding for commercial re-distribution without explicit authorization.

Disclaimer of Warranty
======================

NEMS Linux is provided **"AS IS"** without warranty of any kind, express or implied. The NEMS Linux project, its maintainers, and contributors accept no liability for data loss, service interruption, or operational damages resulting from the deployment or use of this software.
