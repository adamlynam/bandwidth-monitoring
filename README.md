Bandwidth Monitoring
====================

A Python application for logging data usage by machines on a network

Requires iptables and mysql to be available and the machine the code is running on needs to see all the data you want to record (we ran it on a router box).

Usage is:

1) Run start.py once to create iptables rules.

2) Run log.py as regularly as you like, it will log a database entry each time it is run for each MAC address that was seen during the window. 15 minutes is an appropriate window.

3) Run end.py once to teardown iptables rules.

4) You can add a web interface to read the usage, or just run the provided SQL statement from the commandline to get a readout of usage per MAC address.
