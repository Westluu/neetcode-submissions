class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #input: An array of ints called nums
        #output: The maximum subarray product of nums

        #by definition sub array is contiguous and non-empty
        #thus largest product subarray is the product of an element of all its elements

        #2 4 -3 5
        #8 -12 -15

        #if there is a odd num negative avoid it all cost
        #if its even then we want to do them together
        
        #prefix and suffix products
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        res = max(nums[0], nums[-1])
        for i in range(1, len(nums)):
            prefix[i] = (prefix[i-1] or 1) * nums[i]
            res = max(res, prefix[i])
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = (suffix[i+1] or 1) * nums[i]
            res = max(res, suffix[i])
        return res

        
