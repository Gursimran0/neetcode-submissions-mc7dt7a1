# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        if not root:
            root = TreeNode(val)
        
        while curr!= None:
            if curr.val>val:
                if curr.left == None:
                    curr.left = TreeNode(val)
                    break
                curr=curr.left
            elif curr.val<val:
                if curr.right==None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
        
        
        return root

        