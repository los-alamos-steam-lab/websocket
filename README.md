# websocket

This is a basic websocket server (python) and client (Feather Huzzah ESP8266)
based on and modified from Khoi Hoang's library https://github.com/khoih-prog/Websockets2_Generic

Licensed under MIT license

### Server

* Requires Python 10 with up to date websockets library 
  * As of Feb '23 pip has the latest version, but not apt-get 
  * I could not get this to work without python 3.10 being my default python3 because websockets would remain out of date
* Run the server simply by running the app in any directory in your publicly accesible webserver
* You may need to unblock the port you use

### ESP8266 Client

* Tested on a Feather Huzzah
* Copy settings.js.in to settings.js and update the applicable networks, passwords, url, port, and ssh fingerprints
* The board will connect to the server, send a JSON Message and a text message
* The server will echo the messages back.
  
### Web Client

* Copy settings.h.in to settings.h and update the server string
* The web client will connect to the server.  Clicking "Send Message" will send a message to the server.
* The server will echo the message back.
  
### Altogether Now

#### Coming Next

* Clicking "Who's Connected" in the web client will show all connections to the server 
* The web client can then send messages to each connection
* Those connections will echo back the message
* The web client can also broadcast a message to all connected clients