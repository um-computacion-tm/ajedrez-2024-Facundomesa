import unittest
from game.chess import Chess
from game.pawn import Pawn
from game.board import Board
from game.knight import Knight
from game.exceptions import NonPieceOriginError, WrongTurnError, InvalidPieceMoveError

class TestChess(unittest.TestCase):

    def setUp(self):
        """
        Inicializa un objeto de la clase Chess y configura el tablero inicial.
        """
        self.board = Board()
        self.chess = Chess()
        self.chess._board.set_piece(6, 0, Pawn("WHITE", self.board))  # Coloca un peón blanco en (6, 0)
        self.chess._board.set_piece(7, 1, Knight("WHITE", self.board))  # Coloca un caballo blanco en (7, 1)
        self.chess._board.set_piece(1, 0, Pawn("BLACK", self.board))  # Coloca un peón negro en (1, 0)
        self.chess._board.set_piece(1, 1, Pawn("BLACK", self.board))  # Coloca otro peón negro en (1, 1)

    def test_initialization(self):
        """
        Verifica que el juego se inicializa correctamente.
        """
        self.assertEqual(self.chess.turno, "WHITE", "El turno inicial debería ser WHITE.")
        self.assertIsNotNone(self.chess.get_board(), "El tablero no debería estar vacío.")

    def test_valid_pawn_move(self):
        """
        Verifica que un peón se mueva correctamente.
        """
        self.chess.move(6, 0, 4, 0)  # Mueve el peón blanco de (6, 0) a (4, 0)
        self.assertEqual(self.chess.turno, "BLACK", "El turno debería cambiar a BLACK.")
        self.assertEqual(self.chess.get_board()[6][0], ' ', "La posición (6, 0) debería estar vacía.")
        self.assertIsNotNone(self.chess.get_board()[4][0], "La posición (4, 0) debería tener una pieza.")

    def test_valid_knight_move(self):
        """
        Verifica que un caballo se mueva correctamente.
        """
        self.chess.move(7, 1, 5, 2)  # Mueve el caballo de (7, 1) a (5, 2)
        self.assertEqual(self.chess.turno, "BLACK", "El turno debería cambiar a BLACK.")
        self.assertEqual(self.chess._board.board[7][1], None, "La posición (7, 1) debería estar vacía.")
        self.assertIsNotNone(self.chess._board.board[5][2], "La posición (5, 2) debería tener una pieza.")

    def test_invalid_pawn_move(self):
        """
        Verifica que se lance una excepción si un peón se mueve a una posición inválida.
        """
        with self.assertRaises(InvalidPieceMoveError) as context:
            self.chess.move(6, 0, 3, 0)  # Movimiento inválido
        self.assertEqual(str(context.exception), "Invalid move for the selected piece.")

    def test_move_without_piece(self):
        """
        Verifica que se lance una excepción al intentar mover desde una posición sin pieza.
        """
        with self.assertRaises(NonPieceOriginError) as context:
            self.chess.move(3, 3, 4, 3)  # Intento de mover sin pieza
        self.assertEqual(str(context.exception), "There is no piece at the origin position.")

    def test_invalid_turn(self):
        """
        Verifica que se lance una excepción si el turno es incorrecto.
        """
        self.chess.move(6, 0, 4, 0)  # Mueve el peón blanco
        with self.assertRaises(InvalidPieceMoveError) as context:
            self.chess.move(1, 6, 4, 6)  # Intenta mover un peón negro
        self.assertEqual(str(context.exception), "Invalid move for the selected piece.")

    def test_move_to_own_piece_position(self):
        """
        Verifica que no se pueda mover a una posición ocupada por una pieza propia.
        """
        self.chess.move(6, 0, 4, 0)  # Mueve el peón blanco
        with self.assertRaises(InvalidPieceMoveError) as context:
            self.chess.move(1, 1, 2, 0)  # Intenta mover un peón negro a (2, 0)
        self.assertEqual(str(context.exception), "Invalid move for the selected piece.")

    def test_turn_change_after_valid_move(self):
        """
        Verifica que el turno cambie correctamente después de un movimiento válido.
        """
        self.chess.move(6, 0, 4, 0)  # Mueve el peón blanco
        self.assertEqual(self.chess.turno, "BLACK", "El turno debería ser BLACK después del movimiento.")
        self.chess.move(1, 0, 2, 0)  # Mueve el peón negro
        self.assertEqual(self.chess.turno, "WHITE", "El turno debería ser WHITE después del movimiento.")

    def test_invalid_move_does_not_change_turn(self):
        """
        Verifica que un movimiento inválido no cambie el turno.
        """
        self.chess.move(6, 0, 4, 0)  # Mueve el peón blanco
        initial_turn = self.chess.turno
        with self.assertRaises(WrongTurnError):
            self.chess.move(7, 1, 5, 3)  # Movimiento inválido de caballo
        self.assertEqual(self.chess.turno, initial_turn, "It is not the turn of the selected piece.")

    def test_moving_to_occupied_position(self):
        """
        Verifica que se lance una excepción al intentar mover a una posición ocupada por una pieza enemiga.
        """
        self.chess.move(6, 0, 4, 0)  # Mueve el peón blanco
        self.chess.move(1, 0, 3, 0)  # Mueve el peón negro
        with self.assertRaises(InvalidPieceMoveError) as context:
            self.chess.move(4, 0, 3, 0)  # Intenta mover a la posición ocupada por el peón negro
        self.assertEqual(str(context.exception), "Invalid move for the selected piece.")

    def test_moving_knight_to_invalid_position(self):
        """
        Verifica que un caballo no pueda moverse a una posición inválida.
        """
        self.chess.move(7, 1, 5, 2)  # Mueve el caballo de (7, 1) a (5, 2)
        with self.assertRaises(WrongTurnError) as context:
            self.chess.move(5, 2, 4, 4)  # Movimiento inválido de caballo
        self.assertEqual(str(context.exception), "It is not the turn of the selected piece.")

if __name__ == '__main__':
    unittest.main()
