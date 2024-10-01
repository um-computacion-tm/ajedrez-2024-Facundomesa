from piezas.Rook import Rook
from piezas.Knight import Knight
from piezas.Bishop import Bishop
from piezas.Queen import Queen
from piezas.King import King
from piezas.Pawn import Pawn


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

    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        else:
            raise IndexError("Posición fuera del tablero")