Title: Building a Raspberry Pi Jukebox
Category: Projects
Tags: raspberry-pi, music, projects
Slug: rpi-jukebox-build
Authors: Mike Mallin
Summary: Network Jukebox w/ a Raspberry Pi
Date: 2013-09-10
Logo: {static|images/Header.png}

![Header]({static|images/Header.png}){: .align-center}

You will need:

* Raspberry Pi  
      I used a Model B for the Ethernet port. You'll need to find how to add wifi yourself if you use a Model A
* USB Sound Card  
      I used a Soundblaster Play USB as it was cheap at my local Canada Computers. (Sound quality isn't bad either)
* SD Card  
      Minimum 2Gb. As long as you can install raspbian. After I was done, I only used 1.1Gb.

Step 1: Install Raspbian  

Head over to www.raspbian.org and get your brand new Pi running with it.
However you choose to install doesn't matter.
Just get a basic system with network/ssh access going (don't install the "Debian Desktop Environment") and come back for step 2.

Step 2: Add software  
For there to be music, we need some software to play it. As root run:

        apt-get install mpd cifs-utils alsa-base alsa-utils alsa-oss oss-compat alsa-plugins

This installs:  

* CIFS Utilities. Useful for mounting SMB shares (coincidentally where my music is located)
* MPD. Music Player Daemon, the root of this project.
* ALSA. Useful if you want sound output.

Now that this is all installed, let's get some music playing!

Step 3: Configure MPD

Configuring MPD isn't too ridiculous. Just read the comments and google for the more challenging questions.

Fire up your editor of choice on /etc/mpd.conf.

Essential config items are:

        music_directory = <dir> # Set this to your library

        bind_to_address “any” # Useful if not a static IP

        # Following allow autodiscovery over zeroconf/avahi
        zeroconf_enabled “yes”
        zerconf_name “Boombox MPD”

        # Audio output for my sound card
        audio_output {
                type            "alsa"
                name            "My ALSA Device"
                options         "dev=dmixer"
                device          "plug:dmix"
        }

        mixer_type “software” # My soundcard mixer is in software

Step 4: Just add Music  

Add the following to /etc/fstab to auto-mount a network share on boot:

        //X.Y.Z.W/Music /mnt/Music cifs credentials=/root/.credentials,iocharset=utf8,file_mode=0777,dir_mode=077 0 0

With /root/.credentials being a file that contains:

        username=<your username>
        password=<your password>

and X.Y.Z.W being the IP of your file server.

Run as root to mount your share:

        mount -a

Now you should have access to your music!
