from constants import SUITS, RANKS, PRINTED
from itertools import product
from random import shuffle


class Card:
    def __init__(self, suit, rank, picture, points):
        self.suit = suit
        self.rank = rank
        self.picture = picture
        self.points = points

    def __str__(self):
        return str(self.picture) + '\nPoints:'+ str(self.points)
        

class Deck:
    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    def _generate_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10   
            picture = PRINTED.get(rank)  
            card = Card(suit=suit, rank=rank, points=points, picture=picture)
            cards.append(card)
        return cards
    
    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


