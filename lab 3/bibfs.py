from collections import deque

def bidirectional_bfs(V, adj, src, dest):
    if src == dest:
        return [src]

    q1 = deque([src])
    q2 = deque([dest])

    vis1 = [False] * V
    vis2 = [False] * V

    parent1 = [-1] * V
    parent2 = [-1] * V

    vis1[src] = True
    vis2[dest] = True

    meet = -1

    while q1 and q2:
        node = q1.popleft()
        for nei in adj[node]:
            if not vis1[nei]:
                vis1[nei] = True
                parent1[nei] = node
                q1.append(nei)

                if vis2[nei]:
                    meet = nei
                    break
                
        if meet != -1:
            break

        node = q2.popleft()
        for nei in adj[node]:
            if not vis2[nei]:
                vis2[nei] = True
                parent2[nei] = node
                q2.append(nei)

                if vis1[nei]:
                    meet = nei
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

    return path


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

    path = bidirectional_bfs(V, adj, src, dest)

    print("Bi-Directional BFS Shortest Path:")
    print(path)


if __name__ == "__main__":
    main()
