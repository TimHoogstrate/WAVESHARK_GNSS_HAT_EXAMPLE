#!/usr/bin/python
# Filename: text.py
import serial
import time
ser = serial.Serial("/dev/ttyS0",115200)

W_buff = ["AT+CGNSPWR=1\r\n", "AT+CGNSSEQ=\"RMC\"\r\n", "AT+CGNSINF\r\n", "AT+CGNSURC=2\r\n","AT+CGNSTST=1\r\n"]
ser.write(W_buff[0].encode())
ser.flushInput()
data = ""
num = 0

try:
    while True:
        #print ser.inWaiting()
        file = open("Documents/test.txt", "a")
        while ser.inWaiting() > 0:
            data += ser.read(ser.inWaiting()).decode("utf-8")
        if data != "":
            file.write(data+"\n")
            data = data.split("\r\n")
            numberOfRows = len(data)
            #print ("length data")
           # print (len(data))
            if numberOfRows > 1:
                print ("gps")
                print (data[2])
                file.write(data+"\n")
                print ("accuracy")
                print (data[numberOfRows - 2])
                print ("course and ground speed")
                print (data[numberOfRows - 3])
                print ("number of active sattelites")
                print (sum("GLGSA" in s for s in data))
                print ("number of sattelites")
                print (sum("GPGSV" in s for s in data))
            #print ("length data")
            #print (data)
            if  num < 4:	# the string have ok
                #print (num)
                time.sleep(1)
                ser.write(W_buff[num+1].encode())
                num =num +1
            if num == 4:
                time.sleep(1)
                ser.write(W_buff[4].encode())
            data = ""
except keyboardInterrupt:
    if ser != None:
        ser.close()
            
