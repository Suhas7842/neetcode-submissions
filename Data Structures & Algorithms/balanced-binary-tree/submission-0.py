# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)!=-1
    def dfs(self,root):
        if root==None:
            return 0
        lh,rh=self.dfs(root.left),self.dfs(root.right)
        if lh==-1 or rh==-1 or abs(lh-rh)>1:
            return -1
        return max(lh,rh)+1