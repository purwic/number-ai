import sqlite3

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


con = sqlite3.connect('database.db')

cursor = con.cursor()

# weights = (layer; weights_layer)
# weights_layer = (j; weights_i)
# weights_i is just list of all weights that we got for that layer and j

with con:
    cursor.execute("SELECT * FROM weights")

    # (id, layer, i, j, value)
    db_weights = cursor.fetchall()

    weights = []
    weights_layer = []

    count = 1

    for item in db_weights:
        value = item[4]

        weights_layer.append(value)




print(weights)

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

app.mainloop()
