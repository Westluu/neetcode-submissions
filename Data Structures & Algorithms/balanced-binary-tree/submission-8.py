class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1

    def getHeight(self, root):
        if not root:
            return 0

        left_height = self.getHeight(root.left)

        if left_height == -1:
            return -1

        right_height = self.getHeight(root.right)

        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)