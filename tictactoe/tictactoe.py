"""
Tic Tac Toe Player
"""

import math

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
    count = moves(board)
    if count%2==0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = set()
    for x in range(3):
        for y in range(3):
            if board[x][y] == EMPTY:
                actionSet.add((x, y))
    return actionSet

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    for x in range(3):
        for y in range(3):
            newBoard[x][y] = board[x][y]
    newBoard[action[0]][action[1]] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for x in range(3):
        if checkRow(x, board) != None:
            return checkRow(x, board)
        elif checkColumn(x, board) != None:
            return checkColumn(x, board)
        elif board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
    return None
def checkRow(x, board):
    if board[x][0] == board[x][1] == board[x][2]:
        if board[x][0] == X:
            return X
        elif board[x][0] == O:
            return O
    return None
def checkColumn(x, board):
    if board[0][x] == board[1][x] == board[2][x]:
        if board[0][x] == X:
            return X
        elif board[0][x] == O:
            return O
    return None
        
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif moves(board) < 9:
        return False
    return True
def moves(board):
    count = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] != EMPTY:
                count+=1
    return count
                


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if moves(board) == 0:
        return(1,1)
    if player(board) == X:
        actiony = (-1,-1)
        v = -2
        for action in actions(board):
            if v < MinValue(result(board, action)):
                actiony = action
                v = max(v, MinValue(result(board, action)))
        return actiony
    else:
        actiony = (-1,-1)
        v = 2
        for action in actions(board):
            if v > MaxValue(result(board, action)):
                actiony = action
                v = min(v, MaxValue(result(board, action)))
        return actiony



    raise NotImplementedError
def MinValue(board):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))
    return v
def MaxValue(board):
    if terminal(board):
        return utility(board)
    v = -2
    for action in actions(board):
        v = max(v, MinValue(result(board, action)))
    return v
