Monitor Your Web Site with check_http
=====================================

Exercise Introduction
---------------------

Your web site is the face of your business. If it ever goes down for any reason, or becomes sluggish, it’s important to be proactive in remedying the situation. What's worse than having a customer contact you to let you know your web site is down? Realizing it might have been down for a week and the customers during that time didn’t let you know: They just went elsewhere.

Having your web site become sluggish or unresponsive can also damage your organic SEO standings.

In this exercise, we'll learn how to setup NEMS Linux to notify you if your web site fails to respond for more than 10 minutes. With this skill, you will be able to proactively monitor your own, your customers’ or any http/https web site for uptime or slow response time.

If your site goes offline, or becomes unresponsive or sluggish, NEMS Linux can send you an alert by a number of methods including email, Telegram or Pushover. This capability makes NEMS Linux a fantastic tool for web designers and hosts who want to ensure their customer sites are always up so the customer doesn’t notice any downtime. If your site is hosted over SSL, NEMS can even notify you if your certificate has expired – or is about to expire. There are so many options since NEMS Linux has been built to monitor everything.

For this exercise, we'll use the built-in *check_http* command. For my example, I’ll use https://nemslinux.com/ – I would suggest you do the same for the sake of the lesson, and then try changing the Host to your own domain once you understand how everything is connected.

It may appear onerous as you glance over the following 6 steps, but keep in mind once you create your config, you can reuse it for as many web site hosts as you like by simply assigning your host to the *web_site_ssl* host group, which you’ll learn to create below.

Configuration is done in NEMS Configurator (NConf). Open that tool via the Configuration menu on NEMS Dashboard.

IPv4 or IPv6
------------

#. The *check-host-alive* command, found in *misccommands* in NConf, is used to check hosts to determine if they are up or down. My web site, nemslinux.com, will only respond on IPv4. However, the default *check-host-alive* command will attempt to use IPv6. Rather than editing the sample command, let’s add a new one based upon it, but this one will only use IPv4. That way, we can still use the old command if we need IPv6 for a different host.

  #. Show the misccommands list.
  #. Edit *check-host-alive*
  #. Highlight and copy the entire command line to your clipboard.
  #. Click Add next to misccommands to add a new command.
  #. Name your new command `check-host-alive-ipv4`
  #. Paste the command line from your clipboard.
  #. At the very end of the command line, simply add a space, followed by -4 to tell it to use IPv4 for this check.
  #. Save the new command.

  .. figure:: ../../img/Create-New-misccommand-to-check-host-alive-Using-IPv4.png
    :width: 600
    :align: center
    :alt: Create IPv4 Check Command

  Create New misccommand to check-host-alive Using IPv4

#. Our commands are ready for us, so now it’s time to setup our hostpreset. We want to create one for IPv4 Web Sites. That way, we can reuse the preset for every web site we want to monitor with NEMS Linux.

  #. Add a new host preset.
  #. Name your preset Web Site IPv4
  #. Set the host alive check to the new command you created in Step 2: check-host-alive-ipv4
  #. Save your host preset.
  
  .. figure:: ../../img/New-Host-Preset-for-IPv4-Web-Sites.png
    :width: 600
    :align: center
    :alt: Create IPv4 Host Preset

    New Host Preset for IPv4 Web Sites

#. So far, everything we’ve done can be reused for any web site whose hostname resolves to an IPv4 address. From here forward however, we’ll be setting up our host group specifically for a secure (SSL) web site.

  #. Add a new hostgroup.
  #. Call this web_site_ssl
  #. Leave everything else as is and save your new hostgroup.
