class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        pal=[[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or pal[i+1][j-1]):
                    pal[i][j]=True
                    
        res,partition=[],[]
        def dfs(i):
            if i>=len(s):
                res.append(partition.copy())
                return
            for j in range(i,len(s)):
                if pal[i][j]:
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
        dfs(0)
        return res