import unittest
from game.Board import Board
from game.chess import Chess

class TestChess(unittest.TestCase):

    def setUp(self):
        """
        Inicializa un objeto de la clase Chess y una configuración de tablero inicial.
        """
        self.chess = Chess()

    def test_initial_turn(self):
        """
        Verifica que el turno inicial sea 'WHITE'.
        """
        self.assertEqual(self.chess.turn, "WHITE", "El turno inicial debería ser WHITE.")

    def test_change_turn(self):
        """
        Verifica que el turno cambie correctamente entre 'WHITE' y 'BLACK'.
        """
        self.chess._change_turn()
        self.assertEqual(self.chess.turn, "BLACK", "El turno debería ser BLACK después de cambiar.")
        
        self.chess._change_turn()
        self.assertEqual(self.chess.turn, "WHITE", "El turno debería ser WHITE después de cambiar nuevamente.")

    def test_valid_move(self):
        """
        Verifica que se pueda realizar un movimiento válido.
        """
        self.chess._board.set_piece(1, 0, "WHITE")
        try:
            self.chess.move(1, 0, 2, 0)  # Movimiento válido
        except ValueError as e:
            self.fail(f"move() lanzó ValueError inesperadamente: {e}")

    def test_invalid_move_out_of_bounds(self):
        """
        Verifica que se lance un error al intentar mover fuera de los límites del tablero.
        """
        with self.assertRaises(ValueError, msg="El movimiento fuera de los límites no debería ser permitido."):
            self.chess.move(-1, 0, 8, 0)  # Movimiento fuera de los límites

    def test_move_without_piece(self):
        """
        Verifica que se lance un error al intentar mover desde una posición vacía.
        """
        with self.assertRaises(ValueError, msg="No debería poder mover desde una posición sin pieza."):
            self.chess.move(0, 0, 2, 0)  # No hay pieza en (0, 0)

    def test_move_wrong_turn(self):
        """
        Verifica que se lance un error al intentar mover una pieza que no corresponde al turno actual.
        """
        self.chess._board.set_piece(1, 0, "BLACK")
        with self.assertRaises(ValueError, msg="No debería poder mover una pieza que no corresponde al turno actual."):
            self.chess.move(1, 0, 2, 0)  # Es el turno de 'WHITE'

if __name__ == '__main__':
    unittest.main()

