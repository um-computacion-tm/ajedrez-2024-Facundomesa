import unittest

class King:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{self.color} King"

    def get_valid_moves(self, position, board):
        row, col = position
        moves = []
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Movimientos diagonales y verticales hacia arriba
            (0, -1),          (0, 1),  # Movimientos horizontales
            (1, -1), (1, 0), (1, 1)   # Movimientos diagonales y verticales hacia abajo
        ]

        for direction in directions:
            r, c = row + direction[0], col + direction[1]
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board[r][c]
                if piece is None or piece.color != self.color:
                    moves.append((r, c))

        return moves

class TestKing(unittest.TestCase):
    def test_king_initialization(self):
        king = King("white")
        self.assertEqual(king.color, "white")
        self.assertEqual(str(king), "white King")

    def test_king_valid_moves_center(self):
        king = King("white")
        board = [[None for _ in range(8)] for _ in range(8)]
        position = (4, 4)
        expected_moves = [
            (3, 3), (3, 4), (3, 5),
            (4, 3),        (4, 5),
            (5, 3), (5, 4), (5, 5)
        ]
        self.assertCountEqual(king.get_valid_moves(position, board), expected_moves)

    def test_king_valid_moves_edge(self):
        king = King("black")
        board = [[None for _ in range(8)] for _ in range(8)]
        position = (0, 0)
        expected_moves = [
            (0, 1), 
            (1, 0), (1, 1)
        ]
        self.assertCountEqual(king.get_valid_moves(position, board), expected_moves)

    def test_king_valid_moves_with_pieces(self):
        king = King("white")
        board = [[None for _ in range(8)] for _ in range(8)]
        board[3][3] = King("white")  # Mismo color, no debería poder moverse aquí
        board[5][5] = King("black")  # Diferente color, debería poder moverse aquí
        position = (4, 4)
        expected_moves = [
            (3, 4), (3, 5),
            (4, 3),        (4, 5),
            (5, 3), (5, 4), (5, 5)
        ]
        self.assertCountEqual(king.get_valid_moves(position, board), expected_moves)

if __name__ == '__main__':
    unittest.main()
