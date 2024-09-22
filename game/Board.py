from game.Piece import Piece

class Board:
    def __init__(self):
        """
        Inicializa un tablero vacío de 8x8. Cada celda del tablero empieza con None.
        """
        self._board = [[None for _ in range(8)] for _ in range(8)]
    
    def set_piece(self, row, col, color):
        """
        Coloca una pieza de un color específico en una posición (row, col).
        """
        self._board[row][col] = Piece(color)

    def get_piece(self, row, col):
        """
        Retorna la pieza en la posición (row, col) o None si no hay pieza.
        """
        return self._board[row][col]
    
    def move_piece(self, from_row, from_col, to_row, to_col):
        """
        Mueve una pieza desde una posición a otra en el tablero.
        Si no hay pieza en la posición de origen, lanza ValueError.
        """
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            raise ValueError("No hay ninguna pieza en la posición de origen.")
        
        self._board[to_row][to_col] = piece  # Coloca la pieza en la nueva posición
        self._board[from_row][from_col] = None  # Vacía la posición de origen

    def __str__(self):
        """
        Devuelve una representación en cadena del tablero para depuración.
        """
        display = ""
        for row in self._board:
            display += " ".join(["." if piece is None else piece.color[0] for piece in row]) + "\n"
        return display
