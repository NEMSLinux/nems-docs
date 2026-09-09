nems-api
========

*nems-api* is a lightweight, web-based RESTful API interface that outputs JSON
data and accepts control commands for your NEMS Linux server. It processes
requests in real time by connecting directly to Nagios via the MK Livestatus
UNIX socket (``live.sock``).

All requests return a standard JSON object containing a top-level ``success``
boolean indicator (``true`` or ``false``).

Amalgamation with nagios-api
---------------------------

With the release of NEMS Linux 1.8 *nems-api* has absorbed the full feature set
and endpoints of the legacy *nagios-api* (formerly ``zorkian/nagios-api``).

- **Legacy Daemon Retirement:** The separate Python service on port ``6315`` is
  deprecated and replaced by *nems-api*.
- **Absorbed Endpoints:** The ``/state`` query endpoint and ``/schedule_check``
  command endpoint have been fully integrated into the REST API route table.
- **Performance Improvement:** Rather than reading realtime Nagios data from disk,
  all state and command queries now interface directly with memory yielding
  microsecond response times and eliminating background service overhead.
- **Unified Security:** Legacy *nagios-api* requests now inherit *nems-api*'s
  subnet filtering and access rules.

IP Restrictions
---------------

By default, access to *nems-api* is strictly restricted to local loopback and
standard private IPv4 subnets (RFC 1918):

- 127.0.0.1 (Loopback)
- 10.0.0.0 - 10.255.255.255 (Class A Private)
- 172.16.0.0 - 172.31.255.255 (Class B Private)
- 192.168.0.0 - 192.168.255.255 (Class C Private)

Requests originating outside these address ranges will receive an HTTP ``403
Forbidden`` response.

If you need to add an outside IP address, please put in a feature request in
the nems-www Issue Tracker requesting this feature be added to NEMS-SST.

Secure Certificate & HTTPS Requirement
---------------------------------------

*nems-api* strictly uses HTTPS. Any unencrypted HTTP requests sent to *nems-api*
will automatically receive an HTTP 301/302 redirect to the secure HTTPS URL.

Because NEMS Linux utilizes self-signed SSL/TLS certificates by default, all API
requests sent via ``curl`` or external applications must ignore certificate 
validation errors by passing the ``-k`` (or ``--insecure``) flag.

Quick Testing Links (Click to Test)
-----------------------------------

If you are on the same local network as your NEMS Server, click any of the links
below to view live sample JSON output directly in your web browser. 

