# gui/tkinter_version.py

import tkinter as tk
from tkinter import messagebox
from ia.minimax import best_move, check_winner

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe - Joueur vs IA")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
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
        self.board[i][j] = "X"
        self.buttons[i][j].config(
        text="X",
        state="disabled",
        bg="#FFCCCC",  # Rouge clair
        fg="black",
        disabledforeground="black",
        activebackground="#FFCCCC",
        highlightbackground="#FFCCCC"
        )
        winner = check_winner(self.board)
        if winner or self.is_draw():
            self.end_game(winner)
            return
        self.root.after(500, self.ai_move)

    def ai_move(self):
       i, j = best_move(self.board)
       if i is not None:
        self.board[i][j] = "O"
        self.buttons[i][j].config(
                text="O",
                state="disabled",
                bg="#FFFFCC",  # Jaune clair
                fg="black",
                disabledforeground="black",
                activebackground="#FFFFCC",
                highlightbackground="#FFFFCC"
            )
        winner = check_winner(self.board)
        if winner or self.is_draw():
            self.end_game(winner)

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def end_game(self, winner):
        if winner:
            msg = "Tu as gagné !" if winner == "X" else "L'IA a gagné !"
        else:
            msg = "Match nul !"

        if messagebox.askyesno("Fin de partie", f"{msg}\n\nRejouer ?"):
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state="normal")

#  Fonction à appeler depuis main.py
def launch_vs_ai():
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

# Test direct
if __name__ == "__main__":
    launch_vs_ai()
