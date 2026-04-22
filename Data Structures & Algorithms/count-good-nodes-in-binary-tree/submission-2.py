from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good_nodes = 0
        queue = deque([(root, root.val)])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node, max_val = queue.popleft()
                if node.val  >= max_val:
                    good_nodes += 1
                
                new_max = max(max_val, node.val)
                if node.left:
                    queue.append((node.left, new_max))
                if node.right:
                    queue.append((node.right, new_max))
        return good_nodes

                


                
