import tkinter as tk
from gui.tkinter_version import launch_vs_ai
from gui.tkinter_2p import launch_2_players_gui  # Adapte selon ton fichier 2 joueurs
import sys

def start_menu():
    root = tk.Tk()
    root.title("🎮 Bienvenue dans Tic-Tac-Toe !")
    root.configure(bg="#FFFFCC")  # 💙 fond bleu

    # Titre
    tk.Label(root, text="Choisis un mode :", font=("Arial", 20, "bold"), fg="white", bg="#007ACC").pack(pady=20)

    # Style commun des boutons
    button_style = {
        "font": ("Arial", 16),
        "width": 20,
        "height": 2,
        "bg": "#FFFFFF",  # blanc
        "fg": "#000000",  # noir
        "activebackground": "#CCCCCC"
    }

    # Boutons
    tk.Button(root, text="1. Joueur vs IA", command=lambda: [root.destroy(), launch_vs_ai()], **button_style).pack(pady=10)
    tk.Button(root, text="2. Deux Joueurs", command=lambda: [root.destroy(), launch_2_players_gui()], **button_style).pack(pady=10)
    tk.Button(root, text="Quitter", command=root.quit, **button_style).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    start_menu()
