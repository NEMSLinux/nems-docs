NEMS Command Line Tests
=======================

Run some command line tests manually.

Internet Speed Test
-------------------

When manually running a speedtest, it is important to note your settings
in NEMS SST. Ie., if you change the server to a manually chosen server
number, but have NEMS SST set to use the automatically detected server,
your switch will be ignored.

/usr/lib/nagios/plugins/check_speedtest-cli.sh -w 5 -W 5 -c 1 -C 1 -l e
-s \`nems-info speedtest-server\`
