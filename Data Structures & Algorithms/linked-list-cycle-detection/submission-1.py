# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        while head:
            if head in d:
                return True
            else:
                d[head] = 0
            head = head.next
        return False