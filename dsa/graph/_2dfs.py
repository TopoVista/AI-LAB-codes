def dfs_util(node, vis, adj, dfs_list):
    vis[node] = 1
    dfs_list.append(node)
    
    for it in adj[node]:
        if not vis[it]:
            dfs_util(it, vis, adj, dfs_list)


def dfs_of_graph(V, adj):
    vis = [0] * V
    dfs_list = []
    
    dfs_util(0, vis, adj, dfs_list)
    return dfs_list


if __name__ == "__main__":
    V, E = map(int, input().split())

    adj = [[] for _ in range(V)]

    # Reading edges (undirected graph)
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)  # remove if directed

    ans = dfs_of_graph(V, adj)
    print(*ans)
