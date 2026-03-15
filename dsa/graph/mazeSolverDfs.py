def solve_maze_dfs(maze, start, goal):
    n, m = len(maze), len(maze[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    visited = set()
    path = []

    def dfs(x, y):
        if (x, y) in visited:
            return False
        if x < 0 or y < 0 or x >= n or y >= m:
            return False
        if maze[x][y] == 1:
            return False

        visited.add((x, y))
        path.append((x, y))

        if (x, y) == goal:
            return True

        for dx, dy in directions:
            if dfs(x + dx, y + dy):
                return True

        path.pop()
        return False

    if dfs(start[0], start[1]):
        return path
    return None

def main():
    maze = [
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (2, 3)

    path = solve_maze_dfs(maze, start, goal)

    if path:
        print("DFS Path Found:")
        print(path)
        print("Path Length:", len(path)-1)
    else:
        print("No path found")


if __name__ == "__main__":
    main()
