from collections import deque

def bfs_of_graph(adj, src):
    q = deque()
    vis = set()
    q.append(src)
    vis.add(src)
    bfs = []
    while q:
        node = q.popleft()
        bfs.append(node)
        for nei in adj[node]:
            if nei not in vis:
                vis.add(nei)
                q.append(nei)
    return bfs


def dfs_graph_recursive(adj, src):
    vis = set()
    dfs = []
    def dfs_fn(node):
        vis.add(node)
        dfs.append(node)
        for nei in adj[node]:
            if nei not in vis:
                dfs_fn(nei)
    dfs_fn(src)
    return dfs


def dfs_graph_stack(adj, src):
    stack = [src]
    vis = set([src])
    dfs = []
    while stack:
        node = stack.pop()
        dfs.append(node)
        for nei in reversed(adj[node]):
            if nei not in vis:
                vis.add(nei)
                stack.append(nei)
    return dfs


def main():
    adj = {
        "S": ["A", "B"],
        "A": ["S", "C", "D"],
        "B": ["S", "D"],
        "C": ["A", "E"],
        "D": ["A", "B", "E"],
        "E": ["C", "D", "G"],
        "G": ["E"]
    }

    src = "S"

    print("bfs:", bfs_of_graph(adj, src))
    print("dfs(rec):", dfs_graph_recursive(adj, src))
    print("dfs(stack):", dfs_graph_stack(adj, src))


if __name__ == "__main__":
    main()
