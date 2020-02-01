import socket
from game import Game
from _thread import *
import pickle
import random

# Home IP
#server = "192.168.1.40"
# UCR IP
server = "10.13.201.251"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started. Waiting for connection...")

games = {}
id_count = 0

def threaded_client(conn, p, game_id):
    global id_count
    conn.send(str.encode(str(p)))

    while True:
        try:
            data = conn.recv(4096).decode()
            if data != "get":
                print("Received:", data)
            
            if game_id in games:
                game = games[game_id]

                if not data:
                    break
                elif len(data) == 5: 
                    player = int(data[0])
                    position = int(data[1]) * 10 + int(data[2])
                    guess = int(data[3]) * 10 + int(data[4])
                    if game.guess_num(player, position, guess):
                        game.set_guess_correct(1) 
                    else:
                        game.switch_turn()
                        game.get_player(not(player)).draw_card(game.get_deck())
                elif data == "Continue guessing":
                    game.set_guess_correct(0) 
                elif data == "Stop guessing":
                    game.set_guess_correct(0) 
                    game.switch_turn()
                    game.get_player(not(player)).draw_card(game.get_deck())
                elif data == "Gameover":
                    game.set_gameover(1)
                elif data == "0" or data == "1":
                    game.set_player_responded((data == "1"), 1)
                elif data == "n":
                    del games[game_id]
                elif data == "Restart":
                    game.restart_game() 
                    
            else:
                break

            conn.sendall(pickle.dumps(game))

        except:
            break

    print("Lost connection")
    try:
        del games[game_id]
        print("Closing game", game_id)
    except:
        pass

    id_count -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    id_count += 1
    p = 0 
    game_id = (id_count - 1) // 2
    if id_count % 2 == 1:
        games[game_id] = Game(game_id)
        games[game_id].start_game()
        print("Creating a new game...")
    else:
        games[game_id].set_ready(1) 
        p = 1

    start_new_thread(threaded_client, (conn, p, game_id))
