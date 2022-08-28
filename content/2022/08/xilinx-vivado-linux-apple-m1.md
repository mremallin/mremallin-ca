Title: Xilinx Vivado on an Apple M1 Pro
Category: Other
Tags: fpga
Slug: xilinx-vivado-linux-apple-m1
Authors: Mike Mallin
Summary: It's only a matter of time...
Date: 2022-08-27

I recently picked up a new 14" MacBook Pro and have started to migrate all of my projects to it as my single, portable workstation. Besides gaming, the only thing at this time that requires an x86_64 processor are the FPGA toolchains I use on occasion. I figured this would be a good time to see what the current state of x86_64 emulation is on the Apple M1 processors.

The first thing I tried out was using [UTM](https://getutm.app) to emulate a debian x86_64 installation. I thought this would be fairly close to my old laptop setup (2012 MacBook Air, i7, 8GB Ram + 16GB Swap, Arch x86_64) in performance. That is not the case at the moment. The main limitation at the moment is that QEMU (which UTM is based on) only supports single-core emulation of x86-family CPUs. It wasn't too bad getting Debian 11 installed in emulation, roughly 30m or so. Vivado was a lot more painful unfortunately. I started off with the Web installer of 2020.2. I gave up after 4 hours as it was only downloading at 500KB/s - 1MB/s. I downloaded the complete installer from MacOS and scp'd it over in less than 30m... Installing it from disk wasn't too bad and it took 1h 3m to copy all the files. I'll let the next table speak for itself. This is a very rough benchmark for building [pcileech-fpga/ScreamerM2](https://github.com/ufrisk/pcileech-fpga) from scratch.

| Computer | Project Generation | Synthesis | Implementation | Bitstream Generation |
| --- | --- | --- | --- | --- |
| 2012 MacBook Air | 36s | 3m26s | 7m20s | 37s |
| 2022 MacBook Pro | 2m40s | 2h50m | 1h10m | 4m41s |

As you can see, even a 10 year old computer is still 10x faster than x86 emulation on a M1 Pro.

You may be thinking, "what about running a native OS and only emulating Vivado?" That's a very good point! There are two options for this that I know of:

1. Run Windows 11 ARM - Dev Branch Insider Edition in the hypervisor and rely on windows to translate the x86_64 binary
2. Wait for MacOS 13 and the exposure of Rosetta 2 to hypervisor guests

I attempted 1. after the excruciating wait for Debian to finish building. This time things were much faster and almost approaching the level of performance as the old MacBook Air. Project generation was within spitting distance at 42s. Unfortunately that's where all the good luck ran out. I ran into crash every time I tried to launch the Vivado GUI. I used TCL mode from the command promt to generate the project but when starting the build one of the subprocesses would always hang during out-of-module synthesis of the IP. I tried deleting and rebuilding the project many times but was unable to get past this step.

As you can see, it's really promising that it's theoretically possible to run and use Vivado on the M1-series CPUs, but the performance and stability isn't there yet. I'm hopeful that this will change over the coming years as the emulation infrastructure is built out further.
