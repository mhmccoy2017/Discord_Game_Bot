'''
Contains two classes, Card and Deck intended for virtual
card games within the discord bot.
Card is an object that contains the values equivlent to
an actual card
Deck is an object containing a list of Cards that can be
Manipulated with popping and shuffling
'''

import random

class Card:
    '''
    Card Object, takes two arguements v for value and
    s for suit which are choosen from suits and values list
    '''
    suits = ["Spades",
             "Hearts",
             "Diamonds",
             "Clubs"]

    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, _v, _s):
        """suit + value are ints"""
        self.value = _v
        self.suit = _s

    #Less than function
    def __lt__(self, _c2):
        if self.value < _c2.value:
            return True
        if self.value == _c2.value:
            return bool(self.suit < _c2.suit)
        return False

    #Greater than function
    def __gt__(self, _c2):
        if self.value > _c2.value:
            return True
        if self.value == _c2.value:
            return bool(self.suit > _c2.suit)
        return False

    def __repr__(self):
        _v = self.values[self.value] + " of " + self.suits[self.suit]
        return _v

class Deck:
    '''
    Deck takes no arguments and will create a list of 52
    unique cards
    '''

	#Sets up an unshuffled deck
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))

    def remove_card(self):
        '''
        Pops a card from the deck object, takes no arguments
        returns the poped card
        '''
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def shuffle_deck(self):
        '''
        Shuffles the deck list takes no arguments
        returns nothing
        '''
        random.shuffle(self.cards)

   	#Will print the entire deck
    def __str__(self):
    	return f'{self.cards}'

    def __len__(self):
    	return len(self.cards)
