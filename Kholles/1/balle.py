import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400


###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    global compteur, item
    compteur = 0
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    item = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [item, dx, dy]



def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global compteur, status, after
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    after = canvas.after(10, mouvement)
    status = True
    if compteur >= 30:
        print("arrêt")
        canvas.after_cancel(after)
        status = False


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, compteur, item
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        compteur += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        compteur += 1
    if (compteur / 5) % 2 == 1:
        canvas.delete(item)
        item = canvas.create_rectangle((x0, y0), (x1, y1), fill="red")
        balle[0] = item
    elif (compteur / 5) % 2 == 0:
        canvas.delete(item)
        item = canvas.create_oval((x0, y0), (x1, y1), fill="blue")
        balle[0] = item


def clic(event):
    global compteur, status, after
    compteur = 0
    if status is True:
        canvas.after_cancel(after)
        status = False
    else:
        after = canvas.after(10, mouvement)
        status = True


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.bind("<Button-1>", clic)
canvas.grid()

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
