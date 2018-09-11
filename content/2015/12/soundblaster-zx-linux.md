Title: Towards Soundblaster ZX Support on Linux 
Category: Information
Tags: linux
Slug: soundblaster-zx-linux
Authors: Mike Mallin
Summary: Almost there
Date: 2015-12-15

After a number of dead-ends towards getting sound running on my desktop, I think it's almost there after the hard work of some of the linux kernel maintainers.
[Bug 55541](https://bugzilla.kernel.org/show_bug.cgi?id=55541)
[Bug 109191](https://bugzilla.kernel.org/show_bug.cgi?id=109191)

The first bug is for the CA0132 DSP series of cards (Recon3D, Soundblaster Z). This fixes the DSP not working on x86_64 kernels.
The second bug is specifically for the Soundblaster Z series of cards. This is *not* yet resolved, but it seems like there's active work towards fixing it.

Only downside to recent fixes is that there's no current support or patches in Debian 8 (yet). This means compiling a new kernel. I've chosen to run 4.4-rc5, but in the future non-RC kernels should be used (4.4+ should be good).

For reference, here's the steps to build a new kernel on Debian 8. DO NOT DO THIS UNLESS YOU KNOW WHAT YOU ARE DOING. YOU CAN BREAK YOUR INSTALL BY MINDLESSLY FOLLOWING THESE INSTRUCTIONS.

    wget https://cdn.kernel.org/pub/linux/kernel/v4.x/testing/linux-4.4-rc5.tar.xz
    mv linux-4.4-rc5.tar.xz /usr/src

A note here, due to my local setup I had to copy the source, set ownership to root:root and build as root. For regular users, having your own user own the source folder should be fine.

    tar xvf linux-4.4-rc5.tar.xz
    cd linux-4.4-rc5.tar.xz
    cp /boot/config-3.16.0-4-amd64 .config
    make-kpkg clean
    make-kpkg --rootcmd fakeroot --revision=1.0.mmallin --initrd --jobs 8 kernel_image modules-image
    cd ..
    dpkg -i linux-image-4.4.0-rc1_1.0.mmallin_amd64.deb

Reboot at this point. Then you'll have to install an updated NVIDIA driver due to the kernel change. One last reboot later and you should be staring at your X desktop again.
