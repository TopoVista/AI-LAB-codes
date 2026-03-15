import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
# networkx → used to create and manage graph structures
# matplotlib → used for visualization of the graph
# deque → used for efficient queue operations in BFS


def bidirectional_bfs(V, adj, src, dest):
    # If source and destination are the same,
    # the shortest path is just the source itself
    if src == dest:
        return [src]

    # Queue for BFS starting from the source
    q1 = deque([src])
    # Queue for BFS starting from the destination
    q2 = deque([dest])

    # Visited array for BFS from source side
    vis1 = [False]*V
    # Visited array for BFS from destination side
    vis2 = [False]*V

    # Parent array for reconstructing path from source side
    parent1 = [-1]*V
    # Parent array for reconstructing path from destination side
    parent2 = [-1]*V

    # Mark source as visited in source BFS
    vis1[src] = True
    # Mark destination as visited in destination BFS
    vis2[dest] = True

    # Variable to store the meeting point of the two BFS searches
    meet = -1

    # Continue BFS until either queue becomes empty
    while q1 and q2:
        # Expand one level from source side
        u = q1.popleft()
        for v in adj[u]:
            # Visit unvisited neighbors
            if not vis1[v]:
                vis1[v] = True
                parent1[v] = u  # store parent for path reconstruction
                q1.append(v)
                # If destination BFS has already visited this node,
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
                # If source BFS has already visited this node,
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
    path.reverse()  # reverse to get correct order from source

    # Append path from meeting point to destination
    cur = parent2[meet]
    while cur != -1:
        path.append(cur)
        cur = parent2[cur]

    # Return the complete shortest path
    return path


def main():
    # Number of vertices in the graph
    V = 12

    # Adjacency list representation of the graph
    # Each index represents a node
    # Each list contains nodes directly connected to it
    adj = [
        [1, 2, 3],        # Node 0 connections
        [0, 4, 5],        # Node 1 connections
        [0, 6, 7],        # Node 2 connections
        [0, 8],           # Node 3 connections
        [1, 9],           # Node 4 connections
        [1, 6, 10],       # Node 5 connections
        [2, 5, 11],       # Node 6 connections
        [2, 8],           # Node 7 connections
        [3, 7, 9],        # Node 8 connections
        [4, 8, 10],       # Node 9 connections
        [5, 9, 11],       # Node 10 connections
        [6, 10]           # Node 11 connections
    ]

    # Source node
    src = 0
    # Destination node
    dest = 11

    # Find shortest path using bi-directional BFS
    path = bidirectional_bfs(V, adj, src, dest)

    # Create an undirected graph using NetworkX
    G = nx.Graph()

    # Add edges to the graph using adjacency list
    for u in range(V):
        for v in adj[u]:
            G.add_edge(u, v)

    # Compute positions for visualization using force-directed layout
    pos = nx.spring_layout(G, seed=42)

    # Create a figure for visualization
    plt.figure(figsize=(9, 7))

    # Draw the full graph
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="lightblue",
        font_size=12,
        font_weight="bold"
    )

    # Convert path into edge pairs for highlighting
    path_edges = list(zip(path, path[1:]))

    # Highlight shortest path edges in red
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        edge_color="red",
        width=4
    )

    # Highlight source node in green
    nx.draw_networkx_nodes(
        G, pos, nodelist=[src], node_color="green", node_size=2300
    )

    # Highlight destination node in orange
    nx.draw_networkx_nodes(
        G, pos, nodelist=[dest], node_color="orange", node_size=2300
    )

    # Add title to the visualization
    plt.title("Complex Graph – Bi-Directional BFS Shortest Path", fontsize=14)

    # Display the graph
    plt.show()


# Entry point of the program
if __name__ == "__main__":
    main()
