class Queen:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{self.color} Queen"

    def get_valid_moves(self, position, board):
        row, col = position
        moves = []
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Movimientos verticales y horizontales
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Movimientos diagonales
        ]

        for direction in directions:
            r, c = row, col
            while True:
                r += direction[0]
                c += direction[1]
                if 0 <= r < 8 and 0 <= c < 8:
                    piece = board[r][c]
                    if piece is None:
                        moves.append((r, c))
                    elif piece.color != self.color:
                        moves.append((r, c))
                        break
                    else:
                        break
                else:
                    break

        return moves
