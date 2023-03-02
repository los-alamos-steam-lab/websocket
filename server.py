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

sockets = {}
connected = {}
available = {}

# Generate with Lets Encrypt, copied to this location, chown to current user and 400 permissions
if not LOCAL :
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_cert = serversettings.SSL_CERT
    ssl_key = serversettings.SSL_KEY
    ssl_context.load_cert_chain(ssl_cert, keyfile=ssl_key)



async def error(websocket, message):
    await websocket.send("ERROR: " + message)

async def webclienthandler(websocket, event):
    # add the new scoket to connected, we'll want to manage available, too
    newsocket = {}
    id = str(websocket.id)
    sockets[id] = websocket
    newsocket['name'] = event['name']
    newsocket['client'] = event['client']
    connected[id] = newsocket
    logging.debug("NEW CLIENT: " + json.dumps(newsocket))

    async for message in websocket:
        # Parse a "play" event from the UI.
        event = json.loads(message)
        try:
            type = event['type']
        except:
            await error(websocket, "No type declared")
        
        if type == "command":
            await processWebCommand(websocket, event)
        else:
            logging.debug("JSON: " + json.dumps(event))
            # echo message back
            await websocket.send(json.dumps(event))


async def processWebCommand(websocket, event):
    try:
        command = event["command"]
    except:
        await error(websocket, "No command declared")
    
    if command == "getconnected":
        await websocket.send(json.dumps(connected))
    else:
        await error(websocket, "Unknown command")

    return

async def espclienthandler(websocket, event):
    logging.debug("JSON: " + json.dumps(event))
    logging.debug("ID: " + str(websocket.id))
    newsocket = {}
    id = str(websocket.id)
    sockets[id] = websocket
    newsocket['name'] = event['name']
    newsocket['client'] = event['client']
    connected[id] = newsocket

    async for message in websocket:
        # Parse a "play" event from the UI.
        event = json.loads(message)
        logging.debug("JSON: " + json.dumps(event))
        await websocket.send(json.dumps(event))
    async for message in websocket:
        # Parse a "play" event from the UI.
        event = json.loads(message)
        logging.debug("JSON: " + json.dumps(event))
        await websocket.send(json.dumps(event))


async def handler(websocket):
    """
    Handle a connection and dispatch it according to who is connecting.

    """

    # Determine if the client is originating from an acceptable domain
    # or has the correct "secret" path to the server.

    # Determine if the client is originating from an acceptable domain
    # or has the correct "secret" path to the server.
    origin = websocket.request_headers["Origin"]


    if origin in serversettings.ACCEPTABLE_ORIGINS:
        pass
    elif websocket.path in serversettings.ACCEPTABLE_PATHS:
        pass
    else:
        await websocket.send("Unknown Client")
        return
    
    # Receive and parse the "init" event from the UI.
    # Receive and parse the "init" event from the UI.
    message = await websocket.recv()
    logging.debug("INIT MESSAGE: " + message)
    event = json.loads(message)
    assert event["type"] == "init"

    if event["client"] == "webclient":
        # Second player joins an existing game.
        await webclienthandler(websocket, event)
    elif event["client"] == "espclient":
        # Spectator watches an existing game.
        await espclienthandler(websocket, event)
    event = json.loads(message)
    assert event["type"] == "init"

    if event["client"] == "webclient":
        # Second player joins an existing game.
        await webclienthandler(websocket, event)
    elif event["client"] == "espclient":
        # Spectator watches an existing game.
        await espclienthandler(websocket, event)
    else:
        # First player starts a new game.
        await websocket.send("Unknown Client")
        return
    
    # wait around to clean up connected
    try:
        await websocket.wait_closed()
    finally:
        logging.debug("Removing " + str(connected[websocket.id]))
        connected.pop(websocket.id)
        sockets.pop(websocket.id)



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
