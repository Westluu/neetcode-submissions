class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #input: array of ints nums
        #output: largest sum of subarray nums
        
        #by definition subarray is a contiguous and non-empty

        # 2,     -3,     4,    -2,      2,       1,       -1,       4
        #[2, 2] [2,-1]  [4,4]  [4, 2]  [4, 4]   [5, 5]    [5, 4]   [8,8]

        #DP[i] = is a 2D cache where it stores the max sum of the array at idx i
        # [j, k], where j represents the max sum at idx i and k represents the sum of the subarry at idx i or before

        #Solution: max(DP[n])
        #                      best_so_far                 ,  current
        #Formula: DP[i] = ( max(dp[i-1][0], dp[i][1]), max(dp[i-1][1] + nums[i], nums[i] )

        current = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            best = max(best, current)
        
        return best
        

        