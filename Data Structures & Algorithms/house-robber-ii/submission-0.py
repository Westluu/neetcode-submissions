class Solution:
    def rob(self, nums: List[int]) -> int:
        skip_first = nums[1:]
        skip_last = nums[:-1]
        
        return max(nums[0], self.helper(skip_first), self.helper(skip_last))
    
    def helper(self, nums):
        prev, curr = 0,0
        for num in nums:
            temp = num + prev
            prev = curr
            curr = max(temp, curr)
        return curr


        