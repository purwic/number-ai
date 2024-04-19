from customtkinter import *

set_appearance_mode("System")
set_default_color_theme("blue")

app = CTk()
app.geometry("300x500")
app.title("Number AI")
app.resizable(0,0)

label = CTkLabel(app, text="Draw a number", font=("Arial", 18))
label.pack()






drown_pixels = []
last_drowned = []

# canvas n to n
n = 200

# the grid k to k on the canvas:
k = 10

def draw(event):

    if (n > event.x >= 0) & (n > event.y >= 0):

        print(drown_pixels)

        if not last_drowned:
            drown_pixels.append([event.x, event.y])
            last_drowned.append(event.x)
            last_drowned.append(event.y)

        else:
            x1, y1 = last_drowned[0], last_drowned[1]
            x2, y2 = event.x, event.y

            drown_pixels.append([x2, y2])
            last_drowned[0] = x2
            last_drowned[1] = y2

            canvas.create_line(x1, y1, x2, y2, fill='red')


canvas = CTkCanvas(bg="white", width=n, height=n)
canvas.pack(anchor="center")

canvas.bind('<ButtonPress-1>', draw)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', lambda event: last_drowned.clear())

compute_btn = CTkButton(master=app, text="compute")
compute_btn.pack()

app.mainloop()