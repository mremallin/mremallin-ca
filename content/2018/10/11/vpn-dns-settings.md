Title: Fixing DNS Resolution with OpenVPN
Category: Other
Tags: openvpn
Slug: fix-dns-resolution-openvpn
Authors: Mike Mallin
Summary: Check your VPN client settings!
Date: 2018-10-11

I've had some troubles after re-configuring my VPN with resolving DNS names within my local network. I fixed this by pointing my VPN client DNS server to the VPN gateway address and setting my lcocal domain to the same as my local network.

Time to play with pfSense some more to see if I can get that configuration pushed from my server to my clients instead of manual configuration.
