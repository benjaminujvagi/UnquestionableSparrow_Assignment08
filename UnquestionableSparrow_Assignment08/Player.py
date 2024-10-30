#player.py
# Name: Ben Ujvagi, Jacob Shultze, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: We created a game using three different classes and combined them in the main
# Brief Description of what this module does. In this module, we create the players for the game 

class my_class(object):
    pass

class Player:

    def __init__(self, name, position, touchdowns=0):
        self.name = name
        self.position = position
        self.touchdowns = touchdowns

    def score_touchdown(self):
        self.touchdowns += 1

    def __str__(self):
        return f"Player(name={self.name}, position={self.position}, touchdowns={self.touchdowns})"

    def __repr__(self):
        return f"Player(name={self.name}, position={self.position}, touchdowns={self.touchdowns})"
