import pygame
from selector import Selector
pygame.font.init()

WIDTH = 1050
HEIGHT = 700

# Colors
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FONT = pygame.font.Font("fonts/bebasneue_regular.ttf", 50)

def home_screen(window):
    algo_font = pygame.font.Font("fonts/bebasneue_regular.ttf", 80)
    sq_font = pygame.font.Font("fonts/bebasneue_regular.ttf", 50)
    text_algo = algo_font.render("ALGO", 1, WHITE, True)
    text_start = sq_font.render("Start Game", 1, BLACK, True)
    text_quit = sq_font.render("Quit Game", 1, BLACK, True)
    text_algo_rect = text_algo.get_rect(center=(WIDTH/2, HEIGHT/2-40))
    text_start_rect = text_start.get_rect(center=(WIDTH/2, HEIGHT/2+80))
    text_quit_rect = text_quit.get_rect(center=(WIDTH/2, HEIGHT/2+130))
    home_selector = Selector(430, 405, 200, 50)
    display_home = True 

    while display_home:
        window.fill(GRAY)
        home_selector.display(window)
        window.blit(text_algo, text_algo_rect)
        window.blit(text_start, text_start_rect)
        window.blit(text_quit, text_quit_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                display_home = False 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    home_selector.move_up(50) 
                if event.key == pygame.K_DOWN:
                    home_selector.move_down(50, 2)
                if event.key == pygame.K_RETURN:
                    if home_selector.get_selection() == 0:
                        display_home = False 
                        return True
                    if home_selector.get_selection() == 1:
                        display_home = False 
                        pygame.quit()
                        return False

def wait_screen(window):
    text_waiting = FONT.render("Waiting for another player to join...", 1, BLACK, True)
    text_waiting_rect = text_waiting.get_rect(center=(WIDTH/2, HEIGHT/2))
    window.blit(text_waiting, text_waiting_rect)

