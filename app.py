#!/usr/bin/env python

import asyncio
import os
import time
import websockets

async def echo(websocket, path):
    async for message in websocket:
        f = open("data.txt", 'r')
        
        # Establish connection with phone second
        print(message)
        # Start recording the audio files
        for i in f:
            print("Start Recording for {} seconds".format(str(i)))
            await websocket.send("StartRec")
            await asyncio.sleep(int(i))
            await websocket.send("StopRec")
            print("Stopped recording")
            print("Pausing everything for 5 seconds to sync up")
            await asyncio.sleep(5)
        
        print("Should be done")

# For testing purposes you can change that last int to just 3000
start_server = websockets.serve(echo, "", int(os.environ["PORT"]))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
