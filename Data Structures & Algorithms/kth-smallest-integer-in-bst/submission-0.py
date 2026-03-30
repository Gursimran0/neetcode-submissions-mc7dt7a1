# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        res = []
        def dfs(curr):
            if not curr:
                return
            dfs(curr.left)
            res.append(curr.val)
            dfs(curr.right)
        dfs(curr)
        for i in range(len(res)):
            if i+1 == k:
                return res[i]
        return res[0]
        