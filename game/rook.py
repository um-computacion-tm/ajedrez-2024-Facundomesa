from game.piece import Piece

class Rook(Piece):
    def possible_moves(self, position, board=None):
        row, col = position

        # Verificar si la posición está fuera del tablero
        if not (0 <= row < 8 and 0 <= col < 8):
            raise ValueError(f"Posición inválida: {position}")

        valid_moves = []

        # Movimiento hacia arriba (misma columna, filas decreciendo)
        for r in range(row - 1, -1, -1):
            if board.board[r][col] is None:
                valid_moves.append((r, col))
            elif board.board[r][col].color != self.color:
                valid_moves.append((r, col))  # Captura de una pieza del oponente
                break
            else:
                break  # Bloqueada por una pieza del mismo color

        # Movimiento hacia abajo (misma columna, filas aumentando)
        for r in range(row + 1, 8):
            if board.board[r][col] is None:
                valid_moves.append((r, col))
            elif board.board[r][col].color != self.color:
                valid_moves.append((r, col))  # Captura de una pieza del oponente
                break
            else:
                break  # Bloqueada por una pieza del mismo color

        # Movimiento hacia la izquierda (misma fila, columnas decreciendo)
        for c in range(col - 1, -1, -1):
            if board.board[row][c] is None:
                valid_moves.append((row, c))
            elif board.board[row][c].color != self.color:
                valid_moves.append((row, c))  # Captura de una pieza del oponente
                break
            else:
                break  # Bloqueada por una pieza del mismo color

        # Movimiento hacia la derecha (mismapytp fila, columnas aumentando)
        for c in range(col + 1, 8):
            if board.board[row][c] is None:
                valid_moves.append((row, c))
            elif board.board[row][c].color != self.color:
                valid_moves.append((row, c))  # Captura de una pieza del oponente
                break
            else:
                break  # Bloqueada por una pieza del mismo color

        return valid_moves

    def can_attack(self, from_pos, to_pos):
        # Solo puede atacar en la misma fila o columna
        return from_pos[0] == to_pos[0] or from_pos[1] == to_pos[1]

    def __repr__(self):
        return f"Rook({self.color})"

    def __str__(self):
        return "♖" if self.color == "WHITE" else "♜"

    def possible_positions_vd(self, row, col, increment=1):
        possibles = []
        dest = 8 if increment==1 else 1
        for r in range(row + increment, dest, increment):
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
