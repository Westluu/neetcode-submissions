# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and root:
            return True
        
        if not root and subRoot:
            return False
        
        if root.val == subRoot.val:
            check = self.checkTree(root, subRoot)
            if check:
                return check
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        


    def checkTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.checkTree(root.left, subRoot.left) and self.checkTree(root.right, subRoot.right)
        return False

        

        