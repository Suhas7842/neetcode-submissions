class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        count=0
        visit=set()
        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    dfs(neighbor)
        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                count += 1
        return count