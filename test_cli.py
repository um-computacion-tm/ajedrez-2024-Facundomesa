import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from chess import Chess
from cli import play, render_board_with_icons
from exceptions import InvalidPieceMoveError, GameOverException

class TestChessCLI(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_render_board_with_icons(self, mock_stdout):
        board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        render_board_with_icons(board)
        expected_output = (
            '♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n'
            '♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n'
            '♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n'
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['0', '0', '7', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_move(self, mock_stdout, mock_input):
        chess = MagicMock(spec=Chess)
        chess.get_board.return_value = [['.'] * 8 for _ in range(8)]
        chess.turno = 'WHITE'
        play(chess)
        
        chess.realizar_movimiento.assert_called_with(0, 0, 7, 7)
        self.assertIn("Movimiento realizado", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['EXIT'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_exit_game(self, mock_stdout, mock_input):
        chess = MagicMock(spec=Chess)
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Juego terminado.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['0', '0', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_move(self, mock_stdout, mock_input):
        chess = MagicMock(spec=Chess)
        chess.realizar_movimiento.side_effect = InvalidPieceMoveError("Invalid move")
        
        play(chess)
        
        self.assertIn("Movimiento inválido: Invalid move", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['1', 'a', 'EXIT'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_non_numeric_input(self, mock_stdout, mock_input):
        chess = MagicMock(spec=Chess)
        play(chess)
        
        self.assertIn("Entrada inválida. Por favor ingresa un número entre 0 y 7.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['0', '1', '2', '3', 'EXIT'])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.exit', side_effect=SystemExit)  
    def test_valid_move_then_exit(self, mock_stdout, mock_input, mock_exit):
        chess = MagicMock(spec=Chess)
        chess.get_board.return_value = [['.'] * 8 for _ in range(8)]
        chess.turno = 'WHITE'
        play(chess)
        
        chess.realizar_movimiento.assert_called_with(0, 1, 2, 3)
        
        # Llamada a exit después del movimiento
        self.assertIn("Juego terminado.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
