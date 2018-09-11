Title: Configuring your tftpboot share for PXE
Category: Information
Tags: bsd, pxe, networking
Slug: tftpboot-pxe
Authors: Mike Mallin
Summary: Netboot makes life easy!
Date: 2013-08-25
Logo: {static|images/Header.png}
![Header]({static|images/Header.png}){: .align-center}

Now that your servers are set up for PXE booting, you need something to share to the BIOS of your target computers.

![Figure 1]({static|images/Figure1.png}){: .align-center}
Figure 1 - Directory layout of my tftpboot share

There are some essential files you need and a specific structure to follow. You need pxelinux.0 from a syslinux distribution. (More info here: http://www.syslinux.org/wiki/index.php/PXELINUX)

Once you have that, you need a config file for it. First, create the directory “pxelinux.cfg” in your tftpboot share. In that directory, create a file named “default”.

My “default” config file is:

        DEFAULT linux
        prompt 0
        timeout 0
        MENU INCLUDE /pxelinux.cfg/memtest86+.conf
        MENU INCLUDE /pxelinux.cfg/gparted.conf
        MENU INCLUDE /pxelinux.cfg/lubuntu.conf
        MENU INCLUDE /pxelinux.cfg/memdisk.conf
        MENU INCLUDE /pxelinux.cfg/arch.conf
        MENU INCLUDE /pxelinux.cfg/ping.conf
        MENU INCLUDE /pxelinux.cfg/clonezilla.conf
        include debian-installer/amd64/boot-screens/menu.cfg
        default debian-installer/amd64/boot-screens/vesamenu.c32

You do not need all of the lines that I have. I made a separate config for each of my PXE booted OSes. I’ve also added the debian netboot ones at the end so that I get a nice screen like the title shot. My configs are located here.

Once your configs are setup, just put your kernel/initrd in a sane place and update your config. Look at my sample ones for guidance.

For some OSes, you will need to enable NFS access on your nas4Free box. I’ll add that in a later entry.
