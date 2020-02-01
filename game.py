import random
from player import Player
from deck import Deck

class Game:
    def __init__(self, game_id):
        self.id = game_id
        self.ready = False
        self.deck = Deck()
        self.p0 = Player()
        self.p1 = Player()
        self.whos_turn = 0
        self.gameover = False
        self.guess_correct = False 
        self.play_again = False
        self.p0_responded = False
        self.p1_responded = False

    def get_ready(self):
        return self.ready
    
    def set_ready(self, state):
        self.ready = state

    # Function to start the game
    def start_game(self):
        self.deck.fill_deck()
        self.deck.shuffle_deck()
        for i in range(8):
            if i % 2 == 0:
                self.p0.draw_card(self.deck)
            else:
                self.p1.draw_card(self.deck)

        self.whos_turn = random.randint(0,1)
        if self.whos_turn:
            self.p1.draw_card(self.deck)
        else:
            self.p0.draw_card(self.deck)

    def get_whos_turn(self):
        return self.whos_turn

    def get_player(self, p_num):
        if p_num:
            return self.p1
        else:
            return self.p0

    def display_deck(self, window, x, y):
        self.deck.display(window, x, y)

    def guess_num(self, player, position, guess):
        if player:
            opponent_hand = self.p0.get_hand()
            your_hand = self.p1.get_hand()
        else:
            opponent_hand = self.p1.get_hand()
            your_hand = self.p0.get_hand()

        if opponent_hand[position].get_number() == guess: 
            opponent_hand[position].set_revealed_to_you(1)
            opponent_hand[position].set_revealed_to_opponent(1)
            return True
        else:
            your_hand[position].set_revealed_to_you(1)
            your_hand[position].set_revealed_to_opponent(1)
            return False

    def get_guess_correct(self):
        return self.guess_correct 

    def set_guess_correct(self, state):
        self.guess_correct = state

    def switch_turn(self):
        self.whos_turn = not self.whos_turn

    def get_deck(self):
        return self.deck

    def set_gameover(self, state):
        self.gameover = state

    def is_gameover(self):
        return self.gameover

    def get_both_respond(self):
        return self.p0_responded and self.p1_responded

    def get_player_respond(self, p_num):
        if p_num:
            return self.p1_responded
        else:
            return self.p0_responded

    def set_player_responded(self, p_num, state):
        if p_num:
            self.p1_responded = state
        else:
            self.p0_responded = state

    def restart_game(self):
        self.deck.empty_deck()
        self.p1.empty_hand()
        self.p0.empty_hand()
        self.gameover = False
        self.guess_correct = False 
        self.play_again = False
        self.p0_responded = False
        self.p1_responded = False
        self.ready = False

        self.start_game()
        self.ready = True
