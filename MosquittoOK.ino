#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* ssid = "CasaDePiedra";
const char* password = "iranzueirene";
const char* mqtt_server = "192.168.1.191";

WiFiClient espClient;
PubSubClient client(espClient);

long lastMsg = 0;
char msg[50];
int value = 0;
int pin_rele = D1;
int pin_bi = D4;

void setup_wifi()
  {
  delay(10);
  Serial.println(); Serial.print("Connecting to "); Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
  Serial.println("\nWiFi connected, IP address: "); Serial.println(WiFi.localIP());
  }

void callback(char* topic, byte* payload, unsigned int length)
  {
  Serial.print("Message arrived ["); Serial.print(topic); Serial.print("] ");
  for (int i = 0; i < length; i++) { Serial.print((char)payload[i]); }
  Serial.println();
  switch ((char)payload[0])
    {
    case '0':                 // HIGH es apagar
      digitalWrite(pin_rele, HIGH);
      digitalWrite(pin_bi, HIGH);
      Serial.println('0');
      break;
    case '1':                 // LOW es encender
      digitalWrite(pin_rele, LOW);
      digitalWrite(pin_bi, LOW);      
      Serial.println('1');
      break;
    case '?':    // your hand is a few inches from the sensor
      if (digitalRead(pin_rele)==0) Serial.println("Encendido");
      else                          Serial.println("Apagado");
      for (int x=0; x<4 ; x++) { digitalWrite(BUILTIN_LED, LOW); delay(300); digitalWrite(BUILTIN_LED, HIGH); delay(300); }
      break;
    }
  }

void reconnect()
  {
  while (!client.connected())
    {
    Serial.print("Intentando conectar MQTT...");
    if (client.connect("D1-0002"))
      {
      Serial.println("Conectado");
      client.publish("casa/2", "Soy el D1 - 2.");
      client.subscribe("casa/2");
      }
    else
      {
      Serial.print("Error, rc="); Serial.print(client.state());
      Serial.println(" Reintento en 5 segundos ..."); delay(5000);
      }
    }
  }

void setup()
  {
  pinMode(pin_rele, OUTPUT);
  pinMode(pin_bi, OUTPUT);
  digitalWrite(pin_rele, HIGH);
  digitalWrite(pin_bi, HIGH);
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  }

void loop()
  {
  if (!client.connected()) reconnect();
  client.loop();
  long now = millis();
  if (now - lastMsg > 10000) // un minuto entre transmisiones
    {
    lastMsg = now;
    Serial.print("Publicando: Hola");
    client.publish("casa/2", "Hola");
    }
  }
