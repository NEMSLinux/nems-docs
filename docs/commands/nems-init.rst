NEMS Linux Commands: nems-init
==============================

**Welcome to NEMS Linux!**

In order to begin using your new NEMS Server, you must first initialize
it. The *nems-init* process makes initialization quick and easy by
automating many of the first-boot tasks for you. After initialization,
you'll be left with a fully-operational NEMS Server, complete with a
small selection of sample check commands.

**Please Note:**

If any of the included sample check commands report error, perhaps they
need adjusting or removal in NEMS NConf. Here are a couple quick
examples:

1. If the particular platform of your NEMS Server doesn't have a thermal
   sensor, you'll see an error when the thermal check runs, so you can
   remove that check and re-generate your Nagios config since it doesn't
   apply to you.
2. If you have slow Internet, you'll see an alert when the default
   thresholds are met, so you can adjust the thresholds to numbers that
   are more appropriate for your configuration and re-generate your
   Nagios config.

**Let's Begin:**

To initialize NEMS Linux, simply `connect to your NEMS Linux server over
SSH <https://docs.nemslinux.com/usage/connect_to_nems_ssh>`__ or use the
in-browser terminal feature
of `Cockpit <https://docs.nemslinux.com/features/cockpit>`__ on
supported platforms and type:

**sudo** nems-init

On Docker, the method is instead to run the following command on your
Docker host:

**sudo** docker exec -it nems nems-init

Important Note
--------------

If you are trying to initialize NEMS via a connected keyboard and TV,
please note that you will potentially be working with a different keymap
than your local system, which could cause you issues in future. It is
recommended to use the supported solutions listed above. In the case of
a Raspberry Pi Zero (or other device where Ethernet is not included
on-board) you can use an OTG or other supported Ethernet adapter to be
able to initialize over the network. Keyboard / TV support is available
for the extreme case where it is the only option, but it is not the
recommended method, nor officially supported.

What nems-init Does
-------------------

*nems-init* automates and simplifies the following operations:

1. **Randomizes the password of the default Linux user and removes that
   user.** You should never have a production server using the default
   username:password since there are many malware scripts that seek out
   and destroy such devices.
2. **Creates your NEMS Linux admin user.** This is the username and
   password you will use to access web-based systems such as NConf,
   Nagios Core, and your NEMS-Migrator backups (over https or samba), as
   well as when you login to the NEMS server over SSH. Make sure you
   select a strong password as this user will have SSH and super user
   access. This is also the user you will use to access network shares
   located on your NEMS Linux server.
3. **Configures your timezone.** NEMS Linux uses NTP to automatically
   update your NEMS Server's date and time based on your configured
   timezone.
4. **Configures your keyboard locale/language.**
5. **Generates and installs your self-signed SSL certificates.** Every
   NEMS Server has its own custom self-signed SSL certificate.

Once NEMS Linux is initialized, you can access its interface through
your web browser. The *nems-init* process is the only time you should
need to access the NEMS Linux terminal.