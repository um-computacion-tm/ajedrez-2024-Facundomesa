import unittest
from unittest.mock import patch
from game.chess import Chess
from game.main import play

class TestChessGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['0', '1', '2', '3'])
    @patch('builtins.print')
    def test_valid_move(self, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertTrue(mock_print.called)
        # Asegúrate de que el mensaje coincida con lo que imprime tu función
        mock_print.assert_any_call("Turno:", chess.turn)

    @patch('builtins.input', side_effect=['-1', '8', '2', '3'])
    @patch('builtins.print')
    def test_invalid_move(self, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertTrue(mock_print.called)
        # Asegúrate de que el mensaje coincida con lo que imprime tu función
        mock_print.assert_any_call('Error:', 'Movimiento inválido')

if __name__ == '__main__':
    unittest.main()

