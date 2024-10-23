# Ajedrez
Facundo Mesa

## Introduccion
Este proyecto es un juego de ajedrez hecho en Python utilizando un enfoque orientado a objetos. El juego permite a dos jugadores enfrentarse, respetando parte las reglas estándar de los movimientos del ajedrez tradicional.
Cada jugador alterna turnos para mover una pieza por turno de acuerdo a las siguientes reglas de movimiento:

    Rey: Se mueve exactamente una casilla en cualquier dirección: horizontal, vertical o diagonal. Movimiento especial: Enroque (el rey se mueve dos casillas hacia una torre, y la torre se mueve a la casilla adyacente al rey).

    Reina: Se mueve cualquier número de casillas en cualquier dirección: horizontal, vertical o diagonal.

    Torre: Se mueve cualquier número de casillas en dirección horizontal o vertical. No puede saltar sobre otras piezas. Movimiento especial: Enroque (involucra al rey).

    Alfil: Se mueve cualquier número de casillas en dirección diagonal. No puede saltar sobre otras piezas.

    Caballo: Se mueve en forma de "L": dos casillas en una dirección y luego una casilla perpendicular, o una casilla en una dirección y dos casillas perpendiculares. Los caballos pueden saltar sobre otras piezas.

    Peón: Se mueve hacia adelante una casilla. En su primer movimiento, un peón puede avanzar dos casillas. Los peones capturan en diagonal. Movimientos especiales: En passant (un peón puede capturar a otro peón enemigo que haya avanzado dos casillas en su primer movimiento, como si hubiera avanzado solo una) y promoción (cuando un peón alcanza la última fila del oponente, puede ser promovido a cualquier otra pieza, usualmente una reina).

## Reglas 
El juego no cuenta con jaque, jaque mate, tablas, ni jugadas por tiempo. El juego se ejecuta en la consola con un tablero mostrado en la terminal de vscode

## Requisitos 
Se necesita [Docker](https://www.docker.com/)

## Pasos a seguir

```bash
sudo apt install docker
```
clonar el [reposotorio] (https://github.com/um-computacion-tm/ajedrez-2024-Facundomesa.git)

```bash
git clone https://github.com/um-computacion-tm/ajedrez-2024-Facundomesa.git

```bash
 source ent/bin/activate
```
activar el entorno virtual

```bash
pip install -r requirements.txt 
```
## Jugar

Crear una image Docker del juego
```bash
docker buildx build -t ajedrez-2024-Facundomesa .
```
Jugar y correr los test
```bash
docker run -i ajedrez-2024-Facundomesa

# Circleci
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-Facundomesa/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-Facundomesa/tree/main)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/f27f1f51ededdf0fa6ad/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Facundomesa/maintainability)

# Test coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/f27f1f51ededdf0fa6ad/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Facundomesa/test_coverage)

