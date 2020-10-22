Check Command: check_http
=========================

Check the status of a HTTP/HTTPS server running on a domain or IP
address on a remote host.

The included default check_https command uses the IP address of your
host, as configured in NEMS Configurator.

check_http Argument Syntax
--------------------------

+----+-----------------+---------------------------------------------+
| -H | --hostname      | host name of the server where HTTP (or      |
|    |                 | HTTPS) daemon is running                    |
+----+-----------------+---------------------------------------------+
| -I | --IP-address    | ip address of the HTTP (or HTTPS) server    |
+----+-----------------+---------------------------------------------+
| -p | --port          | Port number where HTTP server runs. Default |
|    |                 | is 80                                       |
+----+-----------------+---------------------------------------------+
| -4 | --use-ipv4      | This will use IPv4 connection               |
+----+-----------------+---------------------------------------------+
| -6 | --use-ipv6      | This will use IPv6 connection               |
+----+-----------------+---------------------------------------------+
| -S | --ssl           | This will use HTTPS using default 443 port  |
+----+-----------------+---------------------------------------------+
|    | --sni           | Enable SSL/TLS hostname extension support   |
|    |                 | (SNI)                                       |
+----+-----------------+---------------------------------------------+
| -C | --certificate   | Minimum number of days a SSL certiface must |
|    |                 | be valid.                                   |
+----+-----------------+---------------------------------------------+
| -e | --expect        | Expected response string. Default is HTTP/1 |
+----+-----------------+---------------------------------------------+
| -s | --string        | Expected content string.                    |
+----+-----------------+---------------------------------------------+
| -u | --url           |  to check                                   |
+----+-----------------+---------------------------------------------+
| -P | --post          |  encoded http POST data                     |
+----+-----------------+---------------------------------------------+
| -N | --no-body       | Do not wait for whole document body to      |
|    |                 | download. Stop once the headers are         |
|    |                 | downloaded.                                 |
+----+-----------------+---------------------------------------------+
| -M | --max-age       | Check whether a document is older than x    |
|    |                 | seconds. Use 5 for 5 seconds, 5m for 5      |
|    |                 | minutes, 5h for 5 hours, 5d for 5 days.     |
+----+-----------------+---------------------------------------------+
| -T | --content-type  | Indicate content type in header for POST    |
|    |                 | request                                     |
+----+-----------------+---------------------------------------------+
| -l | --linespan      | Regular expression can span to new line     |
|    |                 | (Use this with -r or -R option)             |
+----+-----------------+---------------------------------------------+
| -r | --regex, --ereg | Use this regular expression to search for   |
|    |                 | string in the HTTP page                     |
+----+-----------------+---------------------------------------------+
| -R | --eregi         | Same as above, but with ignore case.        |
+----+-----------------+---------------------------------------------+
| -a | --authorization | If the site uses basic authentication send  |
|    |                 | uid, pwd in the format uid:pwd              |
+----+-----------------+---------------------------------------------+
| -A | --useragent     | Pass the specified string as “User Agent”   |
|    |                 | in HTTP header.                             |
+----+-----------------+---------------------------------------------+
| -k | --header        | Add additional tags that should be sent in  |
|    |                 | the HTTP header.                            |
+----+-----------------+---------------------------------------------+
| -L | --link          | The output is wrapped as  link              |
+----+-----------------+---------------------------------------------+
| -f | --onredirect    | When a  is redirected, use this to either   |
|    |                 | follow the , or send ok, warning, or        |
|    |                 | critical notification                       |
+----+-----------------+---------------------------------------------+
| -m | --pagesize      | Specify the minimum and maximum page size   |
|    |                 | expected in bytes. Format is                |
|    |                 | minimum:maximum                             |
+----+-----------------+---------------------------------------------+
| -m | --pagesize      | Specify the minimum and maximum page size   |
|    |                 | expected in bytes. Format is                |
|    |                 | minimum:maximum                             |
+----+-----------------+---------------------------------------------+
| -w | --warning       | Response time in seconds for warning state  |
+----+-----------------+---------------------------------------------+
| -c | --critical      | Response time in seconds for critical state |
+----+-----------------+---------------------------------------------+
| -t | --timeout       | Number of seconds to wait before connection |
|    |                 | times out. Default is 10 seconds            |
+----+-----------------+---------------------------------------------+

NEMS Configurator Service Parameter Examples
--------------------------------------------

Check if a host is responding on the default http port (ie., 80):

[blank]

Check if a host is responding on the default https port (ie., 443):

-S

Check if a host is responding on an alternate https port (ie., 8080):

-S -p 8080

Check the state of the hosts SSL certificate and treat as a problem if
it expires in 30 days or less:

-C 30

Troubleshooting
---------------

**I receive a message “CRITICAL - Cannot make SSL connection. SSL alert
number 40” when trying to check a secure web site**

Are you using Cloudflare or another SSL redirecting system where your
certificate might be shared with other hostnames? Try adding --sni to
your service parameters to enable Server Name Indication (SNI), which
allows the server to safely host multiple TLS Certificates for multiple
sites, all under a single IP address.

Test openssl's response by running this command from your NEMS server:

openssl s_client -connect YOURDOMAIN.COM:443 -debug

**I receive a message “CRITICAL - Socket timeout after 10 seconds” on
NEMS TV Dashboard, Adagios and so-on**

This means the particular board you're using to run NEMS is a bit slow
for the task. By default, check_http will timeout after 10 seconds. But
what happens if your board takes 11? It generates the error “CRITICAL -
Socket timeout after 10 seconds”.

To remedy this, yes, you could move to a faster board. But I'd suggest
you could also add these two things to your service check ARGS as per
the syntax above:

-N - only download the headers: this will result in a smaller
transaction, which in turn takes less time.

-T 30 - increase the timeout to 30 seconds.

So your ARGS would become:

-N -T 30