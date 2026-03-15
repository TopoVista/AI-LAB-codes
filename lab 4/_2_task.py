import heapq                     # heapq provides a priority queue (min-heap) which Best-First Search relies on

# Manhattan heuristic moved outside the function so it is reusable and clearer
def manhattan(x, y, tx, ty):     # Computes estimated distance from (x,y) to target (tx,ty)
    return abs(x - tx) + abs(y - ty)   # Manhattan distance: moves only vertically/horizontally


def best_first_search(grid, start, treasure):
    n, m = len(grid), len(grid[0])     # Dimensions of the grid (rows = n, columns = m)
    sx, sy = start                     # Start coordinates
    tx, ty = treasure                  # Target/treasure coordinates

    def h(x, y):                       # Internal wrapper that uses the external heuristic
        return manhattan(x, y, tx, ty) # Evaluate heuristic for a specific cell

    pq = []                            # Priority queue storing (heuristic_value, node)
    heapq.heappush(pq, (h(sx, sy), (sx, sy)))  # Insert starting node with its heuristic score

    visited = set()                    # Keeps track of visited cells so we don't revisit them
    visited.add((sx, sy))              # Mark start as visited
    parent = {}                        # To reconstruct the path once treasure is found

    directions = [(1,0), (-1,0), (0,1), (0,-1)]  # Moves allowed: down, up, right, left (no diagonals)

    while pq:                          # Continue while there are nodes to process
        _, (x, y) = heapq.heappop(pq)  # Pop the node with the smallest heuristic value (most promising)

        if (x, y) == (tx, ty):         # If we reached the treasure:
            path = []                  # Reconstruct path backwards using parent dictionary
            while (x, y) != (sx, sy):  # Stop when we return to the start
                path.append((x, y))    # Add current cell to path
                x, y = parent[(x, y)]  # Move one step backwards along the stored parent path
            path.append((sx, sy))      # Finally add start
            return path[::-1]          # Reverse path to get direction from start → treasure

        for dx, dy in directions:      # Try exploring all 4 directions from current cell
            nx, ny = x + dx, y + dy    # Calculate next position
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                # This checks:
                # 1. new cell is inside grid boundaries
                # 2. the cell is not an obstacle (grid value 0 = walkable, 1 = blocked)

                if (nx, ny) not in visited:   # Explore only if not visited before
                    visited.add((nx, ny))     # Mark as visited immediately to avoid duplicates
                    parent[(nx, ny)] = (x, y) # Store how we reached this cell
                    heapq.heappush(pq, (h(nx, ny), (nx, ny)))
                    # Push the new cell into the priority queue along with its heuristic score
                    # Lower score = explored sooner

    return None                         # If priority queue empties without finding treasure → not reachable



def main():
    grid = [
        [0, 0, 0, 0],                   # 0 = free cell
        [0, 1, 1, 0],                   # 1 = wall/obstacle
        [0, 0, 0, 0]
    ]

    start = (0, 0)                      # Starting cell (top-left corner)
    treasure = (2, 3)                   # Treasure cell (bottom-right corner)

    print("Grid:")
    for row in grid:
        print(row)

    print("\nStart:", start)
    print("Treasure:", treasure)

    path = best_first_search(grid, start, treasure)  # Run the search

    if path is None:
        print("\nTreasure not reachable.")
    else:
        print("\nPath found:")
        print(path)
        # The path printed is the greedy route the heuristic chooses.


if __name__ == "__main__":
    main()                              # Entry point of the script
