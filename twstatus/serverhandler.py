import socket
import os
import sys
from .serverinfo import ServerInfo
from .player import Player


def create_info_packet():
    data = bytearray()
    data.extend(map(ord, "xe"))
    extra_token = os.urandom(2)
    token = os.urandom(1)
    data += extra_token
    for x in range(6):
        data.append(0xff)
    data.extend(map(ord, "gie3"))
    data += token
    return data, int.from_bytes(token, byteorder=sys.byteorder), int.from_bytes(extra_token, byteorder=sys.byteorder)


class ServerHandler:
    def __init__(self,
                 address: str,
                 port: int=8303,
                 ignore_token: bool=False,
                 timeout: int=5):
        self.address = address
        self.port = port
        self.ignore_token = ignore_token
        self.timeout = timeout

    async def get_info(self, sock: socket.socket=None, close_socket: bool=True):
        if sock is None:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(self.timeout)
        data, token, extra_token = create_info_packet()

        sock.sendto(data, (self.address, self.port))

        try:
            data, (address, port) = sock.recvfrom(4096)
        except socket.timeout:
            return None
        finally:
            if close_socket:
                sock.close()

        if address != self.address:
            return

        svtype = data[10:14].decode()
        stype = ""

        if svtype == "inf3":
            svtype = "vanilla"
        elif svtype == "dtsf":
            svtype = "64legacy"
        elif svtype == "iext":
            svtype = "ext"
        elif svtype == "iex+":
            svtype = "extmore"
            stype = "ext"

        data = data[14:]
        slots: list = data.split("\x00".encode())

        received_token = int(slots.pop(0))

        if not self.ignore_token:
            if token != (received_token & 0xff):
                raise AssertionError("Token is invalid.")

            if stype == "ext" and extra_token != (token & 0xffff00) >> 8:
                raise AssertionError("Ext Token is invalid.")

        info = ServerInfo()

        if svtype != "extmore":
            info.version = slots.pop(0).decode()
            info.name = slots.pop(0).decode()
            info.map = slots.pop(0).decode()

            if svtype == "ext":
                info.mapcrc = int(slots.pop(0))
                info.mapsize = int(slots.pop(0))

            info.game_type = slots.pop(0).decode()
            info.password = int(slots.pop(0)) == 1
            info.player_count = int(slots.pop(0))
            info.max_player_count = int(slots.pop(0))
            info.client_count = int(slots.pop(0))
            info.max_client_count = int(slots.pop(0))

        if svtype == "ext":
            slots.pop(0)  # reserved

        for i in range(info.client_count):
            info.players.append(Player(slots.pop(0).decode(),
                                       slots.pop(0).decode(),
                                       int(slots.pop(0)),
                                       int(slots.pop(0)),
                                       int(slots.pop(0)) == 0)
                                )
            if svtype == "ext":
                slots.pop(0)  # reserved
        return info
