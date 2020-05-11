from tkinter import *
from tkinter import ttk

import random


def draw_x(board_list):
    """
    Draws all of the X's in the list of the board
    """
    pass


def draw_o(board_list):
    """
    Draws all of the O's in the list of the board
    """
    pass


def draw_board(board_list):
    """
    Draws the board in the game space
    """

    # clears out the canvas to make an empty board
    canvas.delete("all")

    # Horizontal Lines
    canvas.create_rectangle(600, 170, 0, 160, fill="black")
    canvas.create_rectangle(600, 330, 0, 320, fill="black")

    # Vertical Lines
    canvas.create_rectangle(210, 480, 200, 0, fill="black")
    canvas.create_rectangle(410, 480, 400, 0, fill="black")

    for x in range(len(board_list)):
        for y in range(len(board_list[0])):

            if board_list[x][y] == "x":
                draw_x(board_list)
            elif board_list[x][y] == "o":
                draw_o(board_list)


def start_game():
    """
    Starts the game
    """
    # will also choose how the game will be played based on the opponent choice
    # print(opponent_choice.get())

    # this list will represent the choices of the user/computer
    board_list = [["x", 0, 0], [0, "x", 0], [0, 0, "x"]]

    draw_board(board_list)
    pass


root = Tk()
root.title("Tic-Tac-Toe")
root.maxsize(900, 600)
root.config(bg="black")

opponent_choice = StringVar()

# create the options menu abuve
ui_frame = Frame(root, width=600, height=100, bg="grey")
ui_frame.grid(row=0, column=0, padx=10, pady=5)

# create the game space bwlow
canvas = Canvas(root, width=600, height=480, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# makes the start button
Button(ui_frame, text="Start", command=start_game, bg="red").grid(
    row=0, column=1, padx=5, pady=5
)

# a label for the opponent choice
Label(ui_frame, text="Choose your opponent", padx=5, pady=5).grid(
    row=0, column=0, padx=5, pady=5
)

# create the choice for the opponent
opponent_menu = ttk.Combobox(
    ui_frame, textvariable=opponent_choice, values=["Human", "Computer"]
)
opponent_menu.grid(row=1, column=0, padx=5, pady=5)

# set the default to the human opponent
opponent_menu.current(0)

# run the main loop and start the application
root.mainloop()
