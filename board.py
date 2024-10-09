from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn


class Board:
    def __init__(self):
        # 8x8 matrix filled with None
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self._initialize_pieces()

    def _initialize_pieces(self):
        # Black pieces (first row)
        self.board[0][0] = Rook("black")
        self.board[0][7] = Rook("black")
        self.board[0][1] = Knight("black")
        self.board[0][6] = Knight("black")
        self.board[0][2] = Bishop("black")
        self.board[0][5] = Bishop("black")
        self.board[0][3] = Queen("black")
        self.board[0][4] = King("black")
        
        # Black pawns (second row)
        for col in range(8):
            self.board[1][col] = Pawn("black")

        # White pieces (last row)
        self.board[7][0] = Rook("white")
        self.board[7][7] = Rook("white")
        self.board[7][1] = Knight("white")
        self.board[7][6] = Knight("white")
        self.board[7][2] = Bishop("white")
        self.board[7][5] = Bishop("white")
        self.board[7][3] = Queen("white")
        self.board[7][4] = King("white")
        
        # White pawns (seventh row)
        for col in range(8):
            self.board[6][col] = Pawn("white")

    def set_piece(self, row, col, piece):
        """
        Coloca una pieza en la posición especificada.
        """
        if self.is_within_bounds(row, col):
            self.board[row][col] = piece
        else:
            raise ValueError("Posición fuera de los límites del tablero")

    def get_piece(self, row, col):
        """
        Devuelve la pieza en la posición especificada.
        """
        if self.is_within_bounds(row, col):
            return self.board[row][col]
        else:
            raise ValueError("Posición fuera de los límites del tablero")

    def is_within_bounds(self, row, col):
        """
        Verifica si la posición está dentro de los límites del tablero.
        """
        return 0 <= row < 8 and 0 <= col < 8
    
    
