# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy
        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                res.next=ListNode(list1.val)
                list1=list1.next
                res=res.next
            elif list1.val==list2.val:
                res.next=ListNode(list1.val)
                list1=list1.next
                res=res.next
                res.next=ListNode(list2.val)
                list2=list2.next
                res=res.next
            else:
                res.next=ListNode(list2.val)
                list2=list2.next
                res=res.next
        while list1 is not None:
            res.next=ListNode(list1.val)
            list1=list1.next
            res=res.next
        while list2 is not None:
            res.next=ListNode(list2.val)
            list2=list2.next
            res=res.next
        return dummy.next