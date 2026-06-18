class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank=[1]*(n+1)
        def find(node):
            if node!=parent[node]:
                return find(parent[node])
            return parent[node]
        def union(node1,node2):
            root1,root2=find(node1),find(node2)
            if root1==root2:
                return False
            if rank[root2]>rank[root1]:
                parent[root1]=root2
                rank[root2]+=rank[root1]
            else:
                parent[root2]=root1
                rank[root1]+=rank[root2]
            return True
        for u,v in edges:
            if not union(u,v):
                return [u,v]