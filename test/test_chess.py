import unittest
from game.chess import Chess

class TestChess(unittest.TestCase):

    def setUp(self):
        """
        Inicializa un objeto de la clase Chess y una configuración de tablero inicial.
        """
        self.chess = Chess()
        # Suponiendo que Board tiene un método para agregar piezas en posiciones específicas.
        self.chess._board.set_piece(1, 0, "WHITE")  # Coloca una pieza blanca en (1, 0)
        self.chess._board.set_piece(6, 0, "BLACK")  # Coloca una pieza negra en (6, 0)

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

    # Asegura que haya una pieza en (1, 0) antes de moverla
        self.chess._board.set_piece(1, 0, "WHITE")  # Coloca una pieza blanca en (1, 0)

    # Movimiento válido de una pieza blanca desde (1, 0) a (2, 0)
    try:
        self.chess.move(1, 0, 2, 0)  # Movimiento válido
    except ValueError:
        self.fail("move() lanzó ValueError inesperadamente para un movimiento válido.")


    def test_invalid_move_out_of_bounds(self):
        """
        Verifica que se lance un error al intentar mover fuera de los límites del tablero.
        """
        with self.assertRaises(ValueError, msg="El movimiento fuera de los límites no debería ser permitido."):
            self.chess.move(-1, 0, 8, 0)  # Movimiento fuera de los límites

    def test_move_to_same_position(self):
        """
        Verifica que se lance un error si se intenta mover a la misma posición.
        """
        with self.assertRaises(ValueError, msg="No deberías poder mover una pieza a la misma posición."):
            self.chess.move(1, 0, 1, 0)  # Movimiento a la misma posición

    def test_move_to_occupied_position_by_own_piece(self):
        """
        Verifica que no se pueda mover una pieza a una posición ocupada por una pieza del mismo color.
        """
        self.chess._board.set_piece(2, 0, "WHITE")  # Coloca una pieza blanca en la posición destino
        with self.assertRaises(ValueError, msg="No puedes capturar tu propia pieza."):
            self.chess.move(1, 0, 2, 0)  # Intenta mover a una posición ocupada por una pieza blanca

    def test_move_wrong_turn(self):
        """
        Verifica que no se pueda mover una pieza cuando no es el turno del jugador.
        """
        # Es el turno de 'WHITE', intentamos mover una pieza negra
        with self.assertRaises(ValueError, msg="No deberías poder mover una pieza negra en el turno de WHITE."):
            self.chess.move(6, 0, 5, 0)  # Intenta mover la pieza negra en el turno de 'WHITE'

if __name__ == '__main__':
    unittest.main()
