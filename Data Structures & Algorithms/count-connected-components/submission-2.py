class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank=[1]*n
        def find(node):
            while node!=parent[node]:
                parent[node]=parent[parent[node]]
                node=parent[node]
            return node
        def union(node1,node2):
            root1,root2=find(node1),find(node2)
            if root1==root2:
                return 0
            if rank[root2]>rank[root1]:
                parent[root1]=root2
                rank[root2]+=rank[root1]
            else:
                parent[root2]=root1
                rank[root1]+=rank[root2]
            return 1
        count=n
        for u,v in edges:
            if union(u,v):
                count-=1
        return count