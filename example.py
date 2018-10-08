from twstatus import ServerHandler
import asyncio

server = ServerHandler("95.172.92.151", 8339)


async def main():
    info = await server.get_info()
    print(len(info.players))
    print(info.player_count)
    print(info)

asyncio.run(main())
