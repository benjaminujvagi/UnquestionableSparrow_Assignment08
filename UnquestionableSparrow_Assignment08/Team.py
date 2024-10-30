class my_class(object):
    pass

"""
    A class to represent a sports team.
    
    Param: 
    name : str, The name of the team.
    players : list, A list of players in the team.
"""

class Team:

    def __init__(self, name, players=None):
        self.name = name
        self.players = players if players is not None else []

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        return f"Team(name={self.name}, players={[player.name for player in self.players]})"

    def __repr__(self):
        return self.__str__()



