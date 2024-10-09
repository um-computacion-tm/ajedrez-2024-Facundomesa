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

        for direction in directions:
            r, c = row + direction[0], col + direction[1]
            # Verificar si las coordenadas están dentro de los límites del tablero
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board[r][c]
                # Si la casilla está vacía o contiene una pieza de color contrario, es un movimiento válido
                if piece is None or piece.color != self.color:
                    moves.append((r, c))

        return moves