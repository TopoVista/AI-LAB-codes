import heapq

def best_first_search(grid, start, treasure):
    n, m = len(grid), len(grid[0])
    sx, sy = start
    tx, ty = treasure

    def h(x, y):
        return abs(x - tx) + abs(y - ty)

    pq = []
    heapq.heappush(pq, (h(sx, sy), (sx, sy)))

    visited = set()
    visited.add((sx, sy))
    parent = {}

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while pq:
        _, (x, y) = heapq.heappop(pq)

        if (x, y) == (tx, ty):
            path = []
            cur = treasure
            while cur != start:
                path.append(cur)
                cur = parent[cur]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    heapq.heappush(pq, (h(nx, ny), (nx, ny)))

    return None

def uniform_cost_search(grid, start, treasure):
    n, m = len(grid), len(grid[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    pq = [(0, start)]
    dist = {start: 0}
    parent = {}

    while pq:
        cost, (x, y) = heapq.heappop(pq)

        if cost > dist[(x, y)]:
            continue

        if (x, y) == treasure:
            path = []
            cur = treasure
            while cur != start:
                path.append(cur)
                cur = parent[cur]
            path.append(start)
            return cost, path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                new_cost = cost + 1
                if (nx, ny) not in dist or new_cost < dist[(nx, ny)]:
                    dist[(nx, ny)] = new_cost
                    parent[(nx, ny)] = (x, y)
                    heapq.heappush(pq, (new_cost, (nx, ny)))

    return -1, None


def main():
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    start = (0, 0)
    treasure = (2, 3)

    print("Grid:")
    for row in grid:
        print(row)

    print("\nStart:", start)
    print("Treasure:", treasure)

    path_best = best_first_search(grid, start, treasure)
    cost_ucs, path_ucs = uniform_cost_search(grid, start, treasure)

    if path_best is None:
        print("\nTreasure not reachable.")
    else:
        print("\nBest First path:")
        print(path_best)

    if path_ucs is None:
        print("\nUniform Cost Search could not reach the treasure.")
    else:
        print("\nUniform Cost Search path:")
        print(path_ucs)
        print("Uniform Cost Search cost:", cost_ucs)


if __name__ == "__main__":
    main()
