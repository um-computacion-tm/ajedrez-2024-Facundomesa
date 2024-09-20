from piezas.Rook import Rook


class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("BLACK") # Black
        self.__positions__[0][7] = Rook("BLACK") # Black
        self.__positions__[7][7] = Rook("WHITE") # White
        self.__positions__[7][0] = Rook("WHITE") # White

    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def is_empty(self, row, col):
        return self.grid[row][col] is None

    def set_piece(self, row, col, piece):
        # Coloca una pieza en una posición específica
        if not (0 <= row < 8 and 0 <= col < 8):
            raise ValueError("Posición fuera del tablero")
        self.grid[row][col] = piece

    def get_piece(self, row, col):
        # Retorna la pieza en una posición específica
        if not (0 <= row < 8 and 0 <= col < 8):
            raise ValueError("Posición fuera del tablero")
        return self.grid[row][col]
    