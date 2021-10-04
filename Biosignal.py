import serial

class Biosignal:
    ser = serial.Serial('/dev/cu.usbmodem1301', 115200, timeout=1)



    def read(self):
        string = line.decode()
        #signal.ibi = ibi
        signal.bpm = string
        #signal.gsr = gsr
