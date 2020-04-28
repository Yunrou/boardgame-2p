import os
import numpy as np

from board import display_board, display_cards, place_chess, win_check
from agent import MinimaxAgent

CARDS = {4: np.array([2, 3, 5, 8, 13, 
                      -2, -3, -5, -8, -13]), 
         6: np.array([2, 2, 3, 3, 5, 5, 8, 8, 8, 13, 13,
                      -2, -2, -3, -3, -5, -5, -8, -8, -8, -13, -13])}
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
    turn = int(input("User first? (0/1): ").split(' ')[0])
    if turn not in (0, 1):
        continue
    
    # b. Initialize board
    boardsize = int(input("Board Size? (4 or 6): ").split(' ')[0])
    if boardsize not in (4, 6):
        continue
    

    board = np.zeros((boardsize, boardsize), dtype=np.int8)
    # c. Initialized cards
    cards = CARDS[boardsize].copy()

    display_board(board)
    display_cards(cards)
    
    depth = max_depth(boardsize, not turn)

    while True:
        print("")
        if turn == 1:
            # user turn
            while True:
                row, col, weight = [int(i) for i in input("Input (row, col, weight): ").split(' ')[:3]]

                next_state = place_chess(False, board.copy(), cards.copy(), 
                                         row, col, -weight)
                if isinstance(next_state, tuple):
                    (board, cards) = next_state 
                    break
                print("Oops! Wrong input ...")

            print("\n\x1b[92m[User]:\x1b[0m ("+str(row)+", "+str(col)+", "+str(weight)+")")

            display_board(board)
            display_cards(cards)

            turn = 0
        else:

            agent = MinimaxAgent(board.copy(), cards.copy(), depth, TIMEOUT)
            # t = Timer(TIMEOUT, print, ['Sorry, times up'])
            # t.start()
            # choose the bestmove
            (row, col, weight) = agent.move()
            # t.cancel()
            (board, cards) = place_chess(True, board.copy(), cards.copy(), 
                                         row, col, weight)
            print("\n\x1b[93m[AI]:\x1b[0m ("+str(row)+", "+str(col)+", "+str(weight)+")")
            # B.check()
            display_board(board)
            display_cards(cards)
            
            depth -= 2
            turn = 1
        

        if not len(cards): # empty
            win = win_check(board)
            if win == 'user':
                print('User Win')
            elif win == 'ai':
                print('AI Win')
            else:
                print('Draw')
            break

    break