from typing import List
from .player import Player


class ServerInfo:
    def __init__(self,
                 version: str=None,
                 name: str=None,
                 _map: str=None,
                 game_type: str=None,
                 password: bool=None,
                 player_count: int=None,
                 max_player_count: int=None,
                 client_count: int=None,
                 max_client_count: int=None,
                 mapcrc: int=None,
                 mapsize: int=None,
                 players: List[Player]=None):
        self.name = name
        self.map = _map
        self.version = version
        self.game_type = game_type
        self.password = password
        self.player_count = player_count
        self.max_player_count = max_player_count
        self.client_count = client_count
        self.max_client_count = max_client_count
        self.mapcrc = mapcrc
        self.mapsize = mapsize
        self.players = players

        if self.players is None:
            self.players: List[Player] = []

    def __str__(self):
        return f"{self.name} [{self.player_count}/{self.max_player_count}]"
