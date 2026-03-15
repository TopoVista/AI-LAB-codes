import heapq
from collections import deque

def uniform_cost_search(adj, src, dst):
    n = len(adj)
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        cost, u = heapq.heappop(pq)
        if cost > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > cost + w:
                dist[v] = cost + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    if dist[dst] == float('inf'):
        return -1, []
    path = []
    cur = dst
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return dist[dst], path

def bfs(adj, src, dst):
    n = len(adj)
    dist = [-1] * n
    parent = [-1] * n
    q = deque([src])
    dist[src] = 0
    while q:
        u = q.popleft()
        for v, _ in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)
    if dist[dst] == -1:
        return -1, []
    path = []
    cur = dst
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return dist[dst], path

def main():
    adj = [[] for _ in range(30)]
    for i in range(29):
        adj[i].append((i+1, 1))
    adj[0].append((29, 200))
    src, dst = 0, 29
    cost, path = uniform_cost_search(adj, src, dst)
    print("UCS cost:", cost)
    print("UCS path length:", len(path)-1, "edges")
    print("UCS path:", path)
    dist, path_bfs = bfs(adj, src, dst)
    print("BFS distance:", dist)
    print("BFS path:", path_bfs)

if __name__ == "__main__":
    main()



