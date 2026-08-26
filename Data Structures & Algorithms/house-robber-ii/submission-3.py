class Solution:
    def rob(self, nums: List[int]) -> int:
        #so its a circular array
        #meaning if we rob the 1st house we can't rob the last house
        #if we rob the last house we can rob the first house

        #thus if we exclude the first house and check for max rob
        #then exclude the second house and check for max rob
        #we can them compare then and take the biggest one
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        dp_1 = [0] * len(nums)
        dp_1[1] = nums[1]
        dp_1[2] = max(nums[1], nums[2])

        dp_2 = [0] * len(nums)
        dp_2[0] = nums[0]
        dp_2[1] = max(nums[0], nums[1])

        #excluding the 1st house and last house
        for i in range(2, len(nums)):
            if i >  2:
                dp_1[i] = max(dp_1[i-2] + nums[i], dp_1[i-1])
            if i < len(nums) - 1:
                dp_2[i] = max(dp_2[i-2] + nums[i], dp_2[i-1])
        
        return max(dp_1[len(nums)-1], dp_2[len(nums)-2])


