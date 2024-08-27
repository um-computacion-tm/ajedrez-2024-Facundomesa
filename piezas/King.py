from piezas import King

class King:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{self.color} King"

    def get_valid_moves(self, position, board):
        row, col = position
        moves = []
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Movimientos diagonales y verticales hacia arriba
            (0, -1),          (0, 1),  # Movimientos horizontales
            (1, -1), (1, 0), (1, 1)   # Movimientos diagonales y verticales hacia abajo
        ]

        for direction in directions:
            r, c = row + direction[0], col + direction[1]
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board[r][c]
                if piece is None or piece.color != self.color:
                    moves.append((r, c))

        return moves
