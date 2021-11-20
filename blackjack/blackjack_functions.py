#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define functions for Blackjack game."""

from typing import List

def calculate_hand(hand: List[str]) -> int:
    '''
    Return the value of the hand.

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
    listFig = ['J','Q','K']
    tot_hand = 0
    nbAces = 0
    for card in hand:
        if card in listFig:
            tot_hand += 10
        elif card == 'A':
            nbAces += 1
        else:
            tot_hand += int(card)
    if nbAces != 0:
        test = tot_hand+(nbAces-1)+11
        if test <= 21:
            tot_hand = test
        else:
            tot_hand += nbAces
    return tot_hand


def blackjack_hand_greater_than(hand_1, hand_2) -> bool:
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points.
    Face cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Function description from Kaggle Python course Lesson 7 Working
    with External Libraries (exercice 3).

    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    if calculate_hand(hand_1) > 21:
        return False
    elif calculate_hand(hand_1) > calculate_hand(hand_2) or calculate_hand(hand_2) > 21:
        return True
    else:
        return False
