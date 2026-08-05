from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return self.helpRightSideView(root, res, 0)
    

    def helpRightSideView(self, root, res, depth):
        if not root:
            return res
        
        right = self.helpRightSideView(root.right, res, depth + 1)
        left = self.helpRightSideView(root.left, res, depth + 1)

        while len(res) < depth + 1:
            res.append(0)
 
        if res[depth] == 0:
            res[depth] = root.val
        
        return res
        
        


       