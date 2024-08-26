
class InvalidMove(Exception):
    """Excepción base para movimientos inválidos."""
    pass

class InvalidMoveNoPiece(InvalidMove):
    """Excepción lanzada cuando se intenta mover desde una posición sin pieza."""
    def __init__(self, position):
        super().__init__(f"No hay ninguna pieza en la posición {position}.")

class InvalidMoveRookMove(InvalidMove):
    """Excepción lanzada cuando una torre intenta realizar un movimiento inválido."""
    def __init__(self, start, end):
        super().__init__(f"Movimiento inválido para la torre desde {start} hasta {end}.")
