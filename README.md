# websocket

This is a basic websocket server (python) and client (Feather Huzzah ESP8266)
based on and modified from Khoi Hoang's library https://github.com/khoih-prog/Websockets2_Generic

Requires Python 10 with up to date websockets library (i.e not the one installed on Ubuntu)

Licensed under MIT license

* Run the websocket from a public facing server (make sure you have the correct ports visible)
* Copy settings.h.in to settings.h and update the applicable networks, passwords, url, port, and
  ssh fingerprints
* The board will connect to the server, send a JSON Message and a text message
* The server will echo the messages back.
