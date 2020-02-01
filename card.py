import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.revealed_to_you = False
        self.revealed_to_opponent = False
        self.newest = False
        self.width = 70
        self.height = 100

    def get_color(self):
        return self.color

    def get_number(self):
        return self.number

    def set_newest(self, state):
        if state:
            self.newest = True
        else:
            self.newest = False
     
    def display(self, win, x, y):
        if self.newest:
            pygame.draw.rect(win, (0, 0, 255), (x, y-5, self.width, 5))

        if self.color == 'b':
            pygame.draw.rect(win, BLACK, (x, y, self.width, self.height))
        else: 
            pygame.draw.rect(win, WHITE, (x, y, self.width, self.height))

        if self.revealed_to_you:
            font = pygame.font.Font('fonts/bebasneue_bold.ttf', 70)
            if self.color == 'w':
                number = font.render(str(self.number), True, BLACK)
            elif self.color == 'b':
                number = font.render(str(self.number), True, WHITE)
            if self.revealed_to_opponent:
                pygame.draw.rect(win, (255, 0, 0), (x, y+self.height, self.width, 5)) 
            number_rect = number.get_rect()
            number_rect.center = (x + self.width // 2, y + self.height // 2 + 5)
            win.blit(number, number_rect)
    
    def set_revealed_to_you(self, state):
        if state:
            self.revealed_to_you = True
        else:
            self.revealed_to_you = False

    def set_revealed_to_opponent(self, state):
        if state:
            self.revealed_to_opponent = True
        else:
            self.revealed_to_opponent = False

    def get_revealed_to_opponent(self):
        return self.revealed_to_opponent
