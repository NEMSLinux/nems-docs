Check Command: check_ping
=========================

Service Parameters
------------------

check_ping requires two parameters: Warn Critical

Each is a group of one integer (response time) followed by a comma and a
percentage (packet loss).

In this example, we'll warn when the round trip average is 10ms or
higher, or the packet loss is 2% or more. We'll go critical if the round
trip average is 20ms or higher, or the packet loss is 5% or more.

10,2% 20,5%