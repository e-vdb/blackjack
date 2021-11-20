#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Define help functions for GUI menu.
"""

import tkinter as tk

def printRules():
    global ruleWindow
    ruleWindow=tk.Toplevel()
    ruleWindow.title("Blackjack rules") 
    with open('rules_eng.txt') as f:
        gameRules=f.read()
    lab_Rule=tk.Label(ruleWindow,text=gameRules,fg="black", anchor="e", justify=tk.LEFT)
    lab_Rule.pack(side=tk.TOP)
    ruleWindow.mainloop()

def about():
    aboutWindow=tk.Toplevel()
    aboutWindow.title("About") 
    with open('about.txt') as f:
        about=f.read()
    lbl_about=tk.Label(aboutWindow,text=about,fg="black", anchor="e", justify=tk.LEFT)
    lbl_about.pack(side=tk.TOP)
    aboutWindow.mainloop()    