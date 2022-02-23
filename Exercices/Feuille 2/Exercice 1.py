from multiprocessing import Condition
import tkinter as tk
import random as rdm

root = tk.Tk()
root.title("Exercice")
cond = False
cCanevas = tk.Canvas(root, height=400, width=600, bg="Black")
cCanevas.grid(column=0, row=0)


def creer_balle():
    cercle = cCanevas.create_oval((600 / 2 + 20, 400 / 2 + 20), (600 / 2 - 20, 400 / 2 - 20), fill="Blue")
    rdm1, rdm2 = rdm.randint(-7, 7), rdm.randint(-7, 7)
    listeBalle = [cercle, rdm1, rdm2]
    return listeBalle


def mouvement(balle):
    global cond
    bStart.grid_remove()
    bStop.grid(column=0, row=1)
    cercle = balle[0]
    yPlus = balle[1]
    xPlus = balle[2]
    cCanevas.move(cercle, xPlus, yPlus)
    if cond is True:
        bStop.grid_remove()
        bStart.grid(column=0, row=1)
        cCanevas.after_cancel(balle)
        cond = False
        return
    cCanevas.after(20, lambda: mouvement(balle))


def stop():
    global cond
    cond = True


def rebond1(balle):
    balle[1] = - balle[1]
    balle[2] = - balle[2]
    return balle

bStop = tk.Button(root, background="blue", text="Stop!", command=stop)
balle = creer_balle()
bStart = tk.Button(root, background="blue", text="Démarrer!", command=lambda: mouvement(balle))
bStart.grid(column=0, row=1)
root.mainloop()
