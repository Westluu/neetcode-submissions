# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #checking if tree is balanced
            #by definition a tree is balences if its left and right subtrees
            #height differ no more than 1

        #Thus a tree is balanced if abs(root.left.height - root.right.height) <= 1
            #To find the height of a tree (we have to reach the deepest node and count how far we traveled)
            #Since we are reaching down DFS seems like the most logical approach

        #Solution
            # get height of left tree
            # get height of right tree
            # check if absolute diff of left and right height <= 1
            # if so return true
            # else return false

        #How to get height
            #using DFS rescursively go left and right until reaching leaf
            #along the way keep track of how many levels reached
        if not root:
            return True
        
        return self.checkBalance(root) and self.checkBalance(root.left) and self.checkBalance(root.right)

    def checkBalance(self, root):
        if self.checkHeight(root) != -1:
            return True
        return False
    
    def checkHeight(self, root):
        if not root:
            return 0

        left_height = self.checkHeight(root.left)
        if left_height == -1:
            return -1
        
        right_height = self.checkHeight(root.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1

        

    
   


    
        


        