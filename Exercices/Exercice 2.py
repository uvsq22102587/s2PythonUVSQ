import tkinter as tk


nLine = 0
l = []
compte = 0
historique = []
check = True
root = tk.Tk()
canvasHeigth = 500
canvasWidth = 500


def timeoutMan(event):
    global check
    if check is True:
        check = False
        canvas.itemconfigure(button, text="recommencer")
    else:
        check = True
    return


def createline(event):
    global l, nLine, historique
    x1 = l[0][0]
    x2 = l[1][0]
    y1 = l[0][1]
    y2 = l[1][1]
    if nLine < 2:
        line = canvas.create_line(x1, y1, x2, y2, fill="blue")
        nLine += 1
        historique.append(line)
    return

def lancementLigne(event):
    global l, check
    compteClic(event)
    if check is not False:
        x = event.x
        y = event.y
        if len(l) >= 2:
            l = []
        l.append((x, y))
        if len(l) == 2:
            createline(event)

def compteClic(event):
    global compte, historique
    compte += 1
    if compte == 5:
        canvas.delete(historique[1], historique[0])
        historique = []
        compte = 0

    

canvas = tk.Canvas(background="Black", width=canvasWidth, height=canvasHeigth)
canvas.grid(column=0, row=0)
button = tk.Button(text="Pause", command=timeoutMan)
button.grid(column=0, row=1)
canvas.bind("<Button-1>", lancementLigne)
root.mainloop()
