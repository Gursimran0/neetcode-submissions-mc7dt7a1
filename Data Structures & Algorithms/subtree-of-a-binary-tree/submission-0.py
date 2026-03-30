# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameNode(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def sameNode(self,x,y) -> bool:
        if not x and not y:
            return True
        if x and y and x.val == y.val:
            return self.sameNode(x.left,y.left) and self.sameNode(x.right,y.right)
        return False
        


            

        