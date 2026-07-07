class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #input: An array of ints called nums and an int called target
        #output: the indices i and j, where i and j represent the
        #        idx of nums where the sum of i and j is the target

        #initial thought: sort the array then 2 pointer approach
        # or keep track of past values and see if we found the diff
        
        diff_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_map:
                return [min(i, diff_map[diff]), max(i, diff_map[diff])]
            diff_map[nums[i]] = i
        


        
        