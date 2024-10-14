class Rook:
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

        # Movimientos verticales descendentes
        moves += self.possible_positions_vd(row, col)
        
        # Movimientos verticales ascendentes
        moves += self.possible_positions_va(row, col)
        
        # Movimientos horizontales a la derecha
        moves += self.possible_positions_hr(row, col)
        
        # Movimientos horizontales a la izquierda
        moves += self.possible_positions_hl(row, col)

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
            piece = self.board.get_piece(r, col)
            if piece:
                if piece.color != self.color:
                    possibles.append((r, col))  # Puede capturar pieza enemiga
                break
            possibles.append((r, col))  # Casilla vacía
        return possibles

    def possible_positions_va(self, row, col):
        possibles = []
        for r in range(row - 1, -1, -1):
            piece = self.board.get_piece(r, col)
            if piece:
                if piece.color != self.color:
                    possibles.append((r, col))  # Puede capturar pieza enemiga
                break
            possibles.append((r, col))  # Casilla vacía
        return possibles

    def possible_positions_hr(self, row, col):
        """ Movimientos horizontales a la derecha (col++) """
        possibles = []
        for c in range(col + 1, 8):
            piece = self.board.get_piece(row, c)
            if piece:
                if piece.color != self.color:
                    possibles.append((row, c))  # Puede capturar pieza enemiga
                break
            possibles.append((row, c))  # Casilla vacía
        return possibles

    def possible_positions_hl(self, row, col):
        """ Movimientos horizontales a la izquierda (col--) """
        possibles = []
        for c in range(col - 1, -1, -1):
            piece = self.board.get_piece(row, c)
            if piece:
                if piece.color != self.color:
                    possibles.append((row, c))  # Puede capturar pieza enemiga
                break
            possibles.append((row, c))  # Casilla vacía
        return possibles
