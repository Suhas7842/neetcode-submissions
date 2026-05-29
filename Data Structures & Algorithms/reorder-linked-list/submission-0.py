# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        prev=slow.next=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        one,two=head,prev
        while two:
            temp1,temp2=one.next,two.next
            one.next=two
            two.next=temp1
            one,two=temp1,temp2