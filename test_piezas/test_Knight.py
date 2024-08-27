import unittest
from piezas.Knight import Knight


class TestKnight(unittest.TestCase):
    def test_knight_initialization(self):
        knight = Knight("white")
        self.assertEqual(knight.color, "white")
        self.assertEqual(str(knight), "white Knight")

    def test_knight_moves_from_center(self):
        knight = Knight("white")
        board = [[None for _ in range(8)] for _ in range(8)]
        position = (4, 4)
        expected_moves = [
            (2, 3), (2, 5),
            (3, 2), (3, 6),
            (5, 2), (5, 6),
            (6, 3), (6, 5)
        ]
        self.assertCountEqual(knight.get_valid_moves(position, board), expected_moves)

    def test_knight_moves_with_obstructions(self):
        knight = Knight("white")
        board = [[None for _ in range(8)] for _ in range(8)]
        board[6][5] = Knight("white")
        board[2][5] = Knight("black")
        position = (4, 4)
        expected_moves = [
            (2, 3), (2, 5),
            (3, 2), (3, 6),
            (5, 2), (5, 6),
            (6, 3)
        ]
        self.assertCountEqual(knight.get_valid_moves(position, board), expected_moves)

    def test_knight_moves_from_corner(self):
        knight = Knight("black")
        board = [[None for _ in range(8)] for _ in range(8)]
        position = (0, 0)
        expected_moves = [(2, 1), (1, 2)]
        self.assertCountEqual(knight.get_valid_moves(position, board), expected_moves)

if __name__ == '__main__':
    unittest.main()
