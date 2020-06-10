#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"
#define DHTTYPE DHT22
#define BICHO "casa/3-in"
#define SALIDA "casa/3-out"
const char* ssid = "Bichoteca";
const char* password = "cucaracha";
const char* mqtt_server = "10.10.10.10";
int pin_rele = D1;
int pin_ht   = D3;
int pin_bi   = D4;
float h;
float t;
String res;
DHT dht(pin_ht, DHTTYPE);

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.print ("Conectando a "); Serial.println(ssid);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
  Serial.print("Conectado a la red WiFi con IP "); Serial.println(WiFi.localIP());
  }

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Mensaje recibido <"); Serial.print(topic); Serial.print("> ");
  for (int i = 0; i < length; i++) { Serial.print((char)payload[i]); } 
  Serial.println();
  switch ((char)payload[0]) {
    case '0':                 // HIGH es apagar
      digitalWrite(pin_rele, HIGH);
      digitalWrite(pin_bi, HIGH);
      client.publish("outTopic", "Encendido");
      break;
    case '1':                 // LOW es encender
      digitalWrite(pin_rele, LOW);
      digitalWrite(pin_bi, LOW);      
      client.publish("outTopic", "Apagado");
      break;
    case '2':  
      h = dht.readHumidity();
      t = dht.readTemperature();
      if (isnan(h) || isnan(t)) { h=0; t=0; }
      Serial.print("H: "); Serial.print(h); Serial.print(" T: "); Serial.println(t);
      res = "T:" + (String)t + "H:" + (String)h;
      Serial.println("Publicando: " + res + "\n");      
      delay(500);      
      client.publish(SALIDA, (char*)res.c_str());
      delay(500);
      break;
    case '9':
      if (digitalRead(pin_rele) == 1)
        client.publish(SALIDA, "Apagado");
      else
        client.publish(SALIDA, "Encendido");
      break;
    }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Intentando conectar con broker MQTT ... ");
    if (client.connect(BICHO)) {
      Serial.println("conectado");
      client.publish(SALIDA, "Aquí estoy");
      client.subscribe(BICHO);
    } else {
      Serial.print("Error de conexción con el broker MQTT, rc=");
      Serial.print(client.state());
      Serial.println(" reintento en 5 segundos");
      delay(5000);
    }
  }
}

void setup()
  {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  pinMode(pin_bi, OUTPUT);
  digitalWrite(pin_bi, HIGH);
  pinMode(pin_rele, OUTPUT);
  digitalWrite(pin_rele, HIGH);
  }

void loop()
  {
  if (!client.connected()) reconnect();
  client.loop();
  }
