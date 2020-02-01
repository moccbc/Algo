def cards(window, game, p_num, card_selector):
    if game.get_whos_turn() == p_num:
        card_selector.display(window)
    # If it is player 1
    if p_num == 1:
        game.get_player(1).reveal_all()
        game.get_player(0).display(window, 50, 50)
        game.get_player(1).display(window, 50, 310)
    # If it is player 0
    else:
        game.get_player(0).reveal_all()
        game.get_player(1).display(window, 50, 50)
        game.get_player(0).display(window, 50, 310)

    game.display_deck(window, 490, 180)
