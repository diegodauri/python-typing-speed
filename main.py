from tkinter import *
from tkinter import messagebox
import random

random_text = ""


def end():
    errors = 0
    wpm = 0
    for word in text.get("1.0", END).split(" "):
        if word not in random_text.split(" "):
            errors += 1

    wpm = len(text.get("1.0", END).split(" ")) / 6

    if messagebox.showinfo("Test Finished", f"Words per minute: {wpm}\nErrors: {errors}") == "ok":
        window.quit()

class UpdateLabel(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self._count = 0

    def update_text(self):
        self.config(text=str(self._count))
        self._count += 1
        self.after(1000, self.update_text)


def check_update():
    if len(text.get("1.0", END)) != 1:
        label.update_text()
    else:
        text.after(1, check_update)


with open(f"text{random.randint(1, 5)}.txt") as text:
    random_text = text.read()

window = Tk()

window.title("Image Watermarking")
window.config(padx=50, pady=50)

label = UpdateLabel(window, text="0 s",
                    font=("Arial 30"), width=10, bg='#d3e0fa', fg='green')

label.pack()

canvas = Canvas(width=700, height=109)

title = canvas.create_text(350, 30, text="Welcome to the typing speed test desktop app!", width=6000,
                           font=("Arial", 20, "bold"))
subtitle = canvas.create_text(350, 55, text="Get started by typing the following words in the box below the "
                                            "button below!", width=6000, font=("Arial", 15),
                              fill="gray")

canvas.pack()

text_canvas = Canvas(width=700, height=209, bg="white")
text_display = text_canvas.create_text(350, 100, text="", width=600, font=("Arial", 8, "bold"))
text_canvas.pack()

text_canvas.itemconfigure(text_display, text=random_text)

spacing = Canvas(width=700, height=50)
spacing.pack()

text = Text(height=5, width=30)
text.focus()
text.pack()

check_update()

text.after(60000, end)

window.mainloop()
