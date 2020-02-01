import pygame
from selector import Selector
from network import Network
from screen import * 
import display

pygame.init()

WIDTH = 1050
HEIGHT = 700
WINDOW_SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(WINDOW_SIZE)

# Colors
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FONT = pygame.font.Font("fonts/bebasneue_regular.ttf", 50)

def text_box(window, game, p_num, choice, choice_selector, again_selector):
    font_size = 50
    message_font = pygame.font.Font("fonts/bebasneue_regular.ttf", font_size)
    if p_num == 0:
        pygame.draw.rect(window, WHITE, (20, 420, 1010, 260))  
    else:
        pygame.draw.rect(window, BLACK, (20, 420, 1010, 260))  
    pygame.draw.rect(window, GRAY, (30, 430, 720, 240))
    pygame.draw.rect(window, GRAY, (760, 430, 260, 240))
    if not game.is_gameover():
        if p_num == game.get_whos_turn():
            if not game.get_guess_correct():
                if p_num == 0:
                    text1 = message_font.render("Your turn", 1, BLACK, True)
                    text2 = message_font.render("Select a card and enter a number.", 1, BLACK, True)
                    text3 = message_font.render("Press enter to confirm.", 1, BLACK, True)
                    if len(choice) > 0:
                        if choice[0] == "0":
                            text4 = message_font.render("Your guess:" + choice[1], 1, BLACK, True)
                        else:
                            text4 = message_font.render("Your guess:" + choice, 1, BLACK, True)
                    else:
                        text4 = message_font.render("Your guess:", 1, BLACK, True)
                elif p_num == 1:
                    text1 = message_font.render("Your turn", 1, WHITE, True)
                    text2 = message_font.render("Select a card and enter a number.", 1, WHITE, True)
                    text3 = message_font.render("Press enter to confirm.", 1, WHITE, True)
                    if len(choice) > 0:
                        if choice[0] == "0":
                            text4 = message_font.render("Your guess:" + choice[1], 1, WHITE, True)
                        else:
                            text4 = message_font.render("Your guess:" + choice, 1, WHITE, True)
                    else:
                        text4 = message_font.render("Your guess:", 1, WHITE, True)
                texts = [text1, text2, text3, text4]
            else:
                choice_selector.display(window)
                if p_num == 0:
                    text1 = message_font.render("Guess is correct!", 1, BLACK, True)
                    text2 = message_font.render("Continue guessing?", 1, BLACK, True)
                    text3 = message_font.render("YES   NO", 1, BLACK, True)
                elif p_num == 1:
                    text1 = message_font.render("Guess is correct!", 1, WHITE, True)
                    text2 = message_font.render("Continue guessing?", 1, WHITE, True)
                    text3 = message_font.render("YES   NO", 1, WHITE, True)
                texts = [text1, text2, text3]
        else: 
            if p_num == 0:
                text1 = message_font.render("Opponent's turn", 1, BLACK, True)
                text2 = message_font.render("Opponent is selecting a card.", 1, BLACK, True)
            elif p_num == 1:
                text1 = message_font.render("Opponent's turn", 1, WHITE, True)
                text2 = message_font.render("Opponent is selecting a card.", 1, WHITE, True)
            texts = [text1, text2]
    else:
        if p_num == 0:
            if not game.get_player_respond(p_num):
                again_selector.display(window)
                text1 = message_font.render("Gameover", 1, BLACK, True)
                if p_num == game.get_whos_turn():
                    text2 = message_font.render("You won!", 1, BLACK, True)
                else:
                    text2 = message_font.render("You lost...", 1, BLACK, True)
                text3 = message_font.render("Play again?", 1, BLACK, True)
                text4 = message_font.render("YES   NO", 1, BLACK, True)
                texts = [text1, text2, text3, text4]
            else:
                text1 = message_font.render("Waiting for other player...", 1, BLACK, True)
                texts = [text1]
        if p_num == 1:
            if not game.get_player_respond(p_num):
                again_selector.display(window)
                text1 = message_font.render("Gameover", 1, WHITE, True)
                if p_num == game.get_whos_turn():
                    text2 = message_font.render("You won!", 1, WHITE, True)
                else:
                    text2 = message_font.render("You lost...", 1, WHITE, True)
                text3 = message_font.render("Play again?", 1, WHITE, True)
                text4 = message_font.render("YES   NO", 1, WHITE, True)
                texts = [text1, text2, text3, text4]
            else:
                text1 = message_font.render("Waiting for other player...", 1, WHITE, True)
                texts = [text1]

    y = 440
    for i in range(len(texts)):
        window.blit(texts[i], (40, y))
        y += font_size + 5 


