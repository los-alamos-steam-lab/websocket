/****************************************************************************************************************************
  Secured-ESP8266-Client.ino
  For ESP8266.
  
  Based on and modified from Khoi Hoang's library https://github.com/khoih-prog/Websockets2_Generic
  This example provides a working websocket client for an ESP8266
  
  Built by Lisabeth Lueninghoener 
  Licensed under MIT license
 *****************************************************************************************************************************/
/*
 Secured Esp8266 Websockets Client
  This sketch:
        1. Connects to a WiFi network (using a multi-server)
        2. Connects to a Websockets server (using WSS)
        3. Sends the websockets server a message
        4. Sends the websocket server a "ping"
        5. Prints all incoming messages while the connection is open

  Hardware:
        For this sketch you only need an ESP8266 board.
  Originally Created  : 15/02/2019
  Original Author     : By Gil Maimon
  Original Repository : https://github.com/gilmaimon/ArduinoWebsockets
*****************************************************************************************************************************/

#include <WebSockets2_Generic.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include "settings.h"
#include "defines.h"

using namespace websockets2_generic;

// Used by network.ino
ESP8266WiFiMulti wifiMulti;
WebsocketsClient client;
// SECURE = false is untested because I couldn't find an unsecure websocket server to try it on
const bool SECURE = true;


void onMessageCallback(WebsocketsMessage message) 
{
  Serial.print("Got Message: ");
  Serial.println(message.data());
}

void setup() 
{
  Serial.begin(115200);
  while (!Serial && millis() < 5000);

  Serial.print("\nStart Secured-ESP8266-Client on "); Serial.println(ARDUINO_BOARD);
  Serial.println(WEBSOCKETS2_GENERIC_VERSION);
  
  startWiFi(); 
  startSocket();
  
}

void loop() 
{
  client.poll();
}