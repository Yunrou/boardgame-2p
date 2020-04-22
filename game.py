import os
import time
from threading import Timer
from copy import deepcopy
import numpy as np

from state import State
from agent import MinimaxAgent

CARDS = {4: np.array([2, 3, 5, 8, 13]), 6: np.array([2, 2, 3, 3, 5, 5, 8, 8, 8, 13, 13])}
TIMEOUT = 15

def max_depth(boardsize, AI_first):
    if boardsize == 4:
        if AI_first: return 10
        else: return 9
    else:
        if AI_first: return 22 
        else: return 21 

os.system("")

while True:
    
    # a.
    turn = int(input("User first? (0/1): "))
    if turn not in (0, 1):
        continue
    
    # b. Initialize board
    boardsize = int(input("Board Size? (4 or 6): "))
    if boardsize not in (4, 6):
        continue
    

    board_user = np.zeros((boardsize, boardsize), dtype=np.int8)
    board_ai = np.zeros((boardsize, boardsize), dtype=np.int8)
    board_legal = np.full((boardsize, boardsize), True, dtype=bool)

    # c.
    user_cards, ai_cards = deepcopy(CARDS[boardsize]), deepcopy(CARDS[boardsize])

    B = State(boardsize, board_user, board_ai, board_legal, user_cards, ai_cards)
    B.display_board()
    B.display_cards()
    
    depth = max_depth(boardsize, not turn)

    while True:
        print("")
        if turn == 1:
            # user turn
            while True:
                row, col, weight = [int(i) for i in input("Input (row, col, weight): ").split(' ')]

                if B.place_chess(False, row, col, weight):
                    break
                
                print("Oops! Wrong input ...")

            print("[User]: ("+str(row)+", "+str(col)+", "+str(weight)+")")
            # B.check()

            B.display_board()
            B.display_cards()

            turn = 0
        else:

            agent = MinimaxAgent(deepcopy(B), depth, TIMEOUT)
            # t = Timer(TIMEOUT, print, ['Sorry, times up'])
            # t.start()
            # choose the bestmove
            (row, col, weight) = agent.move()
            # t.cancel()
            print(row, col, weight)
            B.place_chess(True, row, col, weight)
            print("[AI]: ("+str(row)+", "+str(col)+", "+str(weight)+")")
            # B.check()
            B.display_board()
            B.display_cards()
            
            depth -= 2
            turn = 1
        

        if B.check_end():
            win = B.win_check()
            if win == 'user':
                print('User Win')
            elif win == 'ai':
                print('AI Win')
            else:
                print('Draw')
            break

    break