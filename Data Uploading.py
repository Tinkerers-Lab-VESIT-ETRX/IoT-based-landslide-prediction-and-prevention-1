import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))

ser = serial.Serial("COM3", 9600)
print(ser.readline())
res =1
i=0
time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

while res:
     firebase1 = firebase.FirebaseApplication('https://python-sample-4df98-default-rtdb.firebaseio.com/', None)
     
     for i in range(0,5):
             string1=str(ser.readline())
             string1=string1[2:][:13]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':string1,
               'time': datetime.now().strftime("%H:%M")               
          }
             result = firebase1.patch('https://python-sample-4df98-default-rtdb.firebaseio.com/'+'/Vibration/'+ str(i), data)
             print(result)
             string1=str(ser.readline())
             string1=string1[15:][:19]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':string1,
               'time': datetime.now().strftime("%H:%M")               
          }
             result = firebase1.patch('https://python-sample-4df98-default-rtdb.firebaseio.com/'+ '/Humidity/'+ str(i), data)
             print(result)
             string1=str(ser.readline())
             string1=string1[33:][:30]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':string1,
               'time': datetime.now().strftime("%H:%M")               
          }
             result = firebase1.patch('https://python-sample-4df98-default-rtdb.firebaseio.com/'+ '/Temperature/'+ str(i), data)
             print(result)
             string1=str(ser.readline())
             string1=string1[62:][:27]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':string1,
               'time': datetime.now().strftime("%H:%M")               
          }
             result = firebase1.patch('https://python-sample-4df98-default-rtdb.firebaseio.com/'+ '/Heat_Index/'+ str(i), data)
             print(result)
     

    
     res=0
