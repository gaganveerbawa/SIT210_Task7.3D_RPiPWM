# Made by
# Gaganveer Singh
# 2210994783

# Importing necessary modules
from gpiozero import DistanceSensor, PWMOutputDevice
from time import sleep

# Defining GPIO pins
trigPin = 17  
echoPin = 27 
buzzerPin = 22   

# Initializing the buzzer for PWM control
buzzer = PWMOutputDevice(buzzerPin)

# Initializing the ultrasonic distance sensor with defined pins and max distance of 1.0 meter
ultraSonicSensor = DistanceSensor(trigger=trigPin, echo=echoPin, max_distance=1.0)

try:
    while True: 
        sleep(0.5)   
        
        # Calculating object's distance in centimeters      
        distanceInCM = ultraSonicSensor.distance * 100 
        print("Distance (CM): %.2f" %distanceInCM) # Printing the calculated distance
        
		# Mapping the distance to a value between 0 and 1 for PWM control of the buzzer
        # If distance is 100cm or more, buzzer value is 0 (silent). 
        # As distance decreases, buzzer sound intensity increases.
        buzz =  1.0 - (distanceInCM / 100)
        print("Buzz: %.2f" % buzz)
        
        # Setting the mapped value to the buzzer
        buzzer.value = buzz

except KeyboardInterrupt:
    print("Program Ended") # Printing a message when the program is terminated by the user
