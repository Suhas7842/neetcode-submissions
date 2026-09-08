class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Every land cell contributes 4 sides
                    perimeter += 4
                    # Shared edge with land on the right
                    if c + 1 < cols and grid[r][c + 1] == 1:
                        perimeter -= 2
                    # Shared edge with land below
                    if r + 1 < rows and grid[r + 1][c] == 1:
                        perimeter -= 2
        return perimeter