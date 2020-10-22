Check Commands: custom_check_mem
================================

NEMS Linux includes
the `custom_check_mem <https://support.nagios.com/kb/article/memory-checks-774.html>`__ checkcommand,
as well as an Advanced Service called *Memory Usage NRPE* to allow
checking of remote systems.

It is recommended to add *Memory Usage NRPE* to
the *linux-servers* hostgroup.

For WMI, use *check_win_mem* instead.