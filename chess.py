from board import Board

class Chess:
    def __init__(self):
        """
        Inicializa el juego de ajedrez con un tablero y un turno inicial.
        """
        self._board = Board()
        self.turn = "WHITE"  # El turno inicial es para las piezas blancas

    def move(self, start_row, start_col, end_row, end_col):
        """
        Realiza un movimiento de una pieza desde una posición de inicio a una posición de destino.
        """
        # Verifica si el movimiento está fuera de los límites del tablero
        if not self._board.is_within_bounds(start_row, start_col) or not self._board.is_within_bounds(end_row, end_col):
            raise ValueError("Movimiento fuera de los límites del tablero")

        # Verifica si se está intentando mover a la misma posición
        if start_row == end_row and start_col == end_col:
            raise ValueError("No puedes mover una pieza a la misma posición")

        # Obtiene la pieza en la posición inicial
        piece = self._board.get_piece(start_row, start_col)
        if piece is None:
            raise ValueError("No hay una pieza en la posición inicial")

        # Verifica si la pieza es del color correcto según el turno
        if piece != self.turn:
            raise ValueError(f"No es el turno de {piece}")

        # Verifica si la posición de destino está ocupada por una pieza del mismo color
        destination_piece = self._board.get_piece(end_row, end_col)
        if destination_piece == self.turn:
            raise ValueError("No puedes mover una pieza a una posición ocupada por tu propia pieza")

        # Realiza el movimiento
        self._board.set_piece(end_row, end_col, piece)
        self._board.set_piece(start_row, start_col, None)

        # Cambia el turno después del movimiento válido
        self._change_turn()

    def _change_turn(self):
        """
        Cambia el turno entre 'WHITE' y 'BLACK'.
        """
        self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"
