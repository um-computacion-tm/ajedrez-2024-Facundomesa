import unittest
from game.board import Board
from game.chess import Chess

class TestChess(unittest.TestCase):

    def setUp(self):
        """
        Inicializa un objeto de la clase Chess y una configuración de tablero inicial.
        """
        self.chess = Chess()

    def test_initial_turn(self):
        """
        Prueba que el turno inicial sea 'WHITE'.
        """
        self.assertEqual(self.chess.turn, "WHITE")

    def test_change_turn(self):
        """
        Prueba que el turno cambie de 'WHITE' a 'BLACK' y viceversa.
        """
        self.chess._change_turn()
        self.assertEqual(self.chess.turn, "BLACK")
        self.chess._change_turn()
        self.assertEqual(self.chess.turn, "WHITE")

    def test_valid_move(self):
        """
        Prueba un movimiento válido.
        """
        # Suponiendo que hay una pieza en la posición (1, 0) que pertenece a 'WHITE'
        self.chess._board.set_piece(1, 0, "WHITE")
        try:
            self.chess.move(1, 0, 2, 0)  # Movimiento válido
        except ValueError:
            self.fail("move() lanzó ValueError inesperadamente.")

    def test_invalid_move_out_of_bounds(self):
        """
        Prueba un movimiento inválido fuera de los límites del tablero.
        """
        with self.assertRaises(ValueError):
            self.chess.move(-1, 0, 8, 0)  # Movimiento fuera de los límites

    def test_move_without_piece(self):
        """
        Prueba un movimiento desde una posición sin pieza.
        """
        with self.assertRaises(ValueError):
            self.chess.move(0, 0, 2, 0)  # No hay ninguna pieza en (0, 0)

    def test_move_wrong_turn(self):
        """
        Prueba un movimiento de una pieza que no corresponde al turno actual.
        """
        # Suponiendo que hay una pieza en la posición (1, 0) que pertenece a 'BLACK'
        self.chess._board.set_piece(1, 0, "BLACK")
        with self.assertRaises(ValueError):
            self.chess.move(1, 0, 2, 0)  # Es el turno de 'WHITE', no puede mover 'BLACK'

if __name__ == '__main__':
    unittest.main()
