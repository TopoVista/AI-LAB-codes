import heapq
# heapq provides a min-heap implementation
# UCS relies on always expanding the node with the minimum total cost


def uniform_cost_search(adj, src, dest):
    """
    Uniform Cost Search (UCS)

    adj  : adjacency list where adj[u] = [(v, cost), ...]
    src  : starting node
    dest : goal node
    """

    # Priority Queue stores:
    # (total_cost_from_src, current_node, path_so_far)
    pq = []

    # Push source with cost 0 and path containing only src
    heapq.heappush(pq, (0, src, [src]))

    # Dictionary to store minimum cost at which a node is visited
    # This avoids revisiting nodes with higher cost paths
    visited_cost = {}

    while pq:
        # Pop node with minimum cumulative cost
        curr_cost, node, path = heapq.heappop(pq)

        # If destination is reached, UCS guarantees this is optimal
        if node == dest:
            return path, curr_cost

        # If node already visited with a lower or equal cost, skip it
        if node in visited_cost and visited_cost[node] <= curr_cost:
            continue

        # Record the best cost for this node
        visited_cost[node] = curr_cost

        # Explore all neighbors
        for nei, edge_cost in adj[node]:
            new_cost = curr_cost + edge_cost

            # Push neighbor with updated cost and path
            heapq.heappush(
                pq,
                (new_cost, nei, path + [nei])
            )

    # Destination unreachable
    return None, float("inf")


def main():
    """
    Bigger weighted graph:

            2        3
        S ------ A ------ C
        |        |        |
      5 |        | 8      | 2
        |        |        |
        B ------ D ------ E ------ G
            2        1        3

    There are MANY paths from S to G.
    UCS must choose the one with minimum TOTAL COST,
    not minimum edges.
    """

    # Weighted adjacency list
    adj = {
        "S": [("A", 2), ("B", 5)],
        "A": [("S", 2), ("C", 3), ("D", 8)],
        "B": [("S", 5), ("D", 2)],
        "C": [("A", 3), ("E", 2)],
        "D": [("A", 8), ("B", 2), ("E", 1)],
        "E": [("C", 2), ("D", 1), ("G", 3)],
        "G": [("E", 3)]
    }

    src = "S"
    dest = "G"

    path, cost = uniform_cost_search(adj, src, dest)

    print("\n===== UNIFORM COST SEARCH (BIGGER GRAPH) =====")
    print("Optimal Path:", path)
    print("Total Path Cost:", cost)


# Program entry point
if __name__ == "__main__":
    main()
