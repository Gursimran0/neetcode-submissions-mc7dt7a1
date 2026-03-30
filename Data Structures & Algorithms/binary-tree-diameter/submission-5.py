# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        def height(root):
            if not root:
                return 0
            leftHeight=height(root.left)
            rightHeight=height(root.right)
            total = leftHeight + rightHeight
            nonlocal res
            res = max(total,res)
            return 1+max(height(root.left),height(root.right))
        
        height(root)
        return res
        
        