import heapq
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from collections import deque

# -------------------------
# GRID SETUP
# -------------------------

GRID = [
    [0,0,0,0,0,0],
    [0,1,1,1,0,0],
    [0,0,0,1,0,0],
    [0,1,0,0,0,0],
    [0,1,0,1,1,0],
    [0,0,0,0,0,0]
]

ROWS = len(GRID)
COLS = len(GRID[0])

START = (0,0)
GOAL = (5,5)

# -------------------------
# HEURISTICS
# -------------------------

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def euclidean(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# -------------------------
# PATH RECONSTRUCTION
# -------------------------

def reconstruct_path(parent, start, goal):
    if start == goal:
        return [start]
    if goal not in parent:
        return []

    path = [goal]
    cur = goal
    while cur != start:
        cur = parent[cur]
        path.append(cur)
    path.reverse()
    return path

# -------------------------
# NEIGHBORS
# -------------------------

def get_neighbors(node, diagonal=False):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    if diagonal:
        directions += [(-1,-1),(-1,1),(1,-1),(1,1)]
    neighbors = []
    for dx,dy in directions:
        nx,ny = node[0]+dx, node[1]+dy
        if 0<=nx<ROWS and 0<=ny<COLS and GRID[nx][ny]==0:
            cost = math.sqrt(2) if diagonal and abs(dx)==1 and abs(dy)==1 else 1
            neighbors.append(((nx,ny),cost))
    return neighbors

# -------------------------
# A*
# -------------------------

def a_star(start,goal,heuristic,diagonal=False):
    open_set=[]
    heapq.heappush(open_set,(0,start))
    g={start:0}
    parent={}
    visited=set()
    nodes=0

    while open_set:
        _,current=heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        nodes+=1

        if current==goal:
            break

        for neighbor,cost in get_neighbors(current,diagonal):
            temp_g=g[current]+cost
            if neighbor not in g or temp_g<g[neighbor]:
                g[neighbor]=temp_g
                f=temp_g+heuristic(neighbor,goal)
                heapq.heappush(open_set,(f,neighbor))
                parent[neighbor]=current

    path = reconstruct_path(parent, start, goal)

    return path,nodes,len(path)-1

# -------------------------
# BFS
# -------------------------

def bfs(start,goal):
    q=deque([start])
    parent={}
    visited={start}
    nodes=0

    while q:
        current=q.popleft()
        nodes+=1
        if current==goal:
            break
        for neighbor,_ in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor]=current
                q.append(neighbor)

    path = reconstruct_path(parent, start, goal)

    return path,nodes,len(path)-1

# -------------------------
# UCS
# -------------------------

def ucs(start,goal):
    pq=[]
    heapq.heappush(pq,(0,start))
    g={start:0}
    parent={}
    visited=set()
    nodes=0

    while pq:
        cost,current=heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        nodes+=1

        if current==goal:
            break

        for neighbor,c in get_neighbors(current):
            temp=cost+c
            if neighbor not in g or temp<g[neighbor]:
                g[neighbor]=temp
                heapq.heappush(pq,(temp,neighbor))
                parent[neighbor]=current

    path = reconstruct_path(parent, start, goal)

    return path,nodes,len(path)-1

# -------------------------
# VISUALIZATION
# -------------------------

def draw_grid(ax, path, title):
    for i in range(ROWS):
        for j in range(COLS):
            color = "black" if GRID[i][j] == 1 else "white"
            ax.add_patch(
                Rectangle((j - 0.5, i - 0.5), 1, 1, facecolor=color, edgecolor="gray")
            )

    if path:
        xs = [p[1] for p in path]
        ys = [p[0] for p in path]
        ax.plot(xs, ys, color="red", marker="o", linewidth=2.5, markersize=5)
    else:
        ax.text(
            (COLS - 1) / 2,
            (ROWS - 1) / 2,
            "No path found",
            ha="center",
            va="center",
            color="red",
            fontsize=11,
            fontweight="bold",
        )

    ax.scatter(START[1], START[0], color="green", s=120, edgecolors="black", zorder=3)
    ax.scatter(GOAL[1], GOAL[0], color="blue", s=160, marker="*", edgecolors="black", zorder=3)

    ax.set_title(title)
    ax.set_xlim(-0.5, COLS - 0.5)
    ax.set_ylim(ROWS - 0.5, -0.5)
    ax.set_aspect("equal")
    ax.set_xticks(range(COLS))
    ax.set_yticks(range(ROWS))
    ax.tick_params(length=0)

def visualize(results):
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    axes = axes.flatten()

    for ax, (path, title) in zip(axes, results):
        draw_grid(ax, path, title)

    plt.tight_layout()
    plt.show()

# -------------------------
# RUN ALL
# -------------------------

if __name__=="__main__":

    path1,n1,d1=a_star(START,GOAL,manhattan,False)
    path2,n2,d2=a_star(START,GOAL,euclidean,True)
    path3,n3,d3=bfs(START,GOAL)
    path4,n4,d4=ucs(START,GOAL)

    print("A* Manhattan -> Nodes:",n1,"Depth:",d1)
    print("A* Euclidean -> Nodes:",n2,"Depth:",d2)
    print("BFS -> Nodes:",n3,"Depth:",d3)
    print("UCS -> Nodes:",n4,"Depth:",d4)

    visualize([
        (path1, f"A* Manhattan\nNodes: {n1}, Depth: {d1}"),
        (path2, f"A* Euclidean\nNodes: {n2}, Depth: {d2}"),
        (path3, f"BFS\nNodes: {n3}, Depth: {d3}"),
        (path4, f"UCS\nNodes: {n4}, Depth: {d4}")
    ])
