from collections import deque
import time

# ------------------------------------------------------------
# STANDARD BFS (EXACTLY AS GIVEN BY USER)
# ------------------------------------------------------------
def bfs_of_graph(V, adj, src):
    vis = [False]*V
    q = deque()
    vis[src] = True
    q.append(src)
    bfs = []
    
    while q:
        node = q.popleft()
        bfs.append(node)
        for nei in adj[node]:
            if not vis[nei]:
                vis[nei] = True
                q.append(nei)

    return bfs, sum(vis), len(bfs)


# ------------------------------------------------------------
# STANDARD DFS (RECURSIVE – EXACTLY AS GIVEN BY USER)
# ------------------------------------------------------------
def dfs_of_graph_recursive(V, adj, src):
    vis = [False]*V
    dfs = []
    
    def dfs_fn(node):
        vis[node] = True
        dfs.append(node)
        for nei in adj[node]:
            if not vis[nei]:
                dfs_fn(nei)
    
    dfs_fn(src)
    return dfs, sum(vis), len(dfs)


# ------------------------------------------------------------
# BI-DIRECTIONAL BFS (SAME AS PREVIOUSLY USED)
# ------------------------------------------------------------
def bidirectional_bfs(V, adj, src, dest):
    if src == dest:
        return [src], 1, 1

    q1 = deque([src])
    q2 = deque([dest])

    vis1 = [False]*V
    vis2 = [False]*V

    parent1 = [-1]*V
    parent2 = [-1]*V

    vis1[src] = True
    vis2[dest] = True

    meet = -1

    while q1 and q2:
        u = q1.popleft()
        for v in adj[u]:
            if not vis1[v]:
                vis1[v] = True
                parent1[v] = u
                q1.append(v)
                if vis2[v]:
                    meet = v
                    break
        if meet != -1:
            break

        u = q2.popleft()
        for v in adj[u]:
            if not vis2[v]:
                vis2[v] = True
                parent2[v] = u
                q2.append(v)
                if vis1[v]:
                    meet = v
                    break
        if meet != -1:
            break

    path = []
    cur = meet
    while cur != -1:
        path.append(cur)
        cur = parent1[cur]
    path.reverse()

    cur = parent2[meet]
    while cur != -1:
        path.append(cur)
        cur = parent2[cur]

    nodes_explored = sum(vis1) + sum(vis2)
    path_length = len(path) - 1

    return path, nodes_explored, path_length


# ------------------------------------------------------------
# PERFORMANCE COMPARISON DRIVER
# ------------------------------------------------------------
def main():
    V = 12
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

    src = 0
    dest = 11

    print("\n===== PERFORMANCE COMPARISON =====\n")

    start = time.perf_counter()
    bfs_path, bfs_nodes, bfs_len = bfs_of_graph(V, adj, src)
    bfs_time = time.perf_counter() - start

    start = time.perf_counter()
    dfs_path, dfs_nodes, dfs_len = dfs_of_graph_recursive(V, adj, src)
    dfs_time = time.perf_counter() - start

    start = time.perf_counter()
    bibfs_path, bibfs_nodes, bibfs_len = bidirectional_bfs(V, adj, src, dest)
    bibfs_time = time.perf_counter() - start

    print("STANDARD BFS")
    print("Traversal Order:", bfs_path)
    print("Nodes Explored:", bfs_nodes)
    print("Traversal Length:", bfs_len)
    print("Time Taken (seconds):", bfs_time)
    print()

    print("STANDARD DFS (RECURSIVE)")
    print("Traversal Order:", dfs_path)
    print("Nodes Explored:", dfs_nodes)
    print("Traversal Length:", dfs_len)
    print("Time Taken (seconds):", dfs_time)
    print()

    print("BI-DIRECTIONAL BFS")
    print("Shortest Path:", bibfs_path)
    print("Path Length:", bibfs_len)
    print("Nodes Explored:", bibfs_nodes)
    print("Time Taken (seconds):", bibfs_time)
    print()

    print("===== FINAL OBSERVATIONS =====")
    print("• DFS does not guarantee shortest path and explores deeply.")
    print("• BFS guarantees shortest path but explores many nodes.")
    print("• Bi-Directional BFS guarantees shortest path with fewer explorations.")
    print("• Bi-Directional BFS is the most efficient for shortest paths in unweighted graphs.\n")


if __name__ == "__main__":
    main()
