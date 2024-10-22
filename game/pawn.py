from game.piece import Piece

class Pawn(Piece):
    def __repr__(self):
        return f"Pawn({self.color})"

    def __str__(self):
        return "♙" if self.color == "WHITE" else "♟"

    def possible_moves(self, position, board):
        row, col = position
        moves = []

        # Determina la dirección en la que el peón se mueve
        direction = -1 if self.color == "WHITE" else 1

        # Movimiento estándar hacia adelante
        if 0 <= row + direction < 8 and board.board[row + direction][col] is None:
            moves.append((row + direction, col))
            # Movimiento inicial de dos casillas hacia adelante
            if (self.color == "WHITE" and row == 6) or (self.color == "BLACK" and row == 1):
                if board.board[row + 2 * direction][col] is None:
                    moves.append((row + 2 * direction, col))

        # Captura diagonal a la izquierda
        if 0 <= col - 1 < 8 and 0 <= row + direction < 8:
            left_diagonal = board.board[row + direction][col - 1]
            if left_diagonal is not None and left_diagonal.color != self.color:
                moves.append((row + direction, col - 1))

        # Captura diagonal a la derecha
        if 0 <= col + 1 < 8 and 0 <= row + direction < 8:
            right_diagonal = board.board[row + direction][col + 1]
            if right_diagonal is not None and right_diagonal.color != self.color:
                moves.append((row + direction, col + 1))
        
        return moves