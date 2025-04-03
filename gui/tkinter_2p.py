# gui/tkinter_2p.py

import tkinter as tk
from tkinter import messagebox

class TwoPlayersGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe - 2 Joueurs")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text=" ", width=8, height=4,
                                font=("Arial", 20), command=lambda i=i, j=j: self.player_move(i, j))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    
    def player_move(self, i, j):
        if self.board[i][j] != " ":
            return
        self.board[i][j] = self.current
        color = "#FFCCCC" if self.current == "X" else "#FFFFCC"
        self.buttons[i][j].config(
            text=self.current,
            state="disabled",
            bg=color,
            fg="black",
            disabledforeground="black",
            activebackground=color,
            highlightbackground=color
        )
        winner = self.check_winner()
        if winner or self.is_draw():
            self.end_game(winner)
            return
        self.current = "O" if self.current == "X" else "X"


    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        return None

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def end_game(self, winner):
        if winner:
            msg = f"Le joueur {winner} a gagné !"
        else:
            msg = "Match nul !"

        if messagebox.askyesno("Fin de partie", f"{msg}\n\nRejouer ?"):
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state="normal")

def launch_2_players_gui():
    root = tk.Tk()
    game = TwoPlayersGUI(root)
    root.mainloop()
