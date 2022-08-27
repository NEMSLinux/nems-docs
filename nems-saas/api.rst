NEMS SaaS API
=============

Trends API
^^^^^^^^^^

Obtain the JSON output of your NEMS SaaS endpoint trends for a duration of time.

``https://api-saas.nemslinux.com/trends/SAASKEY?ver=[num]``

``SAASKEY`` = Your NEMS SaaS Key

``ver``:

- ``0`` = [Default] The current state of your NEMS SaaS endpoints
- ``1`` = The last hour's trends for your NEMS SaaS endpoints
- ``2`` = The past 6 hours trends
- ``3`` = The past 12 hours trends
- ``4`` = 24 hour trend for your NEMS SaaS endpoints
- ``5`` = 7 days worth of trends
- ``6`` = 1 month trend
