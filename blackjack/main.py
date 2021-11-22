#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define main module for Blackjack game."""

import tkinter as tk
from help_GUI import about, printRules
from game import Game


window = tk.Tk()
window.title("Blackjack")
frame = tk.Frame(window)
frame.pack(side=tk.TOP)
top = tk.Menu(window)
window.config(menu=top)
game = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=game)
can = tk.Canvas(window, bg='black', height=600, width=500)
can.pack(side=tk.TOP, padx=5, pady=5)
lab_Message2 = tk.Label(window, text="", fg="black")
lab_Message2.pack(side=tk.BOTTOM)
name = 'pictures/bankruptcy.gif'
imageBankruptcy = tk.PhotoImage(file=name)
instruction = "Click on Game to start a new game"
lab_Message = tk.Label(frame, text=instruction, fg="black")
lab_Message.pack(side=tk.TOP)

newGame = Game(can, lab_Message, lab_Message2, window, imageBankruptcy)

game.add_command(label='New game', command=newGame.newGame)
game.add_command(label='Exit', command=window.destroy)

top.add_command(label='Rules', command=printRules)
top.add_command(label='About', command=about)

but_hit = tk.Button(window, text='Hit', command=newGame.hit)
but_hit.pack(side=tk.LEFT)
but_stand = tk.Button(window, text='Stand', command=newGame.stand)
but_stand.pack(side=tk.LEFT)

window.mainloop()
