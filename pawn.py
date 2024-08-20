from piece import Piece

class Pawn(Piece):
    def movements(self, row, col, board):
        moves = []
        direction = -1 if self.color == 'white' else 1
        start_row = 6 if self.color == 'white' else 1

        # Movimiento hacia adelante
        if self.is_move_valid(row + direction, col, board):
            moves.append((row + direction, col))
            if row == start_row and self.is_move_valid(row + 2 * direction, col, board):
                moves.append((row + 2 * direction, col))

        # Captura en diagonal
        if self.is_move_valid(row + direction, col - 1, board):
            moves.append((row + direction, col - 1))
        if self.is_move_valid(row + direction, col + 1, board):
            moves.append((row + direction, col + 1))
        
        return moves

# rook

from piece import Piece

class Rook(Piece):
    def movements(self, row, col, board):
        moves = []
        for d in [-1, 1]:
            for i in range(1, 8):
                if self.is_move_valid(row + d * i, col, board):
                    moves.append((row + d * i, col))
                    if board[row + d * i][col] is not None:
                        break
                else:
                    break

                if self.is_move_valid(row, col + d * i, board):
                    moves.append((row, col + d * i))
                    if board[row][col + d * i] is not None:
                        break
                else:
                    break
        return moves

# knight

from piece import Piece

class Knight(Piece):
    def movements(self, row, col, board):
        moves = []
        offsets = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        for r_offset, c_offset in offsets:
            new_row, new_col = row + r_offset, col + c_offset
            if self.is_move_valid(new_row, new_col, board):
                moves.append((new_row, new_col))
        return moves

# bishop

from piece import Piece

class Bishop(Piece):
    def movements(self, row, col, board):
        moves = []
        for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for i in range(1, 8):
                new_row, new_col = row + dr * i, col + dc * i
                if self.is_move_valid(new_row, new_col, board):
                    moves.append((new_row, new_col))
                    if board[new_row][new_col] is not None:
                        break
                else:
                    break
        return moves

# queen

from piece import Piece

class Queen(Piece):
    def movements(self, row, col, board):
        moves = []
        rook = Rook(self.color)
        bishop = Bishop(self.color)

        moves.extend(rook.movements(row, col, board))
        moves.extend(bishop.movements(row, col, board))
        
        return moves

# king

from piece import Piece

class King(Piece):
    def movements(self, row, col, board):
        moves = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row, new_col = row + dr, col + dc
                if self.is_move_valid(new_row, new_col, board):
                    moves.append((new_row, new_col))
        return moves
