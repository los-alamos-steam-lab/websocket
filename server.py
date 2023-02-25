#!/usr/bin/env python

import asyncio
import json
import secrets
import websockets
import logging
import sys
import ssl
import serversettings

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

LOCAL  = False

# Generate with Lets Encrypt, copied to this location, chown to current user and 400 permissions
if not LOCAL :
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_cert = serversettings.SSL_CERT
    ssl_key = serversettings.SSL_KEY
    ssl_context.load_cert_chain(ssl_cert, keyfile=ssl_key)

async def error(websocket, message):
    await websocket.send("ERROR: " + message)

async def jsonhandler(websocket, event):
    logging.debug("JSON: " + json.dumps(event))
    # echo back
    await websocket.send(json.dumps(event))

async def texthandler(websocket, message):
    logging.debug(message)
    # echo back
    await websocket.send(message)


async def handler(websocket):
    """
    Handle a connection and dispatch it according to who is connecting.

    """
    origin = websocket.request_headers["Origin"]
    url = websocket.path
    logging.debug("DEBUG HEADERS: " + str(websocket.path))
    

    if origin in serversettings.ACCEPTABLE_ORIGINS:
        pass
    elif websocket.path in serversettings.ACCEPTABLE_PATHS:
        pass
    else:
        await websocket.send("Unknown Client")
        return
    
    # Receive and parse the "init" event from the UI.
    message = await websocket.recv()
    logging.debug("MESSAGE RECIEVED")
    i = 0
    try:
        event = json.loads(message)
    except ValueError as e:
        await texthandler(websocket, message)
    else:
        await jsonhandler(websocket, event)
 
    async for message in websocket:
        try:
            event = json.loads(message)
        except ValueError as e:
            await texthandler(websocket, message)
        else:
            await jsonhandler(websocket, event)



async def main():
    if LOCAL:
        async with websockets.serve(handler, port=8001):
            await asyncio.Future()  # run forever
    else:
        async with websockets.serve(handler, port=8001, ssl=ssl_context):
            print("not local")
            await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
