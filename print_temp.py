import spidev
import max6675
import time
import sys

# Raspberry Pi software SPI configuration.
#CLK = 14
#CS  = 10
#DO  = 13
#sensor = max6675.Max6675(CLK, DO)

sensor = max6675.Max6675(0, 0)

while True:
    try:
        print(sensor.temperature)
        time.sleep(0.5)
    except KeyboardInterrupt:
            print("Terminating")
            sys.exit()
            #reset code that resets the temperatureadfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfg