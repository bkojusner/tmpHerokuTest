#!/usr/bin/env python

import asyncio
import os

import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

start_server = websockets.serve(echo, "", int(3000))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
