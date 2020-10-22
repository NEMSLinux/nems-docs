Check Command: check_esxi_hardware
==================================

*check_esxi_hardware* queries the CIM (Common Information Model) server
running on the ESXi server to retrieve the current status of all
discovered hardware. This check command comes
from `claudiokuenzler.com <https://www.claudiokuenzler.com/monitoring-plugins/check_esxi_hardware.php>`__.

Frequently Asked Questions
--------------------------

**Q:** The plugin is executed fine but then it hangs on a certain CIM
element on a DELL server. Verbose output:

20111104 18:21:56 Connection to https://esxi-001

20111104 18:21:56 Check classe OMC_SMASHFirmwareIdentity

20111104 18:21:57 Element Name = System BIOS

20111104 18:21:57 VersionString = 1.3.6

20111104 18:21:57 Check classe CIM_Chassis

20111104 18:21:57 Element Name = Chassis

20111104 18:21:57 Manufacturer = Dell Inc.

20111104 18:21:57 SerialNumber = xxxxx

20111104 18:21:57 Model = PowerEdge R710

20111104 18:21:57 Element Op Status = 0

20111104 18:21:57 Check classe CIM_Card

20111104 18:21:58 Element Name = unknown

20111104 18:21:58 Element Op Status = 0

20111104 18:21:58 Check classe CIM_ComputerSystem

CRITICAL: Execution time too long!

**A:** According to user feedback and lots of tests, such problems are
related to the Dell OMSA Offline Bundle. Especially OMSA version 6.5
made problems on ESXi 5.x servers.

—

**Q:** I get the following error message from the plugin:

(0, 'Socket error: [Errno 111] Connection refused')

**A:** Make sure the Monitoring Server is able to access tcp port 5989
(cim) on the ESX(i) server. Alternatively you can also set a different
port with the -C parameter if you have a special DNAT or port forwarding
in place.

—

**Q:** How do I use the -i parameter to ignore certain alarms?

**A:** As written in the documentation, the -i parameter awaits a comma
separated list of elements to ignore. The &quot;tricky&quot; part is to
find the correct element names (they can be pretty long sometimes). Run
the plugin in verbose mode to have a list of all CIM elements. Here's an
example how to ignore several elements:

./check_esxi_hardware.py -H myesxi -U root -P mypass -V dell -i "IPMI
SEL","Power Supply 2 Status 0: Failure status","System Board 1 Riser
Config Err 0: Config Error"

—

**Q:** I have the following warning showing up but my server shows all
sensors green:

WARNING : System Board 1 Riser Config Err 0: Connected - Server: Dell
Inc. PowerEdge R620 s/n: xxxxxxx System BIOS: 1.1.2 2012-03-08

**A:** It seems that all Dell PowerEdge x620 servers are affected, it
looks like a BMC firmware bug to me. A workaround for this bugger is in
place since version 20121027. Please check <a
href=“/blog/299/check_esxi_hardware_dell-pe-620-workaround-riser-config-err-connected”>this
post</a> for detailed information.

—

**Q:** The plugin returns the following output:

Authentication Error! - Server:

**A:** There are several answers to that:

1. Make sure you are either using the ESXi root user or that you create
   a user which is member of the root group. See <a
   href=“/blog/114/check-esxi-wbem-esxi-4.1-user-authorization”>this
   post</a> for a short description how to do that.
2. The password you are using has some special characters like a
   question mark and you need to quote them.
3. The password you are using has a Dollar sign ($) which you need to
   single-quote.

Generally, always put quotes around your password as this assures the
content is handled as string.

—

**Q:** Can the plugin also monitor other stuff like VMFS disk usage or
cpu/memory usage?

**A:** No. The plugin makes use of the CIM (Common Infrastructure
Model) . The so-called CIM elements cover hardware only.

—

**Q:** Some hardware is not being monitored by the plugin.

**A:** The plugin can only monitor the hardware which is “shown” by the
server via the CIM . If the hardware vendor does not include a certain
hardware element into the CIM elements, then this piece of hardware can
not be monitored. In all the years I've only seen this on no-name
machines (and SUN) though.

—

**Q:** The plugin is so slow that a timeout occurs.

