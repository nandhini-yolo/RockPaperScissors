#!/usr/local/bin/python3
"""
It is a hand game played between two players. Each player simultaneously shows a
hand signal: one of rock, scissors, or paper.  

Typical ruleset: Rock crushes Scissors, Scissors cuts Paper, Paper wraps Rock

- Based on these rules, winner gets 1 point every round. 
- In case of tie, no one gets a point.
- Whoever scores the maximum points at the end of N rounds is the winner.
"""

from RPS.game             import RPSGame
from RPS.player           import Player
from RPS.prompt_validator import IntegerValidator, UserNameValidator
from prompt_toolkit       import prompt


if __name__ == "__main__":

    # Prompt the player to enter their name and validate whether its length >= 5 chars
    player_name = prompt("Enter your username: ", validator=UserNameValidator())

    # Prompt the player to enter the number of rounds and validate whether
    # it is a valid integer.
    rounds = prompt("Enter the number of rounds you would like to play: ",
                    validator=IntegerValidator())

    # Create the player dict for two players.
    # For the given question, playerA is a Computer and playerB is a Human.
    # If we want to later change the game to play betweem two human player,
    # we just to need to update these dictionaries.
    playerA = Player.create_player("computer", "Computer") 
    playerB = Player.create_player("human", player_name)

    # Instantiate the RPSGame object with player details and number of rounds.
    # By default, the game follows the rules mentioned in the doc string.
    # We can also change the rules by passing the different rules class to
    # rule_set variable.
    game = RPSGame(playerA, playerB, int(rounds))

    # Start the game
    game.start_game()
