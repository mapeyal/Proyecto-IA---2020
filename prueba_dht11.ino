#include "DHT.h" //Importamos la librería que nos perimte trabajar con el sensor DHT

// CONSTRUCTOR DEL OBJETO DHT RECIBE EL PIN EN EL QUE SE CONECTA EL SENSOR
// Y TAMBIEN RECIBE EL TIPO DE SENSOR QUE VAMOS A CONECTAR
DHT dht(2, DHT11);

void setup() {
  // PREPARAR LA COMUNICACION SERIAL
  Serial.begin(9600);  
  // PREPARAR LA LIBRERIA PARA COMUNICARSE CON EL SENSOR
  dht.begin();
}

void loop() {
  // LEER LA TEMPERATURA USANDO EL METODO READTEMPERATURE
  int t = dht.readTemperature();
  //LEER EL VALOR DEL LA LUZ UTILIZANDO UNA ENTRADA ANALÓGICA
  int sensorluz = analogRead(A1);
  // CONVERTIR EL VALOR DE LUZ A LUX
  int Lux = 1024.0 * 10 / sensorluz - 10;
  // IMPRIMIR EN PANTALLA LOS VALORES
  Serial.print(Lux);Serial.print(","); Serial.print(t);Serial.print("\n");

  // ESPERAR ENTRE MEDICIONES, NECESARIO PARA EL BUEN FUNCIONAMIENTO
  delay(2000);
}
