#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Define classes.
"""
from blackjack_functions import calculate_hand
import tkinter as tk
import random


colors = ['coeur', 'carreau', 'trefle', 'pique']
values = ['as', '2', '3', '4', '5', '6', '7',
          '8', '9', '10', 'valet', 'dame', 'roi']
repCards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Player(object):
    """
    A class to represent player/dealer.

    Methods
    -----------
    add_card(card)

    cards_number()

    total_hand()

    reinit()

    """
    def __init__(self):
        self.hand = []

    def getHand(self):
        return self.hand

    def add_card(self, card):
        card_id = values.index(card.getValue())
        self.hand.append(repCards[card_id])

    def cards_number(self):
        return len(self.hand)

    def total_hand(self):
        return calculate_hand(self.hand)

    def reinit(self):
        self.hand = []


class Card(object):
    """
    A class to represent a card.
    
    Methods
    -----------
    """
    def __init__(self, val='as', col='carreau'):
        self.value = val
        self.color = col

    def getValue(self):
        return self.value

    def display(self):
        print("{} de {}".format(self.value, self.color))

    def picture(self):
        name = 'pictures/' + self.value + '_' + self.color + '.gif'
        return tk.PhotoImage(file=name)


class Pack52cards(object):
    """
    A class to represent a pack of 52 cards.

    Methods
    -----------
    shuffle_pack()
        Shuffle the pack of cards.
    pick_card()
        Remove the first card of the remaining pack.
    """
    def __init__(self) -> None:
        """
        Build the pack of 52 cards.

        Returns
        -------
        None.

        """
        self.cards = []
        for value in values:
            for color in colors:
                card = Card(value, color)
                self.cards.append(card)

    def shuffle_pack(self) -> None:
        """
        Shuffle the pack of cards.

        Returns
        -------
        None.

        """
        random.shuffle(self.cards)

    def pick_card(self) -> Card():
        """
        Remove the first card of the remaining pack.

        Returns
        -------
        card : Card
            First card of the remaining pack.
        """
        if len(self.cards) > 0:
            card = self.cards.pop(0)
            return card
        else:
            return None
