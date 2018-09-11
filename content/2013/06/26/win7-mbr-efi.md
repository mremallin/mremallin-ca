Title: Windows 7 on UEFI vs. MBR Disks
Category: Information
Tags: windows, uefi, mbr
Slug: win7-efi-mbr
Authors: Mike Mallin
Summary: UEFI and MBR can't get along...
Date: 2013-06-26
Logo: {static|images/Header.jpg}

![Header]({static|images/Header.jpg}){: .align-center}

I was attempting to install Arch Linux the other day, and managed to tank my partitions... Oh Well, let’s install windows again and use UEFI! I followed the guide [here](http://forums.lenovo.com/t5/Windows-7-Knowledge-Base/Prepare-an-usb-thumb-drive-to-boot-windows-7-in-UEFI-mode/ta-p/656637) to install, but I kept getting the same error; 0xc0000225. I attempted to reinstall multiple times, with different partition layouts, but kept getting the same error. It took an hour of googling but I stumbled across [this post](http://forums.anandtech.com/showpost.php?p=34621321&postcount=10), which details that you cannot have any MBR disks in your system, with a UEFI install.

To recap: If you’re installing a UEFI install of windows, you CANNOT have any MBR disks in your system or it will fail.
