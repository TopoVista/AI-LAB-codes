import heapq
from collections import deque

START, GOAL = 1, 30
JUMPS = {3: 22, 5: 8, 11: 26, 20: 29, 17: 4, 19: 7, 21: 9, 27: 1}

def next_states(pos):
    for dice in range(1, 7):
        raw = pos + dice
        if raw <= GOAL:
            yield JUMPS.get(raw, raw), dice, raw

def reconstruct_path(parent, pos):
    path = []
    while pos is not None:
        prev = parent[pos]
        path.append((pos, None, None) if prev is None else (pos, prev[1], prev[2]))
        pos = None if prev is None else prev[0]
    return path[::-1]

def heuristic(pos):
    if pos == GOAL:
        return 0
    best_next = max(JUMPS.get(pos + d, pos + d) for d in range(1, 7) if pos + d <= GOAL)
    return (GOAL - best_next + 5) // 6

def search(mode):
    parent, nodes = {START: None}, 0

    if mode == "astar":
        fringe, best = [(heuristic(START), 0, START)], {START: 0}
        while fringe:
            _, depth, pos = heapq.heappop(fringe)
            if depth > best.get(pos, float("inf")):
                continue
            nodes += 1
            if pos == GOAL:
                path = reconstruct_path(parent, pos)
                return path, nodes, len(path) - 1
            for nxt, dice, raw in next_states(pos):
                cost = depth + 1
                if cost >= best.get(nxt, float("inf")):
                    continue
                best[nxt], parent[nxt] = cost, (pos, dice, raw)
                heapq.heappush(fringe, (cost + heuristic(nxt), cost, nxt))
        return [], nodes, -1

    fringe, seen = (deque([START]) if mode == "bfs" else [START]), {START}
    while fringe:
        pos = fringe.popleft() if mode == "bfs" else fringe.pop()
        nodes += 1
        if pos == GOAL:
            path = reconstruct_path(parent, pos)
            return path, nodes, len(path) - 1
        states = list(next_states(pos))
        for nxt, dice, raw in (states if mode == "bfs" else reversed(states)):
            if nxt not in seen:
                seen.add(nxt)
                parent[nxt] = (pos, dice, raw)
                fringe.append(nxt)
    return [], nodes, -1

bfs_search = lambda: search("bfs")
dfs_search = lambda: search("dfs")
a_star = lambda: search("astar")

def print_path(path):
    if not path:
        print("No path found.\n")
        return
    for step, (pos, dice, raw) in enumerate(path):
        if dice is None:
            print(f"Move {step}: Start at square {pos}")
            continue
        jump = ""
        if raw != pos:
            jump = f" via {'Ladder' if pos > raw else 'Snake'} {raw}->{pos}"
        print(f"Move {step}: rolled {dice}, reached square {pos}{jump}")
    print()

if __name__ == "__main__":
    print("Snakes and Ladders Board")
    print("Ladders:", {k: v for k, v in JUMPS.items() if v > k})
    print("Snakes:", {k: v for k, v in JUMPS.items() if v < k})

    results = [("BFS", *bfs_search()), ("DFS", *dfs_search()), ("A*", *a_star())]
    for name, _, nodes, depth in results:
        print(f"{name} explored nodes:", nodes, "| Dice throws:", depth)
    for i, (name, path, _, _) in enumerate(results):
        print(f"\n{name} path:" if i == 0 else f"{name} path:")
        print_path(path)
