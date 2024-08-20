from chess import Chess

def main():
    chess = Chess()  # Inicializa el tablero de ajedrez
    while True:
        play(chess)

def play(chess):
    try:
        # Muestra el tablero y el turno actual
        print(chess.show_board())
        print("Turno: ", chess.turn)
        
        # Solicita las coordenadas de la pieza a mover
        from_row = int(input("Desde la fila: "))
        from_col = int(input("Desde la columna: "))
        to_row = int(input("Hacia la fila: "))
        to_col = int(input("Hacia la columna: "))
        
        # Realiza el movimiento
        chess.move(from_row, from_col, to_row, to_col)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
