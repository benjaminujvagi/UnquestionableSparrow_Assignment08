#main.py
# Name: Ben Ujvagi, Jacob Shultze, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: We created a game using three different classes and combined them in the main
# Brief Description of what this module does. In this module, we call all three classes and run the results to see who won the game. 
from Player import Player
from Team import Team
from Match import Match

def main():
    # Create players
    player1 = Player(name="Alice", position="Forward")
    player2 = Player(name="Bob", position="Midfielder")
    player3 = Player(name="Charlie", position="Defender")
    player4 = Player(name="Diana", position="Goalkeeper")

    # Create teams
    team1 = Team(name="Team A", players=[player1, player2])
    team2 = Team(name="Team B", players=[player3, player4])

    # Create a match
    match = Match(team1=team1, team2=team2)

    # Simulate some actions
    player1.score_touchdown()
    match.goal_team1()
    player1.score_touchdown()
    match.goal_team1()
    player2.score_touchdown()
    match.goal_team1()
    player1.score_touchdown()
    match.goal_team1()
    player3.score_touchdown()
    match.goal_team2()
    player3.score_touchdown()
    match.goal_team2()


    # Print details
    print(player1)
    print(player2)
    print(player3)
    print(player4)
    print(team1)
    print(team2)
    print(match)

if __name__ == "__main__":
    main()
