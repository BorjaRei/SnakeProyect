import pygame
import random
import snake
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter import *
from snake import *
from ranking import Ranking
import pickle as pk

global puntuaciones
global nombre
global v
global foodType
global dificultad
v=150
nombre="Rodri"
foodType=0
dificultad="Facil"
try:
    puntuaciones = pk.load(open("rank.p", "rb"))
except (OSError, IOError) as e:
    puntuaciones = {}

print(puntuaciones)

ventana = tk.Tk()
ventana.title("Snake GAME (API)")
ventana.geometry("760x475")
ventana.iconbitmap("Resources/icono.ico")
fondo = PhotoImage(file="Resources/wall.gif")
fondo1 = Label(ventana, image=fondo).place(x=0, y=0)
menuBar = Menu(ventana)
ventana.config(menu=menuBar)

TamanoTablero = Menu(menuBar, tearoff=0)
ColorSerpiente = Menu(menuBar, tearoff=0)
ColorTablero = Menu(menuBar, tearoff=0)
VelSerpiente = Menu(menuBar, tearoff=0)
Bordes = Menu(menuBar, tearoff=0)

dificultad="Facil"

Ranking = Menu(menuBar, tearoff=0)

# Colores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(35, 155, 86)
blue = pygame.Color(0, 0, 255)

# Menu de opciones


# Tamano del tablero
s1 = 30
s2 = 20

menuBar.add_cascade(label="Dificultad", menu=TamanoTablero)

label=Label(ventana, text="HOLA")
label.pack
Label(ventana, text=dificultad).pack()
Label(ventana, text="¡Otra etiqueta!").pack()
Label(ventana, text="¡Última etiqueta!").pack()

def dificil():
    global dificultad
    dificultad="Dificil"
    v = 590
    foodType=1

    Label(ventana, text=dificultad).pack()


TamanoTablero.add_command(label="Dificil", command=dificil)


def medio():
    global dificultad
    dificultad = "Medio"
    v = 350
    foodType = 0


TamanoTablero.add_command(label="Medio", command=medio)


def facil():

    global dificultad
    dificultad = "Facil"
    v = 150
    foodType = 1


TamanoTablero.add_command(label="Facil", command=facil)

# Color de la serpiente
cs = green
menuBar.add_cascade(label="Color de la serpiente", menu=ColorSerpiente)


def rojo():
    global cs
    cs = red


ColorSerpiente.add_command(label="Rojo", command=rojo)


def azul():
    global cs
    cs = blue


ColorSerpiente.add_command(label="Azul", command=azul)


def verde():
    global cs
    cs = green


ColorSerpiente.add_command(label="Verde", command=verde)

# Color del tablero
t = black
menuBar.add_cascade(label="Color del tablero", menu=ColorTablero)


def oscuro():
    global t
    t = black



ColorTablero.add_command(label="Oscuro", command=oscuro)


def claro():
    global t
    t = white



ColorTablero.add_command(label="Claro", command=claro)

# Velocidad


# Bordes
b = False
menuBar.add_cascade(label="Bordes", menu=Bordes)


def bordesSi():
    global b
    b = True


Bordes.add_command(label="Si", command=bordesSi)


def bordesNo():
    global b
    b = False


Bordes.add_command(label="No", command=bordesNo)


#################
def jugar():
    ranking()
    be = Board(s1, s2, v, t, cs, b, foodType)
    score=be.play()
    print("score")
    newScore={str(nombre):[score,dificultad]}
    puntuaciones.update(newScore)
    pk.dump(puntuaciones, open("rank.p", "wb"))
    print(puntuaciones)
    pygame.quit()

def nada():
    return True

def ranking():
    rank = Ranking()
    rank.showRanking()


button = tk.Button(master=ventana, text='Jugar', command=jugar, height=3, width=15)
button.pack()
button.place(relx=0.5, rely=0.5, anchor=CENTER)



dif = tk.Button(master=ventana, text="JAIDJias", command=nada, height=6, width=15)
dif.pack()
dif.place(relx=1.5, rely=7.5, anchor=CENTER)

# be.play()
ventana.update()
ventana.mainloop()

# while ventana.mainloop():
# for event in pygame.event.get():

# if event.type == pygame.QUIT:
# pygame.quit()
# sys.exit()
# if event.type == pygame.key.get_pressed():
#   be = Board(s1,s2,v,t,cs,b,0)
#  be.play()

# Por defecto
# be = Board(30, 20, 70, black, green, False, 0)
# be = Board(s1,s2,v,t,cs,b,0)
# be.play()
# pygame.quit()
# Board(size,dotSize, speed, backColour, snakeColour,borders,foodType)
# Size(int)=: proporcion del tablero (el tamaño real sera size*dotSize)
# dotSize(int): tamaño de la serpiente y la comida
# Speed(int): velocidad de refresco del juego, cuanto mas pequeño mas rapido
# backColour(int,int,int)=: rgb con el color del tablero
# snakeColour(int. int,int): rgb con el color de la serpiente
# borders(bool): booleano para indicar si los bordes matan a la serpiente o reaparece en el otro extremo
# foodType(int): elegir el modo de puntucion (0=> 1 punto por comida, 1=> 1 punto por manzana y puntos extra por comida especial)





