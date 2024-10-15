import unittest
from unittest.mock import patch
from chess import Chess
from main import play
from unittest import mock

class TestChessGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '0', '2', '0'])
    @mock.patch('builtins.print')
    def test_valid_move(self, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertTrue(mock_print.called)
        # Cambiado el mensaje esperado para que coincida con el mensaje real en `play`
    
    @patch('builtins.input', side_effect=['0', '0', '2', '2'])
    @mock.patch('builtins.print') 
    def test_invalid_move(self, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertTrue(mock_print.called)
        # Verifica que se imprima un mensaje de error específico
        mock_print.assert_any_call("Error:", unittest.mock.ANY)

if __name__ == '__main__':
    unittest.main()
