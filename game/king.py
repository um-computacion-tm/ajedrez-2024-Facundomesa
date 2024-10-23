from game.piece import Piece

class King(Piece):
    def __str__(self):
        return "♔" if self.color == "WHITE" else "♚"
    
    def possible_moves(self, from_row, from_col):
        # Usa las mismas direcciones que la reina pero con un solo paso
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        return super().possible_moves_general(from_row, from_col, directions, un_paso=True)