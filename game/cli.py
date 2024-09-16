

def play(chess):
    """Función que controla el flujo del juego de ajedrez."""
    while True:
        chess.display_turn()

        try:
            # Simular input del usuario para los movimientos
            start = input("Introduce la posición inicial (ej. 1,1): ")
            end = input("Introduce la posición final (ej. 2,2): ")

            chess.move(start, end)  # Realizar el movimiento
            
            chess.switch_turn()  # Cambiar de turno después de un movimiento exitoso
        except InvalidMove as e:
            print(f"Error: {e}")
        except ValueError:
            print("Entrada inválida. Por favor, introduce las coordenadas en el formato correcto.")
