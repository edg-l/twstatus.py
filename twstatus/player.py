class Player:
    def __init__(self,
                 name: str,
                 clan: str,
                 country: int,
                 score: int,
                 is_spectator: bool):
        self.name = name
        self.clan = clan
        self.country = country
        self.score = score
        self.is_spectator = is_spectator

    def __str__(self):
        return f"{self.name} [{self.clan}]"
