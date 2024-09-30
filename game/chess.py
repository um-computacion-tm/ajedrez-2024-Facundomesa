from game.Board import Board
from game.chess import Chess

class Chess:
    def __init__(self):
        """
        Inicializa un juego de ajedrez con un tablero vacío y con el turno inicial en 'WHITE'.
        """
        self._board = Board()
        self._turn = "WHITE"  # El turno inicial es de las piezas blancas

    def move(self, from_row, from_col, to_row, to_col):
        """
        Mueve una pieza desde (from_row, from_col) a (to_row, to_col).
        Valida las coordenadas, verifica que la pieza es del turno actual y actualiza el turno.
        """
        if not self._is_valid_move(from_row, from_col, to_row, to_col):
            raise ValueError("Movimiento no válido: fuera de los límites del tablero.")

        if from_row == to_row and from_col == to_col:
            raise ValueError("Movimiento no válido: la posición de origen y destino son las mismas.")

        piece = self._board.get_piece(from_row, from_col)
        if piece is None:
            raise ValueError("No hay ninguna pieza en la posición de origen.")

        if piece.color != self._turn:
            raise ValueError(f"Es el turno de {self._turn}. No puedes mover una pieza {piece.color}.")

        destination_piece = self._board.get_piece(to_row, to_col)
        if destination_piece is not None:
            if destination_piece.color == self._turn:
                raise ValueError("No puedes capturar tu propia pieza.")

        # Mueve la pieza y cambia el turno
        self._board.move_piece(from_row, from_col, to_row, to_col)
        self._change_turn()

    @property
    def turn(self):
        """
        Retorna el turno actual ('WHITE' o 'BLACK').
        """
        return self._turn

    def _change_turn(self):
        """
        Cambia el turno de juego entre 'WHITE' y 'BLACK'.
        """
        self._turn = "BLACK" if self._turn == "WHITE" else "WHITE"

    def _is_valid_move(self, from_row, from_col, to_row, to_col):
        """
        Verifica si un movimiento es válido, asegurando que las coordenadas están dentro de los límites del tablero.
        """
        return 0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8

