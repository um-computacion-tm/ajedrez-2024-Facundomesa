# Exceptions
class InvalidMove(Exception):
    message = "Invalid piece movement"
    def __str__(self):
        return self.message

class OutOfBoundsError(InvalidMove):
    message = "Row and column values must be between 0 and 7."

class NonNumericInputError(InvalidMove):
    message = "You must enter numeric values between 0 and 7."

class WrongTurnError(InvalidMove):
    message = "It is not the turn of the selected piece."

class InvalidPieceMoveError(InvalidMove):
    message = "Invalid move for the selected piece."

class NonPieceOriginError(InvalidMove):
    message = "There is no piece at the origin position."

class NonCaptureOwnPieceError(InvalidMove):
    message = "You cannot capture your own pieces."

class NonPassOverPieceError(InvalidMove):
    message = "You cannot pass over other pieces."

class NonCaptureForwardError(InvalidMove):
    message = "You cannot capture forward."
      
class GameOverException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)