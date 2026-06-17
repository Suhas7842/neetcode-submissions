class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if not n:
            return True
        adj={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit=set()
        def dfs(node,prev):
            if node in visit:
                return False
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor==prev:
                    continue
                if not dfs(neighbor,node):
                    return False
            return True
        return dfs(0,-1) and len(visit)==n