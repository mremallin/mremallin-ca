Title: Xilinx Vivado on an Apple M1 Pro - Rosetta 2 Edition
Category: Other
Tags: fpga
Authors: Mike Mallin
Summary: Rosetta 2 has no right to be this good
Date: 2022-10-24
Logo: {static|images/VivadoOnARM64.jpg}
Gallery:
    {static|images/VivadoOnARM64.jpg}||Vivado Running on ARM64


# Summary
- Expect some bugs to appear
- Stupid fast for what it is (within 15% of a 3800x for building [pcileech-fpga/ScreamerM2](https://github.com/ufrisk/pcileech-fpga))
- Can't easily migrate an existing VM to add Rosetta 2 support (yet)


# Short Version
- Upgrade to MacOS 13
- Upgrade to the latest UTM (4.0.9)
- Create a new VM with Apple's virtualization framework as the backend (instead of QEMU)
- Follow these steps to enable rosetta support: https://docs.getutm.app/advanced/rosetta/
- Make the VM multiarch with `sudo dpkg --add-architecture amd64`
- Install all the necessary x86_64 packages for Vivado
- Extract your choice of Vivado installer (`./Xilinx_Unified_2020.2_1118_1232_Lin64.bin --keep`)
- Edit the setup script to skip the architecture check
- Install Vivado
- Edit the launcher script to skip the architecture check
- Launch Vivado and enjoy!

# Long Version

The day has come with the release of MacOS 13 Ventura that Rosetta 2 is now available to Linux virtual machines! Apple has provided a handy way of exposing Rosetta 2 to the virtual machine via their [Virtualization framework](https://developer.apple.com/documentation/virtualization/running_intel_binaries_in_linux_vms_with_rosetta).

Once I had installed the new MacOS, I was eager to give it a try. I use [UTM](https://getutm.app/) to run virtual machines on my M1 Pro. After the upgrade, I was hoping I could just tweak my existing VM to gain rosetta 2 support but unfortunately that is not possible. I had to create a brand new VM in order to switch from QEMU to Apple's Virtualization framework. I also tried to convert my existing qcow2 image to raw in hope I could import it that way but was unsuccessful. The VM would shutdown within a few seconds of booting while flashing an error message on screen.

This led to creating a new VM for just FPGA development... One Debian netinstall later and I'm staring at a fresh VM waiting to explore. After installing Debian, and the `binfmt-support` package I continued with the [instructions here](https://docs.getutm.app/advanced/rosetta/) to enable Rosetta 2 within my VM.

You can verify that the VM is ready to direct x86_64 executables to Rosetta 2 by running `/usr/sbin/update-binfmts --display` and looking for `rosetta` in the output:
```
rosetta (enabled):
     package = <local>
        type = magic
      offset = 0
       magic = \x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x3e\x00
        mask = \xff\xff\xff\xff\xff\xfe\xfe\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff
 interpreter = /media/rosetta/rosetta
    detector = 
```

With Rosetta 2 available, we can now turn to getting the system setup for x86_64 executables. First thing to do is to enable multiarch support with `sudo dpkg --add-architecture amd64`. Verify that there is now an `amd64` entry in the output of `dpkg --print-foreign-architectures`.

## Necessary Packages
After adding multiarch support to the VM, make sure to update the package repository (`sudo apt-get update`) before continuing. The following is the list of packages needed to see Vivado through from installer to a successful build:

```
sudo apt-get install gcc-10-base:amd64 glib-networking:amd64 libatk-bridge2.0-0:amd64 libatk1.0-0:amd64 libatspi2.0-0:amd64 libavahi-client3:amd64 libavahi-common-data:amd64 libavahi-common3:amd64 libblkid1:amd64 libbrotli1:amd64 libbsd0:amd64 libc6:amd64 libcairo-gobject2:amd64 libcairo2:amd64 libcolord2:amd64 libcom-err2:amd64 libcrypt1:amd64 libcups2:amd64 libdatrie1:amd64 libdbus-1-3:amd64 libdeflate0:amd64 libepoxy0:amd64 libexpat1:amd64 libffi7:amd64 libfontconfig1:amd64 libfreetype6:amd64 libfribidi0:amd64 libgcc-s1:amd64 libgcrypt20:amd64 libgdk-pixbuf-2.0-0:amd64 libglib2.0-0:amd64 libgmp10:amd64 libgnutls30:amd64 libgpg-error0:amd64 libgraphite2-3:amd64 libgssapi-krb5-2:amd64 libgtk-3-0:amd64 libharfbuzz0b:amd64 libhogweed6:amd64 libicu67:amd64 libidn2-0:amd64 libjbig0:amd64 libjpeg62-turbo:amd64 libjson-glib-1.0-0:amd64 libk5crypto3:amd64 libkeyutils1:amd64 libkrb5-3:amd64 libkrb5support0:amd64 liblcms2-2:amd64 liblz4-1:amd64 liblzma5:amd64 libmd0:amd64 libmount1:amd64 libnettle8:amd64 libnsl2:amd64 libnss-nis:amd64 libnss-nisplus:amd64 libp11-kit0:amd64 libpango-1.0-0:amd64 libpangocairo-1.0-0:amd64 libpangoft2-1.0-0:amd64 libpcre2-8-0:amd64 libpcre3:amd64 libpixman-1-0:amd64 libpng16-16:amd64 libproxy1v5:amd64 libpsl5:amd64 librest-0.7-0:amd64 librsvg2-2:amd64 librsvg2-common:amd64 libselinux1:amd64 libsoup-gnome2.4-1:amd64 libsoup2.4-1:amd64 libsqlite3-0:amd64 libssl1.1:amd64 libstdc++6:amd64 libsystemd0:amd64 libtasn1-6:amd64 libthai0:amd64 libtiff5:amd64 libtinfo5:amd64 libtirpc3:amd64 libudev1:amd64 libunistring2:amd64 libuuid1:amd64 libwayland-client0:amd64 libwayland-cursor0:amd64 libwayland-egl1:amd64 libwebp6:amd64 libx11-6:amd64 libxau6:amd64 libxcb-render0:amd64 libxcb-shm0:amd64 libxcb1:amd64 libxcomposite1:amd64 libxcursor1:amd64 libxdamage1:amd64 libxdmcp6:amd64 libxext6:amd64 libxfixes3:amd64 libxi6:amd64 libxinerama1:amd64 libxkbcommon0:amd64 libxml2:amd64 libxrandr2:amd64 libxrender1:amd64 libxtst6:amd64 libzstd1:amd64 zlib1g:amd64
```

Unfortunately I lost track of my shell history and don't have the condensed list of packages which expanded to this. Sorry!

# Installing Vivado
Now we can get to the main event! Installing and running Xilinx Vivado. For my use, I installed version 2020.2. I'd hope that the edits made are similar across multiple versions.

First thing to get started is to unpack the installer. I used the net installer version, though I'd assume that the complete package version is also similar. The installer can be unpacked by adding the argument `--keep` to its invocation. This will extract all of it's contents to a folder of its choice (`removeLin64` in my case.)

Navigate to that folder and open the xsetup script for editing. Look for a block of code that looks like:
```
# ERROR out if this installation is running on 32 bit OS 
# and does not support 32 bit installation 
if [ "$(uname -m)" != "x86_64" ]; then
    # check that the 32 bit library directory exist or not
    lnx32LibDir="${workingDir}/lib/lnx32.o"
    if [ ! -d $lnx32LibDir ]; then
   	   # terminate with an ERROR
       echo "ERROR: This installation is not supported on 32 bit platforms."
       exit 1;
    fi  
fi

```

Then comment it out so it looks like:
```
# ERROR out if this installation is running on 32 bit OS 
# and does not support 32 bit installation 
#if [ "$(uname -m)" != "x86_64" ]; then
#    # check that the 32 bit library directory exist or not
#    lnx32LibDir="${workingDir}/lib/lnx32.o"
#    if [ ! -d $lnx32LibDir ]; then
#   	   # terminate with an ERROR
#       echo "ERROR: This installation is not supported on 32 bit platforms."
#       exit 1;
#    fi  
#fi
```

This will allow you to start the installer and get Vivado installed. Select the options you'd like and let it run. On my machine, it took about 30m to install. 20m to download and another 10m to install.

During installation, I ran into my first major issue. About 80% of the way through the download, the VM hard locked. This required a few reboots to recover as I had to manually run fsck before my drive would get mounted as `rw` instead of `ro` due to the errors. On the plus side, once I restarted the installer it picked up right where it left off. This was a good intro to the performance seen with Rosetta 2 as it was verifying the previously downloaded files at north of 800Mb/s! Super fast!

After that minor hiccup, the rest of the installation proceeded without fail.

# Running Vivado
Similar to the installation script, the main Vivado executable also checks the system architecture before proceeding. Edit the file `/<path to your install folder>/Vivado/<Version>/bin/loader` and look for the following block:
```
case `uname -m` in
  x86_64)
    ;;
  *)
    echo 1>&2 "Unsupported architecture: `uname -m`"
    exit 1
    ;;
esac
```

Then comment out the exit:
```
case `uname -m` in
  x86_64)
    ;;
  *)
    echo 1>&2 "Unsupported architecture: `uname -m`"
    #exit 1
    ;;
esac
```

I left the warning message in place as a reminder that this is not really supported. Once saved, you should be able to launch and run Vivado as usual.

# Benchmarks

| Computer | Project Generation | Synthesis | Implementation | Bitstream Generation |
| --- | --- | --- | --- | --- |
| 2020 Ryzen 7 Tower (16 threads) | 22s (cache primed), 50s (first boot) | 1m42s | 3m02s | 22s |
| 2022 MacBook Pro (Rosetta 2 - 8 threads) | 26s | 2m04s | 4m09s | 28s |
| 2012 MacBook Air (2 threads) | 36s | 3m26s | 7m20s | 37s |

I've put the chart out first as it speaks volumes to the work Apple has done to polish Rosetta 2. I'll be the first to admit it's not a direct apples-to-apples comparison, but it's definitely a surprising result. These are here to give a rough ballpark as to what you can expect from running your Linux workloads using Rosetta 2. For starters, the disk performance is very different between my Ryzen tower and my M1 Pro; the tower uses a SATA SSD for Linux and a 4Tb WD Red Pro for data drive (Vivado is installed to the Red+) whereas the M1 Pro has a PCIe based SSD running everything.

## Ryzen 7 Tower Specifications
- AMD Ryzen 7 3800x
- Gigabyte x570 Aorus Pro Wifi Motherboard
- 32Gb DDR4-2600 ECC RAM
- MSI RTX3070
- Samsung 840 Pro SATA SSD (Linux Boot Drive)
- WD Red Pro 4TB (ZFS Data Drive)

# Conclusion
I'm quite amazed as to the amount of performance available on this laptop. I was hoping to get somewhere above the 2012 MacBook Air, not within spitting distance of my desktop! I've played around a bit in Vivado to check some of the features/functionality but there's been nothing obviously broken so far. Another night will be needed to see if I can still use any of the FPGA debugging features within Vivado.

This is a solid showing by Apple with the performance of both the M1 Pro and Rosetta 2 with a few minor bumps along the way.