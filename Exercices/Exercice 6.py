###########################################
# Autor: Valentin Jacquin
###########################################
import tkinter as tk

root = tk.Tk()
root.title("Exo 6")
colorCercle = "Black"
cWidth, cHeight, historique = 500, 500, []
cTableau = tk.Canvas(bg="white", width=cWidth, height=cHeight)
cTableau.grid(column=1, row=0)
cTableau.create_rectangle((0, 0), (50, 50), fill="green", outline="green")
cTableau.create_rectangle((50, 0), (100, 50), fill="yellow", outline="yellow")
cTableau.create_rectangle((100, 0), (150, 50), fill="blue", outline="blue")
cercle = cTableau.create_oval((cWidth/2 + 50, cHeight/2 + 50), (cWidth/2 - 50, cHeight/2 - 50), fill=colorCercle, outline=colorCercle)


def checkSide(event):
    global colorCercle, cercle, historique
    y = event.y
    x = event.x
    if y > 50:
        cTableau.delete(cercle)
        colorCercle = "black"
        historique.append(colorCercle)
        cTableau.create_oval((cWidth/2 + 50, cHeight/2 + 50), (cWidth/2 - 50, cHeight/2 - 50), fill=colorCercle, outline=colorCercle)
    elif x < 50:
        cTableau.delete(cercle)
        colorCercle = "green"
        historique.append(colorCercle)
        cTableau.create_oval((cWidth/2 + 50, cHeight/2 + 50), (cWidth/2 - 50, cHeight/2 - 50), fill=colorCercle, outline=colorCercle)
    elif x > 50 and x < 100:
        cTableau.delete(cercle)
        colorCercle = "yellow"
        historique.append(colorCercle)
        cTableau.create_oval((cWidth/2 + 50, cHeight/2 + 50), (cWidth/2 - 50, cHeight/2 - 50), fill=colorCercle, outline=colorCercle)
    else:
        cTableau.delete(cercle)
        colorCercle = "blue"
        historique.append(colorCercle)
        cTableau.create_oval((cWidth/2 + 50, cHeight/2 + 50), (cWidth/2 - 50, cHeight/2 - 50), fill=colorCercle, outline=colorCercle)


def back():
    global colorCercle, historique
    assert len(historique) != 0, "Historique vide"
    colorCercle = historique[len(historique) - 1]
    del historique[len(historique) - 1]
    cTableau.create_oval((cWidth/2 + 50, cHeight/2 + 50), (cWidth/2 - 50, cHeight/2 - 50), fill=colorCercle, outline=colorCercle)
    return


bRetry = tk.Button(text="Annuler", bg="red", command=back)
bRetry.grid(column=0, row=0)
cTableau.bind("<Button-1>", checkSide)
root.mainloop()
