class Piece:
    """Clase base abstracta para las piezas de ajedrez."""
    def __init__(self, color):
        self.color = color

    def get_valid_moves(self, position, board):
        """Método que debe ser implementado por las subclases."""
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

class Knight(Piece):
    """Clase que representa al caballo en ajedrez."""
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        """Devuelve una representación en cadena de la pieza."""
        return f"{self.color} Knight"

    def get_valid_moves(self, position, board):
        """Calcula los movimientos válidos del caballo."""
        row, col = position
        moves = []

        # Definir las 8 posibles direcciones de movimiento del caballo
        directions = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]

        # Iterar sobre las posibles direcciones y agregar movimientos válidos
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self._is_within_bounds(new_row, new_col):
                piece = board[new_row][new_col]
                # Si la casilla está vacía o tiene una pieza del color contrario
                if piece is None or piece.color != self.color:
                    moves.append((new_row, new_col))

        return moves

    def _is_within_bounds(self, row, col):
        """Verifica si la posición está dentro de los límites del tablero (8x8)."""
        return 0 <= row < 8 and 0 <= col < 8
