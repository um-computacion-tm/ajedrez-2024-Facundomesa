import unittest
from knight import Knight

class TestKnight(unittest.TestCase):
    def setUp(self):
        self.knight_white = Knight("white")
        self.knight_black = Knight("black")

    def test_knight_moves(self):
        # Tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Posición inicial del caballo (en el centro del tablero)
        position = (4, 4)
        
        expected_moves = [
            (2, 3), (2, 5),
            (3, 2), (3, 6),
            (5, 2), (5, 6),
            (6, 3), (6, 5)
        ]

        moves = self.knight_white.get_valid_moves(position, board)
        
        # Asegurarse que los movimientos válidos coinciden con los esperados
        self.assertCountEqual(moves, expected_moves)

    def test_knight_with_pieces(self):
        # Tablero con algunas piezas
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Añadir una pieza aliada y una enemiga en las posiciones posibles
        board[2][3] = Knight("white")  # Aliada
        board[3][6] = Knight("black")  # Enemiga
        
        position = (4, 4)
        
        # Movimientos esperados (no debe incluir la posición con la pieza aliada)
        expected_moves = [
            (2, 5), (3, 2), (5, 2), (5, 6),
            (6, 3), (6, 5), (3, 6)  # Puede capturar a la pieza enemiga
        ]

        moves = self.knight_white.get_valid_moves(position, board)
        
        # Asegurarse que los movimientos válidos coinciden con los esperados
        self.assertCountEqual(moves, expected_moves)

if __name__ == "__main__":
    unittest.main()


