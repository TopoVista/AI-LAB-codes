adj = [[] for _ in range(30)]
    for i in range(29):
        adj[i].append((i+1, 1))
    adj[0].append((29, 200))
    src, dst = 0, 29