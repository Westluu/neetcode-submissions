class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = 0
        
        for num in nums:
            total_sum+=num
        target = total_sum // 2
        
        if total_sum % 2 != 0:
            return False

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for cur_sum in range(target, num-1, -1):
                dp[cur_sum] = dp[cur_sum] or dp[cur_sum - num]
        
        return dp[target]


        