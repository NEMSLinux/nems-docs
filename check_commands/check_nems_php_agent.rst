NEMS PHP Server Agent
=====================

Monitor your Linux-based PHP-enabled web server with the NEMS PHP Server Agent.

Requirements
------------

A Linux-based public web server with PHP 5.2+.

I have tested successfully on Debian 10 with PHP 7.3 as well as Debian 7 with PHP 5.2. I have not tested on any non-Debian system, so if you do, please let me know if it works or not and I will add it here.

Usage
-----

Obtaining your PHP Agent
~~~~~~~~~~~~~~~~~~~~~~~~

In NEMS SST, download your custom nems-agent.php file. Upload this file to your web server and add the NEMS PHP Agent check command in NEMS NConf.

.. Tip:: You'll notice in the check commands below, the actual script filename is entered. This is intentional, and allows you to add obscurity if desired by naming your NEMS PHP Server Agent anything you like (as long as it has a .php extension).

Check Command
-------------

*check_nems_php_agent* is part of NEMS Linux 1.6.

Why Use the NEMS PHP Server Agent
---------------------------------

The NEMS PHP Server Agent is designed specifically to collect system data from a PHP server. Disk space and usage, memory size and usage, system load, etc. Unlike NRPE, the agent reports very specific data rather than running remote commands on your server. This makes it easier to use on a public server where firewall rules might be too complex for novice sysadmins to make NRPE a safe option. The NEMS PHP Server Agent is designed to be safe out of the box, and incredibly easy to deploy: Just upload it to a public folder on your web server and point your check commands on your NEMS Server to the URL.

Check Command Arguments
~~~~~~~~~~~~~~~~~~~~~~~

-  **Warn Threshold / Critical Threshold** - Set your
   thresholds. Can be a positive floating point number or integer.
-  **URL** - The full URL to your *nems-agent.php* on the remote
   | server. File can be renamed as desired, but provided URL must
   | resolve to the agent on the remote server.
-  **Check**

  - ``mem`` Percent Memory Usage
  - ``.`` Percent Disk Usage (Running Folder)
  - ``disk`` Percent Disk Usage (/)
  - ``var`` Percent Disk Usage (/var)
  - ``net`` Network Usage Mb/s
  - ``netrx`` Network Usage Mb/s Download Only
  - ``nettx`` Network Usage Mb/s Upload Only
  - ``load`` 15 Minute System Load Average

.. note:: All network checks require ``ifstat`` be installed on the remote server. This can easily be installed with apt or yum, depending on your distro.

CLI Examples
~~~~~~~~~~~~

WARN if 15 minute system load average exceeds 3, CRIT if over 9:

.. code-block:: console

  ./check_nems_php_agent 3 9 https://example.com/nems-agent.php load

WARN if / disk usage is over 80%, CRIT if over 90%.

.. code-block:: console

  ./check_nems_php_agent 80 90 https://example.com/nems-agent.php disk

WARN if either up or down network usage exceed 1 Mb/s, CRIT if over 2 Mb/s:

.. code-block:: console

  ./check_nems_php_agent 1 2 https://example.com/nems-agent.php net

Data Security
-------------

All data is encrypted server-side using AES-128-ECB using an encryption/decryption key you provide in NEMS System Settings Tool.

Under The Hood
--------------

The agent outputs the following JSON string (Sample data):

.. code-block:: JSON

  {"ver":{"nems":"1.6","nemsagent":"1.1"},"data":"pICGwq5UL3O8yNEYdPrQh\/8PGCjsXQUx9mh9VIQloFJ\/K8BsB5AT9L2ixwlsiDAJGjWR1RnhsrCFHVnKD9p3cmRxhQf\/knW6F+EkDS3CnkrlXWLSPJ6p+gfZjIq16NSREvfaaPJZEY93mBrgSFArs+C8advgKL+0jz2a55ItGk0BY6AKvOMuFXfxzwd3i7485tusJaP9X8K9dL5msEvHfPLKdORyTUm7iNt6ssFARMzg4oXoVnebT4okZ6eyG3tjQIBPOFebmNAO78agymi6UEm44u\/wfPmUtkEtU841FVmcfGLxcEIoogzG9vjH8q7urs2RetcBVpVhj5Z+T+v8qa9oQ7Pi1tbf2\/IhF+eLE9cSkmMlmbFbJ70hJqaY2gssiwb9tZ6g0dX+WA8+ujTzmCzBdNJ09HabaLVzXTqR4cGyFM3mXYQl+SdDSdmeZ\/vw\/sG4oSFxxKzhxmOpCM5qBw==","auth":"312433c28349f63c4f387953ff337046e794bea0f9b9ebfcb08e90046ded9c76"}

That is what a user would see if they were to open the agent in their browser, and is what is downloaded to your NEMS Server when the check commands run.

Your NEMS Server knows your decryption key used by the agent to encrypt the data. When decrypted by your NEMS Server, the data looks like this:

.. code-block:: php

  Array
     (
       [ver] => Array
           (
               [nems] => 1.6
               [nemsagent] => 1.1
           )
       [data] => Array
           (
               [cpu] => Array
                   (
                       [usage] => 0
                       [model] => Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz
                       [loadaverage] => Array
                           (
                               [1] => 0
                               [5] => 0
                               [15] => 0
                           )
                   )
               [mem] => Array
                   (
                       [percent] => 23.5
                       [total] => 0.472
                       [free] => 0.032
                       [used] => 0.44
                   )
               [storage] => Array
                   (
                       [.] => Array
                           (
                               [path] => /var/www/html
                               [free] => 6.11
                               [total] => 7.69
                               [used] => 1.58
                               [percent] => 0
                           )
                       [/] => Array
                           (
                               [free] => 6.11
                               [total] => 7.69
                               [used] => 1.58
                               [percent] => 0
                           )
                       [/var] => Array
                           (
                               [free] => 6.11
                               [total] => 7.69
                               [used] => 1.58
                               [percent] => 0
                           )
                   )
               [network] => Array
                   (
                       [rx] => 0.01
                       [tx] => 0.01
                   )
           )
       [auth] => 312433c28349f63c4f387953ff337046e794bea0f9b9ebfcb08e90046ded9c76
     )

The "auth" hash is a cryptographically-safe hash of your encrypted passphrase, and is what your NEMS Server uses to ensure the NEMS Server passphrase matches that of your NEMS PHP Server Agent. In this way, a third party cannot find a nems-agent.php running on your server and access your data from their NEMS Server. They will receive an error that the auth key does not match. Similarily, it means you can deploy your NEMS PHP Server Agent on as many PHP servers as you like, and even use multiple NEMS Servers to monitor it (as long as you key in the same passphrase on each NEMS Server).

This data output above is used by your NEMS Server's *check_nems_php_agent* check commands.
