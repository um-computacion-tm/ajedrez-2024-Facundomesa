import unittest
from piezas.Rook import Rook


class TestRook(unittest.TestCase):
    def setUp(self):
        self.white_Rook = Rook("White")
        self.black_Rook = Rook("Black")

    def test_color_validation(self):
        with self.assertRaises(ValueError):
            Rook("Red")  # Color inválido
        with self.assertRaises(ValueError):
            Rook("")  # Color vacío

    def test_valid_moves_from_corner(self):
        expected_moves = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                          (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
        self.assertEqual(set(self.white_Rook.valid_moves((0, 0))), set(expected_moves))

    def test_valid_moves_from_center(self):
        expected_moves = [(3, 4), (5, 4), (6, 4), (7, 4), (4, 0), (4, 1), (4, 2), (4, 3),
                          (4, 5), (4, 6), (4, 7), (0, 4), (1, 4), (2, 4)]
        self.assertEqual(set(self.white_Rook.valid_moves((4, 4))), set(expected_moves))

    def test_invalid_position(self):
        with self.assertRaises(ValueError):
            self.white_Rook.valid_moves((8, 8))  # Posición fuera del tablero

    def test_can_attack_same_row(self):
        self.assertTrue(self.white_Rook.can_attack((0, 7), (0, 0)))
        self.assertTrue(self.black_Rook.can_attack((4, 4), (4, 1)))

    def test_can_attack_same_column(self):
        self.assertTrue(self.white_Rook.can_attack((7, 0), (0, 0)))
        self.assertTrue(self.black_Rook.can_attack((4, 4), (1, 4)))

    def test_cannot_attack(self):
        self.assertFalse(self.white_Rook.can_attack((1, 1), (0, 0)))
        self.assertFalse(self.black_Rook.can_attack((2, 3), (1, 4)))

    def test_representation(self):
        self.assertEqual(repr(self.white_Rook), "Rook(White)")
        self.assertEqual(repr(self.black_Rook), "Rook(Black)")


    def test_str(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♜",
        )

    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1), (7, 1)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )
        
if __name__ == '__main__':
    unittest.main()
