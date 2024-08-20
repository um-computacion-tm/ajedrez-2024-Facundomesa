import unittest
from unittest.mock import patch
from chess import Chess
from main import main, play  

class TestChessGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '0', '2', '0']) 
    @patch('builtins.print')  
    def test_valid_move(self, mock_print, mock_input):
        chess = Chess()
        play(chess)
        
    
        self.assertTrue(mock_print.called)
        
        
        mock_print.assert_any_call("Turno: ", chess.turn)
        
        

    @patch('builtins.input', side_effect=['0', '0', '2', '2'])  
    @patch('builtins.print')  
    def test_invalid_move(self, mock_print, mock_input):
        chess = Chess()
        play(chess)
        
        
        self.assertTrue(mock_print.called)
        mock_print.assert_any_call("Error:", unittest.mock.ANY)  

if __name__ == '__main__':
    unittest.main()
