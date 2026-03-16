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

def reconstruct_bidirectional_path(parent1, parent2, start, goal, meeting):
    path_from_start = reconstruct_path(parent1, start, meeting)
    path_to_goal = [meeting]
    cur = meeting

    while cur != goal:
        cur = parent2[cur]
        path_to_goal.append(cur)

    return path_from_start + path_to_goal[1:]

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
# DFS
# -------------------------

def dfs(start,goal):
    stack=[start]
    parent={}
    visited={start}
    nodes=0

    while stack:
        current=stack.pop()
        nodes+=1

        if current==goal:
            break

        neighbors = get_neighbors(current)
        for neighbor,_ in reversed(neighbors):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor]=current
                stack.append(neighbor)

    path = reconstruct_path(parent, start, goal)

    return path,nodes,len(path)-1

# -------------------------
# BIDIRECTIONAL SEARCH
# -------------------------

def expand_frontier(queue, visited_this, visited_other, parent_this):
    current = queue.popleft()

    if current in visited_other:
        return current

    for neighbor,_ in get_neighbors(current):
        if neighbor not in visited_this:
            visited_this.add(neighbor)
            parent_this[neighbor]=current
            if neighbor in visited_other:
                return neighbor
            queue.append(neighbor)

    return None

def bidirectional_search(start,goal):
    if start == goal:
        return [start],1,0

    q1=deque([start])
    q2=deque([goal])
    parent1={}
    parent2={}
    vis1={start}
    vis2={goal}
    nodes=0

    while q1 and q2:
        meeting = expand_frontier(q1, vis1, vis2, parent1)
        nodes+=1
        if meeting is not None:
            path = reconstruct_bidirectional_path(parent1, parent2, start, goal, meeting)
            return path,nodes,len(path)-1

        meeting = expand_frontier(q2, vis2, vis1, parent2)
        nodes+=1
        if meeting is not None:
            path = reconstruct_bidirectional_path(parent1, parent2, start, goal, meeting)
            return path,nodes,len(path)-1

    return [],nodes,-1

# -------------------------
# BEST FIRST SEARCH
# -------------------------

def best_first(start,goal,heuristic,diagonal=False):
    pq=[]
    heapq.heappush(pq,(heuristic(start,goal),start))
    parent={}
    seen={start}
    nodes=0

    while pq:
        _,current=heapq.heappop(pq)
        nodes+=1

        if current==goal:
            break

        for neighbor,_ in get_neighbors(current,diagonal):
            if neighbor not in seen:
                seen.add(neighbor)
                parent[neighbor]=current
                heapq.heappush(pq,(heuristic(neighbor,goal),neighbor))

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

    ax.set_title(title, fontsize=13, pad=10)
    ax.set_xlim(-0.5, COLS - 0.5)
    ax.set_ylim(ROWS - 0.5, -0.5)
    ax.set_aspect("equal")
    ax.set_xticks(range(COLS))
    ax.set_yticks(range(ROWS))
    ax.tick_params(length=0, labelsize=10)

def visualize(results):
    if len(results) <= 4:
        cols = 2
    elif len(results) <= 6:
        cols = 3
    else:
        cols = 4

    rows = math.ceil(len(results) / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(4.6 * cols, 4.4 * rows))
    axes = axes.flatten() if hasattr(axes, "flatten") else [axes]

    for idx, (ax, (path, title)) in enumerate(zip(axes, results)):
        draw_grid(ax, path, title)

        row, col = divmod(idx, cols)
        if row < rows - 1:
            ax.tick_params(labelbottom=False)
        if col > 0:
            ax.tick_params(labelleft=False)

    for ax in axes[len(results):]:
        ax.axis("off")

    fig.subplots_adjust(left=0.05, right=0.98, top=0.94, bottom=0.06, wspace=0.22, hspace=0.28)
    plt.show()

# -------------------------
# RUN ALL
# -------------------------

if __name__=="__main__":

    path1,n1,d1=a_star(START,GOAL,manhattan,False)
    path2,n2,d2=a_star(START,GOAL,euclidean,True)
    path3,n3,d3=bfs(START,GOAL)
    path4,n4,d4=dfs(START,GOAL)
    path5,n5,d5=bidirectional_search(START,GOAL)
    path6,n6,d6=best_first(START,GOAL,manhattan,False)
    path7,n7,d7=ucs(START,GOAL)

    print("A* Manhattan -> Nodes:",n1,"Depth:",d1)
    print("A* Euclidean -> Nodes:",n2,"Depth:",d2)
    print("BFS -> Nodes:",n3,"Depth:",d3)
    print("DFS -> Nodes:",n4,"Depth:",d4)
    print("Bidirectional Search -> Nodes:",n5,"Depth:",d5)
    print("Best First (Manhattan) -> Nodes:",n6,"Depth:",d6)
    print("UCS -> Nodes:",n7,"Depth:",d7)

    visualize([
        (path1, f"A* Manhattan\nNodes: {n1}, Depth: {d1}"),
        (path2, f"A* Euclidean\nNodes: {n2}, Depth: {d2}"),
        (path3, f"BFS\nNodes: {n3}, Depth: {d3}"),
        (path4, f"DFS\nNodes: {n4}, Depth: {d4}"),
        (path5, f"Bidirectional Search\nNodes: {n5}, Depth: {d5}"),
        (path6, f"Best First (Manhattan)\nNodes: {n6}, Depth: {d6}"),
        (path7, f"UCS\nNodes: {n7}, Depth: {d7}")
    ])
