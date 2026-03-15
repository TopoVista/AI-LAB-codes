import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve_maze_astar(maze, start, goal):
    n, m = len(maze), len(maze[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    pq = []
    heapq.heappush(pq, (0, start))

    g_cost = {start: 0}
    parent = {}

    while pq:
        _, (x, y) = heapq.heappop(pq)

        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0:
                new_cost = g_cost[(x, y)] + 1
                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    f_cost = new_cost + manhattan((nx, ny), goal)
                    parent[(nx, ny)] = (x, y)
                    heapq.heappush(pq, (f_cost, (nx, ny)))

    return None


def main():
    maze = [
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (2, 3)

    path = solve_maze_astar(maze, start, goal)

    if path:
        print("A* Path Found:")
        print(path)
        print("Path Length:", len(path)-1)
    else:
        print("No path found")


if __name__ == "__main__":
    main()
