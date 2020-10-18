How NEMS Linux Uses ZRAM To Maximize Memory
===========================================

.. figure:: ../../img/nemsswap.png
  :width: 600
  :align: center
  :alt: NEMS Swap Screenshot

On June 23, 2017 I disabled swap on NEMS 1.2 to decrease the read/writes
to NEMS server SD cards on the Raspberry Pi.

On February 5, 2018 you might notice your swap is … well … back. Or is
it?

Rather than a traditional swap partition or file, I'm doing things
differently with NEMS 1.3. Your pseudo swap is actually (are you ready
for this?) RAM! Well, ZRAM to be exact!

The Raspberry Pi has very little RAM. 1GB. That's not much when it comes
to all the things a NEMS Linux server has to do in its day to day. So
how can I possibly give you more RAM on that wee hardware while not
reducing the lifespan of your hardware? Allow me to explain…

ZRAM allows me to create a ramdisk that can be used as swap. But what's
really unique about ZRAM (which is a Linux kernel module) is that it
compresses the data in the ramdrive on the fly.

So here's how it works: your NEMS server starts to fill up the RAM and
what happens? Well, it starts to swap stuff that should be in RAM to the
swap. Only we disabled swap to extend the life of your SD card… so now,
with this new ZRAM swap, it begins swapping instead to that. A swap
“drive” that is actually compressed RAM. Therefore, if your RAM becomes
full or close to full, it will begin swapping … or rather … compressing!

So, when you see the 1GB swap on your NEMS 1.3 server, don't fear! It is
not using your SD card, and it's actually a brilliant way to increase
the RAM capacity of your Raspberry Pi.
