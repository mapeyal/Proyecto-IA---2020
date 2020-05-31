import httplib2 #Importamos la librería para clientes http
import serial #Importamos la librería para poder trabajar con la placa arduino

writeKey = "Q5BU1GHSLR4MY5AM" # Key que nos da la página de thingspeak para nuestro canal

ser = serial.Serial('COM3',9600) #Abrimos el puerto con el cual permitimos la comunciación entre el Arduino y la PC

ser.readline() #Variable que almacena la información que se lee en una línea de un archivo
conn =  httplib2.Http() #Variable en la que creamos la conexión HTTP

while True:

	datoString = ser.readline() #Leemos una nueva línea enviada por el Arduino
	datos = str(datoString).split(",") #Separamos los datos recibidos
	luz = (datos[0][2:]) #Guardamos en un arreglo los datos recibidos, se lee desde la posición 0 hasta la 2
	temperatura = (datos[1][:-3]) #Guardamos en un arreglo los datos recibidos, se lee desde la posición 0 hasta la -2

	# ejemplo
	# +---+---+---+---+---+---+
	# | 9 | 5 | , | 2 | 8 | \n|
	# +---+---+---+---+---+---+
	#   0   1   2   3   4   5
	#  -5  -4  -3  -2  -1   0

	print ("Temperatura: "+temperatura+"°C Luz: "+luz+"V") #Imprimimos en consola el resultado

	conn.request("https://api.thingspeak.com/update?key=%s&field1=%s&field2=%s" %(writeKey,luz,temperatura) , "GET") #Escribimos los datos en thingspeak.com



