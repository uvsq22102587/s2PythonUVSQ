###########################################
# Autor: Valentin Jacquin
###########################################
import tkinter as tk

root = tk.Tk()
root.title("Exo 5")
cWidth, cHeight = 600, 600
colorL1, colorL2 = "red", "blue"
xline1 = cWidth * (1/3)
xline2 = cWidth * (2/3)
cTableau = tk.Canvas(width=cWidth, height=cHeight, bg="White")
line1 = cTableau.create_line((xline1, 0), (xline1, cHeight), fill=colorL1)
line2 = cTableau.create_line((xline2, 0), (xline2, cHeight), fill=colorL2)
cTableau.grid(column=0, row=0)


def restart():
    global xline1, xline2, colorL1, colorL2
    colorL1, colorL2 = "red", "blue"
    xline1, xline2 = cWidth * (1/3), cWidth * (2/3)
    createLine()
    return


def createLine():
    global xline1, xline2, line1, line2, colorL1, colorL2
    cTableau.delete(line1)
    cTableau.delete(line2)
    line1 = cTableau.create_line((xline1, 0), (xline1, cHeight), fill=colorL1)
    line2 = cTableau.create_line((xline2, 0), (xline2, cHeight), fill=colorL2)
    return


def checkSide(event):
    global xline1, xline2, colorL1, colorL2
    x = event.x
    if x < xline1:
        xline1 -= 10
    else:
        xline1 += 10
    if x < xline2:
        xline2 -= 10
    else:
        xline2 += 10
    colorL1, colorL2 = colorL2, colorL1
    createLine()
    return


bRestart = tk.Button(command=restart, text="Recommencer")
bRestart.grid(column=0, row=1)
cTableau.bind("<Button-1>", checkSide)
root.mainloop()
