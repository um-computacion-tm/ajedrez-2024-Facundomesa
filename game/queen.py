from game.piece import Piece

class Queen(Piece):
    def possible_moves(self, position, board):
        """
        Calcula los movimientos válidos para la reina desde la posición actual.
        La reina puede moverse en líneas rectas o diagonales.
        """
        row, col = position
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Movimientos verticales y horizontales
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Movimientos diagonales
        ]

        valid_moves = []

        for dr, dc in directions:
            r, c = row + dr, col + dc
            while board.is_within_bounds(r, c):
                piece = board.get_piece(r, c)
                if piece is None:
                    valid_moves.append((r, c))
                elif piece.color != self.color:
                    valid_moves.append((r, c))
                    break
                else:
                    break
                r += dr
                c += dc

        return valid_moves

    def __str__(self):
        return "♕" if self.color == "WHITE" else "♛"