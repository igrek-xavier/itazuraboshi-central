import websockets
import asyncio
import pygame

IPADDRESS = "0.0.0.0" # ""127.0.0.1"
PORT = 9999

EVENTTYPE = pygame.event.custom_type()


# handler processes the message and sends "Success" back to the client
async def handler(websocket, path):
    async for message in websocket:
        # print(websocket.remote_address[0])
        await processMsg(message, websocket.remote_address[0])
        await websocket.send("Success")

async def processMsg(message, ip_address):
    pygame.fastevent.post(pygame.event.Event(EVENTTYPE, {'message':message, 'ip_address':ip_address}))

async def main(future):
    async with websockets.serve(handler, IPADDRESS, PORT):
        await future  # run forever

if __name__ == "__main__":
    asyncio.run(main())
