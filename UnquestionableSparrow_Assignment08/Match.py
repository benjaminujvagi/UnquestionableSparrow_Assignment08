#match.py
# Name: Ben Ujvagi, Jacob Shultze, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: We created a game using three different classes and combined them in the main
# Brief Description of what this module does. In this module we create a match setting for the two teams to face off

class Match:
    """
    Represents a match between two teams and tracking their scores.
    Provides methods to track scores and show final match status.
    """
    def __init__(self, team1, team2, score1=0, score2=0):
        self._team1 = team1
        self._team2 = team2
        self._score1 = score1
        self._score2 = score2

    @property
    def team1(self):
        return self._team1

    @team1.setter
    def team1(self, value):
        self._team1 = value

    @property
    def team2(self):
        return self._team2

    @team2.setter
    def team2(self, value):
        self._team2 = value

    @property
    def score1(self):
        return self._score1

    @score1.setter
    def score1(self, value):
        if value >= 0:
            self._score1 = value
        else:
            raise ValueError("Score cannot be negative")

    @property
    def score2(self):
        return self._score2

    @score2.setter
    def score2(self, value):
        if value >= 0:
            self._score2 = value
        else:
            raise ValueError("Score cannot be negative")

    def goal_team1(self):
        self._score1 += 1

    def goal_team2(self):
        self._score2 += 1

    def __str__(self):
        return f"{self._team1} vs {self._team2}: {self._score1}-{self._score2}"

    def __repr__(self):
        return f"Match({self._team1}, {self._team2}, {self._score1}, {self._score2})"