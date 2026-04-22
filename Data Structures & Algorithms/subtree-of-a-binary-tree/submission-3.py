# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #def subtree: if in root, there consits of a node 
        # that has the same structure and node values as the subRoot. 
        # Containting all of its descendants
        
        #Algo: Checking every level until we find a node that matches the root of the subroot
        #then check that node and its descendants to see if it mataches the subRoot values and structure

        #BFS algorithm

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node and node.val == subRoot.val and self.isSameTree(node, subRoot):
                return True
              
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False


    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        
        return False

        


        