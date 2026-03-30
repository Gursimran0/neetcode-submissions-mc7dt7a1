# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        carry = 0
        x1 = l1
        x2 = l2
        dummy=res
        while x1 or x2 or carry:
            v1 = x1.val if x1 else 0
            v2 = x2.val if x2 else 0
            val = v1+v2+carry
            carry = val//10
            val = val%10
            res.next = ListNode(val)
            x1=x1.next if x1 else None
            x2=x2.next if x2 else None
            res = res.next
        return dummy.next
            
        