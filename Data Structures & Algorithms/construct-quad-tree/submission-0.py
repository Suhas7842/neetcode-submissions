"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, size):
            value = grid[r][c]
            same = True
            # Check whether entire region has the same value
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != value:
                        same = False
                        break
                if not same:
                    break
            # Region is uniform
            if same:
                return Node(value == 1, True)
            # Divide into 4 quadrants
            half = size // 2
            topLeft = dfs(r, c, half)
            topRight = dfs(r, c + half, half)
            bottomLeft = dfs(r + half, c, half)
            bottomRight = dfs(r + half, c + half, half)
            return Node(
                True,
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )
        return dfs(0, 0, len(grid))