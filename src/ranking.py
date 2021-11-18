import PySimpleGUI as interf
import pandas as pd
import pickle as pk

class Ranking:
    def __init__(self):
        try:
            self.gameLog = pk.load(open("rank.p", "rb"))
        except (OSError, IOError) as e:
            self.gameLog = {}

    def getEasyRank(self):
        nuevoRank = {}
        for key in self.gameLog.keys():
            if self.gameLog[key][1] == "Fácil":
                nuevoRank[key] = [self.gameLog[key][0], self.gameLog[key][1]]
        return nuevoRank

    def getMediumRank(self):
        nuevoRank = {}
        for key in self.gameLog.keys():
            if self.gameLog[key][1] == "Medio":
                nuevoRank[key] = [self.gameLog[key][0], self.gameLog[key][1]]
        return nuevoRank

    def getHardRank(self):
        nuevoRank = {}
        for key in self.gameLog.keys():
            if self.gameLog[key][1] == "Difícil":
                nuevoRank[key] = [self.gameLog[key][0], self.gameLog[key][1]]
        return nuevoRank

    def showRanking(self):
        if self.gameLog != {}:
            indices = self.gameLog.keys()
            puntos = pd.Series(self.gameLog.values())
            puntos.index = indices
            layout = [[interf.Text("Ranking de Puntuaciones:")], [interf.Text("Nombre  [Puntos, Dificultad]")],
                      [interf.Text(puntos.to_string())], [interf.Button("Fácil"), interf.Button("Medio"),
                      interf.Button("Difícil"), interf.Button("Todas"), interf.Button("Volver")]]
        else:
            layout = [[interf.Text("Ranking de Puntuaciones:")], [interf.Text("Nombre  [Puntos, Dificultad]")],
                      [interf.Text("")], [interf.Button("Fácil"), interf.Button("Medio"),
                      interf.Button("Difícil"), interf.Button("Todas"), interf.Button("Volver")]]
        window = interf.Window("Ranking", layout, margins=(100, 50))

        cond = True
        while cond:
            event, values = window.read()
            # End program if user closes window or
            # presses the OK button
            if event == "Volver" or event == interf.WIN_CLOSED:
                window.close()
                cond = False
            elif event == "Fácil":
                nuevoRank = self.getEasyRank()
                if nuevoRank != {}:
                    indices = nuevoRank.keys()
                    puntos = pd.Series(nuevoRank.values())
                    puntos.index = indices

                    layout = [[interf.Text("Ranking de Puntuaciones:")], [interf.Text("Nombre  [Puntos, Dificultad]")],
                              [interf.Text(puntos.to_string())], [interf.Button("Fácil"), interf.Button("Medio"),
                      interf.Button("Difícil"), interf.Button("Todas"), interf.Button("Volver")]]
                else:
                    layout = [[interf.Text("Ranking de Puntuaciones:")], [interf.Text("Nombre  [Puntos, Dificultad]")],
                              [interf.Text("")], [interf.Button("Fácil"), interf.Button("Medio"),
                      interf.Button("Difícil"), interf.Button("Todas"), interf.Button("Volver")]]
                window.close()
                window = interf.Window("Ranking", layout, margins=(100, 50))
            elif event == "Medio":
                nuevoRank = self.getMediumRank()
                if nuevoRank != {}:
                    indices = nuevoRank.keys()
                    puntos = pd.Series(nuevoRank.values())
                    puntos.index = indices

                    layout = [[interf.Text("Ranking de Puntuaciones:")], [interf.Text("Nombre  [Puntos, Dificultad]")],
                              [interf.Text(puntos.to_string())], [interf.Button("Fácil"), interf.Button("Medio"),
                      interf.Button("Difícil"), interf.Button("Todas"), interf.Button("Volver")]]
                else:
                    layout = [[interf.Text("Ranking de Puntuaciones:")], [interf.Text("Nombre  [Puntos, Dificultad]")],
                              [interf.Text("")], [interf.Button("Fácil"), interf.Button("Medio"),
                      interf.Button("Difícil"), interf.Button("Todas"), interf.Button("Volver")]]
                window.close()
                window = interf.Window("Ranking", layout, margins=(100, 50))
            elif event == "Difícil":
                nuevoRank = self.getHardRank()
                if nuevoRank != {}:
                    indices = nuevoRank.keys()
                    puntos = pd.Series(nuevoRank.values())
                    puntos.index = indices

                    layout = [[interf.Text("Ranking de Puntuaciones:")], [interf.Text("Nombre  [Puntos, Dificultad]")],
                              [interf.Text(puntos.to_string())], [interf.Button("Fácil"), interf.Button("Medio"),
                      interf.Button("Difícil"), interf.Button("Todas"), interf.Button("Volver")]]
                else:
                    layout = [[interf.Text("Ranking de Puntuaciones:")], [interf.Text("Nombre  [Puntos, Dificultad]")],
                              [interf.Text("")], [interf.Button("Fácil"), interf.Button("Medio"),
                      interf.Button("Difícil"), interf.Button("Todas"), interf.Button("Volver")]]
                window.close()
                window = interf.Window("Ranking", layout, margins=(100, 50))
            elif event == "Todas":
                if self.gameLog != {}:
                    indices = self.gameLog.keys()
                    puntos = pd.Series(self.gameLog.values())
                    puntos.index = indices
                    layout = [[interf.Text("Ranking de Puntuaciones:")], [interf.Text("Nombre  [Puntos, Dificultad]")],
                              [interf.Text(puntos.to_string())], [interf.Button("Fácil"), interf.Button("Medio"),
                      interf.Button("Difícil"), interf.Button("Todas"), interf.Button("Volver")]]
                else:
                    layout = [[interf.Text("Ranking de Puntuaciones:")], [interf.Text("Nombre  [Puntos, Dificultad]")],
                              [interf.Text("")], [interf.Button("Fácil"), interf.Button("Medio"),
                      interf.Button("Difícil"), interf.Button("Todas"), interf.Button("Volver")]]
                window.close()
                window = interf.Window("Ranking", layout, margins=(100, 50))


if __name__ == '__main__':
    puntuaciones = {"lion": [25, "Fácil"], "kitty": [17, "Medio"], "snake": [69, "Medio"]}
    pk.dump(puntuaciones, open("rank.p", "wb"))
    rank = Ranking()
    rank.showRanking()