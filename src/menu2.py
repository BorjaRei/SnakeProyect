import PySimpleGUI as interf
import pandas as pd
import pickle as pk
from snake import *
from ranking import Ranking

class Menu:
    def __init__(self):
        self.dificulty = "Medio"
        self.name = ""

    def showMenu(self):
        dif = "Dificultad Actual: " + self.dificulty
        layout = [[interf.Text("Menú Principal:")], [interf.Text("Escribe tu nombre:")], [interf.Multiline(size=(25, 1), key='textbox')], [interf.Text(dif)], [interf.Button("Jugar"), interf.Button("Dificultad"),
                      interf.Button("Ranking")]]
        window = interf.Window("Snake", layout, margins=(100, 50))

        cond = True
        while cond:
            event, values = window.read()
            if event == interf.WIN_CLOSED:
                window.close()
                cond = False
            elif event == "Jugar":
                black = pygame.Color(0, 0, 0)
                green = pygame.Color(35, 155, 86)
                self.name = values['textbox']
                speed = 70
                if self.dificulty == "Fácil":
                    speed = 110
                elif self.dificulty == "Medio":
                    speed = 70
                elif self.dificulty == "Difícil":
                    speed = 30
                be = Board(30, 20, speed, black, green, False, 0)
                be.play()
            elif event == "Dificultad":
                layout = [[interf.Text("Selecciona Dificultad:")],
                          [interf.Button("Fácil"), interf.Button("Medio"),
                           interf.Button("Difícil")]]
                window.close()
                window = interf.Window("Dificultad", layout, margins=(100, 50))
                event, values = window.read()
                if event == "Fácil":
                    self.dificulty = "Fácil"
                elif event == "Medio":
                    self.dificulty = "Medio"
                elif event == "Difícil":
                    self.dificulty = "Difícil"
                dif = "Dificultad Actual: " + self.dificulty
                layout = [[interf.Text("Menú Principal:")], [interf.Text("Escribe tu nombre:")],
                            [interf.Multiline(size=(25, 1), key='textbox')], [interf.Text(dif)],
                            [interf.Button("Jugar"), interf.Button("Dificultad"),
                            interf.Button("Ranking")]]
                window.close()
                window = interf.Window("Snake", layout, margins=(100, 50))
            elif event == "Ranking":
                window.close()
                #puntuaciones = {"Easy": [0, "Fácil"], "Medium": [0, "Medio"], "Snake": [69, "Medio"], "Hard": [0, "Difícil"]}
                #pk.dump(puntuaciones, open("rank.p", "wb"))
                rank = Ranking()
                rank.showRanking()
                dif = "Dificultad Actual: " + self.dificulty
                layout = [[interf.Text("Menú Principal:")], [interf.Text("Escribe tu nombre:")],
                          [interf.Multiline(size=(25, 1), key='textbox')], [interf.Text(dif)],
                          [interf.Button("Jugar"), interf.Button("Dificultad"),
                           interf.Button("Ranking")]]
                window = interf.Window("Snake", layout, margins=(100, 50))

if __name__ == '__main__':
    menu = Menu()
    menu.showMenu()