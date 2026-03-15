from collections import deque
# deque is used for efficient queue operations (O(1) pop from front)


def bidirectional_bfs(V, adj, src, dest):
    # If source and destination are the same,
    # the shortest path is trivially the source itself
    if src == dest:
        return [src]

    # Queue for BFS starting from the source node
    q1 = deque([src])
    # Queue for BFS starting from the destination node
    q2 = deque([dest])

    # Visited array for BFS from the source side
    vis1 = [False] * V
    # Visited array for BFS from the destination side
    vis2 = [False] * V

    # Parent array to reconstruct path from source side
    parent1 = [-1] * V
    # Parent array to reconstruct path from destination side
    parent2 = [-1] * V

    # Mark source as visited in source BFS
    vis1[src] = True
    # Mark destination as visited in destination BFS
    vis2[dest] = True

    # This variable stores the meeting node where both BFS meet
    meet = -1

    # Continue BFS until either side runs out of nodes
    while q1 and q2:
        # Expand one BFS level from source side
        node = q1.popleft()
        for nei in adj[node]:
            # Visit only unvisited nodes
            if not vis1[nei]:
                vis1[nei] = True
                parent1[nei] = node  # record parent for path reconstruction
                q1.append(nei)

                # If destination BFS has already visited this node,
                # the two searches meet here
                if vis2[nei]:
                    meet = nei
                    break
        if meet != -1:
            break

        # Expand one BFS level from destination side
        node = q2.popleft()
        for nei in adj[node]:
            if not vis2[nei]:
                vis2[nei] = True
                parent2[nei] = node
                q2.append(nei)

                # If source BFS has already visited this node,
                # the searches meet here
                if vis1[nei]:
                    meet = nei
                    break
        if meet != -1:
            break

    # Reconstruct the path from source to meeting point
    path = []
    cur = meet
    while cur != -1: # since the parent of the source node is set to -1
        path.append(cur)
        cur = parent1[cur]
    path.reverse()  # reverse to get correct source → meet order

    # Reconstruct path from meeting point to destination
    cur = parent2[meet]
    while cur != -1:
        path.append(cur)
        cur = parent2[cur]

    # Return the complete shortest path
    return path


def main():
    # Number of vertices in the graph
    V = 12

    # Adjacency list representation of an undirected graph
    # Each index represents a node
    # Each list contains its directly connected neighbors
    adj = [
        [1, 2, 3],        # Node 0
        [0, 4, 5],        # Node 1
        [0, 6, 7],        # Node 2
        [0, 8],           # Node 3
        [1, 9],           # Node 4
        [1, 6, 10],       # Node 5
        [2, 5, 11],       # Node 6
        [2, 8],           # Node 7
        [3, 7, 9],        # Node 8
        [4, 8, 10],       # Node 9
        [5, 9, 11],       # Node 10
        [6, 10]           # Node 11
    ]

    # Define source and destination nodes
    src = 0
    dest = 11

    # Compute shortest path using bi-directional BFS
    path = bidirectional_bfs(V, adj, src, dest)

    # Output the result
    print("Bi-Directional BFS Shortest Path:")
    print(path)


# Entry point of the program
if __name__ == "__main__":
    main()
