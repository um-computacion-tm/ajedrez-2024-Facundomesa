import unittest
from pawn import Pawn

class TestPawn(unittest.TestCase):
    def test_pawn_initialization(self):
        pawn = Pawn("white")
        self.assertEqual(pawn.color, "white")
        self.assertEqual(str(pawn), "white Pawn")

    def test_pawn_moves_white_starting_position(self):
        pawn = Pawn("white")
        board = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío
        position = (6, 4)  # Posición inicial para peón blanco
        expected_moves = [(5, 4), (4, 4)]  # Movimientos iniciales
        self.assertCountEqual(pawn.get_valid_moves(position, board), expected_moves)

    def test_pawn_moves_black_starting_position(self):
        pawn = Pawn("black")
        board = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío
        position = (1, 4)  # Posición inicial para peón negro
        expected_moves = [(2, 4), (3, 4)]  # Movimientos iniciales
        self.assertCountEqual(pawn.get_valid_moves(position, board), expected_moves)

    def test_pawn_moves_with_blocking_piece(self):
        pawn = Pawn("white")
        board = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío
        board[5][4] = Pawn("white")  # Peón blanco bloqueando el camino
        position = (6, 4)  # Posición inicial para peón blanco
        expected_moves = []  # No debe haber movimientos porque está bloqueado
        self.assertCountEqual(pawn.get_valid_moves(position, board), expected_moves)

    def test_pawn_capturing(self):
        # Configurar el tablero para que el peón pueda capturar
        position = (3, 3)  # Posición del peón
        pawn = Pawn("white")  # Instanciar un peón blanco
        
        # Colocar un peón blanco en la posición (3, 3)
        self.board.set_piece(3, 3, pawn)
        
        # Colocar piezas enemigas en posiciones capturables
        self.board.set_piece(2, 2, Pawn("black"))  # Peón negro en diagonal izquierda
        self.board.set_piece(2, 4, Pawn("black"))  # Peón negro en diagonal derecha
        
        # Movimientos esperados (las diagonales para capturar)
        expected_moves = [(2, 2), (2, 4)]
        
        # Llamar al método desde la **instancia** de `pawn`
        valid_moves = pawn.get_valid_moves(position, self.board.board)
        
        # Verificar que los movimientos válidos sean los esperados
        self.assertCountEqual(valid_moves, expected_moves)

if __name__ == '__main__':
    unittest.main()
