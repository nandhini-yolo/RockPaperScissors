from prompt_toolkit    import prompt
from .prompt_validator import HandSignalValidator
from .rules            import HandSignals
import random


class Player:
    def __init__(self, name, player_type):
        """
        Initialize a player object

        :param name: Name of the player
        :type name: str
        """
        self.name = name
        self._score = 0
        self.player_type = player_type

    @property
    def score(self):
        """
        Return the current score of the player
        """
        return self._score

    def increment_score(self):
        """
        Increment the score of the player by 1 point
        """
        self._score += 1

    def choose_signal(self):
        raise NotImplementedError("This is implemented by the subclasses")

    @staticmethod
    def create_player(player_type, name):
        """
        Create a player object based the player type
        """
        if player_type == "human":
            return HumanPlayer(name)
        elif player_type == "computer":
            return ComputerPlayer(name)
        else:
            raise ValueError("Invalid player type. Use 'human' or 'computer'.")


class ComputerPlayer(Player):
    _player_type = 'computer'

    def __init__(self, name):
        super().__init__(name, self._player_type)

    def choose_signal(self):
        """
        Random pick a hand signal from HandSignals enum
        """
        return HandSignals(random.choice(HandSignals.get_values()))


class HumanPlayer(Player):
    _player_type = 'human'

    def __init__(self, name):
        super().__init__(name, self._player_type)

    def choose_signal(self):
        """
        Get the hand signal from the player
        """
        hand_signal = prompt(f"{self.name} enter your hand signal: ",
                             validator=HandSignalValidator())
        return HandSignals(hand_signal.lower())
    