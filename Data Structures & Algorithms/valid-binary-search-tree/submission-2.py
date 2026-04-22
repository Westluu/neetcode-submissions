from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #def BST: every node left of root has a val < root.val
        # every node right of root has a val > root.val
        # both left and right nodes are also BST

        # every node as upper and lower bound
        # left child have an upper bound of its ancestor value
        # right child have an lower bound of its ancestor value

        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            node, low, high = queue.popleft()
            
            if not (low < node.val < high):
                return False

            if node.left:
                queue.append((node.left, low, node.val))
            if node.right:
                queue.append((node.right, node.val, high))
        return True 
            


        #       5
        #     /   \
        #    2     6
        #   /  \    \   
        #  1    7     8