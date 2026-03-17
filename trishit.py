from collections import deque
import heapq

# ---------------- GRID ----------------
grid = [
    ['S', '.', 'G', '.'],
    ['.', '#', '.', '.'],
    ['G', '.', '#', 'E'],
    ['.', 'G', '.', '.']
]

ROWS = len(grid)
COLS = len(grid[0])

# movements
moves = [(1,0),(-1,0),(0,1),(0,-1)]

# ---------------- FIND START & GOALS ----------------
goals = set()
start = None
exit_pos = None

for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == 'S':
            start = (i,j)
        elif grid[i][j] == 'G':
            goals.add((i,j))
        elif grid[i][j] == 'E':
            exit_pos = (i,j)


# ---------------- HELPER ----------------
def valid(x,y):
    return 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] != '#'


# ====================================================
# BFS (UNWEIGHTED)
# ====================================================
def bfs_multi_goal():

    queue = deque()
    queue.append((start[0], start[1], frozenset(), []))

    visited = set()

    while queue:
        x,y,collected,path = queue.popleft()

        state = (x,y,collected)
        if state in visited:
            continue
        visited.add(state)

        path = path + [(x,y)]

        new_collected = set(collected)
        if (x,y) in goals:
            new_collected.add((x,y))
        new_collected = frozenset(new_collected)

        # goal condition
        if new_collected == goals and (x,y)==exit_pos:
            return path

        for dx,dy in moves:
            nx,ny = x+dx, y+dy
            if valid(nx,ny):
                queue.append((nx,ny,new_collected,path))
∑
    return None


# ====================================================
# UNIFORM COST SEARCH (weighted goals)
# ====================================================
goal_cost = {
    (0,2):5,
    (2,0):2,
    (3,1):3
}

def ucs_multi_goal():

    pq=[]
    heapq.heappush(pq,(0,start[0],start[1],frozenset(),[]))

    visited=set()

    while pq:
        cost,x,y,collected,path = heapq.heappop(pq)

        state=(x,y,collected)
        if state in visited:
            continue
        visited.add(state)

        path = path + [(x,y)]

        new_collected=set(collected)
        new_cost=cost

        if (x,y) in goals and (x,y) not in collected:
            new_collected.add((x,y))
            new_cost += goal_cost[(x,y)]

        new_collected=frozenset(new_collected)

        if new_collected==goals and (x,y)==exit_pos:
            return path,new_cost

        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if valid(nx,ny):
                heapq.heappush(
                    pq,
                    (new_cost+1,nx,ny,new_collected,path)
                )

    return None


# ====================================================
# A* SEARCH
# ====================================================
def heuristic(x,y,collected):
    remaining = len(goals - set(collected))
    dist = abs(x-exit_pos[0]) + abs(y-exit_pos[1])
    return dist + remaining


def astar_multi_goal():

    pq=[]
    heapq.heappush(pq,(0,0,start[0],start[1],frozenset(),[]))

    visited=set()

    while pq:
        f,cost,x,y,collected,path = heapq.heappop(pq)

        state=(x,y,collected)
        if state in visited:
            continue
        visited.add(state)

        path=path+[(x,y)]

        new_collected=set(collected)
        new_cost=cost

        if (x,y) in goals and (x,y) not in collected:
            new_collected.add((x,y))
            new_cost+=goal_cost[(x,y)]

        new_collected=frozenset(new_collected)

        if new_collected==goals and (x,y)==exit_pos:
            return path,new_cost

        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if valid(nx,ny):
                g=new_cost+1
                h=heuristic(nx,ny,new_collected)
                heapq.heappush(
                    pq,
                    (g+h,g,nx,ny,new_collected,path)
                )

    return None


# ---------------- RUN ----------------
print("BFS Path:")
print(bfs_multi_goal())

print("\nUCS Result:")
print(ucs_multi_goal())

print("\nA* Result:")
print(astar_multi_goal())