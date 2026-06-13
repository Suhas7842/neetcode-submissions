class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS,COLS = len(grid),len(grid[0])
        islands=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            q=collections.deque()
            grid[r][c] = "0"
            q.append((r,c))
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    nr,nc=row+dr,col+dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1"):
                        grid[nr][nc] = "0"
                        q.append((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1
        return islands