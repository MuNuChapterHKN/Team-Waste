/*
 * PROVA 0.2 : collegarsi al wifi e al server; dht
 * 
 */

//librerie necessarie 
#if defined(ESP8266)
#include <ESP8266WiFi.h>
#else
#include <WiFi.h>
#endif
#if defined(ESP8266)
#include <ESP8266WebServer.h>
#else
#include <WebServer.h>
#endif
#include <PubSubClient.h>

//sensore temperatura
#include "DHT.h"
#define DHTTYPE DHT22
#define DHTPIN 4
DHT dht(DHTPIN, DHTTYPE);

//credenziali router e server
const char* mqtt_server = "192.168.1.160"; //mqtt server
const char* ssid = "VillaBetoriRizzardo";
const char* password = "everest8848";

//oggetti wifi e server
WiFiClient espClient;
PubSubClient client(espClient);

//variabili per il messaggio di prova da inviare al server
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;
// per il led di prova
#define PIN_LED 32



void setup() {
  Serial.begin(115200);

  //inizializzo wifi e server
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  //inizializzo sensore temperatura
  dht.begin();
}

void loop() {
  
  //verifico continuamente la connessione, se non è connesso riconnetto tramite funzione
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  //per provare connessione al server invio messaggio ogni 15 sec
  unsigned long now = millis();
  if (now - lastMsg > 1000*5) {
    lastMsg = now;
    ++value;
    snprintf (msg, MSG_BUFFER_SIZE, "hello world #%ld", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("cestino/uscita", msg);

    leggiAmbiente();
  }

}

//funzione per connettersi al wifi
// ATTENZIONE: FUNZIONE BLOCCANTE 
void setup_wifi() {

  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

//funzione per iscriversi ad un topic in ingresso 
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(PIN_LED, HIGH);
  } else {
    digitalWrite(PIN_LED, LOW);  
  }

}

//funzione per connettersi al server
//ATTENZIONE: funzione bloccante
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("cestino/uscita", "hello world");
      // ... and resubscribe
      client.subscribe("cestino/ingresso");
      
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void leggiAmbiente(){
  //leggo temperatura
  float hum = dht.readHumidity();
  float temp = dht.readTemperature();
  
  //verifico i dati letti. se incompatibili azzera
   if (isnan(hum) || isnan(temp)){
    hum = 0;
    temp = 0;
  }

  //converto fa float a char per poter trasmetterlo in MQTT
  static char temperatura[7];
  dtostrf (temp, 6, 2, temperatura);
  static char umidita[7];
  dtostrf(hum, 6, 2, umidita);

  //pubblico al server 
  client.publish("cestino/temperatura", temperatura);
  client.publish("cestino/umidita", umidita);
    
  Serial.println("temperatura");
  Serial.println(temperatura);
  Serial.println("umidita");
  Serial.println(umidita);

  
}
