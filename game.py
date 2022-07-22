import player
from player import Bot, Dealer, Player
from constants import MESSAGES
from deck import Deck
import random


class Game:
    MAX_PL_COUNT = 4

    def __init__(self):
        self.players = []
        self.player = None
        self_player_pos = None
        self.dealer = Dealer()
        self.general_amount = 1
        self.deck = Deck()
        self.min_bet = 0
        self.max_bet = 20

    @staticmethod
    def _ask_beginnig(message):
        while True:
            choise = input(message)
            if choise == 'n':
                return False
            elif choise == 'y':
                return True
            else:
                print('Choose, please, one of given options: ')

    def _launch(self):
        while True:
            bots_amount = int(input('Enter the number of bots. please: '))
            if bots_amount <= self.MAX_PL_COUNT - 1:
                break
        self.general_amount = bots_amount + 1
        for i in range(bots_amount):
            bot = Bot(number=i)
            self.players.append(bot)
            print(bot, 'is created ')
        self.player = Player()
        self.player_pos = random.randint(0, self.general_amount)
        print('Your position is ', self.player_pos)
        self.players.insert(self.player_pos, self.player)

    def ask_bet(self):
        for player in self.players:            
            print("Current money:", player.money, "$")
            if player.money <= 0:
                print(player, "cannot continue playing because of money lack. ")
                self.players.remove(player)
            player.change_bet(self.max_bet, self.min_bet)

    def first_descr(self):
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)
        card = self.deck.get_card()
        self.dealer.take_card(card)
        self.dealer.show_cards()

    def check_stop(self, player):         
        if player.total_points >= 21:            
            return True
        else:           
            return False

    def remove_player(self, player):
        player.show_cards()
        print(player, 'has got overscore and has lost\n')
        self.players.remove(player)

    def ask_cards(self):
        for player in self.players:
            while player.ask_card():
                card = self.deck.get_card()
                player.take_card(card)
                is_stop = self.check_stop(player)
                if is_stop: 
                    if player.total_points > 21:                    
                        self.remove_player(player)
                    break
                if isinstance(player, Player):                    
                    player.show_cards()

    def present_winners(self, winner_list):
        for winner in winner_list:
            winner.money += winner.bet * 2
                    
    def check_winner(self):
        if self.dealer.total_points > 21:
            print("Dealer has got overscore, all players win!\n")
            for winner in self.players:
                winner.money += winner.bet * 2                
                print(winner, ": ", winner.money, "$\n")                                     
        else:
            for player in self.players:
                if player.total_points == self.dealer.total_points:                    
                    player.money += player.bet
                    print(MESSAGES.get('equal').format(player=player, points = player.total_points), '\n')
                    print(player, ": ", player.money, "$\n")
                elif player.total_points > self.dealer.total_points:
                    player.money += player.bet * 2
                    print(MESSAGES.get('win').format(player=player), '\n')
                    print(player, ": ", player.money, "$\n")
                elif player.total_points < self.dealer.total_points:
                    print(MESSAGES.get('lose').format(player=player), '\n')
                    
    def play_with_dealer(self):
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
        self.dealer.show_cards()

    def begin_game(self):
        message = MESSAGES.get('ask_start')
        if not self._ask_beginnig(message=message):
            exit(1)

        self._launch()
        while True:
            self.ask_bet()
            self.first_descr()
            self.player.show_cards()
            self.ask_cards()
            self.play_with_dealer()
            self.check_winner()
            if not self._ask_beginnig(MESSAGES.get('rerun')):
                break
            else:
                for player in self.players:
                    player.cards.clear()
                self.dealer.cards.clear()
       