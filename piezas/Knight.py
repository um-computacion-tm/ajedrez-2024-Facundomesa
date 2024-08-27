from piezas import Knight

class piezas:
    def __init__(self, color):
        self.color = color

    def get_valid_moves(self, position, board):
        raise NotImplementedError("This method should be overridden by subclasses")

class Knight(piezas):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return f"{self.color} Knight"

    def get_valid_moves(self, position, board):
        row, col = position
        moves = []
        directions = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]

        for direction in directions:
            r, c = row + direction[0], col + direction[1]
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board[r][c]
                if piece is None or piece.color != self.color:
                    moves.append((r, c))

        return moves
