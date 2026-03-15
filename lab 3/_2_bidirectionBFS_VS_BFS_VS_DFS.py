from collections import deque
import time
# deque → efficient queue operations for BFS (O(1) pop from left)
# time  → used to measure execution time of each algorithm


# ------------------------------------------------------------
# STANDARD BFS (EXACTLY AS GIVEN BY USER)
# ------------------------------------------------------------
def bfs_of_graph(V, adj, src):
    # vis[i] = True means node i has already been visited
    vis = [False]*V

    # Queue used for BFS traversal
    q = deque()

    # Mark source as visited and push into queue
    vis[src] = True
    q.append(src)

    # Stores BFS traversal order
    bfs = []
    
    # Continue until queue becomes empty
    while q:
        # Remove front element from queue
        node = q.popleft()

        # Add current node to BFS traversal list
        bfs.append(node)

        # Traverse all adjacent neighbors
        for nei in adj[node]:
            # Visit only unvisited neighbors
            if not vis[nei]:
                vis[nei] = True
                q.append(nei)

    # Return:
    # 1) BFS traversal order
    # 2) Number of nodes explored
    # 3) Length of traversal
    return bfs, sum(vis), len(bfs)


# ------------------------------------------------------------
# STANDARD DFS (RECURSIVE – EXACTLY AS GIVEN BY USER)
# ------------------------------------------------------------
def dfs_of_graph_recursive(V, adj, src):
    # vis array to track visited nodes
    vis = [False]*V

    # List to store DFS traversal order
    dfs = []
    
    # Recursive DFS helper function
    def dfs_fn(node):
        # Mark node as visited
        vis[node] = True

        # Add node to DFS traversal
        dfs.append(node)

        # Recursively visit unvisited neighbors
        for nei in adj[node]:
            if not vis[nei]:
                dfs_fn(nei)
    
    # Start DFS from source node
    dfs_fn(src)

    # Return:
    # 1) DFS traversal order
    # 2) Number of nodes explored
    # 3) Length of traversal
    return dfs, sum(vis), len(dfs)


# ------------------------------------------------------------
# BI-DIRECTIONAL BFS (SAME AS PREVIOUSLY USED)
# ------------------------------------------------------------
def bidirectional_bfs(V, adj, src, dest):
    # If source and destination are same,
    # shortest path is just the source
    if src == dest:
        return [src], 1, 1

    # Queue for BFS from source
    q1 = deque([src])

    # Queue for BFS from destination
    q2 = deque([dest])

    # Visited array for source BFS
    vis1 = [False]*V

    # Visited array for destination BFS
    vis2 = [False]*V

    # Parent arrays for path reconstruction
    parent1 = [-1]*V
    parent2 = [-1]*V

    # Mark source and destination as visited
    vis1[src] = True
    vis2[dest] = True

    # Variable to store meeting point of two BFS
    meet = -1

    # Continue while both BFS queues have nodes
    while q1 and q2:
        # Expand one level from source side
        u = q1.popleft()
        for v in adj[u]:
            if not vis1[v]:
                vis1[v] = True
                parent1[v] = u
                q1.append(v)

                # If destination BFS has visited this node,
                # searches meet here
                if vis2[v]:
                    meet = v
                    break
        if meet != -1:
            break

        # Expand one level from destination side
        u = q2.popleft()
        for v in adj[u]:
            if not vis2[v]:
                vis2[v] = True
                parent2[v] = u
                q2.append(v)

                # If source BFS has visited this node,
                # searches meet here
                if vis1[v]:
                    meet = v
                    break
        if meet != -1:
            break

    # Reconstruct path from source to meeting point
    path = []
    cur = meet
    while cur != -1:
        path.append(cur)
        cur = parent1[cur]
    path.reverse()  # reverse to get correct order

    # Reconstruct path from meeting point to destination
    cur = parent2[meet]
    while cur != -1:
        path.append(cur)
        cur = parent2[cur]

    # Total nodes explored = nodes explored from both sides
    nodes_explored = sum(vis1) + sum(vis2)

    # Path length = number of edges
    path_length = len(path) - 1

    # Return:
    # 1) Shortest path
    # 2) Nodes explored
    # 3) Path length
    return path, nodes_explored, path_length


# ------------------------------------------------------------
# PERFORMANCE COMPARISON DRIVER FUNCTION
# ------------------------------------------------------------
def main():
    # Number of vertices
    V = 12

    # Adjacency list representation of graph
    adj = [
        [1, 2, 3],
        [0, 4, 5],
        [0, 6, 7],
        [0, 8],
        [1, 9],
        [1, 6, 10],
        [2, 5, 11],
        [2, 8],
        [3, 7, 9],
        [4, 8, 10],
        [5, 9, 11],
        [6, 10]
    ]

    # Source and destination nodes
    src = 0
    dest = 11

    print("\n===== PERFORMANCE COMPARISON =====\n")

    # Measure BFS performance
    start = time.time()
    bfs_path, bfs_nodes, bfs_len = bfs_of_graph(V, adj, src)
    bfs_time = time.time() - start

    # Measure DFS performance
    start = time.time()
    dfs_path, dfs_nodes, dfs_len = dfs_of_graph_recursive(V, adj, src)
    dfs_time = time.time() - start

    # Measure Bi-Directional BFS performance
    start = time.time()
    bibfs_path, bibfs_nodes, bibfs_len = bidirectional_bfs(V, adj, src, dest)
    bibfs_time = time.time() - start

    # Output BFS results
    print("STANDARD BFS")
    print("Traversal Order:", bfs_path)
    print("Nodes Explored:", bfs_nodes)
    print("Traversal Length:", bfs_len)
    #print("Time Taken (s):", bfs_time)
    print()

    # Output DFS results
    print("STANDARD DFS (RECURSIVE)")
    print("Traversal Order:", dfs_path)
    print("Nodes Explored:", dfs_nodes)
    print("Traversal Length:", dfs_len)
    #print("Time Taken (s):", dfs_time)
    print()

    # Output Bi-Directional BFS results
    print("BI-DIRECTIONAL BFS")
    print("Shortest Path:", bibfs_path)
    print("Path Length:", bibfs_len)
    print("Nodes Explored:", bibfs_nodes)
    #print("Time Taken (s):", bibfs_time)
    print()

    # Final conclusions
    print("===== FINAL OBSERVATIONS =====")
    print("• DFS explores deeply and does not guarantee shortest path.")
    print("• BFS guarantees shortest path but explores many nodes.")
    print("• Bi-Directional BFS guarantees shortest path with fewer explorations.")
    print("• Bi-Directional BFS is most efficient for shortest paths in unweighted graphs.\n")


# Program entry point
if __name__ == "__main__":
    main()
