.. include:: ../../global.rst

NEMS Linux for Khadas Single Board Computers
============================================

Khadas VIM3
-----------

.. figure:: ../../img/khadas_vim3_basic.png
  :width: 400
  :align: center
  :alt: Khadas VIM 3

You can boot from SD or USB, then install NEMS Linux to the integrated
eMMC storage by typing;

.. code-block:: console

    sudo nems-install

LED Indicators
^^^^^^^^^^^^^^

The Khadas VIM3 contains two buil-in LEDs which NEMS Warning Light utilizes by default.

.. list-table:: Warning Light on VIM3
   :header-rows: 1

   * - LED
     - Meaning
   * - White Flashing
     - Unknown State or System is Booting
   * - White Solid
     - OK state
   * - White Solid, Red Flashing
     - Warning State
   * - Red Solid
     - Critical State
