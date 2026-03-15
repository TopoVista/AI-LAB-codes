import math
from collections import deque

# ----------------------------
# GAME LOGIC
# ----------------------------

EMPTY = " "
HUMAN = "O"
AI = "X"

def print_board(board):
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    if EMPTY not in board:
        return "Draw"
    return None

def get_moves(board):
    return [i for i in range(9) if board[i] == EMPTY]

# ----------------------------
# BFS SEARCH
# ----------------------------

def bfs_search(board):
    q = deque([(board, AI)])
    nodes = 0

    while q:
        state, player = q.popleft()
        nodes += 1

        winner = check_winner(state)
        if winner:
            continue

        for move in get_moves(state):
            new_state = state[:]
            new_state[move] = player
            q.append((new_state, HUMAN if player==AI else AI))

    return nodes

# ----------------------------
# DFS SEARCH
# ----------------------------

def dfs_search(board):
    stack = [(board, AI)]
    nodes = 0

    while stack:
        state, player = stack.pop()
        nodes += 1

        winner = check_winner(state)
        if winner:
            continue

        for move in get_moves(state):
            new_state = state[:]
            new_state[move] = player
            stack.append((new_state, HUMAN if player==AI else AI))

    return nodes

# ----------------------------
# A* SEARCH
# ----------------------------

def heuristic(board):
    # number of potential winning lines for AI
    score = 0
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        line = [board[a],board[b],board[c]]
        if HUMAN not in line:
            score += 1
    return -score

def a_star(board):
    open_set = [(0, board, AI)]
    nodes = 0

    while open_set:
        open_set.sort()
        _, state, player = open_set.pop(0)
        nodes += 1

        winner = check_winner(state)
        if winner:
            continue

        for move in get_moves(state):
            new_state = state[:]
            new_state[move] = player
            cost = heuristic(new_state)
            open_set.append((cost, new_state, HUMAN if player==AI else AI))

    return nodes

# ----------------------------
# RUN COMPARISON
# ----------------------------

if __name__ == "__main__":

    board = [EMPTY]*9

    print("Initial Board:")
    print_board(board)

    bfs_nodes = bfs_search(board)
    dfs_nodes = dfs_search(board)
    astar_nodes = a_star(board)

    print("BFS explored nodes:", bfs_nodes)
    print("DFS explored nodes:", dfs_nodes)
    print("A* explored nodes:", astar_nodes)