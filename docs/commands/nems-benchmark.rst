NEMS Linux Command: nems-benchmark
==================================

*nems-benchmark* is a benchmarking tool to determine the performance of
your NEMS Linux server.

You may run it manually if you like, but shouldn't have to since the
benchmark runs automatically every Sunday morning and you can just cat
the log file located at */var/log/nems/benchmark.log*

*nems-benchmark* tests the following:

-  LZMA multi-threaded and single-threaded performance
-  SD Card Read/Write Speed
-  Memory Read/Write Speed
-  Free Space on All Media
-  Free Memory
-  Internet Send/Receive Speed (Provided By https://speedtest.net/)

By observing the results of the weekly benchmark test, you may be able
to spot a failing SD card or other system problem.