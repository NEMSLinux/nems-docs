.. include:: ../global.rst

NEMS Linux Amazon Machine Image (AMI)
=====================================

The NEMS Linux Amazon Machine Image is available in the Amazon EC2
Community AMIs marketplace. Simply search for *NEMS Linux* when
launching your instance.

Important Note
--------------

Your being here means you are an early adopter of NEMS Linux on Amazon
Web Services. During this early testing phase, it is available through
the community marketplace. However, once NEMS has been tried-and-true,
it will be moving into the Amazon Marketplace. This means it will
inevitably fall under Amazon's fee structure. For now, it's as free as
Amazon allows me to make it.

AMI IDs
-------

The NEMS Linux AMI is found under *Community AMIs* on the following AWS
Service Endpoints. If you wish to deploy on a different AWS Service
Endpoint and are a current Patron supporting the project on Patreon,
please let me know and I will copy the AMI to your preferred region.
Since this costs me extra money to do, I only do it by request, and only
for those who contribute to the project.

NEMS 1.5 AMI Build 1
^^^^^^^^^^^^^^^^^^^^

- North Virginia (us-east-1) ami-03480e018178d1c75
- Ireland (eu-west-1) ami-07d0a43c2844ae01c


Introduction
------------

The NEMS Linux AMI leverages Amazon's T2 instance types, dramatically
reducing the cost of running a NEMS Server in the Cloud by bursting to
full core performance only when required. T2 instances are also
available to use in the AWS Free Tier, which includes 750 hours of
t2.micro instances each month for one year for new AWS customers.

The NEMS Linux AMI is an amd64 build.

AWS Requirements
----------------

The NEMS Linux AMI requires the following:

-  If monitoring 1-20 hosts: t2.micro or higher EC2 instance
-  If monitoring more than 20 hosts: t2.medium or higher EC2 instance
-  An elastic IP address
-  Volume is 16 GB by default and may need to be increased in time

Deployment Notes
----------------

-  **Important:** Before booting, you must configure an elastic IP
   address for your NEMS Linux instance. Failure to do this will break
   several key features, including NEMS Cloud Services, NEMS CheckIn,
   and your daily backup.

-  To access NEMS Linux remotely, you will need to configure your
   Security Group for the NEMS Linux instance to allow incoming
   connections on the NEMS Linux ports
   (See `Networking <../config/networking.html>`__ for more
   info). It is recommended to make these accessible :underline:`only`
   from your trusted IP address(es).

-  NEMS Linux allows you to use either
   `username/password combinations <default_password.html>`__ or
   username/key pair combinations to login via SSH. As this could pose a
   security issue, please ensure only your own IP address has access to
   NEMS Linux ports (in your EC2 Security Group configuration for the
   instance).

Re-Initializing
---------------

-  If you run `nems-init <../gettingstarted/initialization.html>`__ on a
   NEMS Server that has already been initialized, the server's public key
   and all trust relationships will be transferred to the new user prior
   to the old user being purged.
