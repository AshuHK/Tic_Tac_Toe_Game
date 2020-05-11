from tkinter import *
from tkinter import ttk

import random


def start_game():
    """
    Starts the game 
    """
    # will also
    pass


root = Tk()
root.title("Tic-Tac-Toe")
root.maxsize(900, 600)
root.config(bg="black")

ui_frame = Frame(root, width=600, height=100, bg="grey")
ui_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=480, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

Button(ui_frame, text="Start", command=start_game, bg="red").grid(
    row=0, column=0, padx=5, pady=5
)

Label(ui_frame, text="Choose your opponent", padx=5, pady=5).grid(
    row=1, column=0, padx=5, pady=5
)

Radiobutton(ui_frame, text="Another Person").grid(row=2, column=1, padx=5, pady=5)


root.mainloop()
