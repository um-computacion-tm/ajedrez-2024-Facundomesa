
class Rook:
    def __init__(self, color):
        if color not in ["White", "Black"]:
            raise ValueError("Color must be 'White' or 'Black'")
        self.color = color

    def valid_moves(self, position):
        row, col = position
        if not (0 <= row <= 7 and 0 <= col <= 7):
            raise ValueError("Invalid position on the board")

        moves = []
        # Horizontal and vertical moves
        for i in range(8):
            if i != row:
                moves.append((i, col))  # vertical moves
            if i != col:
                moves.append((row, i))  # horizontal moves
        return moves

    def can_attack(self, target, current):
        return target[0] == current[0] or target[1] == current[1]

    def __repr__(self):
        return f"Rook({self.color})"
    
    def __str__(self):
        return "♜" if self.color == "BLACK" else "♖"

    def possible_positions_vd(self, row, col):
        possibles = []
        for i in range(row + 1, 8):
            if self.board.is_empty(i, col):
                possibles.append((i, col))
            else:
                if self.board.get_piece(i, col).color != self.color:
                    possibles.append((i, col))
                break
        return possibles

    def possible_positions_va(self, row, col):
        possibles = []
        for i in range(row - 1, -1, -1):
            if self.board.is_empty(i, col):
                possibles.append((i, col))
            else:
                if self.board.get_piece(i, col).color != self.color:
                    possibles.append((i, col))
                break
        return possibles
