#!/usr/bin/python

import sys #make cli arguments available
import time
import serial


def main(argv):
  inputfile = sys.argv[1]
  #ext_off = sys.argv[3]


  print "Using: ", inputfile + " as firmware"

  # Firmware parameters

  offset   = int("0x81000000", base=16) # 0x81000000 is memory!
  #offset   = int("0x9f020000", base=16) # 0x9f020000 is NAND!
  #offset   = int("0x9F02E228", base=16) # 0x9f020000 is NAND!, use different offset if file has been transferd only paritally
  incr     = int("0x4", base=16)
  length   = int("0x7c0000", base=16)
  current  = 0
  end      = current + offset + length
  current  += offset

  # Serial Connection

  port = sys.argv[2]
  baudrate = 115200

  ser = serial.Serial(
      port,
      baudrate
  )

  ser.xonxoff = False
  ser.rtscts = False
  ser.dsrdtr = False
  ser.timeout = 0 

  ser.close()
  ser.open()
  ser.isOpen()

  total_line_count = len(open(inputfile).readlines(  ))
  print "Total Lines: ", total_line_count 

  with open(inputfile) as f:
    line_num = 1

    for line in f:

      send = "mw 0x%0.8X 0x%s" % (current, line)
      ser.write(send)
      #ser.write(line)
      ser.flush()
      current += incr

      buf = ""

      time.sleep(0.01)
      print "[%00000000d/%00000000d] %s" % (line_num, total_line_count, send)
      #pcounter = 0
      while 1:
        waitingToBeRead = ser.inWaiting()
        
        if waitingToBeRead == 0:
          break
        
        time.sleep(0.1)
        buf += ser.read(waitingToBeRead)

        # Wait for the "xb12>" prompt so we know data has been written
        if buf.find("db12x> %s" % send) != -1:
          break
              

      line_num += 1
    
  ser.close()
  print "i am done"
if __name__ == "__main__":
   main(sys.argv[1:])
