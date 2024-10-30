#team.py
# Name: Ben Ujvagi, Jacob Shultze, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: We created a game using three different classes and combined them in the main
# Brief Description of what this module does. In this module we put the players on to two different teams.  
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



