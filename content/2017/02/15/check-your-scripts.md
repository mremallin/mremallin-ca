Title: Slight Service Interruption
Category: Other
Tags: publishing,certificates
Slug: check-your-scripts
Authors: Mike Mallin
Summary: Sometimes programs are not updated.
Date: 2017-02-15

Sorry about the service interruption over the past few days. As you could probably see, my certificates expired and due to my security configuration you could not connect.

I use Let's Encrypt to get a SSL certificate for this site and was previously relying on the simp_le client in order to get certificates. It was more lightweight on required packages than the official certbot. Unfortunately, the implementation of simp_le was not updated to support a recent change and my certificates were failing to be renewed. Now that I'm home, I switched over to the official certbot client. Coupled with a handy cronjob, I shouldn't have to worry about this again.

Lessons learned:

  * Debug logs are not useful if you don't look at them
  * Using unofficial clients is at your own peril
