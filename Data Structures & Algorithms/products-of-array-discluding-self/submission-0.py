class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input: An array of ints nums
        #output: An array of ints where for output[i] is the product
        #of all elements of nums expect nums[i]
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = []
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[i])
        return res
        


       
        

        