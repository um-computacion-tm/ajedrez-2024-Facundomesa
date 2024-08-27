import unittest
from unittest.mock import patch
from game.chess import Chess
from game.main import get_move_input, play

class TestChessMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '0', '2', '0'])
    def test_get_move_input_valid(self, mock_input):
        """
        Prueba que get_move_input devuelva correctamente las coordenadas.
        """
        from_row, from_col, to_row, to_col = get_move_input()
        self.assertEqual((from_row, from_col, to_row, to_col), (1, 0, 2, 0))

    @patch('builtins.input', side_effect=['a', '0', '2', '0'])
    def test_get_move_input_invalid(self, mock_input):
        """
        Prueba que get_move_input lance un ValueError si la entrada no es numérica.
        """
        with self.assertRaises(ValueError):
            get_move_input()

    @patch('builtins.input', side_effect=['1', '0', '2', '0'])
    @patch.object(Chess, 'move')
    @patch.object(Chess, 'turn', new_callable=unittest.mock.PropertyMock, return_value='WHITE')
    def test_play_valid_move(self, mock_turn, mock_move, mock_input):
        """
        Prueba que play ejecute correctamente un movimiento válido.
        """
        chess = Chess()
        play(chess)
        mock_move.assert_called_once_with(1, 0, 2, 0)

    @patch('builtins.input', side_effect=['1', '0', '2', '0'])
    @patch.object(Chess, 'move', side_effect=ValueError("Movimiento no válido"))
    @patch.object(Chess, 'turn', new_callable=unittest.mock.PropertyMock, return_value='WHITE')
    def test_play_invalid_move(self, mock_turn, mock_move, mock_input):
        """
        Prueba que play maneje correctamente un movimiento no válido.
        """
        chess = Chess()
        with patch('builtins.print') as mock_print:
            play(chess)
            mock_move.assert_called_once_with(1, 0, 2, 0)
            mock_print.assert_called_with("Error: Movimiento no válido")

    @patch('builtins.input', side_effect=['1', '0', '2', '0'])
    @patch.object(Chess, 'move', side_effect=Exception("Error inesperado"))
    @patch.object(Chess, 'turn', new_callable=unittest.mock.PropertyMock, return_value='WHITE')
    def test_play_unexpected_error(self, mock_turn, mock_move, mock_input):
        """
        Prueba que play maneje correctamente un error inesperado.
        """
        chess = Chess()
        with patch('builtins.print') as mock_print:
            play(chess)
            mock_move.assert_called_once_with(1, 0, 2, 0)
            mock_print.assert_called_with("Unexpected error: Error inesperado")

if __name__ == '__main__':
    unittest.main()


