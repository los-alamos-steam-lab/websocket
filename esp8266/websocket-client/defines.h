/****************************************************************************************************************************
  defines.h for Secured-ESP8266-Client.ino
  For ESP8266.
  
  Based on and modified from Khoi Hoang's library https://github.com/khoih-prog/Websockets2_Generic
  This example provides a working websocket client for an ESP8266
    
  Built by Lisabeth Lueninghoener 
  Licensed under MIT license
 *****************************************************************************************************************************/

#ifndef defines_h
#define defines_h

#if (ESP8266)
  #define BOARD_TYPE      "ESP8266"
#else
  #error This code is intended to run only on the ESP8266 boards ! Please check your Tools->Board setting.
#endif

#ifndef BOARD_NAME
  #define BOARD_NAME    BOARD_TYPE
#endif

#define DEBUG_WEBSOCKETS_PORT     Serial
// Debug Level from 0 to 4
#define _WEBSOCKETS_LOGLEVEL_     3

#endif      //defines_h