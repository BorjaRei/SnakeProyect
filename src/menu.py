import pygame
import random
import snake
import tkinter
from tkinter import messagebox
from Resources import *
from tkinter.filedialog import askopenfilename
from tkinter import *

ventana = Tk()
ventana.title("Snake GAME (API)")
ventana.geometry("760x475")
ventana.iconbitmap("Resources/icono.ico")
fondo = PhotoImage(file="Resources/wall.gif")
fondo1 = Label(ventana, image=fondo).place(x=0, y=0)
menu = Menu(ventana)
ventana.config(menu=menu)

TamanoTablero = Menu(menu, tearoff=0)
ColorSerpiente = Menu(menu, tearoff=0)
ColorTablero = Menu(menu, tearoff=0)
VelSerpiente = Menu(menu, tearoff=0)
Bordes = Menu(menu, tearoff=0)

Ranking = Menu(menu, tearoff=0)

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
menu.add_cascade(label="Tamaño del tablero", menu=TamanoTablero)
def grande():
    s1 = 60
    s2 = 40
TamanoTablero.add_command(label="Grande", command=grande())
def mediano():
    s1 = 30
    s2 = 20
TamanoTablero.add_command(label="Mediano", command=mediano())
def pequeno():
    s1 = 15
    s2 = 10
TamanoTablero.add_command(label="Pequeño", command=pequeno())

# Color de la serpiente
cs = red
menu.add_cascade(label="Color de la serpiente", menu=ColorSerpiente)
def rojo():
    cs = red
ColorSerpiente.add_command(label="Rojo", command=rojo())
def verde():
    cs = green
ColorSerpiente.add_command(label="Verde", command=verde())
def azul():
    cs = blue
ColorSerpiente.add_command(label="Azul", command=azul())

# Color del tablero
t = black
menu.add_cascade(label="Color del tablero", menu=ColorTablero)
def oscuro():
    t = black
ColorTablero.add_command(label="Oscuro", command=oscuro())
def claro():
    t = white
ColorTablero.add_command(label="Claro", command=claro())

# Velocidad
v = 70
menu.add_cascade(label="Velocidad", menu=VelSerpiente)
def normal():
    v = 70
VelSerpiente.add_command(label="Normal", command=normal())
def rapido():
    v = 120
VelSerpiente.add_command(label="Rapido", command=rapido())

# Bordes
b = False
menu.add_cascade(label="Bordes", menu=Bordes)
def bordesSi():
    b = True
Bordes.add_command(label="Si", command=bordesSi())
def bordesNo():
    b = False
Bordes.add_command(label="No", command=bordesNo())

# Ranking
menu.add_cascade(label="Ranking", menu=Ranking)
ventana.mainloop()



