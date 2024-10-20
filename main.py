from chess import Chess
from cli import play

def main():
    ajedrez = Chess()  # Crear la instancia del juego
    play(ajedrez)      # Pasar el objeto del juego a la función play

if __name__ == "__main__":
    main()

