NEMS Linux To Do List
=====================

This list details features which are planned for future releases of NEMS
Linux. NEMS Linux is released on a semi-annual basis, with a major
release usually falling in or around May and November. Thanks to the
NEMS Linux Migrator, upgrading is a cinch, and thanks to NEMS Linux'
rolling release system, many fixes, patches and upgrades can find their
way into existing installations.

Urgent Issues
-------------

- Backport the new NEMS Linux 1.6 speedtest to 1.5.x


Feature Requests
----------------

This is a curation of various feature requests which have been approved for
further assessment and possible implementation for the next major release of
NEMS Linux.

You can submit a feature request either via Discord (in
#feature-requests) or the Community Forum (in Feature Requests).

-  Add `TrueNAS check command <https://github.com/StewLG/check_truenas_extended_play>`__
-  `Custom icons as per
   Amheus <https://forum.nemslinux.com/viewtopic.php?f=10&t=733&p=3265#p3265>`__ Possible duplicate of `their Discord message <https://discord.com/channels/501816361706717184/654697565937205278/721028392602042410>`__
-  Backup custom icons, should they exist, `as per Baldnerd's note <https://discord.com/channels/501816361706717184/654697565937205278/743125075267682494>`__.
-  Attempt to port check_juniper to modern code `per Baldnerd's comment <https://discord.com/channels/501816361706717184/654697565937205278/743479405908852758>`__ in response to `Neptunum's request <https://discord.com/channels/501816361706717184/654697565937205278/687335872370049044>`__.
-  Log a tabular speedtest report `as per Professor Eric <https://discord.com/channels/501816361706717184/654697565937205278/785579865713803324>`__
-  Explore `RobPickering's notes about Let's Encrypt no longer requiring servers be publicly accessible <https://discord.com/channels/501816361706717184/654697565937205278/791760428186861590>`__. Something to integrate?
-  Add custom Nagios theme support `as per Sly <https://discord.com/channels/501816361706717184/654697565937205278/840230232959090748>`__.
-  While PoE fan should work fine in 1.6 due to upstream fixes from Raspberry Pi, test and make sure before release `as per jaffascout <https://forum.nemslinux.com/viewtopic.php?p=3545>`__.

Features That I Like, But Can't Implement Yet
---------------------------------------------

-  PagerDuty integration `as per ElvisNuno <https://discord.com/channels/501816361706717184/654697565937205278/807482477027000411>`__.


During the 1.6 Release Cycle (Not At Launch)
--------------------------------------------

-  Add Elgato StreamDeck controller support
   via https://github.com/abcminiuser/python-elgato-streamdeck
-  Add multi-tenant support as requested by Kevin Quiambao. Ability to
   add extra users who have access to certain features, such as Adagios
   / Nagios reporting. ULA if possible.
-  Integrate notification tests for Telegram and Pushover.
-  Move notification tests to NEMS Dashboard (rather than Linux
   terminal).
-  Explore integration of ULA for staff.
-  Add sound effects to NEMS TV Dashboard on state change as per
   BastyJuice. See http://www.storiesinflight.com/html5/audio.html
-  NanoPi M4 Ethernet MAC address changes every reboot. Thanks to
   UltimateBugHunter for reporting.
-  The TV output on ODROID-C1+ Build 1 doesn't work. Fix this.
-  DONE in 1.6 - Add `NCPA <https://www.nagios.org/ncpa/?__hstc=189745844.6f4567e25069d3a733d5058a22c1187e.1566995089857.1566995089857.1567168833486.2&__hssc=189745844.2.1567168833486&__hsfp=4019080588#downloads>`__ support.
-  If NEMS is unable to communicate with github, a nems-upgrade will
   erroneously upgrade NEMS' version number even though the upgrade
   itself will have failed, as `reported by
   baggins <https://forum.nemslinux.com/viewtopic.php?f=9&t=93>`__.
-  Documentation at the checkcommands level improved, along with other
   step-by-step guides added to the documentation.
-  Add an audible alarm to NEMS TV Dashboard as
   per `ronjohntaylor <https://forum.nemslinux.com/viewtopic.php?f=10&t=406>`__.
-  NEMS NConf interface revamped to match NEMS' overall look and feel.
   Branding improved. (Is a Patreon goal. Please consider supporting.)
-  Evaluate `nconf PR #
   4 <https://github.com/Cat5TV/nconf/pull/4>`__ for merge.
-  Create NEMS Linux Docker container. (Is a Patreon goal. Please
   consider supporting.)
-  Adagios interface customized to remove features not part of NEMS
   Linux.
-  Make it so NEMS Off Site Backup sends the server the file size before
   the file, which will allow me to log an error if the user's file size
   exceeds the limit (rather than just silently failing).
-  Take a look at `this
   report <https://forum.nemslinux.com/viewtopic.php?f=38&t=405>`__ and make sure
   it is not affecting users in 1.5.

User Requests to Review During Release Cycle
--------------------------------------------

-  Review this plugin and see if it's something that I can squeeze
   in: https://forum.nemslinux.com/viewtopic.php?f=10&t=398 Not liking the fact
   that it is a Windows program.
-  Check ssl `as per
   Zerant <https://forum.nemslinux.com/viewtopic.php?f=10&t=425>`__ (thought not
   particularly needed since check_http supports this already).
-  Add check_pfsense `as per
   mydogboris <https://forum.nemslinux.com/viewtopic.php?f=10&t=412&p=2391&hilit=pfsense#p2391>`__.
-  Veeam checks `as per
   Premium <https://forum.nemslinux.com/viewtopic.php?f=10&t=398&p=3336&hilit=veeam#p3336>`__.
-  Web interface to upload a backup.nems file for restoration as per
   LordOfLevels🔊. Perhaps user can run *nems-restore webupload* and a
   code will be provided which can be entered into the form to confirm
   legitimate usage, and the restore will wait, checking a tmpdir for a
   file upload. Progress and status displayed within the bash window and
   restore prompts “Are you sure” as soon as the upload is complete.

.. _known-issues-1:

Known Issues
============

These issues will be fixed in due time.

-  Number of services per page selection not working in Nagios Core `as
   per baggins <https://forum.nemslinux.com/viewtopic.php?f=38&t=95&p=745&hilit=results#p745>`__.
-  As per `Ricks <https://forum.nemslinux.com/viewtopic.php?f=10&t=707>`__ add
   ability for NEMS to auto-discover hosts and perhaps even compatible
   services. This has been added as a Patreon goal.
-  As pointed out by tripled, check_nconf treats ARG1 as command (-c) in
   its entirety. So we receive “NRPE: Command 'check_disk -w 80 -c 90 -p
   /media/pi” as the full line is treated as command. It should be
   sending -c “check_disk” -a “-w 80 -c 90 -p /media/pi” - will likely
   need to fix the check_command which may break it for those who hacked
   it up by changing the arg to, for example, check_disk“ -a ”-w 80 -c
   90 -p /media/pi
-  Bland-X3 reports: “Have a bug/issue. Check_snmp has issues with
   creating files when using the –rate switch (-C CommunityGoesHere -P
   2c -o .1.3.6.1.2.1.2.2.1.10.1 -w 80000 -c 102400 –rate) results in
   Status Information: Cannot create directory: /usr/var/111 … Can run
   command in CLI using sudo and does record the rate information which
   indicates simple permission problem or can modify the check_snmp
   command to save it somewhere else with permission maybe.” - Quick
   guess is maybe the command was run as root user from CLI which has
   now locked the nagios user from being able to access the folders.
   Will need to test. Also,
   see https://support.nagios.com/forum/viewtopic.php?f=7&t=45864
-  Static IP doesn't persist after reboot in Virtual Appliance. Reported
   by dr_patso and confirmed by 🇨🇷 Benedetti -Ale Morera-.
-  🇨🇷 Benedetti -Ale Morera- reported NEMS SST breaking TLS settings if
   enable background Blur and save. I have not been able to replicate
   this.
-  *check_wmi_plus* has never contained the functionality for the
   documented *checkdns* feature. This has lead to some users saying the
   feature (which is an available check command in NEMS based on their
   docs) doesn't work. Need to remove this check command, and add a new
   one – perhaps *check_dns $HOSTNAME$ $HOSTADDRESS$* which will ensure
   the  of the host matches.
   
Ideas for Future
----------------

There is not necessarily a planned timeline for each of these items, but
here is a list of some of the things I do hope to do in an upcoming
release. This list covers *potential* features for future releases of
NEMS Linux. None of these are set in stone, and should only be
considered ideas.

-  Add `SNMP Trap
   support <https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/int-snmptrap.html>`__ `as
   per mpacey <https://forum.nemslinux.com/viewtopic.php?f=10&t=92&p=2842&hilit=intrusion#p2842>`__?
-  Write a language sub-system for the NEMS UI, allowing users to offer
   translation corrections via . Attempt to migrate the language system
   to all interfaces, including NConf, Adagios, and even nems-info and
   nems-init.
-  Configure Adagios and NEMS to support multiple NEMS servers.
   See `this
   manpage <https://github.com/opinkerfi/adagios/wiki/Users-guide>`__.
   (It is possible NEMS Cloud will do away with this need).
-  Evaluate `openITCockpit <https://github.com/it-novum/openITCOCKPIT>`__ as
   a possible front-end.
-  Add feature to nems-migrator's off site backup that allows a user to
   request an email if their backup fails (can get the email info from
   NEMS SST and send email accordingly, separate of Nagios). Perhaps add
   a service check on the NEMS server instead? - Planning to add this
   feature to NEMS Cloud during the 1.5-1.6 release cycle.
-  Add auto-discovery
   functionality. `this <https://vanheusden.com/java/ScanToNag/>`__ and `this <https://exchange.nagios.org/directory/Addons/Configuration/Auto-2DDiscovery>`__?
-  Make it so first boot automatically takes user into nems-init, with
   the option of instead running it through SSH.
-  Move all commands from commands.cfg to checkcommands.cfg (or
   whichever is more appropriate) within NEMS Migrator.
-  Add some generic true/false data to NEMS Anonymous Stats. In
   particular, discover if any users are using features like Telegram.
   By knowing this, I can decide if a feature should be removed from
   future releases.
-  **Ability to use external storage for all active data.** Ideal for
   reducing read/writes on SD cards. Add interface to allow all active
   data to be saved to an external hard drive or network share as suggested
   by meveric.
-  Build a graphical interface for nems-init.
-  Build a graphical interface for NEMS Migrator's “Restore”
   feature.
-  Add intrusion detection such as Snort or Bro IDS, `as per
   mpacey <https://forum.nemslinux.com/viewtopic.php?f=10&t=92&p=715&hilit=snort#p715>`__.

NEMS Linux Roadmap
------------------

-  1.0 - COMPLETE - Initial release. Bring easy deployment of Nagios to
   Raspberry Pi 3.
-  1.1 - COMPLETE - Creation of upgrade process, nems-migrator and
   optimize performance.
-  1.2 - COMPLETE - Creation of nems-init process to setup initial
   system. Create documentation.
-  1.3 - COMPLETE - Focus on feature set, add off site backup. Being
   laying the groundwork for upcoming 1.4 (in particular, non-Pi
   architectures).
-  1.4 - COMPLETE - New build of NEMS Linux featuring support for
   multiple SBC options and Nagios 4.
-  1.5 - COMPLETE - Focused on integrating user-requested options (mostly check
   commands) and optimizing the defaults/samples. Begin multi-server
   environment back-end, starting with ability to nickname NEMS servers
   via NEMS-SST. Introduction of more SBCs and virtual appliances.
-  1.6 - UX and feature updates. Refine the list of supported devices, removing any
   that are not being used. New peripheral options such as NEMS Warning Light.
-  1.7 - Deprecation of git as an update backend. Now, fully using dpkg repository.
   Complete deprecation of Python 2.7. NEMS Linux to be moved entirely to 64-bit image.
-  1.8 - Begin focusing on UX and feature consolidation. Remove unneeded
   features from NEMS Adagios. Create new interface for NConf that
   matches the NEMS Dashboard interface. Add a safe reboot button to
   NEMS SST. Migrate as many options away from the terminal as possible,
   including nems-init. Write nems-mailtest into nems-sst `as per
   mydogboris <https://forum.nemslinux.com/viewtopic.php?f=10&t=372&p=2178&hilit=nems+mailtest#p2178>`__.
