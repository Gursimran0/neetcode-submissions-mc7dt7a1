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
        def isValidBinary(rightLimit,leftLimit,root):
            if not root:
                return True
            if not(leftLimit<root.val<rightLimit):
                return False
            
            return isValidBinary(rightLimit,root.val,root.right) and isValidBinary(root.val,leftLimit,root.left)
        return isValidBinary(float("inf"),-float("inf"),root)


        