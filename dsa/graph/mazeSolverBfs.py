from collections import deque

def solve_maze_bfs(maze, start, goal):
    n, m = len(maze), len(maze[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    q = deque([start])
    visited = set([start])
    parent = {}

    while q:
        x, y = q.popleft()

        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    q.append((nx, ny))

    return None


def main():
    maze = [
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (2, 3)

    path = solve_maze_bfs(maze, start, goal)

    if path:
        print("BFS Path Found:")
        print(path)
        print("Path Length:", len(path)-1)
    else:
        print("No path found")


if __name__ == "__main__":
    main()
