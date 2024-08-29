class Piece:
    def __init__(self, color):
        self.color = color
    
    def movements(self, row, col, board):
        """Devuelve los movimientos válidos para la pieza en la posición dada (row, col)."""
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def is_move_valid(self, row, col, board):
        """Verifica si el movimiento es válido, considerando el tablero."""
        return (0 <= row < 8) and (0 <= col < 8) and (board[row][col] is None or board[row][col].color != self.color)

    def __init__(self, color, board):
        self.color = color
        self.board = board

    def __str__(self):
        raise NotImplementedError("This method should be overridden.")

    def possible_positions_vd(self, row, col):
        raise NotImplementedError("This method should be overridden.")

    def possible_positions_va(self, row, col):
        raise NotImplementedError("This method should be overridden.")