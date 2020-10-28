NEMS PHP Server Agent
=====================

Monitor your Linux-based PHP-enabled web server with the NEMS PHP Server Agent.

Usage
-----

In NEMS SST, download your custom nems-agent.php file. Upload this file to your web server and add the NEMS PHP Agent check command in NEMS NConf.

Check Command
-------------

*check_nems_php_agent* is part of NEMS Linux 1.6.

Why Use the NEMS PHP Server Agent
---------------------------------

The NEMS PHP Server Agent is designed specifically to collect system data from a PHP server. Disk space and usage, memory size and usage, system load, etc. Unlike NRPE, the agent reports very specific data rather than running commands on your server. This makes it easier to use on a public server where firewall rules might be too complex for novice sysadmins to make NRPE a safe option. The NEMS PHP Server Agent is safe out of the box, and incredibly easy to deploy: Just upload it to a public folder on your web server and point your check commands on your NEMS Server to the URL.

Check Command Arguments
~~~~~~~~~~~~~~~~~~~~~~~

-  **URL** - The URL to your *nems-agent.php* on the remote server.
-  **Check** - Percent Memory Usage [mem], Percent Disk Usage (/) [disk], Percent Disk Usage (/var) [var], Network Usage Mb/s [net], Network Usage Mb/s Download Only [netrx], Network Usage Mb/s Upload Only [nettx], 15 Minute System Load Average [load].
-  **Warn Up / Warn Down / Critical Up / Critical Down** - Set your
   thresholds. Can be a positive floating point number or integer.

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

  {"ver":{"nems":"1.6","nemsagent":"1.0"},"data":"pICGwq5UL3O8yNEYdPrQh\/8PGCjsXQUx9mh9VIQloFJ\/K8BsB5AT9L2ixwlsiDAJGjWR1RnhsrCFHVnKD9p3cmRxhQf\/knW6F+EkDS3CnkrlXWLSPJ6p+gfZjIq16NSREvfaaPJZEY93mBrgSFArs+C8advgKL+0jz2a55ItGk0BY6AKvOMuFXfxzwd3i7485tusJaP9X8K9dL5msEvHfPLKdORyTUm7iNt6ssFARMzg4oXoVnebT4okZ6eyG3tjQIBPOFebmNAO78agymi6UEm44u\/wfPmUtkEtU841FVmcfGLxcEIoogzG9vjH8q7urs2RetcBVpVhj5Z+T+v8qa9oQ7Pi1tbf2\/IhF+eLE9cSkmMlmbFbJ70hJqaY2gssiwb9tZ6g0dX+WA8+ujTzmCzBdNJ09HabaLVzXTqR4cGyFM3mXYQl+SdDSdmeZ\/vw\/sG4oSFxxKzhxmOpCM5qBw==","auth":"312433c28349f63c4f387953ff337046e794bea0f9b9ebfcb08e90046ded9c76"}

That is what a user would see if they were to open the agent in their browser, and is what is downloaded to your NEMS Server when the check commands run.

Your NEMS Server knows your decryption key. When decrypted, the data looks like this:

.. code-block:: php

  Array
     (
       [ver] => Array
           (
               [nems] => 1.6
               [nemsagent] => 1.0
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

This data is used by your NEMS Server's *check_nems_php_agent* check commands.
