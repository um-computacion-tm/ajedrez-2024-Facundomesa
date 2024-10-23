import unittest
from game.king import King

class King:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{self.color} King"
    
    def test_movimientos_rey_blanco(self):
        rey = King('WHITE')
        fila, columna = 4, 4
        movimientos_esperados = [(5, 4), (4, 5), (3, 4), (4, 3), (5, 5), (3, 5), (5, 3), (3, 3)]
        movimientos = rey.possible_moves(fila, columna)
        self.assertCountEqual(movimientos, movimientos_esperados)

# Comprueba que el rey negro, situado en la misma posición central, pueda realizar los movimientos correctos.

    def test_movimientos_rey_negro(self):
        rey = King('BLACK')
        fila, columna = 4, 4
        movimientos_esperados = [(5, 4), (4, 5), (3, 4), (4, 3), (5, 5), (3, 5), (5, 3), (3, 3)]
        movimientos = rey.possible_moves(fila, columna)
        self.assertCountEqual(movimientos, movimientos_esperados)

if __name__ == '__main__':
    unittest.main()
