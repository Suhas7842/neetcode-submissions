# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if (root == None):
            return res
        q=collections.deque()
        q.append(root)
        while q:
            qLen=len(q)
            rightmost=None
            for i in range(qLen):
                node=q.popleft()
                if i==0:
                    rightmost=node
                if node.right!=None:
                    q.append(node.right)
                if node.left!=None:
                    q.append(node.left)
            res.append(rightmost.val)
        return res