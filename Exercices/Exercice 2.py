import tkinter as tk


nLine = 0
cliclist = []
compte = 0
historique = []
check = True
root = tk.Tk()
canvasHeigth = 500
canvasWidth = 500


def timeoutMan():
    global check
    if check is True:
        check = False
        button['text'] = "Recommencer"
    else:
        check = True
        button['text'] = "Pause"
    return


def createline(event):
    global cliclist, nLine, historique
    x1 = cliclist[0][0]
    x2 = cliclist[1][0]
    y1 = cliclist[0][1]
    y2 = cliclist[1][1]
    color = "blue"
    if (nLine % 2) != 0:
        color = "red"
    line = canvas.create_line(x1, y1, x2, y2, fill=color)
    nLine += 1
    historique.append(line)
    return


def lancementLigne(event):
    global cliclist, check
    if check is False:
        return
    compteClic(event)
    if check is not False:
        x = event.x
        y = event.y
        if len(cliclist) >= 2:
            cliclist = []
        cliclist.append((x, y))
        if len(cliclist) == 2:
            createline(event)


def compteClic(event):
    global compte, historique
    compte += 1
    if compte > 4:
        canvas.delete(historique[1], historique[0])
        historique = []
        compte = 1


canvas = tk.Canvas(background="White", width=canvasWidth, height=canvasHeigth)
canvas.grid(column=0, row=0)
button = tk.Button(text="Pause", command=timeoutMan)
button.grid(column=0, row=1)
canvas.bind("<Button-1>", lancementLigne)
root.mainloop()
