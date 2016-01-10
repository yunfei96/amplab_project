import Adafruit_BBIO.UART as UART
import serial
import math
UART.setup("UART1")
ser = serial.Serial(port = "/dev/ttyO0",baudrate = 9600)
if ser.isOpen:
	ser.write(chr(0))
ser.close()
ser.open()
ser.write(chr(0))
step=63
def moveLeft(power):
	if power==0:
		output=64
	elif power>0:
		if power>100:
			power=100
			print("speed cap")
		output=(power/float(100))*step
		output=round(output,0)
		output=int(output)
		output=64+output
	elif power<0:
		if power<-100:
			power=-100
			print("speed cap")
		power=abs(power)
		output=(power/float(100))*step	
		output=round(output,0)
		output=int(output)
		output=64-output
			
	else:
		output=0
		print("power input error")
	print(output)
	ser.write(chr(output))

def moveRight(power):
	if power==0:
		output=192
	elif power>0:
		if power>100:
			power=100
			print("speed cap")
		output=(power/float(100))*step	
		output=round(output,0)
		output=int(output)
		output=192+output
	elif power<0:
		if power<-100:
			power=-100
			print("speed cap")
		power=abs(power)
		output=(power/float(100))*64	
		output=round(output,0)
		output=int(output)
		output=192-output
	else:
		output=0
		print("power input error")
	print (output)
	ser.write(chr(output))



	
