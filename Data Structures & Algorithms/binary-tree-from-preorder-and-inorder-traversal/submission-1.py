# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        inorder_map={val:i for i,val in enumerate(inorder)}
        preorder_index=0
        def helper(left,right):
            if left>right:
                return None
            nonlocal preorder_index
            root_val=preorder[preorder_index]
            root=TreeNode(root_val)
            preorder_index+=1
            mid=inorder_map[root_val]
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root
        return helper(0,len(inorder)-1)