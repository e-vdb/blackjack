#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define classes."""
from blackjack_functions import calculate_hand
import tkinter as tk
import random


colors = ['coeur', 'carreau', 'trefle', 'pique']
values = ['as', '2', '3', '4', '5', '6', '7',
          '8', '9', '10', 'valet', 'dame', 'roi']
repCards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card():
    """
    A class to represent a card.

    Methods
    -----------
    picture
        Return the Image of the card.
    """
    def __init__(self, val='as', col='carreau'):
        """
        Assign the value and color of the card.

        Parameters
        ----------
        val : str, optional
            Card value. The default is 'as'.
        col : str, optional
            Card color. The default is 'carreau'.

        Returns
        -------
        None.

        """
        self.value = val
        self.color = col

    def picture(self):
        """
        Return the Image of the card.

        Load the gif picture of the card and return the PhotoImage.

        Returns
        -------
        PhotoImage
            Picture for the GUI.fk
        """
        name = 'pictures/' + self.value + '_' + self.color + '.gif'
        return tk.PhotoImage(file=name)


class Pack52cards():
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


class Player():
    """
    A class to represent player/dealer.

    Methods
    -----------
    add_card(card)
        Add a card to player hand.
    cards_number()
        Return the number of cards in player hand.
    total_hand()
        Return the value of the player hand.
    reinit()
        Reset the player hand (empty list).
    """
    def __init__(self):
        """
        Constructor.

        Returns
        -------
        None.

        """
        self.hand = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to player hand.

        Parameters
        ----------
        card : Card
            Card.

        Returns
        -------
        None.

        """
        card_id = values.index(card.value)
        self.hand.append(repCards[card_id])

    def cards_number(self) -> int:
        """
        Return the number of cards in player hand.

        Returns
        -------
        int
            DESCRIPTION.

        """
        return len(self.hand)

    def total_hand(self) -> int:
        """
        Return the value of the player hand.

        Returns
        -------
        int
            Value of the player hand.

        """
        return calculate_hand(self.hand)

    def reinit(self):
        """
        Reset the player hand (empty list).

        Returns
        -------
        None.
        """
        self.hand = []
