from collections import deque

def bfs_of_graph(V, adj, src):
    q = deque()
    vis = [False]*V
    q.append(src)
    vis[src] = True
    bfs = []
    while q:
        node = q.popleft()
        bfs.append(node)
        for nei in adj[node]:
            if not vis[nei]:
                vis[nei] = True
                q.append(nei)
    return bfs

def dfs_graph_recursive(V, adj, src):
    vis = [False]*V
    dfs = []
    def dfs_fn(node):
        vis[node] = True
        dfs.append(node)
        for nei in adj[node]:
            if not vis[nei]:
                dfs_fn(nei)
    dfs_fn(src)
    return dfs

def dfs_graph_stack(V, adj, src):
    stack = [src]
    vis = [False]*V
    vis[src] = True
    dfs = []
    while stack:
        node = stack.pop()
        dfs.append(node)
        for nei in reversed(adj[node]):
            if not vis[nei]:
                vis[nei] = True
                stack.append(nei)
    return dfs

def main():
    V, E = map(int, input().split()) 
    adj = [[] for _ in range(V)]

    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)  # remove this if directed

    src = int(input())  # source node

    print("bfs:", bfs_of_graph(V, adj, src))
    print("dfs(rec):", dfs_graph_recursive(V, adj, src))
    print("dfs(stack):", dfs_graph_stack(V, adj, src))

if __name__ == "__main__":
    main()
#sample input
# 6 5
# 0 1
# 0 2
# 1 3
# 1 4
# 2 5
# 0
