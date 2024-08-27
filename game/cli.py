from game.chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        # Mostrar el tablero actual (asumiendo que Chess tiene un método show_board)
        # print(chess.show_board())
        
        print(f"Turn: {chess.turn}")
        
        from_row, from_col, to_row, to_col = get_move_input()

        chess.move(from_row, from_col, to_row, to_col)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def get_move_input():
    """
    Solicita al usuario las coordenadas de la pieza a mover y su destino.
    Devuelve las coordenadas como una tupla de enteros.
    """
    try:
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))
        return from_row, from_col, to_row, to_col
    except ValueError:
        raise ValueError("Las coordenadas deben ser números enteros.")

if __name__ == "__main__":
    main()




if __name__ == '__main__':
    main()