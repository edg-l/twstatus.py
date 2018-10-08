from twstatus import ServerHandler
import asyncio

server = ServerHandler("95.172.92.151", 8339)


async def main():
    info = await server.get_info()
    print(vars(info))

asyncio.run(main())
