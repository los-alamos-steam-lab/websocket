# websocket

This is a basic websocket server (python) and client (Feather Huzzah ESP8266)
based on and modified from Khoi Hoang's library https://github.com/khoih-prog/Websockets2_Generic

Licensed under MIT license

*Server* 

* Requires Python 10 with up to date websockets library 
** pip has the latest version, but not apt-get, 
** I could not get this to work without python 3.10 being my default python3 because websockets would remain out of date
* Run the server simply by running the app in any directory in your publicly accesible webserver
* You may need to unblock the port you use

*Client*

* Copy settings.h.in to settings.h and update the applicable networks, passwords, url, port, and
  ssh fingerprints
  
*Altogether Now*

* The board will connect to the server, send a JSON Message and a text message
* The server will echo the messages back.
