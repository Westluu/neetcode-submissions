# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #def balanced: left and right subtree heights difference <= 1
        #vist each node via PreOrder Traversal, each if balanced (go up)
        #algo: DFS, at each node keep track if balance and its height
        return self.isBalancedHelper(root)[0]

    def isBalancedHelper(self, root):
        if not root:
            return [True, 0] 

        left_tree = self.isBalancedHelper(root.left)
        right_tree = self.isBalancedHelper(root.right)

        balanced_height = True if abs(left_tree[1] - right_tree[1]) <= 1 else False
        balanced = left_tree[0] and right_tree[0] and balanced_height

        return [balanced, 1 + max(left_tree[1], right_tree[1])]

    
   


    
        


        