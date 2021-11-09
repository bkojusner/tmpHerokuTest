#!/usr/bin/env python

import asyncio
import os
import time
import websockets
from ratelimit import limits

@limits(calls=1, period=900)
async def echo(websocket, path):
    async for message in websocket:
        # If message == from computer
        # Else do this
        for i in range(1, 4):
            await websocket.send(message)
            print("starting")
            await websocket.send("StartRec")
            await asyncio.sleep(i)
            print("stopping")
            await websocket.send("StopRec")

start_server = websockets.serve(echo, "", 3000)#int(os.environ["PORT"]))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
