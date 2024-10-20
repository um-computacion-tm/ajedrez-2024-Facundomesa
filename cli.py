from chess import Chess
from exceptions import InvalidMove, OutOfBoundsError, NonNumericInputError, GameOverException, NonPieceOriginError, WrongTurnError, InvalidPieceMoveError


def play(chess_game):
    """
    Función principal que corre el juego en la terminal, permitiendo interacción con el jugador.
    """
    while True:
        try:
            # Mostrar el tablero
            render_board_with_icons(chess_game.get_board())
            print(f"Turno actual: {chess_game.turno}")

            # Solicitar las coordenadas de la jugada
            origen_fila = obtener_input("Ingrese la fila inicial (0-7): ")
            origen_columna = obtener_input("Ingrese la columna inicial (0-7): ")
            destino_fila = obtener_input("Ingrese la fila final (0-7): ")
            destino_columna = obtener_input("Ingrese la columna final (0-7): ")

            # Ejecutar el movimiento de la pieza
            chess_game.realizar_movimiento(origen_fila, origen_columna, destino_fila, destino_columna)

        except (InvalidMove, OutOfBoundsError, NonNumericInputError, InvalidPieceMoveError) as error:
            print(f"Movimiento inválido: {error}")
        
        except GameOverException as game_over:
            print(f"{game_over}")
            print("Juego terminado.")
            break  # Finalizar el juego cuando se lanza la excepción de GameOver

# Función principal para manejar la sesión interactiva del juego de ajedrez
def run_game(chess_game):
    """
    Función principal que corre el juego en la terminal, permitiendo interacción con el jugador.
    """
    while True:
        try:
            # Mostrar el tablero
            render_board_with_icons(chess_game.get_board())
            print(f"Turno actual: {chess_game.turno}")

            # Solicitar las coordenadas de la jugada
            origen_fila = obtener_input("Ingrese la fila inicial (0-7): ")
            origen_columna = obtener_input("Ingrese la columna inicial (0-7): ")
            destino_fila = obtener_input("Ingrese la fila final (0-7): ")
            destino_columna = obtener_input("Ingrese la columna final (0-7): ")

            # Ejecutar el movimiento de la pieza
            chess_game.realizar_movimiento(origen_fila, origen_columna, destino_fila, destino_columna)

        except (InvalidMove, OutOfBoundsError, NonNumericInputError, InvalidPieceMoveError) as error:
            print(f"Movimiento inválido: {error}")
        
        except GameOverException as game_over:
            print(f"{game_over}")
            print("Juego terminado.")
            break  # Finalizar el juego cuando se lanza la excepción de GameOver


# Función para manejar la entrada del usuario y validar que sea correcta
def solicitar_coordenada(mensaje):
    """
    Solicita y valida que el valor ingresado por el usuario sea una coordenada válida.
    """
    while True:
        try:
            coordenada = int(input(mensaje))
            if 0 <= coordenada < 8:  # Limitar el rango a los valores válidos del tablero de ajedrez
                return coordenada
            else:
                print("La coordenada debe estar entre 0 y 7. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número válido.")

# Función para mostrar el tablero con íconos de piezas
def render_board_with_icons(tablero):
    """
    Muestra el tablero de ajedrez con íconos en lugar de letras.
    """
    piezas_con_iconos = {
        'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟',
        'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙',
        '.': '·'  # Representación de una casilla vacía
    }
    
    # Imprimir cada fila del tablero con los íconos
    for fila in tablero:
        print(' '.join(piezas_con_iconos.get(celda, '.') for celda in fila))

def obtener_input(prompt):
    while True:
        valor = input(prompt)
        if valor.upper() == "EXIT":
            print("Juego terminado.")
            exit()  # Esto llama a exit
        if valor.isdigit() and 0 <= int(valor) < 8:
            return valor
        print("Entrada inválida. Por favor ingresa un número entre 0 y 7.")

# Punto de entrada del programa
if __name__ == "__main__":
    play()  # Llamar a la función para iniciar el juego