**A:** In such cases always verify how the behavior is on your vSphere
client in the Hardware tab. Click on the “Update” link and then
“Refresh”. Are they fast or do they also take a long time to update?

In ESXi 5.0 Update 1, a bug was causing slow hardware discovery/checks.
See `this
article <https://docs.nemslinux.com/blog/242/esxi-5.0-u1-slow-hardware-check_esxi_hardware-cim>`__ for
more information.

—

**Q:** The plugin suddenly times out, but it was working fine before.
The plugin returns the following output:

UNKNOWN: (0, 'Socket error: [Errno 110] Connection timed out')

**A:** In rare cases it is possible, that the sfcbd-watchdog service,
running on the ESXi server, isn't working correctly anymore.
Follow `VMware KB entry
1013080 <https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1013080>`__ and
restart the service by logging into the ESXi server by ssh and launch
the following command:

/etc/init.d/sfcbd-watchdog restart

If this still doesn't resolve your issue, a manual restart of the “CIM
Server” could help. This option is found under the “Configuration” tab →
“Security Profile”. Click on “Service … Properties”.

—

**Q:** After an update of the pywbem package the plugin doesnt work
anymore. The following output is shown in verbose mode:

Unknown CIM Error: (0, 'SSL error: certificate verify failed')

**A:** This was seen in SLES 11 SP3 after an update of the package
python-pywbem from 0.7-6.13 to 0.7-6.22. After reverting to the older
version, the plugin worked again.

Update September 9th 2014: This error will be fixed in a future release
of check_esxi_hardware.py, but it depends on the release of the new
pywbem upstream version.
See https://github.com/Napsty/check_esxi_hardware/issues/7.

Update June 26th 2015: This issue was fixed in version 20150626.

—

**Q:** On an IBM server with the ESXi image from IBM the following error
appears but works fine with the regular image vom VMware:

Traceback (most recent call last):

File "./check_esxi_hardware.py", line 625, in verboseoutput("Element
Name = "+elementName)

TypeError: cannot concatenate 'str' and 'NoneType' objects

**A:** The CIM definition coming from the IBM image seems to be lacking
some information. Version 20150119 fixes this issue.

**Q:** I updated my Ubuntu 14.04 and pywbem package
0.7.0-4ubuntu1~14.04.1 was installed. Since then I get the following
error when the plugin is run:

Traceback (most recent call last):

File "/usr/local/bin/check_esxi_hardware.py", line 619, in
<module>instance_list = wbemclient.EnumerateInstances(classe)

File "/usr/lib/pymodules/python2.7/pywbem/cim_operations.py", line 421,
in EnumerateInstances

\**params)

File "/usr/lib/pymodules/python2.7/pywbem/cim_operations.py", line 183,
in imethodcall

no_verification = self.no_verification)

File "/usr/lib/pymodules/python2.7/pywbem/cim_http.py", line 268, in
wbem_request

h.endheaders()

File "/usr/lib/python2.7/httplib.py", line 969, in endheaders

self._send_output(message_body)

File "/usr/lib/python2.7/httplib.py", line 829, in \_send_output

self.send(msg)

File "/usr/lib/pymodules/python2.7/pywbem/cim_http.py", line 115, in
send

self.connect()

File "/usr/lib/pymodules/python2.7/pywbem/cim_http.py", line 167, in
connect

