import heapq
import networkx as nx
import matplotlib.pyplot as plt

def uniform_cost_search(adj, src, dest):
    pq = []
    heapq.heappush(pq, (0, src, [src]))
    visited_cost = {}
    while pq:
        curr_cost, node, path = heapq.heappop(pq)
        if node == dest:
            return path, curr_cost
        if node in visited_cost and visited_cost[node] <= curr_cost:
            continue
        visited_cost[node] = curr_cost
        for nei, edge_cost in adj[node]:
            new_cost = curr_cost + edge_cost
            heapq.heappush(pq, (new_cost, nei, path + [nei]))
    return None, float("inf")

def main():
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

    G = nx.DiGraph()
    for u in adj:
        for v, w in adj[u]:
            G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 7))

    nx.draw(G, pos, with_labels=True, node_size=2500, node_color="lightblue", font_size=12, font_weight="bold")
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4, edge_color="red")

    nx.draw_networkx_nodes(G, pos, nodelist=[src], node_color="green", node_size=2600)
    nx.draw_networkx_nodes(G, pos, nodelist=[dest], node_color="orange", node_size=2600)

    plt.title(f"UCS Shortest Path: {path} (Cost = {cost})")
    plt.show()

if __name__ == "__main__":
    main()
