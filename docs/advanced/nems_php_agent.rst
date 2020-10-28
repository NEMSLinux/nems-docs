NEMS PHP Server Agent
=====================

Monitor your PHP-enabled web server with the NEMS PHP Server Agent.

Data Security
-------------

All data is encrypted server-side using AES-128-ECB.

Usage
-----

In NEMS SST, download your custom nems-agent.php file. Upload this file to your web server and add the NEMS PHP Agent check command in NEMS NConf.

Check Command
-------------

*check_nems_php_agent* is part of NEMS Linux 1.6.

Check Command Arguments
~~~~~~~~~~~~~~~~~~~~~~~

-  **URL** - The URL to your *nems-agent.php* on the remote server.
-  **Check** - Memory Usage, Disk Usage (/), Disk Usage (/var), Network Usage.
-  **Warn Up / Warn Down / Critical Up / Critical Down** - Set your
   thresholds. Can be a positive floating point number or integer.

Under The Hood
--------------

The agent outputs the following JSON string (Sample data):

.. code-block:: json

{"ver":{"nems":"1.6","nemsagent":"1.0"},"data":"pICGwq5UL3O8yNEYdPrQh\/8PGCjsXQUx9mh9VIQloFJ\/K8BsB5AT9L2ixwlsiDAJGjWR1RnhsrCFHVnKD9p3cmRxhQf\/knW6F+EkDS3CnkrlXWLSPJ6p+gfZjIq16NSREvfaaPJZEY93mBrgSFArs+C8advgKL+0jz2a55ItGk0BY6AKvOMuFXfxzwd3i7485tusJaP9X8K9dL5msEvHfPLKdORyTUm7iNt6ssFARMzg4oXoVnebT4okZ6eyG3tjQIBPOFebmNAO78agymi6UEm44u\/wfPmUtkEtU841FVmcfGLxcEIoogzG9vjH8q7urs2RetcBVpVhj5Z+T+v8qa9oQ7Pi1tbf2\/IhF+eLE9cSkmMlmbFbJ70hJqaY2gssiwb9tZ6g0dX+WA8+ujTzmCzBdNJ09HabaLVzXTqR4cGyFM3mXYQl+SdDSdmeZ\/vw\/sG4oSFxxKzhxmOpCM5qBw==","auth":"312433c28349f63c4f387953ff337046e794bea0f9b9ebfcb08e90046ded9c76"}

Your NEMS Server knows your decryption key. When decrypted, the data looks like this:

.. code-block:: json

{"ver":{"nems":"1.6","nemsagent":"1.0"},"data":"{\"cpu\":{\"usage\":0,\"model\":\"Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz\",\"loadaverage\":{\"1\":0,\"5\":0,\"15\":0}},\"mem\":{\"percent\":23.46,\"total\":0.472,\"free\":0.035,\"used\":0.43699999999999994},\"storage\":{\"\\\/\":{\"free\":6.11,\"total\":7.69,\"used\":1.58,\"percent\":0},\"\\\/var\":{\"free\":6.11,\"total\":7.69,\"used\":1.58,\"percent\":0}},\"network\":{\"rx\":0.01,\"tx\":0.01}}","auth":"312433c28349f63c4f387953ff337046e794bea0f9b9ebfcb08e90046ded9c76"}

This data is used by your NEMS Server's *check_nems_php_agent* check commands.
