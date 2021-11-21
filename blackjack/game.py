#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define class Game."""

from blackjack_classes import Player, Pack52cards
from blackjack_functions import blackjack_hand_greater_than
import tkinter as tk
from time import sleep


action=["Click on Game to start a new game",
        "Initial deal","Player action","Dealer's hand revealed","Bets settled"]

class Game:
    def __init__(self, canvas, lab_Message, lab_Message2, window, imageBankruptcy):
        self.player = Player()
        self.player_cards = []
        self.dealer = Player()
        self.dealer_cards = []
        self.player_total = 50
        self.player_bet = 10
        self.can_play = False
        self.can = canvas
        self.lab_Message = lab_Message
        self.lab_Message2 = lab_Message2
        self.window = window
        self.imageBankruptcy = imageBankruptcy
        
    def reinit(self):
        self.lab_Message.configure(text=action[1])
        self.can.delete(tk.ALL)
        self.can.create_text(60,30, text="Dealer", fill='white', font='Arial 18')
        self.can.create_text(60, 470, text='Player', fill='white', font='Arial 18')
        self.pack = Pack52cards()
        self.pack.shuffle_pack()
        self.dealer.reinit()
        self.player.reinit()
        self.dealer_cards=[]
        self.player_cards=[]
        self.p_x = 100
        card1 = self.pack.pick_card()
        self.dealer_cards.append(card1.picture())
        sleep(1)
        self.can.create_image(100, 150, image=self.dealer_cards[0])
        self.can.update()
        self.dealer.add_card(card1)
        self.dealer_score = self.can.create_text(150, 30, text=str(self.dealer.total_hand()),
                                                 fill='white', font='Arial 18')
        card2 = self.pack.pick_card()
        self.player_cards.append(card2.picture())
        sleep(1)
        self.can.create_image(self.p_x, 350, image=self.player_cards[0])    
        self.can.update()
        self.p_x += 20
        self.player.add_card(card2)
        card3 = self.pack.pick_card()
        self.player_cards.append(card3.picture())
        sleep(1)
        self.can.create_image(self.p_x, 350, image=self.player_cards[1])
        self.can.update()
        self.player.add_card(card3)
        self.player_score = self.can.create_text(150, 470, text=str(self.player.total_hand()),
                                          fill='white', font='Arial 18')
        self.can_play = True
        if self.player.total_hand() == 21:
            self.can.create_text(250, 470, text="Blackjack", fill='red',font='Arial 22')
            self.window.after(100, self.stand)
        else:
            self.lab_Message.configure(text=action[2])          

    def stand(self):
        self.lab_Message.configure(text=action[3])
        if self.can_play:
            d_x = 120
            while self.dealer.total_hand() < 17:
                sleep(1)
                newCard = self.pack.pick_card()
                self.dealer_cards.append(newCard.picture())
                self.dealer.add_card(newCard)
                self.can.create_image(d_x, 150, image=self.dealer_cards[-1])    
                d_x += 20
                self.can.delete(self.dealer_score)
                self.dealer_score = self.can.create_text(150, 30,
                                                         text=str(self.dealer.total_hand()),
                                                         fill='white',font='Arial 18')
                self.can.update()
                if self.dealer.total_hand() == 21 and self.dealer.cards_number() == 2:
                    self.can.create_text(250, 30, text="Blackjack", fill='red', font='Arial 22')
            self.window.after(100, self.winner)
            self.can_play = False
    
    def hit(self):
        if self.can_play:
            self.p_x += 20
            newCard = self.pack.pick_card()
            self.player_cards.append(newCard.picture())
            self.player.add_card(newCard)
            self.can.create_image(self.p_x, 350, image=self.player_cards[-1])
            self.can.delete(self.player_score)
            self.player_score = self.can.create_text(150, 470,
                                                     text=str(self.player.total_hand()),
                                                     fill='white',font='Arial 18')
            self.can.update()
            if self.player.total_hand()>21:
                self.lab_Message.configure(text=action[4])
                self.player_total -= self.player_bet
                self.can.create_text(200,550,text="Dealer wins",fill='red',font='Arial 22')
                self.lab_Message2.configure(text="Player total money : "+str(self.player_total))
                self.can_play = False
                if self.player_total >= 10:
                    self.window.after(2000, self.endGame)
                else:
                    self.window.after(2000, self.bankruptcy)

    def endGame(self):
        continueWindow = tk.Toplevel()
        continueWindow.title("Continue game ?")
        lab_end = tk.Label(continueWindow,text='Do you want to continue playing ?')
        lab_end.pack(side=tk.TOP)
        but_yes = tk.Button(continueWindow,text='Yes', fg='white', bg='black', 
                            command=lambda: self.continueGame(continueWindow))
        but_yes.pack(side=tk.LEFT)
        but_no = tk.Button(continueWindow,text='No',fg='white',bg='black',
                           command=lambda: self.exitAll(continueWindow))
        but_no.pack(side=tk.LEFT)
        continueWindow.mainloop()                          
        
    def continueGame(self, continueWindow):
        continueWindow.destroy()
        self.reinit()
    
    def exitAll(self, continueWindow):
        continueWindow.destroy()
        self.can.delete(tk.ALL)
        self.lab_Message2.configure(text="")
        self.lab_Message.configure(text=action[0])
    
    def bankruptcy(self):
        self.can.delete(tk.ALL)
        self.can.create_text(250,550,text="Bankruptcy!!!",fill='red',font='Arial 22')
        self.can.create_image(250,250,image = self.imageBankruptcy)
        self.lab_Message.configure(text=action[0])
    
    def newGame(self):
        self.player_total = 50
        self.lab_Message2.configure(text="Player total money : "+ str(self.player_total))
        self.reinit()

    def winner(self):
        self.lab_Message.configure(text=action[4])
        if blackjack_hand_greater_than(self.player.getHand(),self.dealer.getHand()):
            self.player_total += 2*self.player_bet
            self.can.create_text(200,550,text="Player wins",fill='red',font='Arial 22')
        else:
            self.player_total -= self.player_bet
            self.can.create_text(200, 550, text="Dealer wins", fill='red', font='Arial 22')
        self.lab_Message2.configure(text="Player total money : "+str(self.player_total))
        if self.player_total >= 10:
            self.window.after(2000,self.endGame)
        else:
            self.window.after(2000,self.bankruptcy)
