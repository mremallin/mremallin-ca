Title: Xilinx Vivado 2020.2 Not Starting on Linux
Category: Other
Tags: fpga
Slug: xilinx-vivado-linux-not-starting
Authors: Mike Mallin
Summary: Missing libxcrypt-compat
Date: 2022-04-09

After some recent system updates, I found that Vivado was no longer starting on my Linux box. The following error was seen:

```
[~]$ vivado

****** Vivado v2020.2 (64-bit)
  **** SW Build 3064766 on Wed Nov 18 09:12:47 MST 2020
  **** IP Build 3064653 on Wed Nov 18 14:17:31 MST 2020
    ** Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.

couldn't load file "librdi_tcltasks.so": libcrypt.so.1: cannot open shared object file: No such file or directory
Could not load library 'librdi_tcltasks' needed by 'core', please check installation.
    while executing
"error "$result\nCould not load library '$library' needed by '$feature', please check installation.""
    (procedure "rdi::load_library" line 4)
    invoked from within
"rdi::load_library core librdi_tcltasks"
    (file "/opt/Xilinx/Vivado/2020.2/lib/scripts/rdi/features/core/core.tcl" line 5)
ERROR: [Common 17-217] Failed to load feature 'core'.
INFO: [Common 17-206] Exiting Vivado at Sat Apr  9 20:38:20 2022...
```

This was fixed by installing `libxcrypt-compat`.

