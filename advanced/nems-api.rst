nems-api
========

*nems-api* is a web-based api interface that outputs json data related
to your NEMS server. It is lightweight, fast, and offers a connection
for both internal NEMS features and third-party devices.

*nems-api* will always return either *success: true* or *success: false*
to tell you whether a query was successful or not.

IP Restrictions
---------------

By default, access to *nems-api* is limited to the following IP
addresses:

-  127.0.0.1
-  10.0.0.0 - 10.255.255.255
-  172.16.0.0 - 172.31.255.255
-  192.168.0.0 - 192.168.255.255

If you need to add an outside IP address, please put in a feature
request in the Community Forum to add this feature to NEMS-SST. If there
is demand for it, it will be added.

Secure Certificate
------------------

NEMS Linux uses self-signed certificates. In order to pull *nems-api*
data over ssl (ie., https), you must ignore the certificates via your
application.

Command Examples
----------------

All examples in this document assume that the API is available at

::

   http://nems.local/nems-api/

-  http://nems.local/nems-api/hosts - output all configured hosts
-  http://nems.local/nems-api/services - output all configured services
-  http://nems.local/nems-api/downtimes - output all scheduled downtimes
-  http://nems.local/nems-api/hosts?Columns=name,state - output all host
   names along with their current state

Response Format
~~~~~~~~~~~~~~~

All responses are in JSON and have the following format:

::

   {"success": <bool>, "content": <object>}

If "success" is true, "content" will contain the requested data. If
false, it will contain

::

   {"code": <int>, "message": <string>}

where "code" is the mk-livestatus error code and "message" is a
human-readable explanation of the error.

Query interface
~~~~~~~~~~~~~~~

The query interface returns a list of objects in JSON. The available
endpoints are the same as the tables available from mk-livestatus
itself:

-  hosts
-  services - Nagios services, joined with all data from hosts
-  hostgroups
-  servicegroups
-  contactgroups
-  servicesbygroup - all services grouped by service groups
-  servicesbyhostgroup - all services grouped by host groups
-  hostsbygroup - all hosts grouped by host groups
-  contacts
-  commands - your defined Nagios commands
-  timeperiods - time period definitions (currently only name and alias)
-  downtimes - all scheduled host and service downtimes, joined with
   data from hosts and services.
-  comments - all host and service comments
-  log - a transparent access to the nagios logfiles
-  status - general performance and status information. This table
   contains exactly one dataset.
-  columns - a complete list of all tables and columns available via
   Livestatus, including descriptions!
-  statehist - sla statistics for hosts and services, joined with data
   from hosts, services and log.

To retrieve all records from a table, send a GET request to

::

   http://nems.local/nems-api/{tablename}

For example, to get all host records from the server, GET

::

   http://nems.local/nems-api/hosts

Columns
-------

To limit the returned data to a subset of the available fields, pass a
Columns query parameter containing a comma-separated list of column
names. To fetch the name and services list for all hosts:

::

   http://nems.local/nems-api/hosts?Columns=name,services

Filters
-------

To filter the result set to records meeting some criteria, pass one or
more Filter[] params. Each Filter is a urlencoded LQL filter (see the
[mk-livestatus
documentation](http://mathias-kettner.com/checkmk_livestatus.html#H1:LQL
- The Livestatus Query Language) for detailed LQL filter syntax). If
more than one filter is specified, they are ANDed together. To get all
hosts starting with "api" in state OK (0):

::

   http://nems.local/nems-api/hosts?Filter[]=name - ^api&Filter[]=state = 0

Stats
-----

Stats queries allow you to get a count of objects matching a criteria.
Stats queries return a list of counts and never take a Columns
parameter. You can request several Stats with a single API call. You can
also restrict the objects counted by adding Filters to your query. To
count the number of hosts starting with "api" in state OK:

::

   http://nems.local/nems-api/hosts?&Stats[]=name - ^api&Filter[]=state = 0

Command Interface
~~~~~~~~~~~~~~~~~

All calls to ``nems-api`` to execute Nagios commands **must be HTTP POST
requests**.

