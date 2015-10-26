#Prueba de interrupciones
import RPi.GPIO as GPIO #Libreria Python GPIO
import time #Libreria Time
GPIO.setmode(GPIO.BCM) #Establecemos el sisetma de numeracion de pins BCM
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(21, GPIO.IN)
def my_callback(channel):
	#print "Flanco positivo"
	a= GPIO.input(19)
	b= GPIO.input(26)
	if a==1 and b==1:
		print "1"
	if a==0 and b==1:
		print "2"
	if a==1 and b==0:
		print "3"
	if a==0 and b==0:
		print "Error"
	#print "Fin"	



	
GPIO.add_event_detect(21, GPIO.RISING, callback=my_callback,bouncetime=150)

 
while True:
	n=0
	