except ( Err.SSLError, SSL.SSLError, SSL.SSLTimeoutError

AttributeError: 'module' object has no attribute 'SSLTimeoutError'

**A:** It seems that Ubuntu did the same as SUSE, RedHat and Centos in
the past: The pywbem was patched without changing the upstream version
number. This goes into the same direction as issue #7
(https://github.com/Napsty/check_esxi_hardware/issues/7). A temporary
fix is to manually install the older pywbem package like this:

aptitude install python-pywbem=0.7.0-4

Update June 26th 2015: This issue was fixed in version 20150626.

—

**Q:** I use python3 but the plugin throws an error:

File "./check_esxi_hardware.py3", line 440

print "%s %s" % (time.strftime("%Y%m%d %H:%M:%S"), message)

^

SyntaxError: invalid syntax

**A:** An issue was opened on github
(https://github.com/Napsty/check_esxi_hardware/issues/13) to address
this compatibility issue.

Update: This issue was fixed in version 20181001.

**Q:** I sometimes get the following error on an ESXi host:

CRITICAL: (0, 'Socket error: [Errno 8] \_ssl.c:510: EOF occurred in
violation of protocol')

**A:** After a lot of debugging and testing with a plugin user we came
to the conclusion, that this problem arises from the ESXi host, not the
plugin. A tcpdump revealed, that the ESXi host sent a TCP Reset packet
rather then starting to submit data. A reboot of the affected ESXi host
resolved the problem.

Update October 17th, 2019: Such situations can (sometimes) also be
confirmed in the vSphere Client UI using the Monitor → Hardware Health
window. A click on the “REFRESH” button results in an error in the
recent tasks list:

“A general system error occurred: Server closed connection after 0
response bytes read; <SSL…..

—

**Q:** I have several ESXi hosts behind the same IP (NAT). How can I use
the check_esxi_hardware?

**A:** Since version 20160531 it is possible to manually define the CIM
port (which defaults to 5989). So if you set up port forwarding (DNAT)
you can now monitor all ESXi servers behind the same NAT-address. The
parameter you want in this case is ”-C“ (or –cimport).

—

**Q:** Is the plugin compatible with ESXi 6.x?

**A:** Yes. Please note that starting with ESXi 6.5 you might have to
enable the CIM/WBEM services first, as they are disabled by default.
Refer to https://kb.vmware.com/s/article/2148910.

—

**Q:** I can't execute the plugin and get the following error message.
Permissions are correct however (e.g. 755).

execvpe(/usr/lib64/nagios/plugins/check_esxi_hardware.py) failed:
Permission denied

**A:** This error comes from SELinux. You need to write an allow rule
for it.

—

**Q:** The plugin reports the following problem with memory, but no
memory hardware issues can be found on the server:

CRITICAL : Memory - Server: HP ProLiant DL380p Gen8 s/n....

**A:** It is possible that an alert needs to be cleared in the servers
IPMI log first. To do that, you need to login into your ESXi server with
SSH and run the following commands:

localcli hardware ipmi sel clear

/sbin/services.sh restart

This might affect other CIM entries as well. So it's a wise idea to
clear the IPMI system event log (sel) first before investigating
further.

—

**Q:** Certain hardware elements show incorrect health/operational
states, e.g. “Cooling Unit 1 Fans”:

20190205 00:26:26

Element Name = Cooling Unit 1 Fans

20190205 00:26:26

Element HealthState = 1020190205 00:26:26

Global exit set to WARNING

**A:** Certain server models might show false hardware alarms when these
particular hardware elements were disabled in BIOS, are idle or have
disabled sensors. From the `HP
FAQ <https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-a00053955en_us>`__:

PR 2157501: You might see false hardware health alarms due to disabled
or idle Intelligent Platform Management Interface (IPMI) sensors.
Disabled IPMI sensors, or sensors that do not report any data, might
generate false hardware health alarms.

In this case it makes sense to ignore these elements using the -i
parameter.

—

**Q:** The *check_esxi_hardware* plugin is not working (anymore) since
ESXi 6.7 U2/U3 on DELL servers.

**A:** The issue seems to be the “OpenManage” VIB. This can be verified
by checking the list of installed VIB's on an ESXi server:

esxcli software vib list

After uninstalling the OpenManage VIB, the plugin works again. According
to DELL, ESXi 6.7 U2 is `not yet officially
supported <https://www.dell.com/support/article/ch/de/chdhs1/sln311238/openmanage-integration-for-vmware-vcenter?lang=en>`__ (as
of July 2019) by OpenManage:

OpenManage Integration for VMware vCenter v4.3.1 (Initial 4.3 Download)
(4.3.1 Release Notes) (4.3 Manuals)Does not add official 6.7 U2 support
(support for 6.7 U2 will come in the fall with the next major release)

See also official `VMware KB
74696 <https://kb.vmware.com/s/article/74696>`__ entry for this.

Update October 15th 2019: OMSA 9.3.1 fixes this issue.