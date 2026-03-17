import heapq

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

def best_first_search(adj, src, dst):
    n = len(adj)
    parent = [-1] * n
    visited = [False] * n

    def heuristic(node):
        return abs(dst - node)

    pq = [(heuristic(src), src)]
    visited[src] = True

    while pq:
        _, u = heapq.heappop(pq)
        if u == dst:
            break
        for v, _ in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                heapq.heappush(pq, (heuristic(v), v))

    if not visited[dst]:
        return -1, []

    path = []
    cur = dst
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return len(path) - 1, path

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
    steps, path_best = best_first_search(adj, src, dst)
    print("Best First path length:", steps, "edges")
    print("Best First path:", path_best)

if __name__ == "__main__":
    main()



