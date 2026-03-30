# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 =""
        str2=""
        x1=l1
        x2=l2
        while x1:
            str1 += str(x1.val)
            x1 = x1.next
        int1 = int(str1[::-1])
        while x2:
            str2 += str(x2.val)
            x2 = x2.next
        int2 = int(str2[::-1])
        resInt = int1+int2
        resStr = str(resInt)
        dummy = res = ListNode()
        for i in range(len(resStr)-1,-1,-1):
            res.next = ListNode(int(resStr[i]))
            res = res.next
        return dummy.next

        