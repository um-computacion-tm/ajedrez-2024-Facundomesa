from exceptions import GameOverException, NonCaptureOwnPieceError, NonPassOverPieceError, NonCaptureForwardError, NonPieceOriginError

class Board:
    def __init__(self, forTest=False):
        # Inicializa el tablero con piezas en sus posiciones iniciales o vacío para pruebas
        self.board = [[None] * 8 for _ in range(8)]
        if not forTest:
            self._iniciar_posiciones_iniciales()

    def _iniciar_posiciones_iniciales(self):
        # Importación diferida de las piezas para evitar dependencia circular
        from rook import Rook
        from pawn import Pawn
        from king import King
        from queen import Queen
        from bishop import Bishop
        from knight import Knight

        # Coloca las piezas en sus posiciones iniciales
        self.board[0][0] = Rook("BLACK")
        self.board[0][7] = Rook("BLACK")
        self.board[7][0] = Rook("WHITE")
        self.board[7][7] = Rook("WHITE")

        # Colocar peones
        for i in range(8):
            self.board[1][i] = Pawn("BLACK")
            self.board[6][i] = Pawn("WHITE")

        # Colocar caballos, alfiles, reinas y reyes
        self.board[0][1] = Knight("BLACK")
        self.board[0][6] = Knight("BLACK")
        self.board[7][1] = Knight("WHITE")
        self.board[7][6] = Knight("WHITE")

        self.board[0][2] = Bishop("BLACK")
        self.board[0][5] = Bishop("BLACK")
        self.board[7][2] = Bishop("WHITE")
        self.board[7][5] = Bishop("WHITE")

        self.board[0][3] = Queen("BLACK")
        self.board[7][3] = Queen("WHITE")

        self.board[0][4] = King("BLACK")
        self.board[7][4] = King("WHITE")

    def get_piece(self, row, col):
        # Obtiene la pieza en la posición especificada
        if not self.is_within_bounds(row, col):
            raise IndexError("Posición fuera del tablero.")
        return self.board[row][col]

    def set_piece(self, row, col, piece):
        # Coloca una pieza en la posición especificada
        if not self.is_within_bounds(row, col):
            raise IndexError("Posición fuera del tablero.")
        self.board[row][col] = piece

    def is_within_bounds(self, row, col):
        # Verifica si una posición está dentro de los límites del tablero
        return 0 <= row < 8 and 0 <= col < 8

    def move_piece(self, from_row, from_col, to_row, to_col):
        # Realiza el movimiento de una pieza en el tablero
        piece = self.get_piece(from_row, from_col)
        target_piece = self.get_piece(to_row, to_col)

        if not piece:
            raise NonPieceOriginError(f"No hay ninguna pieza en la posición ({from_row}, {from_col}).")

        # Verifica si está intentando capturar una pieza del mismo color
        if target_piece and piece.get_color() == target_piece.get_color():
            raise NonCaptureOwnPieceError("No puedes capturar tus propias piezas.")

        # Verifica si puede moverse a la posición especificada
        if not self.is_valid_move(from_row, from_col, to_row, to_col):
            raise NonPassOverPieceError("Movimiento inválido o bloqueado por otra pieza.")

        # Verifica reglas especiales para peones
        if isinstance(piece, Pawn):
            if not self._es_movimiento_valido_peon(from_row, from_col, to_row, to_col, target_piece):
                raise NonCaptureForwardError("Un peón no puede capturar hacia adelante.")

        self._realizar_movimiento(from_row, from_col, to_row, to_col)
        self._verificar_fin_partida()

    def is_valid_move(self, from_row, from_col, to_row, to_col):
        # Verifica si el movimiento es válido para la pieza dada
        piece = self.get_piece(from_row, from_col)
        if not piece:
            return False
        posibles_movimientos = piece.possible_moves(from_row, from_col)
        return (to_row, to_col) in posibles_movimientos

    def _es_movimiento_valido_peon(self, from_row, from_col, to_row, to_col, target_piece):
        # Valida las reglas para el movimiento de un peón
        direccion = 1 if self.board[from_row][from_col].get_color() == 'BLACK' else -1
        return not (to_row == from_row + direccion and target_piece is not None and from_col == to_col)

    def _realizar_movimiento(self, from_row, from_col, to_row, to_col):
        # Realiza el movimiento de la pieza
        self.board[to_row][to_col] = self.board[from_row][from_col]
        self.board[from_row][from_col] = None

    def _verificar_fin_partida(self):
        # Verifica si uno de los jugadores ha ganado
        piezas_blancas, piezas_negras = 0, 0
        for fila in self.board:
            for pieza in fila:
                if pieza:
                    if pieza.get_color() == 'WHITE':
                        piezas_blancas += 1
                    elif pieza.get_color() == 'BLACK':
                        piezas_negras += 1

        if piezas_negras == 0:
            raise GameOverException("White wins")
        elif piezas_blancas == 0:
            raise GameOverException("Black wins")

    def get_board_state(self):
        # Devuelve una representación del estado del tablero
        board_repr = []
        for row in self.board:
            row_repr = [str(piece) if piece else '.' for piece in row]
            board_repr.append(row_repr)
        return board_repr
