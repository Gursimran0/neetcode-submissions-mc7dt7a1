# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.sameNode(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def sameNode(self,curr,subRoot):
            if not curr and not subRoot:
                return True
            if curr and subRoot and curr.val == subRoot.val:
                return (self.sameNode(curr.left,subRoot.left) and self.sameNode(curr.right,subRoot.right))
            return False
        
        