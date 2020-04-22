import numpy as np
class State:

    def __init__(self, boardsize, board_user, board_ai, board_legal, user_cards, ai_cards):
        self.boardsize = boardsize
        self.board_user = board_user
        self.board_ai = board_ai
        self.board_legal = board_legal
        self.user_cards = user_cards
        self.ai_cards = ai_cards
        self.change = 0

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


    def display_cards(self):
        print("[User chess pieces]:", list(self.user_cards))
        print("[  AI chess pieces]:", list(self.ai_cards))      

    def check(self, x, y):
        
        """
        A card on the board will be removed if the total of 
        the numbers of the card and its surrounding 8 cards exceed 15.
        """
        boardsize = self.boardsize
        board_user = self.board_user
        board_ai = self.board_ai

        # board with padding zeros to compute total 8 neighbors and itself
        paddingboard = np.pad(board_user+board_ai, ((1,1),(1,1)), 'constant')
        checkboard = np.full((boardsize+2, boardsize+2), False, dtype=bool)
        checkboard[x:x+3, y:y+3]= True
        paddingboard *= checkboard

        # board to mark for removal
        markedboard = np.full((boardsize, boardsize), False, dtype=bool)
        
        nonzero = np.array(np.where(paddingboard > 0)).T

        for [i,j] in nonzero.tolist():
            total = np.sum(paddingboard[i-1:i+2, j-1:j+2])
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

        for [i, j] in marked.tolist():
            if board_user[i, j] != 0:
                board_user[i, j] = 0
            elif board_ai[i, j] != 0:
                board_ai[i, j] = 0

    def place_chess(self, isAI, row, col, weight):
        prev = np.sum(self.board_ai+self.board_user)
        
        if isAI:
            available = np.array(np.where(self.ai_cards==weight)).T
            
            self.board_ai[row, col] = weight
            self.ai_cards = np.delete(self.ai_cards, available[0][0])
        
        else:
            # Check illegal place
            if not (row in range(self.boardsize) and col in range(self.boardsize)):
                return False
            if self.board_legal[row, col] == False:
                return False

            available = np.array(np.where(self.user_cards==weight)).T
            if available.size == 0:
                return False
            
            self.board_user[row, col] = weight
            self.user_cards = np.delete(self.user_cards, available[0][0])

        self.board_legal[row, col] = False
        self.check(row, col)

        self.change += (np.sum(self.board_ai+self.board_user) - prev)

        return True


      
    def check_end(self):
        """
        The game ends when both players have NO cards in hand.
        """
        return (len(self.user_cards)+len(self.ai_cards) == 0)

    def win_check(self):
        """
        Compute two players' score and determine who wins the game!
        """
        score = np.sum(self.board_user) - np.sum(self.board_ai)

        if score > 0:
            return 'user'
        elif score < 0:
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
        if self.change < 0:
            return -50
        elif self.change > 5:
            return 50
        return np.sum(self.board_ai-self.board_user)+self.change+np.sum(self.ai_cards)-np.sum(self.user_cards)

    def getsuccessor(self):
        # Generate childnodes
        available = np.array(np.where(self.board_legal==True)).T
        cards = np.array([self.ai_cards]).T
        
        childnodes = np.hstack((np.tile(available,(len(cards),1)), 
                                np.repeat(cards,len(available),0)))

        # Order childnodes
        rng = np.random.default_rng()
        rng.shuffle(childnodes, axis=0)

        return childnodes