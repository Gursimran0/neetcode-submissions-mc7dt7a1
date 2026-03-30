# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First we will calculate the total length
        l=0
        dummy = head
        while dummy:
            l+=1
            dummy=dummy.next
        print(l)
        remove = l-n
        if remove==0:
            return head.next
        s=0
        dummy = head
        for i in range(l-1):
            if (i+1) == remove:
                dummy.next = dummy.next.next
                break
            dummy=dummy.next
        return head
        