*(Note: If ``nems.local`` does not resolve on your network, replace ``nems.local``
in your browser address bar with your NEMS Server's local IP address).*

- `Full System State Tree <https://nems.local/nems-api/state>`_
- `All Configured Hosts <https://nems.local/nems-api/hosts>`_
- `All Configured Services <https://nems.local/nems-api/services>`_
- `Host Names, States & Addresses <https://nems.local/nems-api/hosts?Columns=name,state,address>`_
- `Active & Scheduled Downtimes <https://nems.local/nems-api/downtimes>`_
- `General System Status & Performance <https://nems.local/nems-api/status>`_
- `Livestatus Schema & Column Descriptions <https://nems.local/nems-api/columns>`_

Response Format
---------------

All responses are in JSON and have the following format:

::

   {"success": <bool>, "content": <object>}

If ``success`` is true, ``content`` will contain the requested data. If false,
it will contain error details:

::

   {"success": false, "content": {"code": <int>, "message": <string>}}

where ``code`` is the HTTP or MK Livestatus error code and ``message`` is a
human-readable explanation of the error.

Query Interface
---------------

All query endpoints expect HTTP GET requests over HTTPS. Command examples assume
the API is available at:

::

   https://nems.local/nems-api/

Absorbed State Endpoint
~~~~~~~~~~~~~~~~~~~~~~~

To fetch the full host and service state tree in a single request (absorbed
from *nagios-api*):

- Click: `state <https://nems.local/nems-api/state>`_
- CLI Example:

::

   curl -sk https://nems.local/nems-api/state

Livestatus Tables
~~~~~~~~~~~~~~~~~

The query interface returns a list of objects in JSON. You can query any MK
Livestatus table directly by clicking its hyperlinked table name or using it as the URL endpoint:

- `hosts <https://nems.local/nems-api/hosts>`_ - all configured hosts
- `services <https://nems.local/nems-api/services>`_ - Nagios services, joined with all data from hosts
- `hostgroups <https://nems.local/nems-api/hostgroups>`_ - host group definitions
- `servicegroups <https://nems.local/nems-api/servicegroups>`_ - service group definitions
- `contactgroups <https://nems.local/nems-api/contactgroups>`_ - contact group definitions
- `servicesbygroup <https://nems.local/nems-api/servicesbygroup>`_ - all services grouped by service groups
- `servicesbyhostgroup <https://nems.local/nems-api/servicesbyhostgroup>`_ - all services grouped by host groups
- `hostsbygroup <https://nems.local/nems-api/hostsbygroup>`_ - all hosts grouped by host groups
- `contacts <https://nems.local/nems-api/contacts>`_ - configured contacts
- `commands <https://nems.local/nems-api/commands>`_ - your defined Nagios commands
- `timeperiods <https://nems.local/nems-api/timeperiods>`_ - time period definitions (currently name and alias)
- `downtimes <https://nems.local/nems-api/downtimes>`_ - all scheduled host and service downtimes, joined with data from hosts and services
- `comments <https://nems.local/nems-api/comments>`_ - all host and service comments
- `log <https://nems.local/nems-api/log>`_ - transparent access to Nagios log files
- `status <https://nems.local/nems-api/status>`_ - general performance and status information (contains exactly one dataset)
- `columns <https://nems.local/nems-api/columns>`_ - complete list of all tables and columns available via Livestatus, including descriptions
- `statehist <https://nems.local/nems-api/statehist>`_ - SLA statistics for hosts and services, joined with data from hosts, services, and log

To retrieve all records from a table, send a GET request to:

::

   https://nems.local/nems-api/{tablename}

For example, to get all host records from the server:

::

   curl -sk https://nems.local/nems-api/hosts

Columns
~~~~~~~

To limit the returned data to a subset of available fields, pass a ``Columns``
query parameter containing a comma-separated list of column names:

- Click: `hosts?Columns=name,state,address <https://nems.local/nems-api/hosts?Columns=name,state,address>`_
- CLI Example:

::

   curl -sk "https://nems.local/nems-api/hosts?Columns=name,state,address"

Filters
~~~~~~~

To filter the result set, pass one or more ``Filter[]`` parameters. Each Filter
is a URL-encoded LQL filter. If more than one filter is specified, they are
ANDed together:

- Click: `hosts?Filter[]=state%20=%200 <https://nems.local/nems-api/hosts?Filter[]=state%20=%200>`_
- CLI Example:

::

   curl -sk "https://nems.local/nems-api/hosts?Filter[]=name%20~%20^api&Filter[]=state%20=%200"

Stats
~~~~~

Stats queries return a list of counts matching specified criteria:

- Click: `hosts?Stats[]=state%20=%200 <https://nems.local/nems-api/hosts?Stats[]=state%20=%200>`_
- CLI Example:

::

   curl -sk "https://nems.local/nems-api/hosts?Stats[]=state%20=%200"

Command Interface
-----------------

All calls to *nems-api* to execute Nagios commands **must be HTTP POST requests**
over HTTPS containing a JSON payload.

Forced Re-checks
~~~~~~~~~~~~~~~~

schedule_check
^^^^^^^^^^^^^^

Force an immediate host or service check execution (absorbed from *nagios-api*).

**Force Host Check:**

::

   curl -sk -X POST https://nems.local/nems-api/schedule_check \
     -d '{"host": "host.example.com"}'

**Force Service Check:**

::

   curl -sk -X POST https://nems.local/nems-api/schedule_check \
     -d '{"host": "host.example.com", "service": "PING"}'

Acknowledgements
~~~~~~~~~~~~~~~~

acknowledge_problem
^^^^^^^^^^^^^^^^^^^

Acknowledge active alerts for hosts or services.

**Acknowledge Host Alert:**

::

   curl -sk -X POST https://nems.local/nems-api/acknowledge_problem \
     -d '{"host": "host.example.com", "author": "nems-admin", "comment": "Investigating outage"}'

**Acknowledge Service Alert:**

::

   curl -sk -X POST https://nems.local/nems-api/acknowledge_problem \
     -d '{"host": "host.example.com", "service": "Apache", "author": "nems-admin", "comment": "Fix in progress"}'

Downtime Management
~~~~~~~~~~~~~~~~~~~

schedule_downtime
^^^^^^^^^^^^^^^^^

Schedule downtime for a host or service. Note that the ``duration`` field expects
a value in seconds.

**Schedule Host Downtime:**

::

   curl -sk -X POST https://nems.local/nems-api/schedule_downtime \
     -d '{"host": "host.example.com", "duration": "7200", "author": "nems-admin", "comment": "OS Patching"}'

**Schedule Service Downtime:**

::

   curl -sk -X POST https://nems.local/nems-api/schedule_downtime \
     -d '{"host": "host.example.com", "service": "CPU", "duration": "3600", "author": "nems-admin", "comment": "Database maintenance"}'

cancel_downtime
^^^^^^^^^^^^^^^

Existing scheduled downtimes can be canceled using the ``downtime_id`` parameter.

**Cancel Host Downtime:**

::

   curl -sk -X POST https://nems.local/nems-api/cancel_downtime \
     -d '{"downtime_id": "12345"}'

**Cancel Service Downtime:**

::

   curl -sk -X POST https://nems.local/nems-api/cancel_downtime \
     -d '{"downtime_id": "12345", "service": "CPU"}'

Notifications
~~~~~~~~~~~~~

disable_notifications
^^^^^^^^^^^^^^^^^^^^^

Disable notifications for a host, a specific service, or all host services.

**Disable Host Notifications:**

::

   curl -sk -X POST https://nems.local/nems-api/disable_notifications \
     -d '{"host": "host.example.com"}'

**Disable Notifications for a Host's Service:**

::

   curl -sk -X POST https://nems.local/nems-api/disable_notifications \
     -d '{"host": "host.example.com", "service": "httpd"}'

**Disable Notifications for All Host Services:**

::

   curl -sk -X POST https://nems.local/nems-api/disable_notifications \
     -d '{"host": "host.example.com", "scope": "all"}'

enable_notifications
^^^^^^^^^^^^^^^^^^^^

Enable notifications for a host, a specific service, or all host services.

**Enable Host Notifications:**

::

   curl -sk -X POST https://nems.local/nems-api/enable_notifications \
     -d '{"host": "host.example.com"}'

**Enable Notifications for a Host's Service:**

::

   curl -sk -X POST https://nems.local/nems-api/enable_notifications \
     -d '{"host": "host.example.com", "service": "httpd"}'

**Enable Notifications for All Host Services:**

::

   curl -sk -X POST https://nems.local/nems-api/enable_notifications \
     -d '{"host": "host.example.com", "scope": "all"}'
