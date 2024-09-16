import unittest
from unittest.mock import patch
from game.chess import Chess
from game.main import play
from unittest import mock

class TestChessGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '0', '2', '0'])
    @mock.patch('builtins.print')
    def test_valid_move(self, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertTrue(mock_print.called)
        # Asegúrate de que el mensaje esperado coincide con lo que imprime la función `play`
        expected_message = "Turno actual: WHITE"  # O `BLACK` dependiendo del turno inicial
        mock_print.assert_any_call(expected_message)
    print("Turno actual: WHITE")
    
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
