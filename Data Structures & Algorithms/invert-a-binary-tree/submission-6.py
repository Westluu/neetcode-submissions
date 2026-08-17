# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = [root]
        while queue:
            cur_node = queue.pop()
            cur_node.right, cur_node.left = cur_node.left, cur_node.right

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return root
        # if not root:
        #     return
        
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)

        # root.left = right
        # root.right = left

        # return root
        