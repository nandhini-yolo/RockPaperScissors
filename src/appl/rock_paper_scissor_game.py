# !/usr/local/bin/python3
"""
Rock Paper Scissor Game  - Hand Game played between two players. 
Each players simultanously show a hand signal rock, scissors or paper.  

Rules:
- Rock crushes Scissors => Rock wins
- Scissors cuts Paper => Scissors wins
- Paper wraps Rock => Paper wins

Based on the above rules, winner get 1 point. Both player pick the same hand signal,
then it is tie. Whoever scores maximum points at the end of n round is the winner.
"""

from RPS.game import RPSGame
from RPS.prompt_validator import IntegerValidator, UserNameValidator
from prompt_toolkit import prompt


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
    playerA = {"name": "Computer", "type": "computer"}
    playerB = {"name": player_name, "type": "human"}

    # Instantiate the RPSGame object with player details and number of rounds.
    # By default, the game follows the rules mentioned in the doc string.
    # We can also change the rules by passing the different rules class to
    # rule_set variable.
    game = RPSGame(playerA, playerB, int(rounds))

    # Start the game
    game.start_game()
