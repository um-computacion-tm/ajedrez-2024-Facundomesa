from game.Board import Board


class Chess:
    def __init__(self):
        self._board = Board()
        self._turn = "WHITE"
    
class InvalidMove(Exception):
    """Excepción base para movimientos inválidos."""
    pass

class InvalidMoveNoPiece(InvalidMove):
    """Excepción lanzada cuando se intenta mover desde una posición sin pieza."""
    def __init__(self, position):
        super().__init__(f"No hay ninguna pieza en la posición {position}.")
        
    
class InvalidMoveRookMove(InvalidMove):
    """Excepción lanzada cuando una torre intenta realizar un movimiento inválido."""
    def __init__(self, start, end):
        super().__init__(f"Movimiento inválido para la torre desde {start} hasta {end}.")


    def move(self, from_row, from_col, to_row, to_col):
        """
        Mueve una pieza desde las coordenadas (from_row, from_col) a (to_row, to_col).
        Valida las coordenadas y actualiza el turno.
        """
        if not self._is_valid_move(from_row, from_col, to_row, to_col):
            raise ValueError("Movimiento no válido")

        piece = self._board.get_piece(from_row, from_col)
        if piece is None:
            raise ValueError("No hay ninguna pieza en la posición de origen")

        if piece.color != self._turn:
            raise ValueError(f"Es el turno de {self._turn}. No puedes mover una pieza {piece.color}.")

        self._board.move_piece(from_row, from_col, to_row, to_col)
        self._change_turn()

    @property
    def turn(self):
        return self._turn

    def _change_turn(self):
        """
        Cambia el turno de juego entre 'WHITE' y 'BLACK'.
        """
        self._turn = "BLACK" if self._turn == "WHITE" else "WHITE"

    def _is_valid_move(self, from_row, from_col, to_row, to_col):
        """
        Valida si un movimiento es posible dentro de los límites del tablero.
        """
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            return False
        return True
