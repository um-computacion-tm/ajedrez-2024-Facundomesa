import unittest
from exceptions import InvalidMove, InvalidMoveNoPiece, InvalidMoveRookMove
from exceptions import InvalidMoveBlockedPath, InvalidMoveOutOfBounds
from exceptions import InvalidMoveCheck, InvalidMoveKingMove
from exceptions import InvalidMovePawnMove, InvalidMoveKnightMove

class TestInvalidMoveExceptions(unittest.TestCase):

    def test_invalid_move(self):
        """Test para la excepción base InvalidMove."""
        with self.assertRaises(InvalidMove):
            raise InvalidMove("Movimiento inválido genérico.")

    def test_invalid_move_no_piece(self):
        """Test para la excepción InvalidMoveNoPiece."""
        position = (3, 4)
        with self.assertRaises(InvalidMoveNoPiece) as context:
            raise InvalidMoveNoPiece(position)
        
        self.assertEqual(str(context.exception), f"No hay ninguna pieza en la posición {position}.")

    def test_invalid_move_rook_move(self):
        """Test para la excepción InvalidMoveRookMove."""
        start = (0, 0)
        end = (1, 2)
        with self.assertRaises(InvalidMoveRookMove) as context:
            raise InvalidMoveRookMove(start, end)
        
        self.assertEqual(str(context.exception), f"Movimiento inválido para la torre desde {start} hasta {end}.")

    def test_invalid_move_out_of_bounds(self):
        with self.assertRaises(InvalidMoveOutOfBounds) as context:
            raise InvalidMoveOutOfBounds("h9")
        
        self.assertEqual(str(context.exception), "La posición h9 está fuera de los límites del tablero.")

def test_invalid_move_blocked_path(self):
        with self.assertRaises(InvalidMoveBlockedPath) as context:
            raise InvalidMoveBlockedPath("d2", "d4")
        
        self.assertEqual(str(context.exception), "El camino de d2 a d4 está bloqueado por otra pieza.")

def test_invalid_move_check(self):
        with self.assertRaises(InvalidMoveCheck) as context:
            raise InvalidMoveCheck()
        self.assertEqual(str(context.exception), "El movimiento deja al rey en jaque.")

def test_invalid_move_king(self):
        with self.assertRaises(InvalidMoveKingMove) as context:
            raise InvalidMoveKingMove("e1", "e3")
        self.assertEqual(str(context.exception), "Movimiento inválido para el rey desde e1 hasta e3.")

def test_invalid_move_pawn(self):
        with self.assertRaises(InvalidMovePawnMove) as context:
            raise InvalidMovePawnMove("e2", "e5")
        self.assertEqual(str(context.exception), "Movimiento inválido para el peón desde e2 hasta e5.")

def test_invalid_move_knight(self):
        with self.assertRaises(InvalidMoveKnightMove) as context:
            raise InvalidMoveKnightMove("g1", "g3")
        self.assertEqual(str(context.exception), "Movimiento inválido para el caballo desde g1 hasta g3.")

if __name__ == '__main__':
    unittest.main()
