import heapq
import time
import math

# Heuristic functions
def manhattan(x, y, tx, ty):
    return abs(x - tx) + abs(y - ty)

def euclidean(x, y, tx, ty):
    return math.sqrt((x - tx)**2 + (y - ty)**2)

def chebyshev(x, y, tx, ty):
    return max(abs(x - tx), abs(y - ty))

def zero_heuristic(x, y, tx, ty):
    return 0

def bad_heuristic(x, y, tx, ty):
    return 100  # Always high, so greedy

def best_first_search(grid, start, treasure, heuristic):
    n, m = len(grid), len(grid[0])
    sx, sy = start
    tx, ty = treasure

    def h(x, y):
        return heuristic(x, y, tx, ty)

    pq = []
    heapq.heappush(pq, (h(sx, sy), (sx, sy)))

    visited = set()
    visited.add((sx, sy))
    parent = {}
    nodes_expanded = 0

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while pq:
        _, (x, y) = heapq.heappop(pq)
        nodes_expanded += 1

        if (x, y) == (tx, ty):
            path = []
            while (x, y) != (sx, sy):
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append((sx, sy))
            return path[::-1], nodes_expanded

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    heapq.heappush(pq, (h(nx, ny), (nx, ny)))

    return None, nodes_expanded

def main():
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    start = (0, 0)
    treasure = (2, 3)

    heuristics = [
        ("Manhattan", manhattan),
        ("Euclidean", euclidean),
        ("Chebyshev", chebyshev),
        ("Zero (Greedy)", zero_heuristic),
        ("Bad (Always 100)", bad_heuristic)
    ]

    print("Grid:")
    for row in grid:
        print(row)
    print(f"\nStart: {start}")
    print(f"Treasure: {treasure}")
    print("\nHeuristic Performance Analysis:")
    print("-" * 50)

    for name, heur in heuristics:
        path, nodes = best_first_search(grid, start, treasure, heur)
        if path:
            path_length = len(path) - 1  # steps
            print(f"{name}:")
            print(f"  Path found: {path}")
            print(f"  Path length: {path_length} steps")
            print(f"  Nodes expanded: {nodes}")
        else:
            print(f"{name}: No path found")
            print(f"  Nodes expanded: {nodes}")
        print()

if __name__ == "__main__":
    main()