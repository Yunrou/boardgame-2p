import numpy as np
class State:

    def __init__(self, boardsize, board_user, board_ai, board_legal, user_cards, ai_cards):
        self.boardsize = boardsize
        self.board_user = board_user
        self.board_ai = board_ai
        self.board_legal = board_legal
        self.user_cards = user_cards
        self.ai_cards = ai_cards

    def __len__(self):
       return len(self.ai_cards) + len(self.user_cards)

    def display_board(self):
        boardsize = self.boardsize
        board_user = self.board_user
        board_ai = self.board_ai
        board_legal = self.board_legal
        print("")
        for i in range(boardsize):
            for j in range(boardsize):
                # check if the place is legal
                 
                if board_user[i, j] != 0:
                    print('\x1b[92m{0:>2}\x1b[0m'.format(board_user[i, j]), end=' ')
                elif board_ai[i, j] != 0:
                    print('{0:>2}'.format(board_ai[i, j]), end=' ')
                elif board_legal[i, j]:
                    print('{0:>2}'.format(0), end=' ')
                else:
                    print('\x1b[91m{0:>2}\x1b[0m'.format('X'), end=' ')
                    
            print('')
        print("")

    def combine_board(self, board_user, board_ai):
        return self.board_user+self.board_ai

    def display_cards(self):
        print("[User chess pieces]:", self.user_cards)
        print("[  AI chess pieces]:", self.ai_cards)      

    def check(self):
        
        """
        A card on the board will be removed if the total of 
        the numbers of the card and its surrounding 8 cards exceed 15.
        """
        boardsize = self.boardsize
        board_user = self.board_user
        board_ai = self.board_ai

        # board with padding zeros to compute total 8 neighbors and itself
        paddingboard = np.pad(board_user+board_ai, ((1,1),(1,1)), 'constant')

        # board to mark for removal
        markedboard = np.full((boardsize, boardsize), False, dtype=bool)
        
        nonzero = np.array(np.where(paddingboard > 0)).T

        for [i,j] in nonzero:
            total = paddingboard[i-1, j-1] + paddingboard[i-1, j] + paddingboard[i-1, j+1] \
                    + paddingboard[i, j-1] + paddingboard[i, j] + paddingboard[i, j+1] \
                    + paddingboard[i+1, j-1] + paddingboard[i+1, j] + paddingboard[i+1, j+1] 
            if total > 15:
                markedboard[i-1, j-1] = True# self.mark(markedboard, i, j)
            
        self.remove(markedboard)



    def remove(self, markedboard):
        """
        remove a card from the board, and the card list.
        and mark 'X' on the board, so that the position will not be reused.
        """
        board_user = self.board_user
        board_ai = self.board_ai

        marked = np.array(np.where(markedboard == True)).T

        for [i, j] in marked:
            if board_user[i, j] != 0:
                board_user[i, j] = 0
            elif board_ai[i, j] != 0:
                board_ai[i, j] = 0

    def place_chess(self, user, row, col, weight):
        
        # Check illegal place
        if self.board_legal[row][col] == False:
            return False
        
        # Check user cards
        if user:
            if weight not in self.user_cards:
                return False
            
            self.user_cards.remove(weight)
            self.board_user[row][col] = weight
        else:
            if weight not in self.ai_cards:
                return False
            
            self.ai_cards.remove(weight)
            self.board_ai[row][col] = weight

        self.board_legal[row][col] = False
        self.check()

        return True


      
    def check_end(self):
        """
        The game ends when both players have NO cards in hand.
        """
        if len(self.user_cards)==0 and len(self.ai_cards)==0:
            return True
        else:
            return False



    def win_check(self):
        """
        Compute two players' score and determine who wins the game!
        """
        user_score = np.sum(self.board_user)
        ai_score = np.sum(self.board_ai)

        if user_score > ai_score:
            return 'user'
        elif user_score < ai_score:
            return 'ai'
        else:
            user_max = np.amax(self.board_user)
            ai_max = np.amax(self.board_ai)

            if user_max > ai_max:
                return 'user'
            elif user_max < ai_max:
                return 'ai'
            else:
                return 'draw'      

    def heuristic(self):
        return np.sum(self.board_ai)-np.sum(self.board_user)+0.8*(np.sum(self.ai_cards)-np.sum(self.user_cards))