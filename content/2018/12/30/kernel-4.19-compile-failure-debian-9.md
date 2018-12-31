Title: Linux Kernel 4.19 Compilation failure on Debian 9
Category: Other
Tags: linux
Slug: linux-kernel-4.19-compile-failure-debian-9
Authors: Mike Mallin
Summary: Note, don't nuke a debian install unless you're really sure...
Date: 2018-12-30

I've spent a good chunk of the day trying to compile a new kernel for my Debian install in order to test out a sound card patch. There's a lovely [reddit thread here](https://www.reddit.com/r/SoundBlasterOfficial/comments/9mm5ad/sound_blaster_r3dr3dizzxrae5_linux_driver/) which descibes a potential patch for using a Sound Blaster Zx under Linux.

When attempting to build the kernel with this patch, I came across the following missing package dependencies when building on Debian 9:

* bison
* flex
* libelf-dev

The last one caused me a lot of pain due to the following compilation errors:

>  CC       /home/mmallin/src/kernel/linux-4.19.13/tools/objtool/special.o
> In file included from /usr/include/gelf.h:32:0,
>                  from elf.h:22,
>                  from check.h:22,
>                  from builtin-orc.c:29:
> /usr/include/libelf.h:46:4: error: unknown type name ‘Elf32_Word’
>     Elf32_Word   ch_type;        /* Compression format.  */
>     ^~~~~~~~~~

Turns out [according to this thread](https://bugzilla.redhat.com/show_bug.cgi?id=1528020) it is my CPATH environment variable causing issues with the libelf header inclusion. Clearing the environment variable fixed the above compilation issue.
