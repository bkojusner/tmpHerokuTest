#!/usr/bin/env python

import asyncio
import os
import time
import websockets

async def echo(websocket, path):
    async for message in websocket:
        vidCount = 0
        
        # Establish connection with computer client first
        # Get data about the amount of audio files we have
        if message == "cpuClient":
            await websocket.send("VidCount")
            vidCount = await websocket.recv()
            print("Audio Count {}".format(vidCount))

        # Establish connection with phone second
        # Start recording the audio files
        if message == "phoneClient":
            if vidCount == 0:
                print("Still waiting on Audio Count")
                # Send message here to phone to make it wait for 10 seconds before trying to reconnect
                break
            for i in range(1, 4):
                await websocket.send(message)
                print("starting")
                await websocket.send("StartRec")
                await asyncio.sleep(i)
                print("stopping")
                await websocket.send("StopRec")

start_server = websockets.serve(echo, "", 3000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
