from copy import deepcopy
import numpy as np
from random import randrange, choice, shuffle
from state import State
import time

class MinimaxAgent:


    def __init__(self, state, max_depth, timelimit):
        self.state = state
        self.depth_limit = 1
        self.max_depth = max_depth
        self.timelimit = timelimit
        self.bestmove = (0, 0, 0)

    def get(self):
        pass

    def is_terminal(self, state, depth):
        if depth == self.depth_limit:
            # (* depth limit cut-off *)
            return True
        elif len(state) == 0:
            return True
        else:
            return False


    def minimax(self, state, curr_depth, isMaximizing):

        # reach bottom, then compute the heuristic score of leaf
        if self.is_terminal(state, curr_depth):
            return state.heuristic()

        if isMaximizing:
            bestscore = -100
            cards = state.ai_cards
            available = np.array(np.where(state.board_legal==True)).T

            for [i, j] in available:
                for c in cards:
                    next_state = deepcopy(state)
                    next_state.place_chess(False, i, j, c)
                    score = self.minimax(next_state, curr_depth+1, False)
                    bestscore = max(score, bestscore)
        else:
            bestscore = -100
            cards = state.user_cards
            available = np.array(np.where(state.board_legal==True)).T
            
            for [i, j] in available:
                for c in cards:
                    next_state = deepcopy(state)
                    next_state.place_chess(True, i, j, c)
                    score = self.minimax(next_state, curr_depth+1, True)
                    bestscore = min(score, bestscore)

        return bestscore

    def alphabeta(self, state, curr_depth, a, b, isMaximizing):
        # reach bottom, then compute the heuristic score of leaf
        if self.is_terminal(state, curr_depth):
            return state.heuristic()

        if isMaximizing:
            value = -100
            cards = deepcopy(state.ai_cards)

            available = np.array(np.where(state.board_legal==True)).T
            # For each child of node
            for [i, j] in available:
                shuffle(cards)
                for c in cards:
                    next_state = deepcopy(state)
                    next_state.place_chess(False, i, j, c)

                    score = self.alphabeta(next_state, curr_depth+1, 
                                              deepcopy(a), deepcopy(b), False)
                    if score > value:
                        value = score
                        if curr_depth == 0: # curr_depth+1 == 1
                            self.bestmove = (i, j, c)
                    # value = max(value, self.alphabeta(next_state, curr_depth+1, 
                    #                           deepcopy(a), deepcopy(b), False))
                    if value > a:
                        a = value
                        if curr_depth == 0: # curr_depth+1 == 1
                            self.bestmove = (i, j, c)

                    if a >= b:
                        break # (* b cut-off *)
                if a >= b:
                    break # (* b cut-off *)
            return value
        else:
            value = 100
            cards = deepcopy(state.user_cards)
            available = np.array(np.where(state.board_legal==True)).T
            
            for [i, j] in available:
                shuffle(cards)
                for c in cards:
                    next_state = deepcopy(state)
                    next_state.place_chess(True, i, j, c)
                    value = min(value, self.alphabeta(next_state, curr_depth+1, 
                                              deepcopy(a), deepcopy(b), True))
                    b = min(b, value)
                    if a >= b:
                        break # (* a cut-off *)
                if a >= b:
                    break # (* a cut-off *)
            return value



    def move(self):
        startTime = time.time()
        # AI to make its turn
        cards = deepcopy(self.state.ai_cards)

        bestscore = -100
        available = np.array(np.where(self.state.board_legal==True)).T
        num = randrange(available.shape[0])
        bestmove = (available[num, 0],
                    available[num, 1],
                    choice(cards))

        for depth_limit in range(1, self.max_depth+1):
            if time.time() - startTime > self.timelimit: break
            print("depthlimit:", depth_limit)
            self.depth_limit = depth_limit

            score = self.alphabeta(deepcopy(self.state),
                                           curr_depth=0,
                                           a=-100,
                                           b= 100,
                                           isMaximizing=True)
            
            bestscore = deepcopy(score)
            bestmove = self.bestmove
            print("bestscore:", bestscore, "bestmove:", bestmove)

        return bestmove