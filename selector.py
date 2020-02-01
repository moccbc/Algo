import pygame
class Selector:
    def __init__(self, x, y, width, height):
        self.height = height
        self.width = width
        self.color = (0, 255, 0)
        self.x = x - 5
        self.y = y - 5
        self.selection_id = 0

    def display(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def move_right(self, amount, id_limit):
        if self.selection_id < id_limit - 1:
            self.x += amount
            self.selection_id += 1

    def move_left(self, amount):
        if self.selection_id > 0:
            self.x -= amount
            self.selection_id -= 1

    def move_down(self, amount, id_limit):
        if self.selection_id < id_limit - 1:
            self.y += amount
            self.selection_id += 1

    def move_up(self, amount):
        if self.selection_id > 0:
            self.y -= amount
            self.selection_id -= 1 

    def get_selection(self):
        return self.selection_id

    def reset_position(self, x):
        self.selection_id = 0
        self.x = x
