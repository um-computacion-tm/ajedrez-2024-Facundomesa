class Rook:
    def __init__(self, color):
        if color.lower() not in ['white', 'black']:
            raise ValueError("Color must be either 'white' or 'black'")
        self.color = color.lower()

    def __repr__(self):
        return f"Rook({self.color.capitalize()})"

    def valid_moves(self, position):
        row, col = position
        if not (0 <= row <= 7 and 0 <= col <= 7):
            raise ValueError("Position must be within the bounds of a standard 8x8 chess board.")

        moves = []
        
        # Rook can move vertically and horizontally
        for i in range(8):
            if i != row:
                moves.append((i, col))  # Vertical moves
            if i != col:
                moves.append((row, i))  # Horizontal moves

        return moves

    def can_attack(self, target_position, current_position):
        """
        Determines if the Rook can attack a piece at the target_position given its current position.
        """
        target_row, target_col = target_position
        current_row, current_col = current_position

        # Rook can attack if on the same row or column
        return target_row == current_row or target_col == current_col

# Ejemplo
rook = Rook("White")
print(rook)
print("Valid moves from (0, 0):", rook.valid_moves((0, 0)))
print("Can attack from (0, 0) to (0, 7):", rook.can_attack((0, 7), (0, 0)))

