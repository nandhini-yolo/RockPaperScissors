"""
Unittest for HandSignals Enum and RPSRules class
"""
from RPS.rules import HandSignals, RPSRules
import pytest

class TestHandSignals:

    def test_get_values(self):
        """
        Test get_values() function
        """
        values = HandSignals.get_values()
        assert values == ['rock', 'paper', 'scissors'], "HandSignals.get_values() returning incorrect signals"

    def test_keys(self):
        """
        Test keys() function
        """
        keys = HandSignals.keys()
        assert keys == ['ROCK', 'PAPER', 'SCISSORS'], "HandSignals.keys() returning incorrect keys"


class TestRPSRules:

    @pytest.mark.parametrize("choiceA, choiceB, expected", [(HandSignals.PAPER, HandSignals.PAPER, 0),
                                                            (HandSignals.PAPER, HandSignals.ROCK, 1), 
                                                            (HandSignals.ROCK, HandSignals.SCISSORS, 1), 
                                                            (HandSignals.SCISSORS, HandSignals.PAPER, 1), 
                                                            (HandSignals.SCISSORS, HandSignals.ROCK, -1)])
    def test_compare(self, choiceA, choiceB, expected):
        """
        Test the compare function of rules
        """
        assert RPSRules.compare(choiceA, choiceB) == expected