from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        return self.levelOrderHelp(root, 0, res)


    def levelOrderHelp(self, root, level, res):
        if not root:
            return res
         
        left = self.levelOrderHelp(root.left, level + 1, res)
        right = self.levelOrderHelp(root.right, level + 1, res)
    
        while len(res) < level + 1:
            res.append([])
        res[level].append(root.val)
        return res
        

        

        

        
        
        


        