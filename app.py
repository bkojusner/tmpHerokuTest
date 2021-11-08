#!/usr/bin/env python

import asyncio
import os
import time
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)
        await websocket.send("StartRec")
        await asyncio.sleep(3)
        await websocket.send("StopRec")

start_server = websockets.serve(echo, "", int(os.environ["PORT"]))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
