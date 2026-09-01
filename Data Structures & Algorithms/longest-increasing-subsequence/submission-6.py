class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i] is the longest increasing subsequence ending at idx i
        #base case: dp[0-n] = 1
        #formula: dp[i] = max(dp[j]) + 1 
        #such that where nums[i] > nums[j] (where j all idx before i)
        dp = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    res = max(res, dp[i])
        
        return res