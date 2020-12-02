/*
 * PROVA 0.3 : collegarsi al wifi e al server; dht; sleep mode; attivazione sensore
 * deep sleep: si risveglia tramite timer. Quando si sveglia ricomincia dal setup.
 * inviare_dati variabile per inviare dati solamente se si è connessi al wifi e al server. Altrimenti torna in sleep e riprova al risveglio successivo, per non sprecare batteria
 * do corrente al sensore dht solo quando devo leggere i valori
 * Leggo la temperatura ogni 30 secondi, faccio la media di 10 valori in circa 5 minuti e poi mando al server
 */

//librerie necessarie wifi e MQTT 
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

//oggetti wifi e server
WiFiClient espClient;
PubSubClient client(espClient);

//credenziali router e server
const char* mqtt_server = "192.168.1.160"; //mqtt server
const char* ssid = "VillaBetoriRizzardo";
const char* password = "everest8848";

//deep sleep
#define uS_TO_S_FACTOR 1000000ULL  /* Conversion factor for micro seconds to seconds */
#define TIME_TO_SLEEP  30        /* Time ESP32 will go to sleep (in seconds) */

// variabile salvata nella RTC memory: non si resetta quando va in sleep
RTC_DATA_ATTR int value = 0;

//sensore temperatura
#include "DHT.h"
#define DHTTYPE DHT22
#define DHTPIN 4
#define DHTVCC 16
DHT dht(DHTPIN, DHTTYPE);
RTC_DATA_ATTR float temperatura_value = 0;

//variabili per il messaggio di prova da inviare al server
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
//int value = 0;
// per il led di prova
#define PIN_LED 32

//variabile per inviare dati solamente se si è connessi al wifi e al server
bool inviare_dati = false;


void setup() {
  Serial.begin(115200);

  //messaggio per vedere inizio del programma
  Serial.println("INIZIO PROGRAMMA");
  Serial.println("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||");  
  
  //inizializzo wifi e server
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  //configuro il metodo di risveglio: risveglio con timer dopo x secondi dall'avvio del deep sleep
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  Serial.println("Setup ESP32 to sleep for every " + String(TIME_TO_SLEEP) +
  " Seconds");
  
  //inizializzo sensore temperatura
  dht.begin();
  pinMode(DHTVCC, OUTPUT);
  digitalWrite(DHTVCC, LOW);
  
}

void loop() {
  
  //verifico continuamente la connessione col server, se non è connesso riconnetto tramite funzione. FUNZIONE BLOCCANTE: se non si connette continua a provare
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  //se sono connesso al wifi e al server, leggo e trasmetto i dati. Altrimenti proseguo e vado in sleep
  if (inviare_dati == true){
    //per provare connessione al server invio messaggio
    ++value;
    snprintf (msg, MSG_BUFFER_SIZE, "hello world #%ld", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("cestino/uscita", msg);

  leggiAmbiente();
  }
  
  //vado in deep sleep 
  Serial.println("Going to sleep now");
  Serial.println("FINE PROGRAMMA");
  Serial.println("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||");    
  Serial.println("");
  Serial.println("");
  Serial.flush(); 
  esp_deep_sleep_start();
}

//funzione per connettersi al wifi
// ATTENZIONE: FUNZIONE NON BLOCCANTE 
void setup_wifi() {

  delay(50);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  //aspetto mezzo secondo
  delay(500);
  
  //se non si connette flag per mandare dati al server = FALSE 
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Not connected");
  }

  if (WiFi.status() == WL_CONNECTED){
    randomSeed(micros()); 
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
    inviare_dati = true;
  }

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
  
  if (!client.connected()) {
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
      inviare_dati = true;
      
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      // Wait 5 seconds before retrying
      inviare_dati = false;
    }
  }
}

//funzione per leggere e trasmettere temperatura ed umidità ambientale
void leggiAmbiente(){
  //attivo pin di alimentazione del sensore
  digitalWrite(DHTVCC, HIGH);
  delay(300);
  
  //leggo temperatura
  float hum = dht.readHumidity();
  float temp = dht.readTemperature();

  //disattivo pin di alimentazione del sensore
  digitalWrite(DHTVCC, HIGH);
  
  //verifico i dati letti. se incompatibili azzera
   if (isnan(hum) || isnan(temp)){
    hum = 0;
    temp = 0;
  }

  //se value (che si aggiorna ogni 30sec al riavvio) non è divisibile per 10 => non ho ancora 10 valori di temperatura per la media e quindi li sommo
  if ( value % 10 != 0){
    temperatura_value = temperatura_value + temp;
    Serial.println("sto sommando la temperatura");
    Serial.print("value= ");
    Serial.println(value);
    Serial.print("umidita = ");
    Serial.println(hum);
  }
  // se invece value è divisibile è il momeno di fare la media ed inviare i dati al server
  else {
    temperatura_value = temperatura_value / 10.0;

    //converto da float a char per poter trasmetterlo in MQTT
    temp = temperatura_value;
    static char temperatura[7];
    dtostrf (temp, 6, 2, temperatura);
    static char umidita[7];
    dtostrf(hum, 6, 2, umidita);

    //trasmetto al server dati di temperatura e umidità 
    client.publish("cestino/temperatura", temperatura);
    client.publish("cestino/umidita", umidita);
    
    Serial.print("temperatura = ");
    Serial.println(temperatura);
    Serial.print("umidita = ");
    Serial.println(umidita);

    //azzero temperatura
    temperatura_value = 0;
   }

  

  
}
