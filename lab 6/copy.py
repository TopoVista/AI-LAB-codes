import heapq
from collections import deque

GOAL_STATE = ((1,2,3),
              (4,5,6),
              (7,8,0))

MOVES = [(-1,0),(1,0),(0,-1),(0,1)]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j

def misplaced_tiles(state):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                cnt += 1
    return cnt

def manhattan_distance(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x = (val-1)//3
                y = (val-1)%3
                dist += abs(i-x) + abs(j-y)
    return dist

def get_neighbors(state):
    x,y = find_zero(state)
    neighbors = []
    for dx,dy in MOVES:
        nx,ny = x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            new = [list(r) for r in state]
            new[x][y],new[nx][ny] = new[nx][ny],new[x][y]
            neighbors.append(tuple(tuple(r) for r in new))
    return neighbors

def a_star(start, heuristic):
    pq = []
    heapq.heappush(pq,(heuristic(start),0,start))
    visited = set()
    parent = {}  # Track parent states
    nodes_expanded = 0

    while pq:
        f,g,state = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)
        nodes_expanded += 1

        if state == GOAL_STATE:
            # Reconstruct path
            path = []
            current = state
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, nodes_expanded

        for nei in get_neighbors(state):
            if nei not in visited:
                parent[nei] = state  # Record parent
                h = heuristic(nei)
                heapq.heappush(pq,(g+1+h,g+1,nei))

    return [], nodes_expanded

def main():
    start_state = ((1,2,3),
                   (4,0,6),
                   (7,5,8))

    print("Initial State:")
    for r in start_state:
        print(r)

    print("\nUsing H1: Misplaced Tiles")
    path1,nodes1 = a_star(start_state,misplaced_tiles)
    print("Solution Path:")
    for step, state in enumerate(path1):
        print(f"Step {step}:")
        for r in state:
            print(r)
        print()
    print("Nodes Expanded:",nodes1)

    print("\nUsing H2: Manhattan Distance")
    path2,nodes2 = a_star(start_state,manhattan_distance)
    print("Solution Path:")
    for step, state in enumerate(path2):
        print(f"Step {step}:")
        for r in state:
            print(r)
        print()
    print("Nodes Expanded:",nodes2)

    print("\nComparison:")
    print("H1 expanded",nodes1,"nodes")
    print("H2 expanded",nodes2,"nodes")

if __name__ == "__main__":
    main()
