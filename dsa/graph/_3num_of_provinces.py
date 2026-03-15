class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [0] * n
        
        def dfs(node):
            vis[node] = 1
            for nei in range(n):
                if isConnected[node][nei] == 1 and not vis[nei]:
                    dfs(nei)

        provinces = 0
        for i in range(n):
            if not vis[i]:
                provinces += 1
                dfs(i)

        return provinces
