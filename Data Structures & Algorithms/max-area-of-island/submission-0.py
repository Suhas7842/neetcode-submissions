class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        visit=set()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            area=1
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    nr,nc=row+dr,col+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc]==1 and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        q.append((nr,nc))
                        area+=1
            return area
        maxArea=0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c]==1:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea