# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #input: binary tree and 2 nodes of the tree
        #output: LCA of the input 2 nodes, LCA is the lowest node in the tree
        #such that its has p and q as descendants

        #By definition for a node to be LCA of p and q then it must have both
        # p and q as descendants. Since the root is a binary tree then it must mean 
        # that LCA is between p and q

        #since we are checking for lowest, then we need to do as deep as possible first
        #DFS is the best case for this
        #since we start at the bottom, we can then ask the left and right subtree
        #if they both contain p and q, then we know the current root is the LCA
        
        #Base Case
        if not root:
          return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        #Check if left or right subtree contains p and q
        if left and right:
            return root
        
        if left:
            return left
        return right    


