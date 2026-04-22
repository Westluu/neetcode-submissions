# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        good_nodes = 0
        stack.append((root, root.val)) #node val, current max val of path
        while stack:
            node, max_val = stack.pop()

            #check if cur_node is good
            if node.val >= max_val:
                good_nodes+=1
                max_val = node.val
            
            if node.right:
                stack.append((node.right, max_val))
            if node.left:
                stack.append((node.left, max_val))

        return good_nodes