def get_event(n, game, run, p_num, card_selector, choice_selector, again_selector):
    global CHOICE 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if not game.is_gameover():
            if not game.get_guess_correct():
                if event.type == pygame.KEYDOWN and game.get_whos_turn() == p_num:
                    if event.key == pygame.K_LEFT:
                        card_selector.move_left(80)
                    if event.key == pygame.K_RIGHT:
                        if (p_num == 1):
                            card_selector.move_right(80, game.get_player(0).get_hand_size())
                        if (p_num == 0):
                            card_selector.move_right(80, game.get_player(1).get_hand_size())
                    if event.key == pygame.K_BACKSPACE and len(CHOICE) != 0:
                        if (len(CHOICE) == 2 and CHOICE[0] == "0"):
                            CHOICE = ""
                        elif (len(CHOICE) == 2 and CHOICE[0] == "1"):
                            CHOICE = "0" + CHOICE[0]
                    if event.key == pygame.K_0:
                        if len(CHOICE) < 1:
                            CHOICE += "00" 
                        elif CHOICE == "01":
                            CHOICE = "10"
                    if event.key == pygame.K_1:
                        if len(CHOICE) < 1:
                            CHOICE += "01" 
                        elif CHOICE == "01":
                            CHOICE = "11"
                    if event.key == pygame.K_2 and len(CHOICE) < 1:
                        CHOICE += "02" 
                    if event.key == pygame.K_3 and len(CHOICE) < 1:
                        CHOICE += "03" 
                    if event.key == pygame.K_4 and len(CHOICE) < 1:
                        CHOICE += "04" 
                    if event.key == pygame.K_5 and len(CHOICE) < 1:
                        CHOICE += "05" 
                    if event.key == pygame.K_6 and len(CHOICE) < 1:
                        CHOICE += "06" 
                    if event.key == pygame.K_7 and len(CHOICE) < 1:
                        CHOICE += "07" 
                    if event.key == pygame.K_8 and len(CHOICE) < 1:
                        CHOICE += "08" 
                    if event.key == pygame.K_9 and len(CHOICE) < 1:
                        CHOICE += "09" 

                    if event.key == pygame.K_RETURN and CHOICE != "" and not(game.get_player(not(p_num)).get_revealed_to_opponent(card_selector.get_selection())):
                        card_selector_position = str(card_selector.get_selection())
                        if card_selector.get_selection() < 10:
                            card_selector_position = "0" + card_selector_position
                        game = n.send(str(p_num) + card_selector_position + CHOICE)
                        CHOICE = ""
            else: 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        choice_selector.move_left(70)
                    if event.key == pygame.K_RIGHT:
                        choice_selector.move_right(70, 2)
                    if event.key == pygame.K_RETURN:
                        if choice_selector.get_selection() == 0:
                            game = n.send("Continue guessing")
                        if choice_selector.get_selection() == 1:
                            game = n.send("Stop guessing")
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    again_selector.move_left(70)
                if event.key == pygame.K_RIGHT:
                    again_selector.move_right(70, 2)
                if event.key == pygame.K_RETURN:
                    if again_selector.get_selection() == 0:
                        game = n.send(str(p_num))
                    if again_selector.get_selection() == 1:
                        game = n.send("n")


CHOICE = ""
def game_screen(window):
    run = True
    clock = pygame.time.Clock()
    n = Network()
    p_num = int(n.get_p())
    print("You are player", p_num)
    card_selector = Selector(50, 50, 80, 110)
    choice_selector = Selector(40, 550, 70, 50)
    again_selector = Selector(40, 605, 70, 50)

    while run:
        window.fill(GRAY)

        # Try to get a game
        try:
            game = n.send("get")
        except:
            run = False
            print("Cannot get game")
            break


        # If there is only one person connected
        if not game.get_ready():
            wait_screen(window)
            pygame.display.update()

        elif game.get_ready():
            display.cards(window, game, p_num, card_selector)
            text_box(window, game, p_num, CHOICE, choice_selector, again_selector)
            pygame.display.update()

        if game.get_player(not(p_num)).is_all_revealed_to_opponent() and game.get_ready():
            game = n.send("Gameover")
        if game.get_both_respond():
            card_selector.reset_position(45)
            choice_selector.reset_position(35)
            again_selector.reset_position(35)
            game = n.send("Restart")

        get_event(n, game, run, p_num, card_selector, choice_selector, again_selector)
                    

def main():
    client_game_started = False
    client_started_game = home_screen(window)

    if client_started_game:
        game_screen(window)

main()
