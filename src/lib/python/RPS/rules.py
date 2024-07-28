from enum import Enum

class HandSignals(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

    @classmethod
    def get_values(cls):
        return [member.value for member in cls]

    @classmethod
    def keys(cls):
        return [member.name for member in cls]

class Rules:

    @staticmethod
    def compare(choiceA, choiceB):
        raise NotImplementedError("This is implemented in the subclasses")

class RPSRules(Rules):
    """
    Defines the rules of Rock Paper Scissor Game
    """

    @staticmethod
    def compare(choiceA, choiceB):
        """
        Compare the given hand signals and return 
         1  - if playerA won
        -1  - if playerB won
         0  - if it is tie
        """
        if choiceA == choiceB:
            return 0

        match (choiceA, choiceB):
            case ((HandSignals.ROCK, HandSignals.SCISSORS)|
                  (HandSignals.SCISSORS, HandSignals.PAPER)|
                  (HandSignals.PAPER, HandSignals.ROCK)):
                return 1
            case _:
                return -1

