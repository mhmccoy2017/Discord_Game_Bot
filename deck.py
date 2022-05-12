import random

class Card:
    suits = ["Spades",
             "Hearts",
             "Diamonds",
             "Clubs"]
    
    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    #Less than function	
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    #Greater than function    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:

	#Sets up an unshuffled deck
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))

    #Will pop a card from the deck
    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

    #Shuffles the deck randomly
    def shuffle_deck(self):
    	random.shuffle(self.cards)

   	#Will print the entire deck
    def __str__(self):
    	return f'{self.cards}'