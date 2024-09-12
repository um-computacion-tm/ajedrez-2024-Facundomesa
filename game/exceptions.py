
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
    
class InvalidMoveOutOfBounds(InvalidMove):
    """Excepción lanzada cuando una pieza intenta moverse fuera del tablero."""
    def __init__(self, position):
        super().__init__(f"La posición {position} está fuera de los límites del tablero.")

class InvalidMoveBlockedPath(InvalidMove):
    """Excepción lanzada cuando una pieza intenta moverse a través de otras piezas."""
    def __init__(self, start, end):
        super().__init__(f"El camino de {start} a {end} está bloqueado por otra pieza.")

class InvalidMoveCheck(InvalidMove):
    """Excepción lanzada cuando el movimiento deja al rey en jaque."""
    def __init__(self):
        super().__init__("El movimiento deja al rey en jaque.")
        
class InvalidMoveKingMove(InvalidMove):
    """Excepción lanzada cuando el rey intenta realizar un movimiento inválido."""
    def __init__(self, start, end):
        super().__init__(f"Movimiento inválido para el rey desde {start} hasta {end}.")


