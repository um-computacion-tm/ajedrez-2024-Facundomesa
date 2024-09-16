import unittest
from unittest.mock import patch
from game.chess import Chess
from game.cli import play
from game.chess import Chess, InvalidMove, InvalidMoveNoPiece, InvalidMoveRookMove

class TestCli(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['1,1', '2,1', '2,2', '1,1'])  # Movimientos válidos
    @patch('builtins.print')  # Patch para capturar las llamadas a print
    @patch.object(Chess, 'move')  # Patch para el método move del juego
    def test_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)

        # Verificamos las llamadas
        self.assertEqual(mock_input.call_count, 4)  # Se solicitan 4 entradas
        self.assertEqual(mock_print.call_count, 2)  # 2 impresiones de turno
        self.assertEqual(mock_chess_move.call_count, 2)  # 2 movimientos exitosos

    @patch('builtins.input', side_effect=['hola', '1,1', '2,2', '3,3'])  # Entrada inválida seguida de entrada válida
    @patch('builtins.print')  # Patch para capturar las llamadas a print
    @patch.object(Chess, 'move', side_effect=[None, InvalidMoveNoPiece("3,3")])  # El segundo movimiento es inválido
    def test_not_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)

        # Verificamos las llamadas
        self.assertEqual(mock_input.call_count, 4)  # 4 entradas solicitadas
        self.assertEqual(mock_print.call_count, 4)  # Imprime error y turno 2 veces
        self.assertEqual(mock_chess_move.call_count, 2)  # Se intenta mover dos veces, pero uno es inválido

    @patch('builtins.input', side_effect=['1,1', '3,3'])  # Movimiento inválido para una torre
    @patch('builtins.print')  # Patch para capturar las llamadas a print
    @patch.object(Chess, 'move', side_effect=InvalidMoveRookMove('1,1', '3,3'))  # Simula movimiento inválido de la torre
    def test_invalid_rook_move(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)

        # Verificamos las llamadas
        self.assertEqual(mock_input.call_count, 2)  # 2 entradas solicitadas
        self.assertEqual(mock_print.call_count, 2)  # Imprime turno y error
        self.assertEqual(mock_chess_move.call_count, 1)  # Se intenta mover una vez, pero es inválido

if __name__ == '__main__':
    unittest.main()
