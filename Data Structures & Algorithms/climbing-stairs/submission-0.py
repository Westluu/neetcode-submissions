class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 2
        if n == 1 or n == 2:
            return n
        for i in range(2, n):
            new_curr = curr + prev
            prev = curr
            curr = new_curr
        return curr

        