###########################################
# Autor: Valentin Jacquin
###########################################
from tabnanny import check
import tkinter as tk
import random as rdm

from pyparsing import col

fenetre = tk.Tk()
fenetre.title("Ecoulement sable")
cWidth, cHeight, dataSand, guiSand = 500, 500, [], []
cTableau = tk.Canvas(width=cWidth, height=cHeight, bg="white")
cTableau.grid(column=2, row=0, rowspan=10)
dataSand, nbrValeur, valeurMaxCase, checkPause = [], 48, 3, False
colorAssignement = ["#FFFFFF", "#707070", "#606060", "#505050", "#404040", "#303030", "#2020200", "#101010", "#000000"]


def clearTableau():
    global guiSand
    for i in range(0, len(guiSand)):
        for j in range(0, len(guiSand[i])):
            cTableau.delete(guiSand[i][j])
    guiSand = []


def diezFormation():
    global dataSand, guiSand, nbrValeur
    x = 20
    y = 10
    sousListGuiSand = []
    clearTableau()
    for j in range(0, 2):
        for i in range(0, nbrValeur - 1):
            diez = cTableau.create_text(x, y, text="#")
            x += 10
            sousListGuiSand.append(diez)
        y = 490
        x = 20
        guiSand.append(sousListGuiSand)
        sousListGuiSand = []
    x = 10
    y = 20
    for j in range(0, 2):
        for i in range(0, nbrValeur - 1):
            diez = cTableau.create_text(x, y, text="#")
            y += 10
            sousListGuiSand.append(diez)
        x = 490
        y = 20
        guiSand.append(sousListGuiSand)
        sousListGuiSand = []


def initialisation():
    global dataSand, guiSand, nbrValeur
    sousListGuiSand = []
    diezFormation()
    y = 20
    for i in range(0, nbrValeur - 1):
        x = 10
        for j in range(0, nbrValeur - 1):
            x += 10
            text = cTableau.create_rectangle((x - 5, y - 5), (x + 5, y + 5), fill="White")
            sousListGuiSand.append(text)
        guiSand.append(sousListGuiSand)
        y += 10


def showSand():
    global dataSand, guiSand, colorAssignement
    sousListeGuiSand = []
    clearTableau()
    y = 20
    diezFormation()
    for i in range(0, len(dataSand) - 1):
        x = 10
        for j in range(0, len(dataSand[i]) - 1):
            x += 10
            text = cTableau.create_rectangle((x - 5, y - 5), (x + 5, y + 5), fill=colorAssignement[dataSand[i][j]])
            sousListeGuiSand.append(text)
        guiSand.append(sousListeGuiSand)
        y += 10


def randomGeneration():
    global dataSand, nbrValeur, valeurMaxCase
    dataSand = []
    for i in range(0, nbrValeur):
        sousListdataSand = []
        for j in range(0, nbrValeur):
            bloc = rdm.randint(0, valeurMaxCase)
            sousListdataSand.append(bloc)
        dataSand.append(sousListdataSand)
    showSand()
    return


def add():
    global dataSand, configDataSand
    configDataSand = []
    assert len(dataSand) == len(configDataSand), "Les deux configuration ne sont pas au même format"
    for i in range(0, len(dataSand) - 1):
        assert len(dataSand[i]) == len(configDataSand[i]), "Les deux configuration ne sont pas au même format"
        for j in range(0, len(dataSand[i]) - 1):
            dataSand[i][j] += configDataSand[i][j]
    showSand()
    return


def soustraction():
    return


def automate():
    global checkPause, guiSand, dataSand
    assert checkPause is False, "L'automate est en pause."


def pause():
    global checkPause
    if checkPause is True:
        checkPause = False
        bPauseAutomate['text'] = "Pause Automate"
    else:
        checkPause = True
        bPauseAutomate['text'] = "Redémarrer Automate"
    return


bRandom = tk.Button(bg="gray", command=randomGeneration, text="Génération aléatoire")
bRandom.grid(column=0, row=2)
bSoustraction = tk.Button(bg="gray", command=soustraction, text="Soustraction Tableau")
bSoustraction.grid(column=0, row=3)
bAdd = tk.Button(bg="gray", command=add, text="Addition Tableau")
bAdd.grid(column=0, row=4)
bAutomate = tk.Button(bg="gray", command=automate, text="Automate")
bAutomate.grid(column=0, row=5)
bEmptySand = tk.Button(bg="gray", command=initialisation, text="Tableau Vide")
bEmptySand.grid(column=0, row=1)
bPauseAutomate = tk.Button(bg="gray", command=pause, text="Pause Automate")
bPauseAutomate.grid(column=0, row=5)
fenetre.mainloop()
