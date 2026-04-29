class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_lookup = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_lookup:
                idx1 = min(diff_lookup[diff], i)
                idx2 = max(diff_lookup[diff], i)
                return [idx1, idx2]
            diff_lookup[nums[i]] = i
        return [-1]
        