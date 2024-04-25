from customtkinter import *
import sqlite3 as sl

def draw(event):
    if (n > event.x >= 0) & (n > event.y >= 0):

        print(drown_gp)

        alpha = n / k

        x_ = event.x // alpha
        y_ = event.y // alpha

        if [x_, y_] not in drown_gp:
            drown_gp.append([x_, y_])

        canvas.create_rectangle(alpha * x_, alpha * y_, alpha * (x_ + 1), alpha * (y_ + 1), fill="black")


def init(layers_, weights_):

    init_layer(324, layers_)
    init_layer(100, layers_)
    init_layer(10, layers_)


def init_layer(n_, layers_):

    layer = []
    for i in range(n_):
        layer.append(0)

    layers_.append(layer)


layers = []
W = []

init(layers)





set_appearance_mode("System")
set_default_color_theme("blue")

app = CTk()
app.geometry("600x800")
app.title("Number AI")
app.resizable(0, 0)

label = CTkLabel(app, text="Draw a number", font=("Arial", 18))
label.pack()

# drown grid pixels
drown_gp = []

# canvas n to n
n = 25 * 18

# the grid k to k (grid pixels) on the canvas:
k = 25

canvas = CTkCanvas(bg="white", width=n, height=n)
canvas.pack(anchor="center")

canvas.bind('<ButtonPress-1>', draw)
canvas.bind('<B1-Motion>', draw)





print(layers)





app.mainloop()
