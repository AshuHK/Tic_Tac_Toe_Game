from tkinter import *
from tkinter import ttk

import random

board_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
move_count = 0


def winner_popup(winner):
    pop_up = Tk()
    pop_up.maxsize(300, 200)
    pop_up.geometry("300x100")
    pop_up.wm_title("The Winner is...")
    label = Label(pop_up, text="{}!".format(winner).title())

    label.pack(side="top", fill="x", pady=10)

    exit_button = Button(pop_up, text="Okay", command=pop_up.destroy)
    exit_button.pack()

    pop_up.mainloop()


def get_winner(row, column, board_list):
    """
    Outputs the winner given the row and column of the winning position 

    :param row: int for the row in the 2D list 
    :param column: int for the column in the 2D list 
    """
    if board_list[row][column] == "x":
        return "x"
    elif board_list[row][column] == "o":
        return "o"


def check_win(board_list):
    """
    Checks the given board and outputs the winner 

    :param board_list: 2D list of strings and ints to represent the board
    """

    for i in range(0, 3):

        # rows
        if board_list[i][0] == board_list[i][1] == board_list[i][2]:
            if board_list[i][0] != 0:
                return get_winner(i, 0, board_list)

        # columns
        elif board_list[0][i] == board_list[1][i] == board_list[2][i]:
            if board_list[0][i] != 0:
                return get_winner(0, 1, board_list)

        # diagonal (top left to bottom right)
        elif board_list[0][0] == board_list[1][1] == board_list[2][2]:
            if board_list[0][0] != 0:
                return get_winner(0, 0, board_list)

        # diagonal (bottom left to top right)
        elif board_list[0][2] == board_list[1][1] == board_list[2][0]:
            if board_list[0][2] != 0:
                return get_winner(0, 2, board_list)

    else:
        return None


def draw_x(row, column):
    """
    Draws a single "x" on the board with a given row and column

    :param row: Integer for the row of the board that the "x" will be at
    :param column: Integer for the column of the board the the "x" will be at
    """

    # adjusting the column and rows to fit the grid
    if column != 1:
        column *= 2
        column -= 1

    if row != 1:
        row *= 2
        row -= 1

    # calculating the center position of the circle
    x_center = row * 100
    y_center = column * 77

    radius = 40

    # from top left to bottom right
    x0 = x_center - radius
    y0 = y_center - radius

    x1 = x_center + radius
    y1 = y_center + radius

    canvas.create_line(x0, y0, x1, y1, fill="blue")

    # from bottom left to top right
    x2 = x_center + radius - 80
    y2 = y_center + radius

    x3 = x_center - radius + 80
    y3 = y_center - radius

    canvas.create_line(x2, y2, x3, y3, fill="blue")

    return None


def draw_o(row, column):
    """
    Drawa a single "o" on the board with a given row and column

    :param row: Integer for the row of the board that the "o" will be at
    :param column: Integer for the column of the board the the "o" will be at
    """

    # adjusting the column and rows to fit the grid
    if column != 1:
        column *= 2
        column -= 1

    if row != 1:
        row *= 2
        row -= 1

    # calculating the center position of the circle
    x_center = row * 100
    y_center = column * 77

    radius = 40

    # create the base circle (the red part)
    x0 = x_center - radius
    y0 = y_center - radius

    x1 = x_center + radius
    y1 = y_center + radius

    canvas.create_oval(x0, y0, x1, y1, fill="red", outline="white")

    # create the inner circle (the hole)
    x2 = x_center - (radius // 1.05)
    y2 = y_center - (radius // 1.05)

    x3 = x_center + (radius // 1.05)
    y3 = y_center + (radius // 1.05)

    canvas.create_oval(x2, y2, x3, y3, fill="white", outline="white")

    return None


def draw_board(board_list):
    """
    Draws the board in the game space
    :param board_list: 2D list of strings and ints to represent the board
    """

    # clears out the canvas to make an empty board
    canvas.delete("all")

    # Horizontal Lines
    canvas.create_rectangle(600, 170, 0, 160, fill="black")
    canvas.create_rectangle(600, 330, 0, 320, fill="black")

    # Vertical Lines
    canvas.create_rectangle(210, 480, 200, 0, fill="black")
    canvas.create_rectangle(410, 480, 400, 0, fill="black")

    # iterate through the board and draw each of the positions
    for row in range(len(board_list)):
        for column in range(len(board_list[0])):

            if board_list[row][column] == "x":
                draw_x(row + 1, column + 1)
            elif board_list[row][column] == "o":
                draw_o(row + 1, column + 1)

    winner = check_win(board_list)

    empty_count = 0

    for i in range(len(board_list)):
        empty_count += board_list[i].count(0)

    if (winner is None) and (empty_count == 0):
        winner = "Draw"
        winner_popup(winner)
    elif winner is not None:
        winner_popup(winner)

    print(winner)


def end_turn():
    """
    Starts the game or goes to the next move
    """

    global board_list
    global move_count

    try:

        # pull the inputs
        row_input = int(row_entry.get()) - 1
        column_input = int(column_entry.get()) - 1

        # only draw the board when both values are in a reasonble range
        if (
            (row_input >= 0 and row_input <= 2)
            and (column_input >= 0)
            and (column_input <= 2)
        ):
            # checks if the position was taken already
            if board_list[row_input][column_input] != 0:
                raise ValueError("Position was taken already")
            else:

                # player 1 has X's
                if (move_count % 2) == 0:
                    print("\nPlayer 1 move is: {}, {}".format(row_input, column_input))
                    board_list[row_input][column_input] = "x"

                # player 2 has O's
                else:
                    print("\nPlayer 2 move is: {}, {}".format(row_input, column_input))
                    board_list[row_input][column_input] = "o"

            move_count += 1

            # print(board_list)

            draw_board(board_list)

        # produces the following output if not
        else:
            print("one of your values is out of range")

    # if a number is not both boxes
    except ValueError:
        print("There is an error. Please try again.")


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

# makes the start button/ end turn button
Button(ui_frame, text="End Turn", command=end_turn, bg="red").grid(
    row=2, column=3, padx=5, pady=5
)

# Row input
Label(ui_frame, text="Column:", bg="grey").grid(row=1, column=0, padx=5, pady=5)
row_entry = Entry(ui_frame)
row_entry.grid(row=1, column=1, padx=5, pady=5)

# Column input
Label(ui_frame, text="Row:", bg="grey").grid(row=2, column=0, padx=5, pady=5)
column_entry = Entry(ui_frame)
column_entry.grid(row=2, column=1, padx=5, pady=5)

# run the main loop and start the application
root.mainloop()
