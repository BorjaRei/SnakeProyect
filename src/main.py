import pygame
import random
import  snake
from snake import *


if __name__ == '__main__':
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color( 35, 155, 86 )
    blue = pygame.Color(0, 0, 255)

    be=Board(30, 20,70,black,green,False,0)
    #Board(size,dotSize, speed, backColour, snakeColour,borders,foodType)
    #Size(int)=: proporcion del tablero (el tamaño real sera size*dotSize)
    #dotSize(int): tamaño de la serpiente y la comida
    #Speed(int): velocidad de refresco del juego, cuanto mas pequeño mas rapido
    #backColour(int,int,int)=: rgb con el color del tablero
    #snakeColour(int. int,int): rgb con el color de la serpiente
    #borders(bool): booleano para indicar si los bordes matan a la serpiente o reaparece en el otro extremo
    #foodType(int): elegir el modo de puntucion (0=> 1 punto por comida, 1=> 1 punto por manzana y puntos extra por comida especial)
    be.play()
    pygame.quit()

#MATRIZ SIZE
#SNAKE COLOUR
#SNAKE SPEED
#SCORE MODE
#BORDERS
