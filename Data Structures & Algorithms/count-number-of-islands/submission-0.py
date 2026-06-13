class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS,COLS = len(grid),len(grid[0])
        islands=0
        visit=set()
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    nr,nc=row+dr,col+dc
                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visit and grid[nr][nc]=="1":
                        visit.add((nr,nc))
                        q.append((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands