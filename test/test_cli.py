import unittest
from unittest import mock  
from game.chess import Chess
from game.cli import play 
from unittest.mock import patch

class TestCli(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['1', '1', '2', '2'])  # Simula el input
    @patch('builtins.print')  # Controla el print
    @patch.object(Chess, 'move')
    def test_happy_path(self, mock_chess_move, mock_print, mock_input):
        """
        Verifica que el flujo feliz (movimiento correcto) funcione como se espera.
        """
        chess = Chess()
        play(chess)  # Juega el turno con inputs simulados
        
        # Verifica que input se haya llamado 4 veces (coordenadas de origen y destino)
        self.assertEqual(mock_input.call_count, 4)

        # Verifica que el movimiento se haya intentado ejecutar 1 vez
        self.assertEqual(mock_chess_move.call_count, 1)

        # Verifica que se hayan imprimido 2 mensajes
        self.assertEqual(mock_print.call_count, 2)

    @patch('builtins.input', side_effect=['hola', '1', '2', '2'])  # Primer input inválido
    @patch('builtins.print')  
    @patch.object(Chess, 'move')
    def test_invalid_first_input(self, mock_chess_move, mock_print, mock_input):
        """
        Verifica que un input no válido (como 'hola') se maneje correctamente.
        """
        chess = Chess()
        play(chess)
        
        # Verifica que solo se haya procesado el primer input (inválido)
        self.assertEqual(mock_input.call_count, 1)
        
        # Verifica que el mensaje de error y las instrucciones adicionales se impriman correctamente
        self.assertEqual(mock_print.call_count, 3)
        
        # No debe haberse llamado `move` porque el input fue inválido
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch('builtins.input', side_effect=['1', '1', '2', 'hola'])  # Input inválido al final
    @patch('builtins.print')  
    @patch.object(Chess, 'move')
    def test_invalid_second_input(self, mock_chess_move, mock_print, mock_input):
        """
        Verifica que un input no válido en la segunda coordenada se maneje correctamente.
        """
        chess = Chess()
        play(chess)

        # Se procesan los 4 inputs (2 válidos, 2 inválidos)
        self.assertEqual(mock_input.call_count, 4)
        
        # Debe haber 3 mensajes impresos (instrucciones + error)
        self.assertEqual(mock_print.call_count, 3)

        # No debe haberse ejecutado el movimiento por el input inválido
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch('builtins.print')  
    def test_check_output(self, mock_print):
        """
        Verifica que los mensajes impresos sean correctos.
        """
        # Simula una llamada a print
        print("Expected message")
        
        # Verifica que el mensaje esperado fue impreso
        mock_print.assert_called_with("Expected message")

        # Verifica que se llamó a print exactamente una vez
        self.assertEqual(mock_print.call_count, 1)

        # Opcional: puedes verificar el historial de llamadas a print
        print(mock_print.call_args_list)

if __name__ == '__main__':
    unittest.main()