Acknowledgements
----------------

Acknowledgements for host and service alerts can be sent via the
``acknowledge_problem`` endpoint.

Acknowledge Host Alerts
~~~~~~~~~~~~~~~~~~~~~~~

::

   curl -is -XPOST https://nems.local/nems-api/acknowledge_problem -d '{"host": "host.example.com", "author": "rfrantz", "comment": "acked from livestatus"}'

Acknowledge Service Alerts
~~~~~~~~~~~~~~~~~~~~~~~~~~

Acknowledging service alerts is similar to host alerts, with the
addition of the ``service`` parameter:

::

   curl -is -XPOST https://nems.local/nems-api/acknowledge_problem -d '{"host": "host.example.com", "service": "Apache", "author": "rfrantz", "comment": "acked from livestatus"}'

Downtime
--------

cancel_downtime
~~~~~~~~~~~~~~~

Existing scheduled downtimes for a host can be canceled.
``cancel_downtime`` expects the ``downtime_id`` parameter. Downtime IDs
can be found by querying a host and extracting the ``downtimes`` array:

::

   curl -s https://nems.local/nems-api/hosts?Filter=name = my_host | jq '.' | grep 'downtimes"' -A 2

   "downtimes": [
       12345
   ],

The subsequent request to cancel the host's downtime is:

::

   curl -s -XPOST 'https://nems.local/nems-api/cancel_downtime' -d '{"downtime_id": "12345"}'

To cancel the downtime for a service, pass the name of the service along
with the downtime_id:

::

   curl -s -XPOST 'https://nems.local/nems-api/cancel_downtime' -d '{"downtime_id": "12345", "service": "CPU"}'

schedule_downtime
~~~~~~~~~~~~~~~~~

Schedule downtime for a host as follows:

::

   curl -s -XPOST 'https://nems.local/nems-api/schedule_downtime' -d '{"host": "host.example.com", "duration": "7200", "author": "rfrantz", "comment": "Downtimed via livestatus"}'

**NOTE**: The ``duration`` field expects a value whose unit is in
seconds.

Downtimes can be scheduled for a particular service by adding a
``"service"`` parameter:

::

   curl -s -XPOST 'https://nems.local/nems-api/schedule_downtime' -d '{"host": "host.example.com", "service": "CPU", duration": "7200", "author": "rfrantz", "comment": "Downtimed via livestatus"}'

Notifications
-------------

disable_notifications
~~~~~~~~~~~~~~~~~~~~~

Notifications for a host, a host's service, or all of the host's
services can be disabled via the ``disable_notifications`` endpoint.

Disable Host Notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request that includes a valid 'host' value:

::

   curl -s -XPOST 'https://nems.local/nems-api/disable_notifications' -d '{"host": "host.example.com"}'

Disable Notifications for a Host's Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request that includes valid 'host' and 'service' values:

::

   curl -s -XPOST 'https://nems.local/nems-api/disable_notifications' -d '{"host": "host.example.com", "service": "httpd"}'

Disable Notifications for All of a Host's Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request that includes a valid 'host' value and set 'scope' to
'all':

::

   curl -s -XPOST 'https://nems.local/nems-api/disable_notifications' -d '{"host": "host.example.com", "scope": "all"}'

enable_notifications
~~~~~~~~~~~~~~~~~~~~

Notifications for a host, a host's service, or all of the host's
services can be enabled via the ``enable_notifications`` endpoint.

Enable Host Notifications
^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request that includes a valid 'host' value:

::

   curl -s -XPOST 'https://nems.local/nems-api/enable_notifications' -d '{"host": "host.example.com"}'

Enable Notifications for a Host's Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request that includes valid 'host' and 'service' values:

::

   curl -s -XPOST 'https://nems.local/nems-api/enable_notifications' -d '{"host": "host.example.com", "service": "httpd"}'

Enable Notifications for All of a Host's Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request that includes a valid 'host' value and set 'scope' to
'all':

::

   curl -s -XPOST 'https://nems.local/nems-api/enable_notifications' -d '{"host": "host.example.com", "scope": "all"}'
