# Mission

## Description

I have a list of prohibited IPs, stored in prohibited_ips.txt.

I need a script to create the commands needed to configure IPTABLES on Linux, so I can drop packages from those IPs
i.e.

sudo iptables -A INPUT -s 203.0.113.51 -j DROP
...
