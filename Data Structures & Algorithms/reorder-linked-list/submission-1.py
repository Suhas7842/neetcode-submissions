# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head

        #step0: find length of linkedlist
        length=0
        while curr is not None:
            length+=1
            curr=curr.next
        curr=head

        #step1: find middle of linked list
        for _ in range((length-1)//2):
            curr=curr.next
        head2=curr.next
        curr.next=None
        #step2: reverse second half
        prev=None
        while head2 is not None:
            temp=head2.next
            head2.next=prev
            prev=head2
            head2=temp
        #step3: interweave both part together using dummy node
        head1,head2=head,prev
        while head1 and head2:
            temp1,temp2=head1.next,head2.next
            head1.next=head2
            head2.next=temp1
            head1,head2=temp1,temp2