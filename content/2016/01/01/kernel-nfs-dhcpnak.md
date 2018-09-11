Title: DHCPNAK When NFS Booting a Kernel
Category: Information
Tags: linux
Slug: kernel-nfs-dhcpnak
Authors: Mike Mallin
Summary: Don't forget to cleanup after yourself
Date: 2016-01-01

I figured out one of my issues when NFS booting my Raspberry Pi monitoring server. During boot, it would hang with DHCP NAK being received by the Pi. This happened after I added a static DHCP lease that was different than the automatic DHCP lease originally configured.

The fix was to remove the old lease file /var/lib/dhcp/dhclient.eth0.leases.
