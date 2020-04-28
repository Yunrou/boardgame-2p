import numpy as np
from table import *

def display_cards(cards):
    print("\x1b[92m[User chess pieces]:\x1b[0m", list(-cards[cards < 0]))
    print("\x1b[93m[  AI chess pieces]:\x1b[0m", list(cards[cards > 0]))

def display_board(board):
    print("")
    for row in board:
        for i in row:
            # check if the place is legal
             
            if i > 1: # AI
                print('\x1b[93m{0:>2}\x1b[0m'.format(i), end=' ')
            elif i < -1: # User
                print('\x1b[92m{0:>2}\x1b[0m'.format(-i), end=' ')
            elif i == 0: # Available
                print('{0:>2}'.format(0), end=' ')
            else: # i == -1: Illegal
                print('\x1b[91m{0:>2}\x1b[0m'.format('X'), end=' ')
                
        print("")
    print("")

def check(board, row, col):
    
    """
    A card on the board will be removed if the total of 
    the numbers of the card and its surrounding 8 cards exceed 15.
    """

    # board transformation for compute neighbors and itself
    realboard = np.absolute(board)
    realboard[realboard == 1] = 0

    # Mark
    marked = np.zeros(shape=(0,2), dtype=np.int8)
    total = 0
    n = len(board)
    for [checki, checkj] in SUMindex[(n, row, col)].tolist():
        if realboard[checki, checkj] == 0: continue
        for [i, j] in SUMindex[(n, checki, checkj)].tolist():
            total += realboard[i, j]

        if total > 15:
            marked = np.concatenate((marked, np.array([[checki, checkj]])))
        total = 0
    # Remove
    for [i, j] in marked.tolist():
        board[i, j] = -1 # become illegal
    
    return board

def place_chess(isAI, board, cards, row, col, weight):
    
    if isAI:
        available = np.array(np.where(cards==weight)).T
    else:
        # Check illegal place
        if not (row in range(len(board)) and col in range(len(board))):
            return False
        if board[row, col] != 0: # Not available
            return False

        available = np.array(np.where(cards==weight)).T
        if available.size == 0:
            return False

    board[row, col] = weight
    cards = np.delete(cards, available[0][0])

    board = check(board.copy(), row, col)

    return (board, cards)

def win_check(board):
    """
    Compute two players' score and determine who wins the game!
    """
    # AI - User
    score = np.sum(board[board > 1]) + np.sum(board[board < -1])

    if score > 0:
        return 'ai'
    elif score < 0:
        return 'user'
    else:
        if not len(board[board > 1]):
            return 'tie'
        ai_max = np.max(board[board > 1])
        user_max = -np.min(board[board < -1])
        if ai_max > user_max:
            return 'ai'
        elif ai_max < user_max:
            return 'user'
        else:
            return 'tie' 

def heuristic(board, cards):
# f(p) = 200(K-K')
#        + 9(Q-Q')
#        + 5(R-R')
#        + 3(B-B' + N-N')
#        + 1(P-P')
#        - 0.5(D-D' + S-S' + I-I')
#        + 0.1(M-M') + ...

# KQRBNP = number of kings, queens, rooks, bishops, knights and pawns
# D,S,I = doubled, blocked and isolated pawns
# M = Mobility (the number of legal moves)

    if not len(cards):
        win =  win_check(board)
        if win == 'ai': return 1000+np.sum(board[board > 1])+np.sum(board[board < -1])
        elif win == 'user': return -1000-(np.sum(board[board > 1])+np.sum(board[board < -1]))
        else: return 0

    # board
    ai_board = board[board > 1]
    user_board = board[board < -1]
    # cards
    ai_cards = cards[cards > 0]
    user_cards = cards[cards < 0]

    delta13 = np.count_nonzero(ai_cards==13)-np.count_nonzero(user_cards==-13)+ \
              0.8 * (np.count_nonzero(ai_board==13)-np.count_nonzero(user_board==-13))
    delta8  = np.count_nonzero(ai_cards==8)-np.count_nonzero(user_cards==-8)+ \
              1 * (np.count_nonzero(ai_board==8)-np.count_nonzero(user_board==-8))
    delta5  = np.count_nonzero(ai_cards==5)-np.count_nonzero(user_cards==-5)+ \
              1 * (np.count_nonzero(ai_board==5)-np.count_nonzero(user_board==-5))
    delta3  = np.count_nonzero(ai_cards==3)-np.count_nonzero(user_cards==-3)+ \
              1 * (np.count_nonzero(ai_board==3)-np.count_nonzero(user_board==-3))
    delta2  = np.count_nonzero(ai_cards==2)-np.count_nonzero(user_cards==-2)+ \
              1 * (np.count_nonzero(ai_board==2)-np.count_nonzero(user_board==-2))

    return 30*delta13 + 9*delta8 + 5*delta5 + 3*delta3 + 3*delta2 

def getsuccessor(board, cards):
    # Generate childnodes (possible moves)
    available_pos = np.array(np.where(board==0)).T
    available_cards = np.array([np.unique(cards)]).T
    
    childnodes = np.hstack((np.tile(available_pos,(len(available_cards),1)), 
                            np.repeat(available_cards,len(available_pos),0)))

    # Order childnodes
    rng = np.random.default_rng()
    rng.shuffle(childnodes, axis=0)

    return childnodes