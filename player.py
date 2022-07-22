import abc
import random
from deck import Deck
from constants import NAMES, MESSAGES



class AbstractPlayer(abc.ABC):
    def __init__(self):
        self.cards = []
        # self.position = position
        self.bet = 0
        self.total_points = 0
        self.money = 100

    def change_points(self):
        # for card in self.cards:
        #     self.total_points += int(card.points)
        self.total_points = sum([card.points for card in self.cards])
        # return self.total_points    
   
    def take_card(self, card):
        self.cards.append(card)
        self.change_points()

    @abc.abstractmethod
    def change_bet(self, max_bet, min_bet):
        pass

    @abc.abstractmethod
    def ask_card(self):
        pass

    def show_cards(self):
        print(self, 'cards: ')
        for card in self.cards:
            print(card)
        print('Total: ', self.total_points, ' points\n =================')
    
    def __str__(self):
        pass


class Player(AbstractPlayer):    
    def change_bet(self, max_bet, min_bet):
        while True:
            value = int(input("What's your bet? "))
            if value <= max_bet and value >= min_bet:
                self.bet = value
                self.money -= self.bet
                break
            else:
                print("Choose a bet between 0$ and 20$: ")
        print("You give: ", self.bet)

    def ask_card(self):        
        choice = input(MESSAGES.get('ask_card'))
        if choice == 'y':
            return True 
        else: 
            return False

    def __str__(self):
        return "You "


class Dealer(AbstractPlayer):
    max_points = 17

    def change_bet(self, max_bet, min_bet):
        raise Exception("Dealer doesn't make bets ")

    def ask_card(self):
        if self.total_points < self.max_points:
            return True
        else:
            return False

    def __str__(self):
        return "Dealer "


class Bot(AbstractPlayer):
    def __init__(self, number):
        super().__init__()
        self.max_points = random.randint(16, 20)    
        self.number = number

    def __str__(self):
        return NAMES[self.number]

    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        print(self, 'gives: ', self.bet)

    def ask_card(self):
        if self.total_points < self.max_points:
            return True
        else:
            return False
