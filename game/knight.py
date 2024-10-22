from game.piece import Piece

class Knight(Piece):
    def __str__(self):
        return "♘" if self.color == "WHITE" else "♞"

    def possible_moves(self, position, board):
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
                piece = board.board[new_row][new_col]
                # Si la casilla está vacía o tiene una pieza del color contrario
                if piece is None or piece.color != self.color:
                    moves.append((new_row, new_col))

        return moves

    def _is_within_bounds(self, row, col):
        """Verifica si la posición está dentro de los límites del tablero (8x8)."""
        return 0 <= row < 8 and 0 <= col < 8
