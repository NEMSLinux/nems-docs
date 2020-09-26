TEMPer Thermal Sensor
=====================

.. figure:: ../../img/temper.png
  :width: 300
  :align: right
  :alt: TEMPer USB Thermal Sensor

  TEMPer USB Thermal Sensor

The TEMPer is an affordable (starting at under $20) USB digital thermometer that accurately senses temperatures from -55 to +125 degrees Celsius / -67 to +257 degrees Fahrenheit. This is an ideal addition to the server room to generate alerts should temperatures fall outside a safe threshold.

TEMPer devices work on all NEMS Linux hardware platforms. It will also work on the NEMS Linux virtual appliance, however you must connect the hardware to the virtual machine, which is beyond the scope of this documentation (please refer to the documentation for your hypervisor).

check_temper supports Critical and Warning states for both low (cold) and high (hot) temperatures.

.. note:: For optimum accuracy, it is recommended to plug your TEMPer device into a short USB extension cord so the thermal data isn't impacted by the heat pulled from the USB port of your NEMS Server.

Setting up check_temper
-----------------------

Simply add check_temper_temp or check_temper_hum as a service to your NEMS host, having connected the TEMPer device to your NEMS Server's USB port. You may specify your temperature thresholds in either degrees Celsius or Fahrenheit. NEMS will automatically determine which you are using.

Sample check commands are already included in NEMS Linux 1.5.2+ in the demo config. If you're deploying a new NEMS Server, simply plug in your TEMPer device and these checks will automatically detect it and begin registering data.

Buy TEMPer Thermal Sensor
-------------------------

* `Amazon.com <https://www.amazon.com/s/ref=as_li_ss_tl?k=temper+usb+sensor&ref=nb_sb_noss&linkCode=sl2&tag=nems-linux-20&linkId=5a736a3096cfce9a9e27e033115b3080&language=en_US>`__
* `Amazon.co.uk <https://www.amazon.co.uk/s/ref=as_li_ss_tl?k=temper+usb+sensor&ref=nb_sb_noss&linkCode=sl2&tag=nemslinux-21&linkId=0d3af2c3db4e8e4d27cd6420364bb94b&language=en_GB>`__
* `From the Manufacturer <http://www.pcsensor.com/usb-temperature-humidity.html>`__

Supported Devices
-----------------

Support is provided via `temper <https://github.com/urwen/temper>`__.

NEMS Linux includes support for TEMPer temperature and humidity sensor data.

+------------+-----------+-----------------+------+-----+
| Product    | Id        | Firmware        | Temp | Hum |
+============+===========+=================+======+=====+
| TEMPer     | 0c45:7401 | TEMPerF1.4      | ✔    | ✘   |
+------------+-----------+-----------------+------+-----+
| TEMPer     | 413d:2107 | TEMPerGold_V3.1 | ✔    | ✘   |
+------------+-----------+-----------------+------+-----+
| TEMPerHUM  | 413d:2107 | TEMPerX_V3.1    | ✔    | ✔   |
+------------+-----------+-----------------+------+-----+
| TEMPer2    | 413d:2107 | TEMPerX_V3.3    | ✔    | ✘   |
+------------+-----------+-----------------+------+-----+
| TEMPer1F   | 413d:2107 | TEMPerX_V3.3    | ✔    | ✘   |
+------------+-----------+-----------------+------+-----+
| TEMPerX232 | 1a86:5523 | TEMPerX232_V2.0 | ✔    | ✔   |
+------------+-----------+-----------------+------+-----+

Terminal Output
---------------

To receive the JSON output, type `nems-info temper`

TEMPer devices seem to have an issue on low-powered systems (such as Raspberry Pi) where due to the low power to the USB port, temper.py will respond with errors such as:

* Cannot read firmware identifier from device
* Unknown firmware ld_V3.1 TEMPerGold_V3.1: b'80800f874e200000'

To remedy this, `nems-info` silently loops through the output multiple times until a good thermal reading is obtained. The errors are hidden and only the clean JSON output is generated. This all happens very quickly and transparently, resulting in good output every time, with no errors.

Adding to your NEMS NConf
-------------------------

TEMPer check commands are already pre-configured in the NEMS Linux 1.5.2+ demo data. If you have removed them, or are using an older version of NEMS Linux, you can add the checks yourself.

*check_temper_temp* (temperature check) and *check_temper_hum* (humidity check) allow you to add TEMPer devices to your NEMS Server. The check has 4 thresholds: Critical Low, Warning Low, Warning High, Critical High. The number you enter may be in *either* degrees Celsius or Fahrenheit in the case of *check_temper_temp*. The system will automatically detect which you are using. The OK temperature will be any temperature that falls between Warning Low and Warning High. This way, you can receive alerts from your NEMS Server should the room temperature be either too cold or too hot. For *check_temper_hum*, the thresholds are in percent (just enter the number, not the percent sign).

Humidity Sensor Support
-----------------------

Sample command line for humidity sensor:

`/usr/lib/nagios/plugins/check_temper 20 35 65 80 hum`

Check Commands
--------------

As of NEMS Linux 1.5.2, both the temperature and humidity sensors are supported, and check commands are included in NEMS NConf.

* check_temper_temp
* check_temper_hum

Calibration
-----------

As of NEMS Linux 1.6, both the thermal sensor and humidity sensor can be calibrated within NEMS SST to ensure the highest level of accuracy.
