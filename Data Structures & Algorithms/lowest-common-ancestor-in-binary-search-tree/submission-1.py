# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #input: root tree, 2 nodes p and q in root
        #output: the LCA node between p and q

        #by definition LCA between 2 nodes is the lowest node in  
        #the tree such that p and q are descendants of the LCA.
        #Also the LCA of p and q can be of themselves

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        elif (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
            return root  

