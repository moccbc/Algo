class Player:
    def __init__(self):
        self.hand = [] 
 
    def sort_hand(self):
        for i in range(len(self.hand)):
            min_index = i
            for j in range(i+1, len(self.hand)):
                if self.hand[j].get_number() < self.hand[min_index].get_number():
                    min_index = j

            self.hand[i], self.hand[min_index] = self.hand[min_index], self.hand[i]

        for i in range(len(self.hand)-1):
            if self.hand[i].get_number() == self.hand[i+1].get_number():
                if self.hand[i].get_color() == 'w' and self.hand[i+1].get_color() == 'b':
                    self.hand[i], self.hand[i+1] = self.hand[i+1], self.hand[i]

    def draw_card(self, deck):
        for i in range(len(self.hand)):
            self.hand[i].set_newest(0)
        self.hand.append(deck.draw_card())
        self.sort_hand()

    def display(self, win, x, y):
        offset = 0
        for i in range(len(self.hand)):
            self.hand[i].display(win, x+offset, y)
            offset += 80

    def reveal_card(self, index):
        self.hand[index].set_revealed_to_you(1)

    def reveal_card_opponent(self, index):
        self.hand[index].set_revealed_to_opponent(1)

    def reveal_all(self):
        for i in range(len(self.hand)):
            self.hand[i].set_revealed_to_you(1)

    def get_hand(self):
        return self.hand

    def get_hand_size(self):
        return len(self.hand)

    def get_revealed_to_opponent(self, position):
        return self.hand[position].get_revealed_to_opponent()

    def is_all_revealed_to_opponent(self):
        for i in range(len(self.hand)):
            if not self.hand[i].get_revealed_to_opponent():
                return False 
        return True

    def empty_hand(self):
        self.hand = []
