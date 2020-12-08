"""Main GUI for Blackjack"""

import tkinter as tk

# Main window and its fixed size.
root = tk.Tk()
root.geometry("800x600")
root.title("Blackjack")
root.resizable(0, 0)

# Blackjack table canvas.
canvas = tk.Canvas(master = root, width = 800, height = 550, bg = "#004400")
canvas.pack()

# Player buttons (HIT & STAY) wrapper.
player_buttons = tk.Frame(root, bg = "blue")
player_buttons.pack(side = "bottom")

hit = tk.Button(player_buttons, width = 30, height = 2, padx = 100, text = "HIT")
hit.pack(side = "left")

stay = tk.Button(player_buttons, width = 30, height = 2, padx = 100, text = "STAY")
stay.pack(side = "right")

# Show Dealers and Players cards.


root.mainloop()
