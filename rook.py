class Rook:
    
    def __init__(self, position):
        self.position = position

    def move(self, new_position):
        self.position = new_position

    VALID_COLORS = {"WHITE", "BLACK"}

    def __init__(self, color, board=None):
        if color.upper() not in Rook.VALID_COLORS:
            raise ValueError(f"Color inválido: {color}")
        self.color = color.upper()
        self.board = board

    def valid_moves(self, position):
        row, col = position
        if not (0 <= row < 8 and 0 <= col < 8):
            raise ValueError("Posición fuera del tablero")
        
        moves = []

        # Movimientos verticales y horizontales
        for i in range(8):
            if i != row:
                moves.append((i, col))  # Movimiento vertical
            if i != col:
                moves.append((row, i))  # Movimiento horizontal

        return moves

    def can_attack(self, from_pos, to_pos):
        # Solo puede atacar en la misma fila o columna
        return from_pos[0] == to_pos[0] or from_pos[1] == to_pos[1]

    def __repr__(self):
        return f"Rook({self.color})"

    def __str__(self):
        return "♖" if self.color == "WHITE" else "♜"

    def possible_positions_vd(self, row, col):
        possibles = []
        for r in range(row + 1, 8):
            if self.board.get_piece(r, col):
                if self.board.get_piece(r, col).color != self.color:
                    possibles.append((r, col))  # Puede capturar pieza enemiga
                break
            possibles.append((r, col))  # Casilla vacía
        return possibles

    def possible_positions_va(self, row, col):
        possibles = []
        for r in range(row - 1, -1, -1):
            if self.board.get_piece(r, col):
                if self.board.get_piece(r, col).color != self.color:
                    possibles.append((r, col))  # Puede capturar pieza enemiga
                break
            possibles.append((r, col))  # Casilla vacía
        return possibles
