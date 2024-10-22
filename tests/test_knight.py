import unittest
from game.knight import Knight
from game.board import Board

class TestKnight(unittest.TestCase):
    def setUp(self):
        self.board = Board(forTest=True)
        self.knight_white = Knight("WHITE", self.board)
        self.knight_black = Knight("BLACK", self.board)

    def test_knight_moves(self):
        
        # Posición inicial del caballo (en el centro del tablero)
        position = (4, 4)
        
        expected_moves = [
            (2, 3), (2, 5),
            (3, 2), (3, 6),
            (5, 2), (5, 6)
        ]

        moves = self.knight_white.possible_moves(position, self.board)
        
        # Asegurarse que los movimientos válidos coinciden con los esperados
        self.assertCountEqual(moves, expected_moves)

    def test_knight_with_pieces(self):
        # Tablero con algunas piezas
        
        # Añadir una pieza aliada y una enemiga en las posiciones posibles
        self.board.board[2][3] = Knight("WHITE", self.board)  # Aliada
        self.board.board[3][6] = Knight("BLACK", self.board)  # Enemiga
        
        position = (4, 4)
        
        # Movimientos esperados (no debe incluir la posición con la pieza aliada)
        expected_moves = [
            (2, 5), (3, 2), (5, 2), (5, 6),
            (3, 6)  # Puede capturar a la pieza enemiga
        ]

        moves = self.knight_white.possible_moves(position, self.board)
        
        # Asegurarse que los movimientos válidos coinciden con los esperados
        self.assertCountEqual(moves, expected_moves)

if __name__ == "__main__":
    unittest.main()


