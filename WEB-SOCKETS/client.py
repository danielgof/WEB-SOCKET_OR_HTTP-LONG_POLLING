import asyncio
import websockets
import time

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            name = input("Enter your name: ")
            start = time.time() 
            await websocket.send(name)
            response = await websocket.recv()
            finish = time.time()
            print(f"result: {finish - start}") # Print the lenght of a latency 
            print(response)

asyncio.get_event_loop().run_until_complete(hello())
