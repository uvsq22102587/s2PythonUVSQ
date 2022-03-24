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
    coords = cCanevas.coords(balle[0])
    if coords[0] <= 0:
        rebond1(balle, 0)
    if coords[2] >= 600:
        rebond1(balle, 2)
    if coords[1] <= 0:
        rebond1(balle, 1)
    if coords[3] >= 400:
        rebond1(balle, 3)
    if cond is True:
        bStop.grid_remove()
        bStart.grid(column=0, row=1)
        cCanevas.after_cancel(balle)
        cond = False
        return
    cCanevas.after(10, lambda: mouvement(balle))


def stop():
    global cond
    cond = True


def rebond1(balle, bords):
    if bords == 1 or bords == 3:
        balle[1] = - balle[1]
        cCanevas.itemconfigure(balle[0], fill="white")
    if bords == 0 or bords == 2:
        balle[2] = - balle[2]
        cCanevas.itemconfigure(balle[0], fill="pink")
    return balle


def rebond2(balle, bords):
    coords = cCanevas.coords(balle[0])
    if bords == 0:
        cCanevas.delete(balle[0])
        balle[0] = cCanevas.create_oval((599, coords[1]), (559, coords[3]), fill="Blue")
    if bords == 1:
        cCanevas.delete(balle[0])
        balle[0] = cCanevas.create_oval((coords[0], 399), (coords[2], 359), fill="Blue")
    if bords == 2:
        cCanevas.delete(balle[0])
        balle[0] = cCanevas.create_oval((1, coords[1]), (41, coords[3]), fill="Blue")
    if bords == 3:
        cCanevas.delete(balle[0])
        balle[0] = cCanevas.create_oval((coords[0], 1), (coords[2], 41), fill="Blue")
    return


bStop = tk.Button(root, background="blue", text="Stop!", command=stop)
balle = creer_balle()
bStart = tk.Button(root, background="blue", text="Démarrer!", command=lambda: mouvement(balle))
bStart.grid(column=0, row=1)
root.mainloop()
