Introduction to NEMS Linux
==========================

Nagios® Core™–which I’ll simply refer to as “Nagios” throughout this article–is a free, open source server application which monitors hosts and services that you specify, alerting you when things go bad and when they get better. I’ve been using Nagios for many years. If I had to hazard a guess as to when I started using it, I’d say it was around 2006.

My wife and I ran a small computer service company out of our home in those days, and in order to keep track of my customer sites and be as proactive as I could be, I had a beast of a computer in the garage keeping check on my customers’ hard drive space, backup state, CPU load, and antivirus definition updates, as well as various other services.

I remember setting up that old Nagios server. The process was onerous, and all the configuration was done through the Linux terminal by opening config files in vi. One malformed syntax and Nagios would fail to start. I made it work, and if anyone has ever doubted my nerdiness, they are clearly mistaken. Ah, who am I kidding? Nobody has ever doubted my nerdiness. As the years went on and my support business customer base continued to grow, I began repurposing old hardware, installing an independent Nagios server at each client site. This worked very well.

I received my first Raspberry Pi in 2014. After it sat on the shelf for a year, I began to consider possible ways I could put it to use. I realized that the power consumption, rack space, and noise of these old Nagios servers was an incredible waste of resources. I was convinced that a single-board computer could make an excellent Nagios server, and began tinkering.

Why reinvent the wheel? Ryan Siegel’s NagiosPi image was out-of-the-box ready and gaining popularity. I started using it, but quickly became dismayed by the state of the distro, which appeared to be aging and was not being updated at a pace suitable for business use. It was a wonderful starting point, but felt in some important ways like an incomplete product. I began working on my own rebuild of NagiosPi, calling it NEMS; short for “Nagios Enterprise Monitoring Server”.

.. image:: /img/first_nems_server.jpg
  :width: 600
  :alt: This customer Nagios server was replaced with the first ever NEMS server in 2016.
