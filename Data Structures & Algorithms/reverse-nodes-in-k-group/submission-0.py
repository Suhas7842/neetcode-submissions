# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # This pointer always sits right BEFORE the k-group we want to reverse.
        # After a group is reversed, this will point to the new end of that reversed group.
        group_tail_prev = dummy
        
        while True:
            # Find the last node of the current k-group
            group_end = self.getKthNode(group_tail_prev, k)
            if not group_end:
                break  # Not enough nodes left to form a group of size k
                
            next_group_start = group_end.next
            curr = group_tail_prev.next
            
            # 'prev' starts as the node after the group, so the first node 
            # we reverse automatically points to the next group.
            prev = next_group_start
            
            # Keep track of the original first node of the group. 
            # After reversal, this node will become the new tail of the group.
            old_group_start = group_tail_prev.next
            
            # Standard linked list reversal for the current k-group
            while curr != next_group_start:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            # Connect the previous section of the list to the new head of the reversed group
            group_tail_prev.next = group_end
            
            # Move our tracker forward. The old start is now the tail of this group,
            # which means it is right BEFORE the next group.
            group_tail_prev = old_group_start
            
        return dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr