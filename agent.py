import numpy as np
from random import randrange, choice, shuffle, sample
from time import time
from board import getsuccessor, place_chess, heuristic

class MinimaxAgent:

    def __init__(self, board, cards, max_depth, timelimit):
        self.board = board
        self.cards = cards
        self.depth_limit = 1
        self.max_depth = max_depth
        self.timelimit = timelimit
        self.startTime = 0
        self.TIMEOUT = False
        self.bestmove = (0, 0, 0)

    def is_terminal(self, cards, depth):
        if self.TIMEOUT:
            return True
        elif time() - self.startTime > self.timelimit:
            self.TIMEOUT = True
            return True
        elif depth == self.depth_limit or not len(cards):
            # (* depth limit cut-off *)
            return True
        else:
            return False

    def alphabeta(self, board, cards, curr_depth, a, b, isAI):
        # reach bottom, then compute the heuristic score of leaf
        if self.is_terminal(cards, curr_depth):
            return heuristic(board.copy(), cards.copy())

        if isAI:
            childnodes = getsuccessor(board, cards[cards>0])
            # For each child of node
            for child in childnodes.tolist():
                
                (next_board, next_cards) = place_chess(True, 
                                                       board.copy(), cards.copy(),
                                                       child[0], child[1], child[2])

                score = self.alphabeta(next_board, next_cards,
                                       curr_depth+1, a, b, False)
                if score >= b: return b # (* b cut-off *)
                if score > a:
                    a = score
                    if curr_depth == 0: # curr_depth+1 == 1
                        self.bestmove = (child[0], child[1], child[2])
            return a
        else:
            childnodes = getsuccessor(board, cards[cards<0])
            # For each child node
            for child in childnodes:
                (next_board, next_cards) = place_chess(True, 
                                                       board.copy(), cards.copy(),
                                                       child[0], child[1], child[2])
                score = self.alphabeta(next_board, next_cards,
                                       curr_depth+1, a, b, True)
                if score <= a: return a # (* a cut-off *)
                b = min(score, b)
            return b


    def move(self):
        self.startTime = time()
        # AI to make its turn
        cards = self.cards.copy()

        bestscore = -10000
        available = np.array(np.where(self.board==0)).T
        num = randrange(available.shape[0])
        bestmove = (available[num, 0],
                    available[num, 1],
                    choice(cards))

        for depth_limit in range(1, self.max_depth+1):
            
            if time() - self.startTime > self.timelimit: break
            
            self.depth_limit = depth_limit
            
            bestscore = self.alphabeta(self.board.copy(), self.cards.copy(), 
                                   curr_depth=0, a=-10000,b=10000, isAI=True)
            
            if self.TIMEOUT:
                self.TIMEOUT = False
                break
            bestmove = self.bestmove
        
        return bestmove