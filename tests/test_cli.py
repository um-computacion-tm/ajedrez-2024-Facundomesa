import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from game.chess import Chess
from game.exceptions import InvalidPieceMoveError, GameOverException
from game.cli import *

class TestChessCLI(unittest.TestCase):

    @patch('builtins.input', side_effect=['0', '0', '7', '7', 'EXIT'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_move(self, mock_stdout, mock_input):
        chess = MagicMock(spec=Chess)
        chess.get_board.return_value = [['.'] * 8 for _ in range(8)]
        chess.turno = 'WHITE'
        with self.assertRaises(SystemExit):
            play(chess)
        
        chess.move.assert_called_with(0, 0, 7, 7)
        self.assertIn("", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['EXIT'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_exit_game(self, mock_stdout, mock_input):
        chess = MagicMock(spec=Chess)
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Juego terminado.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['0', '0', '1', '1', 'EXIT'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_move(self, mock_stdout, mock_input):
        chess = MagicMock(spec=Chess)
        chess.move.side_effect = InvalidPieceMoveError("Invalid move")
        with self.assertRaises(SystemExit):
            play(chess)
        
        self.assertIn("Movimiento inválido: Invalid move", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['1', 'a', 'EXIT'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_non_numeric_input(self, mock_stdout, mock_input):
        chess = MagicMock(spec=Chess)
        with self.assertRaises(SystemExit):
            play(chess)
        
        self.assertIn("Entrada inválida. Por favor ingresa un número entre 0 y 7.", mock_stdout.getvalue())

@patch('builtins.input', side_effect=['0', '1', '2', '3', 'EXIT'])
@patch('sys.stdout', new_callable=StringIO)
@patch('builtins.exit', side_effect=SystemExit)  
def test_valid_move_then_exit(self, mock_stdout, mock_input, mock_exit):
    chess = MagicMock(spec=Chess)
    chess.get_board.return_value = [['.'] * 8 for _ in range(8)]
    chess.turno = 'WHITE'
    
    # Definir manualmente el método 'realizar_movimiento' en el Mock
    chess.realizar_movimiento = MagicMock()

    # Asegurarse de que se lanza SystemExit cuando se llama a exit
    with self.assertRaises(SystemExit):
        play(chess)

    # Verificar que 'realizar_movimiento' se haya llamado con las coordenadas correctas
    chess.realizar_movimiento.assert_called_with(0, 1, 2, 3)

    # Verificar que se haya mostrado el mensaje de finalización del juego
    self.assertIn("Juego terminado.", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
