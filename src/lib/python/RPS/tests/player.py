"""
Unittest for Player class
"""

from RPS.player import Player, HumanPlayer, ComputerPlayer
from RPS.rules import HandSignals
import pytest

class TestPlayer:

    def test_create_player(self):
        """
        Test whether create_player creates the object of HumanPlayer or
        ComputerPlayer based on the player type
        """
        # Check for human player type
        player = Player.create_player("human", "Human Player")
        assert isinstance(player, HumanPlayer) == True

        # Check for computer player type
        player = Player.create_player("computer", "Computer Player")
        assert isinstance(player, ComputerPlayer) == True

        # Check whether create_player raises an error in case of invalid player type
        with pytest.raises(ValueError) as err:
            Player.create_player("AI", "AI")
        assert str(err.value) == "Invalid player type. Use 'human' or 'computer'."

    def test_increment_score(self):
        """
        Test the increment_score function
        """
        player = Player.create_player("human", "Nandhini")
        
        # Check whether initial score is zero
        initial_score = player.score
        assert initial_score == 0

        # Check whether increment score, increase the score by 1
        player.increment_score()
        assert initial_score+1 == player.score

    def test_choose_signals(self):
        """
        Test the choose signals functions
        """
        player = Player.create_player("computer", "Computer")
        assert player.choose_signal() in HandSignals




