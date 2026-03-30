# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        res = []
        q.append(root)
        while q:
            qLen = len(q)
            temp = None
            tempRes = []
            for i in range(qLen):
                temp = q.popleft()
                if temp and temp.left:
                    q.append(temp.left)
                if  temp and temp.right:
                    q.append(temp.right)
                if temp:
                    tempRes.append(temp.val)
            if tempRes !=[]:
                res.append(tempRes)
        return res
                
