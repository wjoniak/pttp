import serial

data = []

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('/dev/cu.usbmodem1301', 115200, timeout=1)


while True:
    line = ser.readline()   # read a byte
    if line:
        #string = line.decode()  # convert the byte string to a unicode string
        #num = int(string) # convert the unicode string to an int
        #data.append(num)
        print(string,'\n')

ser.close()

