from collections import deque

def bfs_of_graph(V, adj):
    vis=[0]*V
    bfs=[]
    q=deque()

    vis[0]=1
    q.append(0)

    while q:
        node=q.popleft()
        bfs.append(node)
        for nei in adj[node]:
            if not vis[nei]:
                vis[nei]=1
                q.append(nei)
    return bfs

if __name__=="__main__":
    V,E=map(int,input().split())

    adj=[[] for _ in range(V)]

    for _ in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)  # remove for directed graph

    ans=bfs_of_graph(V,adj)
    print(ans)
