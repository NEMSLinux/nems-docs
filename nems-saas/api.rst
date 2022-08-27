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
- ``7`` = Last 10 state changes
- ``8`` = Last 25 state changes
- ``9`` = Last 50 state changes

Sample JSON Output:

``{"results":[{"ok":4,"warn":0,"crit":0,"statechange":"2022-08-27 07:51:40"}]}``

Results are presented most recent to oldest. Timezone of statechange matches the user's defined timezone.
