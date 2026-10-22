import tkinter as tk
from tkinter import messagebox

# All possible winning combinations
combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

current_player = "X"
game_over = False


def check_winner():
    global game_over

    for combo in combinations:
        a, b, c = combo

        if (
            buttons[a]["text"]
            == buttons[b]["text"]
            == buttons[c]["text"]
            != ""
        ):
            # Highlight the winning buttons
            for index in combo:
                buttons[index].config(bg="green", fg="white")

            game_over = True
            label.config(text=f"Player {current_player} wins!")

            messagebox.showinfo(
                "Tic-Tac-Toe",
                f"Player {current_player} wins!"
            )
            return True

    return False


def button_click(index):
    global current_player, game_over

    # Do not allow moves after the game ends
    if game_over or buttons[index]["text"] != "":
        return

    buttons[index].config(text=current_player)

    # Check whether someone has won
    if check_winner():
        return

    # Check whether the board is full
    if all(button["text"] != "" for button in buttons):
        game_over = True
        label.config(text="It's a draw!")
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        return

    # Switch players
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")


def restart_game():
    global current_player, game_over

    current_player = "X"
    game_over = False

    # Clear all nine buttons
    for button in buttons:
        button.config(text="", bg="SystemButtonFace", fg="black")

    label.config(text="Player X's turn")


# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)

# Display whose turn it is
label = tk.Label(
    root,
    text="Player X's turn",
    font=("Arial", 16, "bold")
)
label.grid(row=0, column=0, columnspan=3, pady=10)

# Create the nine game buttons
buttons = []

for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 25),
        width=6,
        height=2,
        command=lambda i=i: button_click(i)
    )
    button.grid(row=(i // 3) + 1, column=i % 3)
    buttons.append(button)

# Restart button
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12),
    command=restart_game
)
restart_button.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
