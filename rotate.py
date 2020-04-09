import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BOARD) 

GPIO.setup(35, GPIO.OUT)
p = GPIO.PWM(35,50)	
p.start(5.0)				
p.stop()
GPIO.cleanup()