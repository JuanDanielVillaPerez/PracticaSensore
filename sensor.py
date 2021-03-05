import RPi.GPIO as GPIO
import time

class sensor():

    def ultrasonico(self):
        trig = 6
        ech = 13
         
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(ech, GPIO.IN)

        while True:

            try:
                GPIO.output(trig, GPIO.LOW)
                time.sleep(0.5)

                GPIO.output(trig, GPIO.HIGH)
                time.sleep(0.00001)
                GPIO.output(trig, GPIO.LOW)

                while True:
                    pulso_inicio = time.time()
                    if GPIO.input(ech) == GPIO.HIGH:
                        break
        
                while True:
                    pulso_fin = time.time()
                    if GPIO.input(ech) == GPIO.LOW:
                        break
                    duracion = pulso_fin - pulso_inicio
    
                    distancia = (34300 * duracion) / 2

                    ultrasonico = "Distancica: %.2f cm" % distancia 
                    print(ultrasonico)
    
    
            finally:
                time.sleep(5.0)
        return (1,"Ultrasonico",distancia,2)

    def pir(self):
        # Import required Python libraries

        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT) #Configuramos el pin 7, gpio 4 como salida (para un le
        # Define GPIO to use on Pi
        GPIO_PIR = 21
        #GPIO.setup(4, GPIO.OUT) #Configuramos el pin 4 como salida (para un le
        print ("PIR Module Test (CTRL-C to exit)")
        # Set pin as input
        GPIO.setup(GPIO_PIR,GPIO.IN) # Echo
        Current_State = 0
        Previous_State = 0
        try:
            print ("Waiting for PIR to settle ...")
            # Loop until PIR output is 0
            while GPIO.input(GPIO_PIR)==1:
                Current_State = 0   
                print ("Ready")
                # Loop until users quits with CTRL-C
            while True :
                # Read PIR state
                Current_State = GPIO.input(GPIO_PIR)
                if Current_State==1 and Previous_State==0:
                    # PIR is triggered
                    print ("Motion detected!")
                    GPIO.output(4,False) #Encendemos el led
                    time.sleep(5) #Pausa de 5 segundo
                    GPIO.output(4,True)
                    time.sleep(3)
                    # Record previous state
                    Previous_State=1
                elif Current_State==0 and Previous_State==1:
                    # PIR has returned to ready state
                    print ("Ready")
                    Previous_State=0
                    # Wait for 10 milliseconds
                    time.sleep(0.01)
        except KeyboardInterrupt:
            print ("Quit")
            # Reset GPIO settings
            GPIO.cleanup()
        return

    def temperatura(self):
        return

    def humedad(self):
        return