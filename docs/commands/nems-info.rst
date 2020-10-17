NEMS Linux Commands: nems-info
==============================

*nems-info* parses and outputs a great deal of useful information about
your NEMS Linux deployment. This data is used by various NEMS Linux
features, but can also be called manually if desired.

*nems-info* does not require root privileges, and can be called from any
folder on your NEMS Linux server.

Available Command Options
-------------------------

-  ``nems-info ip`` - Output the IP address of your NEMS Linux
   server. Automatically detects which interface is in use.
-  ``nems-info nemsver`` - Output the currently running full
   version of NEMS Linux, including rolling update subversion.
-  ``nems-info nemsbranch`` - Output the currently running branch
   version of NEMS Linux, excluding rolling update subversion.
-  ``nems-info nemsveravail`` - Output the latest available
   version of NEMS Linux.
-  nems-info  users`` - Output the number of users connected to
   your NEMS Linux server (ie., through SSH or direct console).
-  ``nems-info diskusage`` - Output how much disk usage you are
   currently using on your NEMS Linux server, in percentage.
-  ``nems-info  memusage`` - Output a memory usage breakdown of
   your NEMS Linux server.
-  ``nems-info  country`` - Output the country code of your NEMS
   Linux server, based on the timezone settings you configured
   during `nems-init <https://docs.nemslinux.com/commands/nems-init>`__.
-  ``nems-info  hwver`` - Output the revision of your NEMS Linux
   server hardware.
-  ``nems-info hwid`` - Output your NEMS Linux server's unique
   NEMS Hardware ID.
-  ``nems-info platform`` - Output which platform your NEMS Linux
   server is running on.
-  ``nems-info platform-name`` - Output the name of the platform
   NEMS Linux is running on using local database.
-  ``nems-info drives`` - Output a JSON list of all your NEMS
   Linux server's available storage media.
-  ``nems-info loadaverage`` - Output your NEMS Linux server's
   weekly load average.
-  ``nems-info temperature`` - Output the current average CPU
   temperature.
-  ``nems-info sslcert`` - Display your NEMS SSL certificate
   information.
-  ``nems-info nic`` - Display the network interface (eg., eth0,
   wlan0, enp2s0) currently being used.
-  ``nems-info checkport ####``- See if a port is running on the
   NEMS server. Used to determine if services are up or down. For
   example, to see if apache2 is resonding: *nems-info checkport 80*
-  ``nems-info cpupercent`` - Output the current CPU usage as a
   number representing percent.
-  ``nems-info init`` - Detect if this NEMS server has been
   initialized or not. Returns 0 (not initialized) or 1 (initialized).
-  ``nems-info username`` - Output the username for this NEMS
   server as
   per `nems-init <https://docs.nemslinux.com/commands/nems-init>`__.
-  ``nems-info online`` - Detect if the NEMS Server is online /
   can communicate with GitHub. Returns 0 for false, 1 for true.
-  ``nems-info socket``- Provide the location of the livestatus
   socket.
-  nems-info hosts`` - Output a count of how many hosts you are
   currently monitoring (uses livestatus).
- ``nems-info services`` - Output a count of how many services
   you are currently monitoring (uses livestatus).
-  ``nems-info benchmark [test-name]`` Outputs numeric
   result of NEMS Benchmark. Will return 0 if test has not yet been run
   via cron task, or if being run on an unsupported version of NEMS
   (requires 1.4+). Generally not for end-users. Used by `NEMS Anonymous
   Stats <https://docs.nemslinux.com/anonymous_stats>`__ and `GiggleScore.com <https://gigglescore.com/>`__.
   Available tests: cpu io ram mutex 7z-m 7z-s
-  ``nems-info state`` Output the state information of NEMS hosts
   and services that are in a problem state to JSON format. Honors the
   NEMS TV Dashboard display setting in NEMS SST (immediate display or
   in accordance to service notification settings).
-  ``nems-info state all`` Output the state information of all
   NEMS hosts and services to JSON format, regardless of state.
