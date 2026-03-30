# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        x1 = list1
        x2 = list2
        res = dummy = ListNode()
        while x1 and x2:
            if x1.val<x2.val:
                dummy.next= x1
                x1 = x1.next
            else:
                dummy.next = x2
                x2 = x2.next
            dummy = dummy.next
        if x1:
            dummy.next = x1
        if x2:
            dummy.next = x2
        return res.next