"""
Tic Tac Toe Player
"""

import math

# Constants
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
    # Count the number of X's and O's on the board
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

    if count_X > count_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # The possible actions are any cells on the board that are not already occupied
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Make a deep copy of the board. This is necessary because the board is a list of lists. 
    board_copy = [row[:] for row in board]
    board_copy[action[0]][action[1]] = player(board) # player(board) returns the player who has the next turn. 
    return board_copy
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    # Check columns
    # Transpose the board. This is a common trick to check columns. 
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == X:
            return X
        elif board[0][j] == board[1][j] == board[2][j] == O:
            return O

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If there is a winner or the board is full, the game is over
    if winner(board) is not None:
        return True
    if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
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
    # Define the two helper functions that will be used by the minimax function. 
    # The first helper function is called max_value. It takes a board as input and returns the maximum utility that the current player can get from the board.
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float("-inf")
        for action in actions(board):
            v = max(v, min_value(result(board, action))) # The max_value function calls the min_value function. This is the recursive part of the minimax algorithm.
        return v
    
    # The second helper function is called min_value. It takes a board as input and returns the minimum utility that the current player can get from the board.
    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float("inf")
        for action in actions(board):
            v = min(v, max_value(result(board, action))) # The min_value function calls the max_value function. This is the recursive part of the minimax algorithm.
        return v
    
    if terminal(board):
        return None
    
    best_action = None
    if player(board) == X:
        max_utility = float("-inf")
        for action in actions(board):
            current_utility = min_value(result(board, action))
            if current_utility > max_utility:
                max_utility = current_utility
                best_action = action
    else:
        min_utility = float("inf")
        for action in actions(board):
            current_utility = max_value(result(board, action))
            if current_utility < min_utility:
                min_utility = current_utility
                best_action = action
                
    return best_action
