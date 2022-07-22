from deck import Deck
from game import Game
from player import Bot


if __name__ == '__main__':
    
    game = Game()
    game.begin_game()

    print('\n\nDONE ')

    for pl in game.players:
        pl.show_cards()
        if isinstance(pl, Bot):
            print('Max points', pl.max_points)
        print('----------------------------')
