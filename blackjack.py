#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 12:20:28 2021

@author: Emeline
"""

import tkinter as tk
import random
from time import sleep

colors=['coeur','carreau','trefle','pique']
values=['as','2','3','4','5','6','7','8','9','10','valet','dame','roi']
repCards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def calculate_hand(hand):
    '''
    Parameters
    ----------
    hand : list of string
        Current player/dealer hand

    Returns
    -------
    tot_hand : integer
        evaluation of cards total.
    
    Examples:
    >>> calculate_hand(['3', '4'])
    7
    >>> calculate_hand(['K','10'])
    20
    >>> calculate_hand(['K','A'])
    21
    
    '''
    listFig=['J','Q','K']
    tot_hand=0
    nbAces=0
    for card in hand:
        if card in listFig:
            tot_hand+=10
        elif card == 'A':
            nbAces+=1
        else:
            tot_hand +=int(card)
    if nbAces != 0:
        test=tot_hand+(nbAces-1)+11
        if test <= 21:
            tot_hand=test
        else:
            tot_hand += nbAces
    return tot_hand


def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Function description from
    
    Kaggle Python course Lesson 7 Working with External Libraries (exercice 3)
    
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    if calculate_hand(hand_1)>21:
        return False
    elif calculate_hand(hand_1)>calculate_hand(hand_2) or calculate_hand(hand_2)>21:
        return True
    else:
        return False


class Player(object):
    def __init__(self):
        self.hand = []
    
    def getHand(self):
        return self.hand
    
    def add_card(self,card):
        card_id = values.index(card.getValue())
        self.hand.append(repCards[card_id])
    
    def cards_number(self):
        return len(self.hand)
    
    def total_hand(self):
        return calculate_hand(self.hand)
    
    def reinit(self):
        self.hand = []

class Card(object):
    def __init__(self,val='as',col='carreau'):
        self.value=val
        self.color=col
    
    def getValue(self):
        return self.value
    
    def display(self):
        print("{} de {}".format(self.value,self.color))

    def picture(self):
        name='pictures/'+self.value+'_'+self.color+'.gif'
        return tk.PhotoImage(file=name)

class Pack52cards(object):
    def __init__(self):
        self.cards=[]
        for value in values:
            for color in colors:
                card=Card(value,color)
                self.cards.append(card)
        
        
    def shuffle_pack(self):
        #random.seed(0)
        random.shuffle(self.cards)
        
    def pick_card(self):
        if len(self.cards)>0:
            card=self.cards.pop(0)
            return card
        else:
            return None

def put_card(idx,idy,im):
    global can
    can.create_image(idx,idy,image=im)

def winner():
    global player_total,lab_Message2,lab_Message
    lab_Message.configure(text=action[4])
    if blackjack_hand_greater_than(player.getHand(),dealer.getHand()):
        player_total+=2*player_bet
        can.create_text(200,550,text="Player wins",fill='red',font='Arial 22')
    else:
        player_total-=player_bet
        can.create_text(200,550,text="Dealer wins",fill='red',font='Arial 22')
    lab_Message2.configure(text="Player total money : "+str(player_total))
    if player_total>=10:
        window.after(2000,endGame)
    else:
        window.after(2000,bankruptcy)

def reinit():
    global player,dealer,player_cards,dealer_cards,dealer_score,player_score,p_x
    global can_play
    global pack,can,window,continueWindow
    global player_total,player_bet,lab_Message
    lab_Message.configure(text=action[1])
    can.delete(tk.ALL)
    can.create_text(60,30,text="Dealer",fill='white',font='Arial 18')
    can.create_text(60, 470,text='Player',fill='white',font='Arial 18')
    pack=Pack52cards()
    pack.shuffle_pack()
    dealer.reinit()
    player.reinit()
    dealer_cards=[]
    player_cards=[]
    p_x=100
    card1=pack.pick_card()
    dealer_cards.append(card1.picture())
    sleep(1)
    can.create_image(100,150,image=dealer_cards[0])
    can.update()
    dealer.add_card(card1)
    dealer_score=can.create_text(150,30,text=str(dealer.total_hand()),fill='white',font='Arial 18')
    card2=pack.pick_card()
    player_cards.append(card2.picture())
    sleep(1)
    can.create_image(p_x,350,image=player_cards[0])    
    can.update()
    p_x+=20
    player.add_card(card2)
    card3=pack.pick_card()
    player_cards.append(card3.picture())
    sleep(1)
    can.create_image(p_x,350,image=player_cards[1])
    can.update()
    player.add_card(card3)
    player_score=can.create_text(150,470,text=str(player.total_hand()),fill='white',font='Arial 18')
    can_play=True
    if player.total_hand()==21:
        can.create_text(250,470,text="Blackjack",fill='red',font='Arial 22')
        window.after(100,stand)
    else:
        lab_Message.configure(text=action[2])
    
def stand():
    global player_score,dealer_score,player,dealer,can_play,lab_Message
    lab_Message.configure(text=action[3])
    if can_play:
        d_x=120
        while dealer.total_hand()<17:
            sleep(1)
            newCard=pack.pick_card()
            dealer_cards.append(newCard.picture())
            dealer.add_card(newCard)
            can.create_image(d_x,150,image=dealer_cards[-1])    
            d_x+=20
            can.delete(dealer_score)
            dealer_score=can.create_text(150,30,text=str(dealer.total_hand()),fill='white',font='Arial 18')
            can.update()
            if dealer.total_hand()==21 and dealer.cards_number()==2:
                can.create_text(250,30,text="Blackjack",fill='red',font='Arial 22')
        window.after(100,winner)
        can_play=False
    
def hit():
    global player_score,player,p_x,can_play,player_total,lab_Message2,lab_Message
    if can_play:
        p_x+=20
        newCard=pack.pick_card()
        player_cards.append(newCard.picture())
        player.add_card(newCard)
        can.create_image(p_x,350,image=player_cards[-1])
        can.delete(player_score)
        player_score=can.create_text(150,470,text=str(player.total_hand()),fill='white',font='Arial 18')
        can.update()
        if player.total_hand()>21:
            lab_Message.configure(text=action[4])
            player_total-=player_bet
            can.create_text(200,550,text="Dealer wins",fill='red',font='Arial 22')
            lab_Message2.configure(text="Player total money : "+str(player_total))
            can_play=False
            if player_total>=10:
                window.after(2000,endGame)
            else:
                window.after(2000,bankruptcy)

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
    
def endGame():
    global continueWindow
    continueWindow=tk.Tk()
    continueWindow.title("Continue game ?")
    frameContinue=tk.Canvas(continueWindow,bg='white',height=500,width=500)
    frameContinue.pack()  
    lab_end=tk.Label(frameContinue,text='Do you want to continue playing ?')
    lab_end.pack(side=tk.TOP)
    but_yes=tk.Button(frameContinue,text='Yes',fg='white',bg='black',command=continueGame)
    but_yes.pack(side=tk.LEFT)
    but_no=tk.Button(frameContinue,text='No',fg='white',bg='black',command=exitAll)
    but_no.pack(side=tk.LEFT)
    continueWindow.mainloop() 

def continueGame():
    global continueWindow
    continueWindow.destroy()
    reinit()
    
def exitAll():
    global continueWindow,can,lab_Message
    continueWindow.destroy()
    can.delete(tk.ALL)
    lab_Message2.configure(text="")
    lab_Message.configure(text=action[0])

def bankruptcy():
    global can
    global imageBankruptcy,lab_Message
    can.delete(tk.ALL)
    can.create_text(250,550,text="Bankruptcy!!!",fill='red',font='Arial 22')
    can.create_image(250,250,image=imageBankruptcy)
    lab_Message.configure(text=action[0])

def newGame():
    global player_total,lab_Message2
    player_total=50
    lab_Message2.configure(text="Player total money : "+str(player_total))
    reinit()
    
player=Player()
player_cards=[]
dealer=Player()
dealer_cards=[]
player_total=50
player_bet=10
can_play=False
action=["Click on Game to start a new game",
        "Initial deal","Player action","Dealer's hand revealed","Bets settled"]

'''
GUI
'''
window = tk.Tk()
window.title("Blackjack")
frame=tk.Frame(window)
frame.pack(side=tk.TOP)
top = tk.Menu(window)
window.config(menu=top)
game = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=game)
game.add_command(label='New game', command=newGame)
game.add_command(label='Exit', command=window.destroy)
top.add_command(label='Rules',command=printRules)
top.add_command(label='About',command=about)

can = tk.Canvas(window,bg='black',height=600,width=500)
can.pack(side=tk.TOP,padx=5,pady=5)

but_hit = tk.Button(window,text='Hit',command=hit)
but_hit.pack(side=tk.LEFT)

but_stand = tk.Button(window,text='Stand',command=stand)
but_stand.pack(side=tk.LEFT)


lab_Message2=tk.Label(window,text="",fg="black")
lab_Message2.pack(side=tk.BOTTOM)
name='pictures/bankruptcy.gif'
imageBankruptcy=tk.PhotoImage(file=name)
lab_Message=tk.Label(frame,text=action[0],fg="black")
lab_Message.pack(side=tk.TOP)

window.mainloop()


