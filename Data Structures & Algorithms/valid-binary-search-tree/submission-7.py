# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        

        def validNode(leftLimit,rightLimit,root):
            if not root:
                return True
            if not(leftLimit<root.val<rightLimit):
                return False
            return validNode(leftLimit,root.val,root.left) and validNode(root.val,rightLimit,root.right)
        return validNode(-float("inf"),float("inf"),root) 

        