from game.chess import Chess
from game.exceptions import InvalidMove, OutOfBoundsError, NonNumericInputError, GameOverException, NonPieceOriginError, WrongTurnError, InvalidPieceMoveError


def start_game():
    chess_game = Chess()
    while True:
        try:
            play(chess_game)
        except GameOverException as game_end:
            print(str(game_end))
            print("Juego terminado.")
            break
        

def play(chess_game):
    """
    Función principal que corre el juego en la terminal, permitiendo interacción con el jugador.
    """
    while True:
        try:
            # Mostrar el tablero
            
            print(chess_game.get_board())
            print(f"Turno actual: {chess_game.turno}")
            print("Escribe EXIT para finalizar la partida.")

            # Solicitar las coordenadas de la jugada
            origen_fila = obtener_input("Ingrese la fila inicial (0-7): ")
            origen_columna = obtener_input("Ingrese la columna inicial (0-7): ")
            destino_fila = obtener_input("Ingrese la fila final (0-7): ")
            destino_columna = obtener_input("Ingrese la columna final (0-7): ")
            
            origen_fila, origen_columna, destino_fila, destino_columna = map(int, [origen_fila, origen_columna, destino_fila, destino_columna])

            # Ejecutar el movimiento de la pieza
            chess.move(origen_fila, origen_columna, destino_fila, destino_columna)

        except (ValueError, InvalidMove, OutOfBoundsError, NonNumericInputError, InvalidPieceMoveError) as error:
            print(f"Movimiento inválido: {error}")
        

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


def obtener_input(prompt):
    while True:
        valor = input(prompt)
        if valor.upper() == "EXIT":
            print("Juego terminado.")
            exit()  # Esto llama a exit
        if valor.isdigit() and 0 <= int(valor) < 8:
            return valor
        print("Entrada inválida. Por favor ingresa un número entre 0 y 7.")

import ipdb
# Punto de entrada del programa
if __name__ == "__main__":
    chess = Chess()
    # ipdb.set_trace()
    play(chess)  # Llamar a la función para iniciar el juego
