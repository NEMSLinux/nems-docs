Check MS SQL Memory Usage (check_mssql_mem)
###########################################

Monitor your MS SQL 2008, 2012 or 2019 server memory usage.

*check_mssql_mem* requires NEMS Linux 1.7 or higher.


Configuring MS SQL Server
*************************

Install NSClient++ w/ NRPE and enable it on your MS SQL server, ensuring
"allow_arguments" and "allow_nasty_meta_chars" options are enabled.
  
Enable SQL Server Perfmon Counters.
  
**Parameters:**

- `Port` MS SQL port. [Default 5666]
- `Check` Determines which check to run:
  - **db_memory_calc** - Calculates SQL Memory in use [Default]
  - **db_pages_used** - Pages in use in MB
  - **db_pages_total** - Total pages in MB
- `Warning %` - Specify max percentage for a WARNING state.
- `Critical %` - Specify max percentage for a CRITICAL state.


Source
------

Originally from https://github.com/grune/Nagios/blob/master/Nagios/nagios-mssql-memory.py
with significant changes for NEMS Linux in order to upgrade to Python 3 and enable Server
2019 support.
