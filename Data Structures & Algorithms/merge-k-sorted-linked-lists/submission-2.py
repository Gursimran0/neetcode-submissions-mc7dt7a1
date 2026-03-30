# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists)==1:
            return None
        
        while len(lists)>1:
            mergedLists = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2=lists[i+1] if i+1<len(lists) else None
                mergedLists.append(self.merge2lists(list1,list2))
            lists = mergedLists
        return lists[0]

    def merge2lists(self,list1,list2):
        dummy = res = ListNode(0,None)
        while list1 and list2:
            if list1.val<list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res=res.next
        if list1 :
            res.next = list1
        if list2:
            res.next = list2
        return dummy.next
