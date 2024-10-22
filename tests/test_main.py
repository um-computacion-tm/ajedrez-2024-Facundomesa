import unittest
from unittest.mock import patch
from game.main import main  # Asegúrate de que el nombre del archivo sea correcto

class TestMainFunction(unittest.TestCase):
    @patch('main.play')  # Simula la función play
    @patch('main.Chess')  # Simula la clase Chess
    def test_main_calls_play_with_chess_instance(self, mock_chess, mock_play):
        mock_chess_instance = mock_chess.return_value  # Obtiene la instancia simulada de Chess
        main()  # Llama a la función main

        # Verifica que se creó una instancia de Chess
        mock_chess.assert_called_once()
        
        # Verifica que se llamó a play con la instancia de Chess
        mock_play.assert_called_once_with(mock_chess_instance)

if __name__ == '__main__':
    unittest.main()
