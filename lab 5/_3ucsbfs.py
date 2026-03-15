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
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[src] = 0

    q = deque([src])
    while q:
        node = q.popleft()
        for nei, _ in adj[node]:
            if dist[nei] == float('inf'):
                dist[nei] = dist[node] + 1
                parent[nei] = node
                q.append(nei)

    if dist[dst] == float('inf'):
        return -1, []

    path = []
    cur = dst
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return dist[dst], path


if __name__ == "__main__":
    adj = [
        [(1, 10), (2, 1)],
        [(4, 1)],
        [(3, 1)],
        [(4, 1)],
        []
    ]

    src, dst = 0, 4

    cost, path = uniform_cost_search(adj, src, dst)
    print("UCS cost:", cost)
    print("UCS path length:", len(path) - 1, "edges")
    print("UCS path:", path)

    dist, path_bfs = bfs(adj, src, dst)
    print("BFS distance:", dist)
    print("BFS path:", path_bfs)
