Omzlo NEMS Warninglight pHAT
============================

The NEMS Warninglight pHAT from Omzlo is an i2c accessory for Raspberry Pi GPIO that provides visual feedback by way of status lights. For testing or convenience, the pHAT features state LEDs on-board, which, like a connected tower signal light, will indicate the state of your environment.

.. figure:: ../../img/omzlo-warninglight-prototype.jpg
  :width: 600
  :align: center
  :alt: An early prototype of the Omzlo NEMS Warninglight pHAT

  The early development prototype of the NEMS Warninglight pHAT from Omzlo.

Buy a NEMS Warninglight pHAT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The NEMS Warninglight pHAT is in development testing and will be released soon. Pre-orders may become available, so please check back.

Connection
~~~~~~~~~~

The NEMS Warninglight pHAT features a terminal block which allows the connection of a 12V or 24V NPN (sinking) type signal light.

.. Warning:: Only 12-24V signal lights are supported. Do not connect high-voltage (E.G. 110V/220V) signal lights or power supplies to the pHAT.

.. figure:: ../../img/omzlo-warninglight-phat-connection-diagram.jpg
  :width: 600
  :align: center
  :alt: Omzlo NEMS Warninglight pHAT connection diagram

  Tower signal light connection diagram.

You will need two separate power sources: one 5V USB input for the pHAT, which powers the Raspberry Pi, and one 12V or 24V power source for the connected tower light, depending on the voltage of the light.

Indications
~~~~~~~~~~~

- **Green Solid** Your hosts and services are in an OK state.
- **Orange Solid** At least one host or service has entered a Warning state.
- **Orange Flashing** At least one host or service has entered an unknown state.
- **Green Solid, Orange Flashing** Your hosts and services are in an OK state, however at least one is flapping.
- **Red Solid** At least one host or service has entered a Critical state.

Manufacture
~~~~~~~~~~~

The Omzlo NEMS Warninglight pHAT is designed and assembled in Greece.

Certification
~~~~~~~~~~~~~

None yet. Working on getting CSA certification.

Developers
~~~~~~~~~~

NEMS Warninglight is a software component of NEMS Linux developed by `Robbie Ferguson <https://twitter.com/robbieferguson>`__ for `Category5 TV Network <https://category5.tv/>`__.

NEMS Warninglight pHAT is an accessory designed and developed by `Alain Pannetrat <https://twitter.com/alainpannetrat>`__ for `Omzlo <https://omzlo.com/`__.
