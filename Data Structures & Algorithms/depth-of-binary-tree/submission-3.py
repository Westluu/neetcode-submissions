# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depthHelper(root, 0)
    
    def depthHelper(self, root, depth):
        if not root:
            return depth
        
        return max(self.depthHelper(root.left, depth + 1), self.depthHelper(root.right, depth + 1))

        