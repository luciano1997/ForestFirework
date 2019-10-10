import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# read data using pin 14
instance = dht11.DHT11(pin=4)
while True:
    #result = instance.read()
    #if result.is_valid():
        fecha = str(datetime.datetime.now())
#fecha_

        temperature = 10
        humidity = 25
        fecha = str(datetime.datetime.now())
        print("Ultima Lectura: " + str(datetime.datetime.now()))
        print(f'''Temperatura: {temperature} °C''')
        print(f'''humedad:     {humidity}%''')
        # "w", "r" y si queremos que se abra para añadir sin borrar las líneas actuales del archivo debemos hacerlo con el parámetro "a" (append).
        #print(f'''Temperatura: {result.temperature} °C''')
        #print(f'''humedad:     {result.humidity}%''')
        archivo = open("datos.txt","a")
        archivo.write(f'''Lectura: {fecha[0:16]} temperatura: {temperature} , humedad: {humidity}
''')
        archivo.close
        #if (result.humidity>30):
        #    print(f'''
        #        Alerta!
   # Humedad relativa del aire sobre 30%''')
    #        if (result.temperature>30):
     #           print("temperatura y humedad sobre los rangos")
                # if (viento>30):
                #    print("riesgo de incendio")
        print("--------------------------------------")        
   # else: 
    #    print("Error: %d" % result.error_code)
    #    print(result.humidity)
    #    print(result.temperature)
    #    break
time.sleep(3)

