import unittest
from piezas import Bishop

class TestBishop(unittest.TestCase):
    def test_Bishop_initialization(self):
        bishop = bishop("white")
        self.assertEqual(bishop.color, "white")
        self.assertEqual(str(bishop), "white Bishop")

    def test_Bishop_moves_from_center(self):
        bishop = bishop("white")
        board = [[None for _ in range(8)] for _ in range(8)]
        position = (4, 4)
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0),  # Diagonal arriba izquierda
            (3, 5), (2, 6), (1, 7),          # Diagonal arriba derecha
            (5, 3), (6, 2), (7, 1),          # Diagonal abajo izquierda
            (5, 5), (6, 6), (7, 7)           # Diagonal abajo derecha
        ]
        self.assertCountEqual(bishop.get_valid_moves(position, board), expected_moves)

    def test_Bishop_moves_with_obstructions(self):
        bishop = bishop("white")
        board = [[None for _ in range(8)] for _ in range(8)]
        board[2][2] = bishop("white")  # Obstrucción del mismo color
        board[6][6] = bishop("black")  # Obstrucción de color contrario
        position = (4, 4)
        expected_moves = [
            (3, 3),  # Diagonal arriba izquierda (parada antes del 2,2)
            (3, 5), (2, 6), (1, 7),  # Diagonal arriba derecha
            (5, 3), (6, 2), (7, 1),  # Diagonal abajo izquierda
            (5, 5), (6, 6)           # Diagonal abajo derecha (parada en 6,6)
        ]
        self.assertCountEqual(bishop.get_valid_moves(position, board), expected_moves)

    def test_Bishop_moves_from_corner(self):
        bishop = bishop("black")
        board = [[None for _ in range(8)] for _ in range(8)]
        position = (0, 0)
        expected_moves = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal única disponible
        ]
        self.assertCountEqual(bishop.get_valid_moves(position, board), expected_moves)

if __name__ == '__main__':
    unittest.main()
