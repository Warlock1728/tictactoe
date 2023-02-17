import tkinter as tk

# create main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")

# create global variables
player = "X"
game_over = False

# define function to check for a winner
def check_win():
    global game_over
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            game_over = True
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            game_over = True
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        game_over = True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        game_over = True

# define function to handle button clicks
def button_click(row, col):
    global player
    global board
    global game_over
    if board[row][col] == " " and not game_over:
        board[row][col] = player
        button = buttons[row][col]
        button.config(text=player, state="disabled", disabledforeground=colors[player])
        check_win()
        if not game_over:
            player = "O" if player == "X" else "X"
            player_label.config(text=f"Player {player}'s turn")
        else:
            player_label.config(text=f"Player {player} wins!")
        

# create board and button widgets
board = [[" " for i in range(3)] for j in range(3)]
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text=" ", font=("Arial", 20), width=3, height=1, command=lambda row=i, col=j: button_click(row, col))
        button.grid(row=i, column=j, sticky="nsew")
        row.append(button)
    buttons.append(row)

# create player label
player_label = tk.Label(root, text="Player X's turn", font=("Arial", 12))
player_label.grid(row=3, column=0, columnspan=3)

# create colors for X and O
colors = {"X": "red", "O": "blue"}

# start the main loop
root.mainloop()