-  ``nems-info alias`` Output the alias of your NEMS Linux server.
-  ``nems-info cloudauth`` Check if this NEMS server is authorized
   to use `NEMS
   Cloud <https://docs.nemslinux.com/features/nems-cloud>`__. 1 = yes, 0
   = no.
-  ``nems-info cloudauthcache`` Output the last status of this
   NEMS server's authorization to use `NEMS
   Cloud <https://docs.nemslinux.com/features/nems-cloud>`__. 1 = yes, 0
   = no. Loads from a log file rather than realtime result, making this
   a faster way to load the status.
-  ``nems-info allowupdate`` Show NEMS' automatic update setting.
   1 = Not allowed, 2 = Allowed monthly, 3 = Allowed semi-weekly, 4 =
   Allowed weekly, 5 = Allowed daily
-  ``nems-info wifi`` Output a json-encoded list of detected WiFi
   networks.
-  ``nems-info checkin`` See if user has enabled NEMS Cloud
   Services CheckIn emails. 0 for no, 1 for yes.
-  ``nems-info checkinemail`` Output the email address used for
   CheckIn notifications (configured in NEMS SST).
-  ``nems-info checkininterval`` Output the number of intervals
   before CheckIn notifications are sent. Each interval is 15 minutes
   long. Default is 8, which is 2 hours. Set in NEMS SST.
-  ``nems-info webhook`` Output webhook url as configured in NEMS
   SST.
-  ``nems-info quickfix`` Advise whether a background NEMS update
   is occurring. 0 is no, 1 is yes.
-  ``nems-info fixes`` Advise whether a background NEMS fixes is
   occurring. 0 is no, 1 is yes.
-  ``nems-info piwatcher`` Advise whether a `PiWatcher
   hat <https://cat5.tv/piwatcher>`__ is connected to the NEMS Server.
-  ``nems-info pivoyager`` Advise whether a `PiVoyager
   pHAT <https://cat5.tv/pivoyager>`__ is connected to the NEMS Server.
-  ``nems-info rootfulldev`` Output the full block device name of
   the root partition.
-  ``nems-info rootdev`` Output the root device of the filesystem
   without the partition number.
-  ``nems-info rootpart`` Output the partition number of the root
   filesystem without the block device name.
-  ``nems-info speedtest`` Output current automatically-selected
   speedtest server.
-  ``nems-info speedtest best`` Output the best server.
-  ``nems-info speedtest which`` Output 0 if using
   automatically-selected speedtest server (automatically updates itself
   each day based on which server is best). Output 1 if using the server
   number provided in the ARGS on the check_command in NEMS NConf.
-  ``nems-info fileage [file]`` Output the age of any file on the
   NEMS server. Particularly helpful in determining how long a process
   has been running. Eg., *nems-info fileage /var/run/nems-quickfix.pid*
-  ``nems-info tv_require_notify`` Output the NEMS TV Dashboard
   setting for notification state. 1=Require notification state,
   2=Display state information immediately.
-  ``nems-info tv_24h`` Output the clock format setting for NEMS
   TV Dashboard (configured in NEMS SST). 1=15:35, 2=3:35 PM, 3=3:35
-  ``nems-info livestatus`` Output JSON result of full livestatus
   query.
-  ``nems-info temper`` Output JSON response from
   supported `TEMPer <https://docs.nemslinux.com/hardware/temper>`__ hardware.
-  ``nems-info frequency`` Output the current CPU operating
   frequency in realtime, averaged across all cores.
-  ``nems-info perfdata_cutoff`` Output the cutoff (in days) for
   perfdata retention, as configured in NEMS SST. All perfdata that
   falls outside this number of days will be automatically purged.
-  ``nems-info repos`` Output JSON list of NEMS repositories with
   their operational state. A result of 0 means someone has modified the
   local instance and thereby broken the repository (it will no longer
   be able to update, which could break features in future). A value of
   1 means the repository is fine and being managed by NEMS Linux.
-  ``nems-info [dht11|dht22]`` Output JSON
   response from a connected `DHT
   Sensor <https://docs.nemslinux.com/hardware/dht-sensors>`__.