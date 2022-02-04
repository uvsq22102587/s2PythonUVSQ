###########################################
# Autor: Valentin Jacquin
###########################################
import tkinter as tk

compte = 0
historique = []
nCroix = 0
nCarre = 0
nCercle = 0
root = tk.Tk()
cWidth, cHeight = 500, 500
cTableau = tk.Canvas(background="black", width=500, height=500)
cTableau.grid(column=0, row=0)


def clearFigure():
    global historique, compte, nCroix, nCarre, nCercle
    for i in range(0, len(historique)):
        cTableau.delete(historique[i])
    compte, nCroix, nCarre, nCercle, historique = 0, 0, 0, 0, []
    return


def checkSide(event):
    global compte, historique, nCroix, nCarre, nCercle
    compte += 1
    x = event.x
    y = event.y
    if x < (cWidth * (1/3)) and nCroix < 2:
        cLine1 = cTableau.create_line((x + 30, y + 30), (x - 30, y - 30), fill="Blue")
        cLine2 = cTableau.create_line((x - 30, y + 30), (x + 30, y - 30), fill="Blue")
        historique.append(cLine1)
        historique.append(cLine2)
        nCroix += 1
    if x > (cWidth * (1/3)) and nCarre < 3 and x < (cWidth * (2/3)):
        cCarre = cTableau.create_rectangle((x + 30, y + 30), (x - 30, y - 30), fill="green")
        historique.append([cCarre])
        nCarre += 1
    if x > (cWidth * (2/3)) and nCercle < 3:
        cCercle = cTableau.create_oval((x + 30, y + 30), (x - 30, y - 30), fill="red")
        historique.append([cCercle])
        nCercle += 1


bRestart = tk.Button(text="Redémarrer", command=clearFigure)
bRestart.grid(column=0, row=1)
cTableau.bind("<Button-1>", checkSide)
cTableau.create_line((cWidth * (1/3), 0), (cWidth * (1/3), 500), fill="white")
cTableau.create_line((cWidth * (2/3), 0), (cWidth * (2/3), 500), fill="white")
root.mainloop()
