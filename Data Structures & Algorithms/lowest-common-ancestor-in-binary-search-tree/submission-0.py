# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # def LCA: between nodes p and q, is the lowest node val such that
        # that nodes contains both p and q as descendants.

        # root is BST by definition all values on the left is < root and 
        # on the right > root
        
        # so if p and q < root: then LCA must be on the right side
        # if p and q > root: then LCA must be on the left side
        # if p/q > root and p/q < root: then LCA must be the root

        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
            return root

        #on the left tree        
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        #on the right tree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return -1
        
        



