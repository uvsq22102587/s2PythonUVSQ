###########################################
# Autor: Valentin Jacquin
###########################################
import tkinter as tk

grandeur = 50
cHeight, cWidth = 500, 500
check = True
root = tk.Tk()
root.title("Exo 4")
cTableau = tk.Canvas(bg="white", width=cWidth, height=cHeight)
cRedCarre = cTableau.create_rectangle((cWidth/2 + grandeur, cHeight/2 + grandeur), (cWidth/2 - grandeur, cHeight/2 - grandeur), fill="red", outline="red")
cTableau.grid(column=0, row=0)


def timeout():
    global check
    if check is True:
        check = False
        bPause['text'] = "Restart"

    else:
        check = True
        bPause['text'] = "Pause"
    return


bPause = tk.Button(text="Pause", command=timeout)
bPause.grid(column=0, row=1)


def grossisunpeu():
    global grandeur, cRedCarre
    cTableau.delete(cRedCarre)
    grandeur += 10
    cRedCarre = cTableau.create_rectangle((cWidth/2 + grandeur, cHeight/2 + grandeur), (cWidth/2 - grandeur, cHeight/2 - grandeur), fill="red", outline="red")
    return


def tasprisdupoids():
    global grandeur, cRedCarre
    cTableau.delete(cRedCarre)
    grandeur -= 10
    cRedCarre = cTableau.create_rectangle((cWidth/2 + grandeur, cHeight/2 + grandeur), (cWidth/2 - grandeur, cHeight/2 - grandeur), fill="red", outline="red")
    return


def checkLocalisation(event):
    global cHeight, cWidth, grandeur, check
    if check is False:
        return
    x = event.x
    y = event.y
    if x < (cWidth/2 + grandeur) and y < (cHeight/2 + grandeur) and x > (cWidth / 2 - grandeur) and y > (cHeight/2 - grandeur):
        if grandeur >= 20:
            tasprisdupoids()
    else:
        if grandeur <= 100:
            grossisunpeu()
    return


cTableau.bind("<Button-1>", checkLocalisation)
root.mainloop()
