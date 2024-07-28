from .player import Player
from .rules  import RPSRules


class RPSGame:
    """
    Main class for the Rock, Paper and Scissors Game
    """

    def __init__(self, playerA, playerB, rounds, rule_set=RPSRules):
        """
        Instantiate the two players and rules sets

        :param playerA: Name and type of a player
        :type playerA: dict

        :param playerB: Name and type of a player
        :type playerB: dict

        :param rounds: Number of rounds
        :type rounds: int

        :param rule_set: Rules class that define how to determine a winner. 
        :type rule_set: Rules class with compare func defined
        """
        self.playerA = playerA
        self.playerB = playerB
        self.num_rounds = rounds
        self.rule_set = rule_set
        self.current_round = 1

    def determine_winner(self, choiceA, choiceB):
        """
        Determine the winner based on the defined rule set

        :param choiceA: Hand signal chose by player A
        :type choiceA: HandSignals

        :param choiceB: Hand signal chose by player B
        :type choiceB: HandSignals
        """
        match self.rule_set.compare(choiceA, choiceB):
            case -1:
                return self.playerB
            case 1:
                return self.playerA
            case _:
                return None

    def print_round_result(self, winner):
        """
        Print the winner and current tally of scores at the end of current_round

        :param winner: Player who won the current_round
        :type winner: Player
        """
        if winner is None:
            print("It is a tie!")
        else:
            print(f"{winner.name} won this round!")
        print(f"Scores at the end of round {self.current_round}: "
              f"{self.playerA.name} scored {self.playerA.score}; "
              f"{self.playerB.name} scored {self.playerB.score}")

    def print_final_results(self):
        """
        After the final round, tally the score and print the winner
        """
        if self.playerA.score == self.playerB.score:
            print("The game is a tie!")
        elif self.playerA.score > self.playerB.score:
            print(f"{self.playerA.name} won the game by "
                  f"{self.playerA.score - self.playerB.score} points")
        else:
            print(f"{self.playerB.name} won the game by "
                  f"{self.playerB.score - self.playerA.score} points")

    def play_round(self):
        """
        Get the choices from the players and decide who is the winner
        based on the given rule_set
        """
        playerA_choice = self.playerA.choose_signal()
        playerB_choice = self.playerB.choose_signal()
        print(f"{self.playerA.name} chose {playerA_choice.value}")
        print(f"{self.playerB.name} chose {playerB_choice.value}")

        if (winner := self.determine_winner(playerA_choice, playerB_choice)) is not None:
            winner.increment_score()
        self.print_round_result(winner)

    def start_game(self):
        """
        Start the game. Play the game for num_rounds times. 
        At end, whoever scores the maximum points wins.
        """
        while self.current_round <= self.num_rounds:
            self.play_round()
            self.current_round += 1
        self.print_final_results()
