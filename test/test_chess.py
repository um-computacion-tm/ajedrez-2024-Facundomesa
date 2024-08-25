import unittest
from game.chess import Chess 
 

class TestChess(unittest.TestCase):
    def setUp(self):
        self.game = Chess()

    def test_initial_turn(self):
        
        self.assertEqual(self.game.turn, "WHITE")

    def test_change_turn(self):
        
        self.game.change_turn()
        self.assertEqual(self.game.turn, "BLACK")
        self.game.change_turn()
        self.assertEqual(self.game.turn, "WHITE")

    def test_move(self):
        
        try:
            self.game.move(0, 0, 1, 1)  
        except Exception as e:
            self.fail(f"move() raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
