from game.board import Board
from game.exceptions import NonPieceOriginError, WrongTurnError, InvalidPieceMoveError, GameOverException

class Chess:
    def __init__(self):
        """
        Inicializa el juego de ajedrez con un tablero y un turno inicial.
        """
        self._board = Board()  # Inicializa el tablero
        self._current_turn = "WHITE"  # Turno inicial es para las piezas blancas

    def get_board(self):
        """
        Devuelve el estado actual del tablero.
        """
        return self._board.get_board_state()
    
    @property
    def turno(self):
        return self._current_turn

    def move(self, start_row, start_col, end_row, end_col):
        """
        Realiza un movimiento de una pieza desde una posición de inicio a una posición de destino.
        """
        # Verifica si el movimiento está fuera de los límites del tablero
        if not self._board.is_within_bounds(start_row, start_col) or not self._board.is_within_bounds(end_row, end_col):
            raise ValueError("Movimiento fuera de los límites del tablero")

        # Obtiene la pieza en la posición inicial
        piece = self._board.get_piece(start_row, start_col)
        if piece is None:
            raise NonPieceOriginError("No hay una pieza en la posición inicial")

        # Verifica si la pieza es del color correcto según el turno
        if piece.color != self._current_turn:
            raise WrongTurnError()

        # Verifica si la posición de destino está ocupada por una pieza del mismo color
        destination_piece = self._board.get_piece(end_row, end_col)
        if destination_piece and destination_piece.get_color() == self._current_turn:
            raise ValueError("No puedes mover una pieza a una posición ocupada por tu propia pieza")

        # Verifica si el movimiento es válido
        if not self._board.is_valid_move(start_row, start_col, end_row, end_col):
            raise InvalidPieceMoveError("Movimiento inválido para la pieza")

        # Realiza el movimiento
        self._board.move_piece(start_row, start_col, end_row, end_col)

        # Cambia el turno después de mover
        self._change_turn()
        
    def _change_turn(self):
        """
        Cambia el turno entre 'WHITE' y 'BLACK'.
        """
        self._current_turn = "BLACK" if self._current_turn == "WHITE" else "WHITE"
