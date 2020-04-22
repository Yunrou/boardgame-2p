from copy import deepcopy
import numpy as np
from random import randrange, choice, shuffle, sample
from time import time
from threading import Timer
from state import State

class MinimaxAgent:


    def __init__(self, state, max_depth, timelimit):
        self.state = state
        self.depth_limit = 1
        self.max_depth = max_depth
        self.timelimit = timelimit
        self.startTime = 0
        self.TIMEOUT = False
        self.bestmove = (0, 0, 0)

    def is_terminal(self, state, depth):
        if self.TIMEOUT:
            return True
        elif time() - self.startTime > self.timelimit:
            self.TIMEOUT = True
            return True
        elif depth == self.depth_limit:
            # (* depth limit cut-off *)
            return True
        elif len(state) == 0:
            return True
        else:
            return False

    def alphabeta(self, state, curr_depth, a, b, isAI):
        # reach bottom, then compute the heuristic score of leaf
        if self.is_terminal(state, curr_depth):
            return state.heuristic()

        childnodes = state.getsuccessor()

        if isAI:
            bestscore = -1000
            # For each child of node
            for child in childnodes.tolist():
                next_state = deepcopy(state)
                next_state.place_chess(True, child[0], child[1], child[2])

                score = self.alphabeta(next_state, curr_depth+1, a, b, False)
                
                if curr_depth == 0: # curr_depth+1 == 1
                    if score > bestscore:
                        bestscore = score
                        self.bestmove = (child[0], child[1], child[2])
                    elif score == bestscore:
                        self.bestmove = sample((self.bestmove, 
                                               (child[0], child[1], child[2])), 1)[0]
                else:
                    bestscore = max(bestscore, score)
                
                a = max(a, bestscore)
                if a >= b:
                    break # (* b cut-off *)
            return bestscore
        else:
            bestscore = 1000
            # For each child node
            for child in childnodes:
                next_state = deepcopy(state)
                next_state.place_chess(False, child[0], child[1], child[2])
                bestscore = min(bestscore, self.alphabeta(next_state, curr_depth+1,a, b, True))
                b = min(b, bestscore)
                if a >= b:
                    break # (* a cut-off *)
            return bestscore


    def move(self):
        self.startTime = time()
        # AI to make its turn
        cards = deepcopy(self.state.ai_cards)

        bestscore = -100
        available = np.array(np.where(self.state.board_legal==True)).T
        num = randrange(available.shape[0])
        bestmove = (available[num, 0],
                    available[num, 1],
                    choice(cards))

        for depth_limit in range(1, self.max_depth+1):
            
            if time() - self.startTime > self.timelimit: break
            print("depthlimit:", depth_limit)
            self.depth_limit = depth_limit
            
            bestscore = self.alphabeta(deepcopy(self.state),
                                   curr_depth=0,
                                   a=-1000,
                                   b= 1000,
                                   isAI=True)
            print(self.bestmove)
            if self.TIMEOUT:
                self.TIMEOUT = False
                break
            bestmove = self.bestmove
            
        return bestmove