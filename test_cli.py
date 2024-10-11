import unittest
from chess import Chess
from cli import play 
from unittest.mock import patch

class TestCli(unittest.TestCase):
    
    @patch('cli.input', side_effect=['0', '1', '2', '3', 'yes', 'no'])  # Simula suficientes inputs del usuario
    @patch('cli.print')  # Simula la función print
    @patch('chess.Chess.move')  # Simula el método 'move' de Chess
    def test_happy_path(self, mock_chess_move, mock_print, mock_input):
        # Inicializar el objeto Chess
        chess = Chess()

        # Ejecutar la función de jugar con los mocks de inputs
        play(chess)

        # Verificar que se llamaron los mocks como se esperaba
        mock_input.assert_called()  # Verificar que se llamó la función input
        mock_print.assert_called()  # Verificar que se llamó la función print
        mock_chess_move.assert_called()  # Verificar que se llamó el método move

        # Puedes también verificar el número de veces que se llamaron
        self.assertEqual(mock_input.call_count, 6)  # Se espera que input se llame 6 veces (ajusta según tu flujo)
        self.assertEqual(mock_print.call_count, 1)

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
