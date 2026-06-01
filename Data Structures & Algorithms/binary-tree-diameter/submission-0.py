# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        self.dfs(root,self.res)
        return self.res
    def dfs(self,root,res):
        if not root:
            return 0
        left,right=self.dfs(root.left,res),self.dfs(root.right,res)
        self.res=max(self.res,left+right)
        return max(left,right)+1