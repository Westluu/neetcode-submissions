# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        traversal_stack = [root]
        height_map = {None: (0,0)}

        while traversal_stack:
            node = traversal_stack[-1]

            if node.left and node.left not in height_map:
                traversal_stack.append(node.left)
            elif node.right and node.right not in height_map:
                traversal_stack.append(node.right)
            else:
                node = traversal_stack.pop()

                left_height, left_diameter = height_map[node.left]
                right_height, right_diameter = height_map[node.right]

                #height and diameter
                height_map[node] = (1 + max(left_height, right_height), max(left_height + right_height, left_diameter, right_diameter))

        return height_map[root][1]
