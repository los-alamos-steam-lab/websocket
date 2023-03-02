
void startWiFi() { // Start a Wi-Fi access point, and try to connect to some given access points. Then wait for either an AP or STA connection
  for (int i=0; i<sizeof accesspoints / sizeof accesspoints[0]; i++) {
    wifiMulti.addAP(accesspoints[i].ssid, accesspoints[i].password);
  }

  Serial.println("Connecting");
  while (wifiMulti.run() != WL_CONNECTED && WiFi.softAPgetStationNum() < 1) {  // Wait for the Wi-Fi to connect
    delay(250);
    Serial.print('.');
  }

  Serial.println("\r\n");
  Serial.print("Connected to ");
  Serial.println(WiFi.SSID());             // Tell us what network we're connected to
  Serial.print("IP address:\t");
  Serial.print(WiFi.localIP());            // Send the IP address of the ESP8266 to the computer
  Serial.println("\r\n");
}


void startSocket() { // Start a Wi-Fi access point, and try to connect to some given access points. Then wait for either an AP or STA connection
  Serial.print("Connecting to WebSockets Server @");
  Serial.println(websockets_connection_string);

  // run callback when messages are received
  client.onMessage(onMessageCallback);

  // run callback when events are occuring
  client.onEvent(onEventsCallback);

  if (SECURE) {
    // Before connecting, set the ssl fingerprint of the server
    client.setFingerprint(echo_org_ssl_fingerprint);
  };

  bool connected = client.connect(websockets_connection_string);
  
  Serial.println("Called Connect to server.");

  if (connected) {
    Serial.println("Connected!");

    String WS_msg = String("{\"type\":\"init\", \"name\":\"Huzzah\", \"client\": \"espclient\"}");
    client.send(WS_msg);

    // Send a ping
    client.ping();
  } else {
    Serial.println("Not Connected!");
  }
};

void onEventsCallback(WebsocketsEvent event, String data) {
  (void) data;
  
  if (event == WebsocketsEvent::ConnectionOpened) {
    Serial.println("Connnection Opened");
  } else if (event == WebsocketsEvent::ConnectionClosed) {
    Serial.println("Connnection Closed");
  } else if (event == WebsocketsEvent::GotPing) {
    Serial.println("Got a Ping!");
  } else if (event == WebsocketsEvent::GotPong) {
    Serial.println("Got a Pong!");
  }
}



