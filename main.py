from tkinter import * 
from tkinter import ttk 

import random 

root = Tk() 
root.title("Tic-Tac-Toe")
root.maxsize(900,600) 
root.config(bg="black")

ui_frame = Frame(root, width=600, height=100, bg="grey")
ui_frame.grid(row=0, column=0, padx=10, pady=5) 

canvas = Canvas(root, width=600, height=480, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

root.mainloop() 
