"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = 0
    num_o = 0

    for row in board:
        for cell in row:
            if cell == X:
                num_x += 1
            elif cell == O:
                num_o += 1
    
    if num_o < num_x:
        return O
    
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i -> row of the move (0,1,2)
    j -> cell in the row (0,1,2)
    """
    actions = set()

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    
    return actions        


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    should not modify the original board
    if action is not valid raise exception
    """
    result_board = copy.deepcopy(board)
    turn = player(result_board)

    if action[0] > -1 and action[1] > -1 and result_board[action[0]][action[1]] == EMPTY:
        result_board[action[0]][action[1]] = turn
        return result_board
    
    raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check horizontal
    for r in range(0, 3):
        if all(i == board[r][0] for i in board[r]) and board[r][0] is not None:
            return board[r][0]
    # check vertical
    for c in range(0, 3):
        if board[1][c] == board[0][c] and board[0][c] is not None:
            if board[2][c] == board[0][c]:
                return board[0][c]
    # check diagonal
    if board[1][1] == board[0][0] and board[0][0] is not None:
        if board[2][2] == board[0][0]:
            return board[0][0]
    # check other diagonal
    elif board[1][1] == board[0][2] and board[0][2] is not None:
        if board[2][0] == board[0][2]:
                return board[0][2]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY and winner(board) is None:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        return max_value(board)[-1]
    elif player(board) == O:
        return min_value(board)[-1]
    

def max_value(board):
    """
    to find the maximum value from this state
    """
    v = -math.inf
    act1 = None

    if terminal(board):
        return utility(board), None
    
    for action in actions(board):
        curr, act = min_value(result(board, action))
        if curr > v:
            v = curr
            act1 = action # store the current best action
    
    return v, act1

def min_value(board):
    """
    to find the minimum value from this state
    """
    v = math.inf
    act1 = None

    if terminal(board):
        return utility(board), None

    for action in actions(board):
        curr, act = max_value(result(board, action))
        if curr < v: # flipped for minimizing
            v = curr
            act1 = action 

    return v, act1

