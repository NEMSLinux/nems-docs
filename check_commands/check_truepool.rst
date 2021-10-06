Check Command: check_truepool
=============================

Check Truepool.io to ensure your Chia farm is online and farming to the pool.

*check_truepool* expects just one parameter (your Launcher ID) and responds
accordingly.

This check command requires NEMS Linux 1.6+.

Expected Responses
------------------

.. |check_truepool| image:: ../img/check_truepool.png
    :width: 395px
    :alt: check_truepool output in NEMS Adagios

+-------------------+
| |check_truepool|  |
+-------------------+

- ``OK`` - Farm is online and actively gaining points on Truepool.io
- ``WARNING`` - Farm appears connected, but is not gaining points
- ``CRITICAL`` - Either "Not found" (you provided an invalid Launcher ID) or
  "Farm Offline" (your farm has gained 0 points since the last win)

Configuration
-------------

Obtain your Chia launcher ID. See `this truepool.io knowledgebase article
<https://truepool.io/kb/set-friendly-leaderboard-name>`__ for help with this.

**NEMS Configurator Setup**

- Add a new Advanced Service
- Give the service a name such as "TruePool (Robbie)"
- Give the service a description such as "Chia Farm - Robbie" - I identify my farmer since I monitor multiple farmers
- Set Check Period to 24/7
- Set Notification Period to Work Hours (I don't need to be awoken if my farm goes down)
- Assign the advanced service to host	"NEMS"
- Set max check attempts: 5
- Set check interval: 10
- Set retry interval: 10
- Set first notification delay: 30
- Set notification interval: 120
- Set notification options: w,u,c,r
