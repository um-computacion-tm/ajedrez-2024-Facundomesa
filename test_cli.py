import unittest
from unittest.mock import patch
from chess import Chess
from main import main , play
class TestChessGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['0', '1', '2', '3'])  
    @patch('builtins.print')  
    def test_valid_move(self, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertTrue(mock_print.called)
        mock_print.assert_any_call("turn: ", chess.turn)

    @patch('builtins.input', side_effect=['-1', '8', '2', '3']) 
    @patch('builtins.print') 
    def test_invalid_move(self, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertTrue(mock_print.called)
        mock_print.assert_any_call('error', 'Invalid move')  

if __name__ == '__main__':
    unittest.main()
