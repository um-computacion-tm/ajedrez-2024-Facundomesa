
class Piece:
    def __init__(self, color, board):
        if color not in ["WHITE", "BLACK"]:
            raise ValueError("Color inválido. Debe ser 'WHITE' o 'BLACK'.")
        self.color = color
        self.board = board

    def is_move_valid(self, row, col, board):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        
        current_position = self._find_position()
        if current_position == (row, col):
            return False
        
        destination_piece = board[row][col]
        if destination_piece is None:
            return True
        elif destination_piece.color != self.color:
            return True
        else:
            return False

    def _find_position(self):
        for row in range(8):
            for col in range(8):
                if self.board[row][col] is self:
                    return row, col
        raise ValueError("La pieza no está en el tablero.")

    def movements(self, row, col, board):
        raise NotImplementedError("Este método debe ser implementado por subclases concretas.")

class MockPiece(Piece):
    def movements(self, row, col, board):
        return []
