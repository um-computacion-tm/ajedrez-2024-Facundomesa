

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


