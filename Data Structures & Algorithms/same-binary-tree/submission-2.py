# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Checking if trees are equivalent
        #by def 2 tress 2 are equivalent if the have the exact saem structure and nodes are the same value

        #thus if traverse the trees both the same way using DFS and at each node we compare p and q values
        # if any of them diff then they are not equvivalent otherwise true 
        if not p and not q:
            return True
        
        if not p and q or not q and p:
            return False
            
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right
        

        

        
