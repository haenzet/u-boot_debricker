u-boot_debricker
================

This phyton script was hacked together to flash u-boot or firmware of a TP-Link WDR4300. Unfortunately my router was not responding to TFTP and ymodem/xmodem was not available on this u-boot version. It makes use of the u-boot built in mw (memory write) to flash the binaries.

Use at your own risk, it might destroy your devices. I am not responsible for any damage caused directly or indirectly by this software. Only use this if you fully understand all consequences and what the script is actually doing.

How to use: ./debricker.serial.py hexconverted.dump /dev/tty.usbserial

The file to be flashed can be obtained by converting it with xxd -c ps unhexed.bin > hexed.dump
File should contain something similar to:

100000ff
00000000
100000fd
00000000
100001a0
00000000
1000019e
00000000
1000019c
00000000
