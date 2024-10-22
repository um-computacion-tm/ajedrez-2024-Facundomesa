import unittest
from game.board import Board
from game.exceptions import NonCaptureOwnPieceError, NonPassOverPieceError, GameOverException
from game.pawn import Pawn
from game.rook import Rook

class TestTablero(unittest.TestCase):
    # Verifica el comportamiento del método is_valid_move de la clase Board cuando no hay una pieza en la posición de origen  
    def test_movimiento_invalido_sin_pieza(self):
        tablero = Board()
        self.assertFalse(tablero.is_valid_move(3, 3, 4, 4))

    # Verifica que el método move_piece lance la excepción NonCaptureOwnPieceError cuando se intenta capturar una pieza del mismo jugador.
    def test_intento_captura_propia_pieza(self):
        tablero = Board(forTest=True)  # Usar el modo de prueba
        tablero.set_piece(7, 0, Rook("WHITE"))  # Colocar una torre blanca
        tablero.set_piece(6, 0, Pawn("WHITE"))  # Colocar un peón blanco
        with self.assertRaises(NonCaptureOwnPieceError) as contexto:
            tablero.move_piece(7, 0, 6, 0)  # Intentar mover torre a la posición del peón
        self.assertEqual(str(contexto.exception), "No puedes capturar tus propias piezas.")

    # Verifica que la excepción NonPassOverPieceError se lance cuando una pieza intenta moverse sobre otra.
    def test_pieza_pasa_sobre_otras(self):
        tablero = Board(forTest=True)  # Usar el modo de prueba
        tablero.set_piece(0, 0, Rook("WHITE"))  # Colocar una torre blanca
        tablero.set_piece(0, 1, Pawn("BLACK"))  # Colocar un peón negro
        with self.assertRaises(NonPassOverPieceError) as contexto:
            tablero.move_piece(0, 0, 0, 2)  # Intentar mover la torre sobre el peón
        self.assertEqual(str(contexto.exception), "No puedes pasar sobre otras piezas.")

    # Verifica que se lance la excepción GameOverException con el mensaje "White wins" cuando las piezas negras se quedan sin piezas en el tablero.
    def test_partida_finalizada_gana_blancas(self):
        tablero = Board(forTest=True)  # Usar el modo de prueba
        class Torre:
            def get_color(self):
                return 'WHITE'
        tablero.set_piece(7, 7, Torre())  # Colocar una torre blanca
        tablero.set_piece(0, 0, None)  # Eliminar todas las piezas negras
        with self.assertRaises(GameOverException) as contexto:
            tablero._verificar_fin_partida()
        self.assertEqual(str(contexto.exception), "White wins")

    # Verifica que se lance la excepción GameOverException con el mensaje "Black wins" cuando las piezas blancas se quedan sin piezas en el tablero.
    def test_partida_finalizada_gana_negras(self):
        tablero = Board(forTest=True)  # Usar el modo de prueba
        class Torre:
            def get_color(self):
                return 'BLACK'
        tablero.set_piece(0, 0, Torre())  # Colocar una torre negra
        tablero.set_piece(7, 7, None)  # Eliminar todas las piezas blancas
        with self.assertRaises(GameOverException) as contexto:
            tablero._verificar_fin_partida()
        self.assertEqual(str(contexto.exception), "Black wins")

if __name__ == '__main__':
    unittest.main()
