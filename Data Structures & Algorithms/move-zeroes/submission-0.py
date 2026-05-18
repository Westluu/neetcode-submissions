class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #input: an array on ints
        
        #output: without creating extra space, move all 0 to the back
        #move all ints to the front maintaining order

        #0 0 1 2 0 5
        #1 0 0 2 0 5
        #1 2 0 0 0 5
        #1 2 5 0 0 0
        # 2 pointer approach

        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1


        