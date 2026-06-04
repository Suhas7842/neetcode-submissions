# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath=float('-inf')
        def path(node):
            if not node:
                return 0
            left,right=path(node.left),path(node.right)
            if left<0:
                left=0
            if right<0:
                right=0
            self.maxPath=max(self.maxPath,node.val+left+right)
            return node.val+max(left,right)
        path(root)
        return self.maxPath