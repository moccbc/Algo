from card import Card
import random

class Deck:
    def __init__(self):
        self.deck = []
        self.top = 0

    def fill_deck(self):
        for i in range(12):
            self.deck.append(Card(i, 'w'))
        for i in range(12):
            self.deck.append(Card(i, 'b'))

        self.top = 23

    def shuffle_deck(self):
        for k in range (500):
            c1 = random.randint(0,23)
            c2 = random.randint(0,23)

            temp = self.deck[c1]
            self.deck[c1] = self.deck[c2]
            self.deck[c2] = temp

    
    def draw_card(self):
        self.deck[self.top].set_newest(1)
        card = self.deck[self.top]
        self.top -= 1
        return card

    def is_empty(self):
        empty = True 
        if self.top > -1:
            empty = False

        return empty

    def display(self, window, x, y):
        self.deck[self.top].display(window, x, y)

    def empty_deck(self):
        self.deck = []
        self.top = 0
