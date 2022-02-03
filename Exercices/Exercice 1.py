import tkinter as tk

color = "Blue"
check = True


def retry():
    global check
    check = True
    return


def colorChange(event):
    global color, check
    if check is not False:
        x = event.x
        y = event.y
        if x <= 250 and x >= 200 and y <= 250 and y >= 200:
            Canvas.itemconfigure(rectangleRed, fill=color)
            if color == "Blue":
                color = "Red"
            else:
                color = "Blue"
        else:
            check = False
    return


root = tk.Tk()
root.title("Exo 1")
canvasHeigth = 500
canvasWidth = 500
Canvas = tk.Canvas(background="Black", height=canvasHeigth, width=500, )
Canvas.grid(column=0, row=1)
recommencer = tk.Button(background="Blue", command=retry, text="Recommencer",)
recommencer.grid(column=0, row=2)
rectangleRed = Canvas.create_rectangle((250, 250), (200, 200), fill="Red", outline="red")
root.bind("<Button-1>", colorChange)
root.mainloop()
