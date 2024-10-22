from game.piece import Piece

class Bishop(Piece):
    def __str__(self):
        return "♗" if self.color == "WHITE" else "♝"

    def possible_moves(self, position, board):
        row, col = position
        moves = []
        directions = [
            (-1, -1),  # Diagonal arriba a la izquierda
            (-1, 1),   # Diagonal arriba a la derecha
            (1, -1),   # Diagonal abajo a la izquierda
            (1, 1)     # Diagonal abajo a la derecha
        ]

        for direction in directions:
            r, c = row + direction[0], col + direction[1]
            while 0 <= r < 8 and 0 <= c < 8:
                piece = board.board[r][c]
                if piece is None:
                    moves.append((r, c))
                elif piece.color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
                r += direction[0]
                c += direction[1]

        return moves
