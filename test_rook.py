import unittest
from rook import Rook
from board import Board
from pawn import Pawn

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]  # Crear un tablero vacío
        self.white_Rook = Rook("WHITE", self.board)
        self.black_Rook = Rook("BLACK", self.board)

    def test_color_validation(self):
        with self.assertRaises(ValueError):
            Rook("Red")  # Color inválido
        with self.assertRaises(ValueError):
            Rook("")  # Color vacío

    def test_valid_moves_from_center(self):
        # Movimientos esperados desde la posición (4, 4)
        expected_moves = [
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7),  # Movimientos horizontales
            (0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4)   # Movimientos verticales
        ]
        
        # Llamar a valid_moves con la posición y el tablero
        valid_moves = self.white_Rook.valid_moves((4, 4), self.board)
        
        # Comparar los movimientos calculados con los movimientos esperados
        self.assertEqual(set(valid_moves), set(expected_moves))

    def test_invalid_position(self):
        # Intentar obtener movimientos de una posición inválida
        with self.assertRaises(ValueError):  # Esperamos que se lance un ValueError
            self.white_Rook.valid_moves((8, 8), self.board)  # Posición fuera del tablero

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
        self.assertEqual(repr(self.white_Rook), "Rook(WHITE)")
        self.assertEqual(repr(self.black_Rook), "Rook(BLACK)")

    def test_str(self):
        rook = Rook("WHITE", self.board)
        self.assertEqual(str(rook), "♖")  # Torre blanca, ♖, negra sería ♜

    def test_move_vertical_desc(self):
        possibles = self.white_Rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1), (6, 1), (7, 1)])

    def test_move_vertical_asc(self):
        possibles = self.white_Rook.possible_positions_va(4, 1)
        self.assertEqual(possibles, [(3, 1), (2, 1), (1, 1), (0, 1)])

    def test_move_vertical_desc_with_own_piece(self):
        self.board[6][1] = Pawn("WHITE", self.board)
        self.board[4][1] = self.white_Rook
        possibles = self.white_Rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1)])  # La torre no puede saltar piezas propias

    def test_move_vertical_desc_with_not_own_piece(self):
        self.board[7][1] = self.white_Rook
        self.board[6][1] = Pawn("BLACK", self.board)
        
        # Movimientos esperados: la torre puede capturar el peón en (6, 1)
        valid_moves = self.white_Rook.possible_positions_vd(7, 1)
        expected_moves = [(6, 1)]  # El peón negro en (6, 1) puede ser capturado

        # Verificar que los movimientos válidos sean los esperados
        self.assertEqual(valid_moves, expected_moves)

if __name__ == '__main__':
    unittest.main()
