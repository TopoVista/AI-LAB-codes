import heapq  # Import heapq module for priority queue operations, essential for Uniform Cost Search (UCS) which needs to always expand the node with the lowest cost
from collections import deque  # Import deque from collections for efficient queue operations in BFS, providing O(1) append and popleft operations

def uniform_cost_search(adj, src, dst):  # Define the Uniform Cost Search function that finds the shortest path in terms of cost from source to destination in a weighted graph
    n = len(adj)  # Get the number of nodes in the graph by finding the length of the adjacency list
    dist = [float('inf')] * n  # Initialize distance array with infinity for all nodes, representing the minimum cost to reach each node from source
    parent = [-1] * n  # Initialize parent array to keep track of the path; -1 indicates no parent (used for path reconstruction)
    dist[src] = 0  # Set the distance of the source node to 0, as the cost to reach itself is zero
    pq = [(0, src)]  # Initialize a priority queue (min-heap) with the source node and its cost (0); heapq will maintain the order based on cost
    while pq:  # Continue the search while there are nodes in the priority queue to explore
        cost, u = heapq.heappop(pq)  # Extract the node with the smallest cost from the priority queue; cost is the current minimum distance to u
        if cost > dist[u]:  # If the extracted cost is greater than the recorded distance, skip this node (it means a better path was already found)
            continue  # Skip processing this node as it's outdated
        for v, w in adj[u]:  # Iterate through all neighbors v of node u, where w is the edge weight (cost) from u to v
            if dist[v] > cost + w:  # Check if a shorter path to v is found through u (current cost to u plus edge weight)
                dist[v] = cost + w  # Update the distance to v with the new shorter cost
                parent[v] = u  # Set u as the parent of v for path reconstruction
                heapq.heappush(pq, (dist[v], v))  # Push the updated distance and node v into the priority queue for further exploration
    if dist[dst] == float('inf'):  # After exploration, check if the destination is unreachable (distance still infinity)
        return -1, []  # Return -1 for cost and empty list for path if no path exists
    path = []  # Initialize an empty list to store the path from source to destination
    cur = dst  # Start from the destination node
    while cur != -1:  # Traverse backwards using the parent array until reaching the source (-1 indicates source)
        path.append(cur)  # Append the current node to the path
        cur = parent[cur]  # Move to the parent of the current node
    path.reverse()  # Reverse the path list to get the correct order from source to destination
    return dist[dst], path  # Return the minimum cost to destination and the path as a list of nodes

def bfs(adj, src, dst):  # Define the Breadth-First Search function for unweighted graphs, finding the shortest path in terms of number of edges
    n = len(adj)  # Get the number of nodes in the graph
    dist = [-1] * n  # Initialize distance array with -1 for all nodes; -1 indicates unvisited nodes
    parent = [-1] * n  # Initialize parent array for path reconstruction, similar to UCS
    q = deque([src])  # Initialize a queue with the source node; deque allows efficient FIFO operations
    dist[src] = 0  # Set distance of source to 0
    while q:  # Continue while there are nodes in the queue
        u = q.popleft()  # Dequeue the front node (FIFO order ensures level-by-level exploration)
        for v, _ in adj[u]:  # Iterate through neighbors of u; ignore the weight since BFS treats all edges as cost 1
            if dist[v] == -1:  # If v is not visited (distance is -1)
                dist[v] = dist[u] + 1  # Set distance to v as distance to u plus 1 (since each edge has uniform cost)
                parent[v] = u  # Set parent for path reconstruction
                q.append(v)  # Enqueue v for further exploration
    if dist[dst] == -1:  # Check if destination is unreachable
        return -1, []  # Return -1 and empty path if no path
    path = []  # Initialize path list
    cur = dst  # Start from destination
    while cur != -1:  # Traverse backwards via parents
        path.append(cur)  # Append to path
        cur = parent[cur]  # Move to parent
    path.reverse()  # Reverse to get correct order
    return dist[dst], path  # Return distance (number of edges) and path

def main():  # Define the main function to demonstrate UCS and BFS on a much larger sample graph
    adj = [[] for _ in range(30)]  # Initialize adjacency list for 30 nodes (0 to 29)
    for i in range(29):  # Create a long chain from 0 to 29 with low cost edges (cost 1 each)
        adj[i].append((i+1, 1))  # Each consecutive node connected with cost 1
    adj[0].append((29, 200))  # Add a direct high-cost edge from 0 to 29 (cost 200) to create the difference
    src, dst = 0, 29  # Set source as 0 and destination as 29; this large graph shows BFS taking the direct edge (1 edge, high cost) while UCS takes the long chain (29 edges, low total cost)
    cost, path = uniform_cost_search(adj, src, dst)  # Call UCS; it will find the minimum cost path through the chain
    print("UCS cost:", cost)  # Print the minimum cost (should be 29)
    print("UCS path length:", len(path)-1, "edges")  # Print number of edges in UCS path
    print("UCS path:", path)  # Print the full path found by UCS (all 30 nodes from 0 to 29)
    dist, path_bfs = bfs(adj, src, dst)  # Call BFS; it will find the minimum edge path (direct edge)
    print("BFS distance:", dist)  # Print the distance in edges (should be 1)
    print("BFS path:", path_bfs)  # Print the BFS path (should be [0, 29])

if __name__ == "__main__":  # Standard Python idiom to ensure main() is called only when the script is run directly, not imported
    main()  # Call the main function to execute the demonstration
