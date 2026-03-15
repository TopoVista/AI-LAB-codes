import heapq
from collections import deque

EMPTY, HUMAN, AI, DRAW = " ", "O", "X", "Draw"
WIN_LINES = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
    print()

def check_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    return DRAW if EMPTY not in board else None

def next_states(state, player):
    nxt = HUMAN if player == AI else AI
    for move, cell in enumerate(state):
        if cell == EMPTY:
            new_state = list(state)
            new_state[move] = player
            new_state = tuple(new_state)
            if check_winner(new_state) not in (HUMAN, DRAW):
                yield new_state, nxt

def reconstruct_path(parent, key):
    path = []
    while key is not None:
        path.append(key[0])
        key = parent[key]
    return path[::-1]

def heuristic(board):
    if check_winner(board) == AI:
        return 0
    best, open_lines = 4, 0
    for a, b, c in WIN_LINES:
        line = (board[a], board[b], board[c])
        if HUMAN not in line:
            open_lines += 1
            best = min(best, line.count(EMPTY))
    return best if open_lines else 10

def search(board, mode):
    start = (tuple(board), AI)
    parent, nodes = {start: None}, 0

    if mode == "astar":
        fringe, best = [(heuristic(start[0]), 0, *start)], {start: 0}
        while fringe:
            _, depth, state, player = heapq.heappop(fringe)
            key = (state, player)
            if depth > best.get(key, float("inf")):
                continue
            nodes += 1
            result = check_winner(state)
            if result == AI:
                path = reconstruct_path(parent, key)
                return path, nodes, len(path) - 1
            if result:
                continue
            for new_state, nxt in next_states(state, player):
                next_key, cost = (new_state, nxt), depth + 1
                if cost >= best.get(next_key, float("inf")):
                    continue
                best[next_key], parent[next_key] = cost, key
                heapq.heappush(fringe, (cost + heuristic(new_state), cost, new_state, nxt))
        return [], nodes, -1

    fringe, seen = (deque([start]) if mode == "bfs" else [start]), {start}
    while fringe:
        key = fringe.popleft() if mode == "bfs" else fringe.pop()
        state, player = key
        nodes += 1
        result = check_winner(state)
        if result == AI:
            path = reconstruct_path(parent, key)
            return path, nodes, len(path) - 1
        if result:
            continue
        states = list(next_states(state, player))
        for next_key in (states if mode == "bfs" else reversed(states)):
            if next_key not in seen:
                seen.add(next_key)
                parent[next_key] = key
                fringe.append(next_key)
    return [], nodes, -1

bfs_search = lambda board: search(board, "bfs")
dfs_search = lambda board: search(board, "dfs")
a_star = lambda board: search(board, "astar")

def print_path(path):
    if not path:
        print("No AI-winning path found.\n")
        return
    for step, board in enumerate(path):
        print(f"Move {step}:")
        print_board(board)

if __name__ == "__main__":
    board = [EMPTY] * 9
    print("Initial Board:")
    print_board(board)
    results = [("BFS", *bfs_search(board)), ("DFS", *dfs_search(board)), ("A*", *a_star(board))]
    for name, _, nodes, depth in results:
        print(f"{name} explored nodes:", nodes, "| Winning depth:", depth)
    for i, (name, path, _, _) in enumerate(results):
        print(f"\n{name} winning path:" if i == 0 else f"{name} winning path:")
        print_path(path)
