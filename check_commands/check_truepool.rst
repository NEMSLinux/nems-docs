Check Command: check_truepool
=============================

Check Truepool.io to ensure your Chia farm is online and farming to the pool.

*check_truepool* expects just one parameter (your Launcher ID) and responds
accordingly.

This check command requires NEMS Linux 1.6+.

Expected Responses
------------------

- ``OK`` - Farm is online and actively gaining points on Truepool.io
- ``WARNING`` - Farm appears connected, but is not gaining points
- ``CRITICAL`` - Either "Not found" (you provided an invalid Launcher ID) or
  "Farm Offline" (your farm has gained 0 points since the last win)
  
Configuration
-------------

Obtain your Chia launcher ID. See `this truepool.io knowledgebase article
<https://truepool.io/kb/set-friendly-leaderboard-name>`__ for help with this.
