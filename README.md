# Mission

## Description

I have the following list of prohibited IPs

10.99.14.5
192.168.1.44
10.257.4.5
10.16.123.5

I need a script to create the commands needed to configure IPTABLES on Linux, so I can drop packages from those IPs
i.e.

sudo iptables -A INPUT -s 203.0.113.51 -j DROP
...
