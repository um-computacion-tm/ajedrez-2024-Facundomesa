from game.chess import Chess

def play(chess):
    """
    Simula una sesión de juego de ajedrez interactiva en la CLI.
    """
    while True:
        try:
            # Leer la entrada del usuario
            start_row = int(input("Ingrese la fila inicial: "))
            start_col = int(input("Ingrese la columna inicial: "))
            end_row = int(input("Ingrese la fila final: "))
            end_col = int(input("Ingrese la columna final: "))

            # Intentar realizar el movimiento
            chess.move(start_row, start_col, end_row, end_col)

            # Mostrar éxito
            print(f"Movimiento realizado de ({start_row}, {start_col}) a ({end_row}, {end_col}).")

        except ValueError as e:
            # Mostrar error si hay algún problema con el movimiento
            print(f"Error: {e}")
            break

