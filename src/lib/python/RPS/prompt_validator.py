from prompt_toolkit.validation import  ValidationError, Validator
from .rules                    import HandSignals


class HandSignalValidator(Validator):
    """
    Validate the Hand Signal entered by the player
    """
    def validate(self, player_input):
        if player_input.text.upper() not in HandSignals.keys():
            raise ValidationError(
                message=f"Please enter {' | '.join(HandSignals.get_values())}",
                cursor_position=len(player_input.text)
            )


class IntegerValidator(Validator):
    """
    Check whether the player entered a valid integer for num of rounds
    """
    def validate(self, player_input):
        if not player_input.text.isdigit():
            raise ValidationError(
                message='Please enter a valid integer',
                cursor_position=len(player_input.text)
            )


class UserNameValidator(Validator):
    """
    Validate the username entered by the player
    """
    def validate(self, player_input):
        if len(player_input.text) < 5:
            raise ValidationError(
                message='Username must have atleast 5 chars',
                cursor_position=len(player_input.text)
            )
