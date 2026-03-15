import heapq  # Import heapq module for priority queue operations (min-heap)
from collections import deque  # Import deque for potential queue usage, though not used here

# Define the goal state for the 8-puzzle as a tuple of tuples (immutable)
GOAL_STATE = ((1,2,3),
              (4,5,6),
              (7,8,0))  # 0 represents the empty tile

# Define possible moves: up, down, left, right as (dx, dy) tuples
MOVES = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, Down, Left, Right

def find_zero(state):  # Function to find the position of the empty tile (0)
    for i in range(3):  # Iterate over rows
        for j in range(3):  # Iterate over columns
            if state[i][j] == 0:  # Check if current cell is empty
                return i,j  # Return row and column indices

def misplaced_tiles(state):  # Heuristic function: count misplaced tiles (excluding empty tile)
    cnt = 0  # Initialize counter
    for i in range(3):  # Iterate over rows
        for j in range(3):  # Iterate over columns
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:  # If tile is not empty and not in correct position
                cnt += 1  # Increment counter
    return cnt  # Return the count of misplaced tiles

def manhattan_distance(state):  # Heuristic function: calculate Manhattan distance for all tiles
    dist = 0  # Initialize total distance
    for i in range(3):  # Iterate over rows
        for j in range(3):  # Iterate over columns
            val = state[i][j]  # Get the value of the tile
            if val != 0:  # Skip the empty tile
                x = (val-1)//3  # Calculate goal row: (value-1) // 3
                y = (val-1)%3   # Calculate goal column: (value-1) % 3
                dist += abs(i-x) + abs(j-y)  # Add Manhattan distance for this tile
    return dist  # Return total Manhattan distance

def get_neighbors(state):  # Function to generate all valid neighbor states by moving the empty tile
    x,y = find_zero(state)  # Find current position of empty tile
    neighbors = []  # List to store neighbor states
    for dx,dy in MOVES:  # Iterate over possible moves
        nx,ny = x+dx,y+dy  # Calculate new position
        if 0<=nx<3 and 0<=ny<3:  # Check if new position is within bounds
            new = [list(r) for r in state]  # Create a mutable copy of the state
            new[x][y],new[nx][ny] = new[nx][ny],new[x][y]  # Swap empty tile with the tile at new position
            neighbors.append(tuple(tuple(r) for r in new))  # Convert back to immutable tuple and add to neighbors
    return neighbors  # Return list of neighbor states

def a_star(start, heuristic):  # A* search algorithm implementation
    pq = []  # Priority queue for nodes: (f_score, g_score, state)
    heapq.heappush(pq,(heuristic(start),0,start))  # Push start state with f = h, g = 0
    visited = set()  # Set to track visited states
    came_from = {}  # Track parent states for path reconstruction
    nodes_expanded = 0  # Counter for nodes expanded

    while pq:  # While priority queue is not empty
        f,g,state = heapq.heappop(pq)  # Pop the node with lowest f_score

        if state in visited:  # If state already visited, skip
            continue

        visited.add(state)  # Mark state as visited
        nodes_expanded += 1  # Increment expanded nodes counter

        if state == GOAL_STATE:  # If goal state reached
            # Reconstruct path by backtracking from goal to start
            path = []
            current = state
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, nodes_expanded  # Return path and nodes expanded

        for nxt in get_neighbors(state):  # Generate neighbors
            if nxt not in visited:  # If neighbor not visited
                came_from[nxt] = state  # Record parent for path reconstruction
                h = heuristic(nxt)  # Calculate heuristic for neighbor
                heapq.heappush(pq,(g+1+h,g+1,nxt))  # Push neighbor with f = g+1 + h, g+1

    return [], nodes_expanded  # If no solution found, return empty path and nodes expanded

def main():  # Main function to run the A* search with both heuristics and display paths
    start_state = ((1,2,3),  # Define initial puzzle state
                   (4,0,6),
                   (7,5,8))

    print("Initial State:")  # Print initial state
    for r in start_state:
        print(r)

    print("\nUsing H1: Misplaced Tiles")  # Run A* with misplaced tiles heuristic
    path1,nodes1 = a_star(start_state,misplaced_tiles)
    print("Solution Path:")
    for step, state in enumerate(path1):
        print(f"Step {step}:")
        for r in state:
            print(r)
        print()
    print("Nodes Expanded:",nodes1)

    print("\nUsing H2: Manhattan Distance")  # Run A* with Manhattan distance heuristic
    path2,nodes2 = a_star(start_state,manhattan_distance)
    print("Solution Path:")
    for step, state in enumerate(path2):
        print(f"Step {step}:")
        for r in state:
            print(r)
        print()
    print("Nodes Expanded:",nodes2)

    print("\nComparison:")  # Compare the two heuristics
    print("H1 expanded",nodes1,"nodes")
    print("H2 expanded",nodes2,"nodes")

if __name__ == "__main__":  # Standard Python idiom to run main when script is executed directly
    main()
