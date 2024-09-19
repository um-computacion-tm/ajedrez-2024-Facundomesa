from game.chess import Chess


class Chess:
    def __init__(self):
        self.turn = "WHITE"
    
    def show_board(self):
        return "Tablero actual"

    def move(self, from_row, from_col, to_row, to_col):
        # Simulación de un movimiento de ajedrez válido
        pass


def play(chess):
    try:
        # Mostrar el tablero actual
        print(chess.show_board())
        print(f"Turno actual: {chess.turn}")
        
        from_row, from_col, to_row, to_col = get_move_input()

        chess.move(from_row, from_col, to_row, to_col)
        print(f"Movimiento exitoso de {from_row},{from_col} a {to_row},{to_col}")

    except ValueError as e:
        print(f"Error: {e}")


def get_move_input():
    try:
        from_row = input("Fila de origen: ")
        from_col = input("Columna de origen: ")
        to_row = input("Fila de destino: ")
        to_col = input("Columna de destino: ")

        # Convertir las entradas a enteros
        return int(from_row), int(from_col), int(to_row), int(to_col)
    
    except ValueError:
        raise ValueError("Las coordenadas deben ser números enteros.")


if __name__ == "__main__":
    chess = Chess()
    play(chess)

